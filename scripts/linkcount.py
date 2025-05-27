import os
import re
import argparse
import sys

# Regex to find Markdown inline links: [text](url "optional title")
LINK_REGEX = re.compile(r'\[[^\]]*\]\([^)]*\)')

# --- Function to count links in a single file ---
def count_links_in_file(filepath):
    """
    Reads a file and counts occurrences of the Markdown link pattern.
    Returns the count, suppressing errors.
    """
    try:
        # Open with utf-8 encoding, common for Markdown.
        # 'ignore' errors for robustness against potential encoding issues.
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            matches = LINK_REGEX.findall(content)
            return len(matches)
    except IOError:
        # Ignore files that cannot be read (permissions, etc.)
        return 0
    except Exception:
        # Ignore other potential errors during file processing
        return 0

# --- Main function ---
def main():
    """
    Parses arguments, traverses directory, counts links, and prints only the total count.
    """
    parser = argparse.ArgumentParser(
        description="Recursively count Markdown links `[text](url)` in files and output only the total count."
    )
    parser.add_argument(
        "directory",
        help="The path to the directory to scan."
    )
    parser.add_argument(
        "-e", "--ext",
        action='append', # Allow multiple extensions
        default=['.md', '.markdown'], # Default Markdown extensions
        help="File extensions to check (default: .md, .markdown). Use multiple times (e.g., -e .txt)."
    )

    args = parser.parse_args()
    target_dir = args.directory
    # Ensure extensions start with a dot and are lowercase for consistent matching
    extensions_to_check = tuple(ext.lower() if ext.startswith('.') else '.' + ext.lower() for ext in args.ext)

    if not os.path.isdir(target_dir):
        # Keep critical error message for non-existent directory on stderr
        print(f"Error: '{target_dir}' is not a valid directory.", file=sys.stderr)
        sys.exit(1) # Exit with a non-zero code to indicate failure

    total_link_count = 0

    # Walk through the directory structure
    for root, _, files in os.walk(target_dir):
        for filename in files:
            # Check if the file has one of the desired extensions (case-insensitive)
            if filename.lower().endswith(extensions_to_check):
                filepath = os.path.join(root, filename)
                link_count = count_links_in_file(filepath)
                total_link_count += link_count

    # --- Output ---
    # Print *only* the final total count to standard output
    print(total_link_count)

# --- Script execution ---
if __name__ == "__main__":
    main()