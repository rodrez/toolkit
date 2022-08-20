
# Takes a directory and a pattern and renames the pattern on all files in the directory
# according to the new pattern.
#
# Example:
# python3 bulk_renamer.py /path/to/dir "*.jpg" "new_name.jpg"
#

import os
import sys
import re
import shutil
import argparse


def main():
    parser = argparse.ArgumentParser(description='Bulk renamer')
    parser.add_argument('dir', help='Directory to rename')
    parser.add_argument('pattern', help='Pattern to match')
    parser.add_argument('new_pattern', help='New pattern')
    args = parser.parse_args()
    rename_files(args.dir, args.pattern, args.new_pattern)


def rename_files(dir, pattern, new_pattern):
    for filename in os.listdir(dir):
        if re.search(pattern, filename):
            new_filename = re.sub(pattern, new_pattern, filename)
            shutil.move(os.path.join(dir, filename), os.path.join(dir, new_filename))


if __name__ == '__main__':
    main()
    sys.exit(0)
