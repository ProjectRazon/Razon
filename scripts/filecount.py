import os
import sys

def count_files(directory):
    total = 0
    try:
        with os.scandir(directory) as entries:
            for entry in entries:
                if entry.is_dir(follow_symlinks=False):
                    total += count_files(entry.path)
                else:
                    total += 1
    except PermissionError:
        pass  # Skip directories we can't access
    return total

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python filecount.py <directory>")
        sys.exit(1)
    root_dir = sys.argv[1]
    if not os.path.isdir(root_dir):
        print(f"Error: '{root_dir}' is not a valid directory.")
        sys.exit(1)
    file_count = count_files(root_dir)
    print(f"Total number of files: {file_count}")