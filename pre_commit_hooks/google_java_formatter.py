from __future__ import print_function

import argparse
import subprocess
import os
import errno
import urllib.request

FORMATTER_VERSION = "1.10.0"


def get_google_java_formatter():
    bin_dir = os.path.join(os.path.expanduser("~"), ".google-java-formatter")
    if not os.path.exists(bin_dir):
        try:
            os.makedirs(bin_dir)
        except OSError as exc:  # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

    gjf_jar = os.path.join(
        bin_dir, "google-java-format-" + FORMATTER_VERSION + ".jar")

    if not os.path.isfile(gjf_jar):
        print("Downloading " + gjf_jar + "...")
        url = "https://github.com/google/google-java-format/releases/" \
            + "download/" + FORMATTER_VERSION \
            + "/google-java-format-" \
            + FORMATTER_VERSION + "-all-deps.jar"
        urllib.request.urlretrieve(url, gjf_jar)

    return os.path.abspath(gjf_jar)

def jep396_args():
    try:
        with subprocess.Popen("java -version", stdout=subprocess.PIPE, stderr=subprocess.PIPE) as process:
            output = process.communicate()[1].decode("utf-8")
        if output.find('version "'):
            majorVersion = output.split('"')[1].split(".")[0]
            if int(majorVersion) >= 16:
                return "--add-exports jdk.compiler/com.sun.tools.javac.api=ALL-UNNAMED \
--add-exports jdk.compiler/com.sun.tools.javac.file=ALL-UNNAMED \
--add-exports jdk.compiler/com.sun.tools.javac.parser=ALL-UNNAMED \
--add-exports jdk.compiler/com.sun.tools.javac.tree=ALL-UNNAMED \
--add-exports jdk.compiler/com.sun.tools.javac.util=ALL-UNNAMED"
        return ""
    except ValueError:
        return ""

def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*',
                        help='Java filenames to check.')
    args = parser.parse_args(argv)

    formatter = get_google_java_formatter()
    jep_arg = jep396_args()
    if not jep_arg: 
        return subprocess.call([
            'java', '-jar', formatter, '--replace'] + args.filenames)
    else:
        return subprocess.call([
            'java', jep_arg, '-jar', formatter, '--replace'] + args.filenames)


if __name__ == "__main__":
    exit(main())
