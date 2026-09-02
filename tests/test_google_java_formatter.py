"""Version handling for the google-java-formatter hook.

`java -version` output was split on "." and passed to int(), which raised on an
early access build and left the hook reporting Java 27 as Java 1.
"""
import pytest

from pre_commit_hooks.google_java_formatter import parse_java_version


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
