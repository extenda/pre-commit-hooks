"""Version handling for the google-java-formatter hook.

Two numbers decide whether the hook runs at all: the Java the developer has and
the Java the pinned formatter needs. Both are read out of formats that shift --
a JDK version string, a class file header -- so both are pinned here rather than
left to the first machine that reports a shape nobody anticipated.
"""
import re
import struct
import zipfile

import pytest

from pre_commit_hooks.google_java_formatter import (
    formatter_version,
    parse_java_version,
    required_java_version,
)


@pytest.mark.parametrize("output, expected", [
    # The early access string that blocked commits on Fedora.
    ('openjdk version "27-ea" 2026-09-15', 27),
    ('openjdk version "25.0.4.1" 2026-08-18', 25),
    ('openjdk version "11.0.32" 2026-07-21', 11),
    # Java 8's leading component really is 1, so it stays below the minimum.
    # It looks like the early access case and must not be conflated with it.
    ('openjdk version "1.8.0_504"', 1),
    # Nothing to read: stay below the minimum rather than raise.
    ("java: command not found", 1),
    ("", 1),
])
def test_parse_java_version(output, expected):
    assert parse_java_version(output) == expected


def test_the_pinned_formatter_version_is_readable():
    assert re.fullmatch(r"\d+\.\d+(\.\d+)?", formatter_version())


@pytest.mark.parametrize("class_file_major, expected_jdk", [
    (55, 11),  # google-java-format 1.21.0 and older
    (61, 17),  # 1.25.2 through 1.28.0
    (65, 21),  # 1.36.1
])
def test_required_java_version(tmp_path, class_file_major, expected_jdk):
    jar = tmp_path / "google-java-format.jar"
    with zipfile.ZipFile(jar, "w") as archive:
        archive.writestr(
            "com/google/googlejavaformat/java/Main.class",
            b"\xca\xfe\xba\xbe\x00\x00" + struct.pack(">H", class_file_major))
    assert required_java_version(str(jar)) == expected_jdk
