# Exercise 23 of "Learn Python3 the Hard Way"
# Strings, Bytes, and Character Encodings
#
# UTF8: Unicode Transformation Format 8 Bits
# b'': bytes
# DBES: Decode Bytes, Encode Strings

import sys

script, encoding, error = sys.argv


def main(language_file, encoding, errors):
    line = language_file.readline()

    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)


def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<===>", cooked_string)


# languages = open("lauguages.txt", encoding="utf-8")
languages = open(".\LPY3THW\languages.txt", encoding="utf-8")

main(languages, encoding, error)
