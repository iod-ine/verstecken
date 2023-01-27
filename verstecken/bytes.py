"""Functions for bytes-based file manipulation."""

import pathlib
import re


def reverse_file(file_: str, postfix: str = ".dat") -> None:
    """Reverse the byte order of the given file.

    The new file wil be saved with the name reversed.

    """

    file_ = pathlib.Path(file_)
    dir_ = file_.absolute().parent

    with open(file_, "br") as f:
        contents = f.read()

    postfix_regex = re.compile(f"{postfix}$")
    reverse_file = postfix_regex.sub("", file_.name)[::-1]

    if postfix_regex.search(file_.name) is None:
        reverse_file += ".dat"

    reverse_file = dir_ / reverse_file

    with open(reverse_file, "bw") as f:
        f.write(contents[::-1])
