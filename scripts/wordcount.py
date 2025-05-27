import os
import sys

def main():
    # Determine the starting directory from command line argument or use current directory
    start_dir = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
    total_words = 0

    # Walk through all directories and files
    for dirpath, _, filenames in os.walk(start_dir):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    # Read file content and count words
                    content = f.read()
                    word_count = len(content.split())
                    total_words += word_count
            except UnicodeDecodeError:
                print(f"Skipping binary/non-UTF-8 file: {file_path}")
            except PermissionError:
                print(f"Permission denied: {file_path}")
            except Exception as e:
                print(f"Error processing {file_path}: {str(e)}")

    print(f"Total number of words in all files: {total_words}")

if __name__ == "__main__":
    main()