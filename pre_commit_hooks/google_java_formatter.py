from __future__ import print_function

import argparse
import subprocess
import os
import errno
import re
import struct
import urllib.request
import xml.etree.ElementTree as ElementTree
import zipfile

# The version lives in pom.xml so Dependabot can upgrade it. See the comment there.
POM = os.path.join(os.path.dirname(os.path.abspath(__file__)), "pom.xml")
MAVEN_NS = {"m": "http://maven.apache.org/POM/4.0.0"}


def formatter_version():
    dependency = ElementTree.parse(POM).find(
        "m:dependencies/m:dependency[m:artifactId='google-java-format']",
        MAVEN_NS)
    if dependency is None:
        raise RuntimeError("No google-java-format dependency in " + POM)
    return dependency.find("m:version", MAVEN_NS).text.strip()


def get_google_java_formatter():
    version = formatter_version()
    bin_dir = os.path.join(os.path.expanduser("~"), ".google-java-formatter")
    if not os.path.exists(bin_dir):
        try:
            os.makedirs(bin_dir)
        except OSError as exc:  # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

    gjf_jar = os.path.join(
        bin_dir, "google-java-format-" + version + ".jar")

    if not os.path.isfile(gjf_jar):
        print("Downloading " + gjf_jar + "...")
        url = "https://github.com/google/google-java-format/releases/" \
            + "download/v" + version \
            + "/google-java-format-" \
            + version + "-all-deps.jar"
        urllib.request.urlretrieve(url, gjf_jar)

    return os.path.abspath(gjf_jar)

def required_java_version(jar):
    """The Java feature version the formatter jar was compiled for.

    Read from the class file rather than pinned here, because google-java-format
    raises its floor without warning: 1.21 ran on Java 11, 1.25 needed 17 and
    1.36 needs 21. Deriving it keeps the check honest across every upgrade.
    """
    with zipfile.ZipFile(jar) as archive:
        with archive.open("com/google/googlejavaformat/java/Main.class") as f:
            major = struct.unpack(">H", f.read(8)[6:8])[0]
    # Class file major 52 is Java 8, and they advance in step from there.
    return major - 44


def parse_java_version(output):
    """The Java feature version reported by `java -version`.

    Read the leading integer of the version string rather than splitting on
    ".": early access builds report `27-ea`, which is not an integer, and Java 8
    reports `1.8.0_504`, whose leading component really is 1 and so stays below
    the version the formatter needs.
    """
    match = re.search(r'version "(\d+)', output)
    return int(match.group(1)) if match else 1


def java_version():
    with subprocess.Popen(["java", "-version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE) as process:
        output = process.communicate()[1].decode("utf-8")
    return parse_java_version(output)


def jep396_args(major_version):
    if major_version >= 16:
        return "--add-exports jdk.compiler/com.sun.tools.javac.api=ALL-UNNAMED \
--add-exports jdk.compiler/com.sun.tools.javac.file=ALL-UNNAMED \
--add-exports jdk.compiler/com.sun.tools.javac.parser=ALL-UNNAMED \
--add-exports jdk.compiler/com.sun.tools.javac.tree=ALL-UNNAMED \
--add-exports jdk.compiler/com.sun.tools.javac.util=ALL-UNNAMED".split(" ")
    return ""

def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*',
                        help='Java filenames to check.')
    args = parser.parse_args(argv)

    formatter = get_google_java_formatter()
    required = required_java_version(formatter)
    java_major_version = java_version()
    if java_major_version < required:
        print("ERROR: google-java-format " + formatter_version()
              + " requires Java " + str(required) + " or newer, found Java "
              + str(java_major_version) + ". Will exit.")
        return 1
    jep_arg = jep396_args(java_major_version)
    if not jep_arg:
        return subprocess.call([
            'java', '-jar', formatter, '--replace'] + args.filenames)
    else:
        return subprocess.call([
            'java'] + jep_arg + ['-jar', formatter, '--replace'] + args.filenames)


if __name__ == "__main__":
    exit(main())
