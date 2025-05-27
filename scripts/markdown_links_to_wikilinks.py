import os
import re
import argparse
from urllib.parse import unquote # Added for %20 decoding

# Regex to find Markdown links:
# Group 1: Optional '!' (for images)
# Group 2: Link text (or alt text for images). Allows empty text e.g. []() or ![]()
# Group 3: Link URL
MARKDOWN_LINK_REGEX = re.compile(r'(!?)\[([^\]]*)\]\(([^\)]+)\)')

def generate_wikilink(match):
    """
    Converts a regex match object of a Markdown link into a Wikilink string.
    Handles URL decoding for %20 etc. in link targets.
    """
    prefix = match.group(1)    # '!' if it's an image link, otherwise empty string
    text = match.group(2)      # The text part of [text](link) or alt text
    original_link_url = match.group(3) # The URL part of [text](link)

    # Decode URL-encoded characters (e.g., %20 to space) from the link URL
    # This applies to the path, filename, and fragment/anchor.
    decoded_link_url = unquote(original_link_url)

    # Partition the decoded URL into base and fragment (anchor)
    base_url, hash_char, anchor = decoded_link_url.partition('#')
    
    # Determine the core name part of the wikilink target
    wikilink_name_part = base_url # Default (e.g., for full URLs or simple filenames)

    if base_url.lower().endswith(".md"):
        # For local .md files, use the filename without extension
        # e.g., "My Document.md" (or "My%20Document.md") becomes "My Document"
        wikilink_name_part = os.path.splitext(os.path.basename(base_url))[0]
    elif '://' not in base_url: # It's a local file path (not an external URL)
        # For other local files (images, PDFs, etc.), use the filename
        # e.g., "images/My Picture.png" becomes "My Picture.png"
        # e.g., "My File.pdf" becomes "My File.pdf"
        wikilink_name_part = os.path.basename(base_url)
    # Else (it's an external URL like https://example.com or ftp://...), 
    # wikilink_name_part remains as base_url, which is correct.

    # Construct the full wikilink target, re-appending the anchor if it existed
    wikilink_target = wikilink_name_part
    if anchor: # anchor is already unquoted from decoded_link_url
        wikilink_target = f"{wikilink_target}{hash_char}{anchor}"

    # Determine if the display text is redundant and can be omitted in the wikilink
    display_text_is_redundant = False
    if not text:  # Case 1: Text is empty, e.g., ![](image.png) or [](../doc.md)
        display_text_is_redundant = True
    else:
        # Unquote the display text for comparison, in case it also contained %20
        # e.g. if original link was [My%20Doc](My%20Doc.md), it should become [[My Doc]]
        unquoted_text_for_comparison = unquote(text)
        if unquoted_text_for_comparison.lower() == wikilink_target.lower():
            display_text_is_redundant = True

    if display_text_is_redundant:
        return f"{prefix}[[{wikilink_target}]]"
    else:
        # Use the original 'text' for display, as it was literally in the Markdown
        return f"{prefix}[[{wikilink_target}|{text}]]"

def process_markdown_file(filepath):
    """
    Reads a Markdown file, replaces Markdown links with Wikilinks, and saves it.
    Returns True if changes were made, False otherwise.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Perform substitution, subn returns (new_string, number_of_substitutions_made)
        new_content, num_replacements = MARKDOWN_LINK_REGEX.subn(generate_wikilink, content)

        if num_replacements > 0:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated: {filepath} ({num_replacements} links converted)")
            return True
        # else:
            # print(f"No changes needed for: {filepath}")
        return False
    except Exception as e:
        print(f"Error processing file {filepath}: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(
        description="Recursively convert standard Markdown links to Wikilinks in .md files. Decodes %20 to spaces in links."
    )
    parser.add_argument(
        "folder_path", 
        help="The path to the folder containing Markdown files."
    )
    args = parser.parse_args()

    root_folder = args.folder_path

    if not os.path.isdir(root_folder):
        print(f"Error: The folder '{root_folder}' does not exist.")
        return

    print(f"Scanning for Markdown files in '{root_folder}' and its subdirectories...")
    print("---")
    print("IMPORTANT: This script will MODIFFY FILES IN PLACE.")
    print("It is STRONGLY recommended to BACK UP YOUR FOLDER before proceeding.")
    print("---")
    
    confirm = input("Do you want to continue? (yes/no): ")
    if confirm.lower() != 'yes':
        print("Operation cancelled by user.")
        return

    files_processed_count = 0
    files_changed_count = 0

    for foldername, _, filenames in os.walk(root_folder):
        for filename in filenames:
            if filename.lower().endswith(".md"):
                filepath = os.path.join(foldername, filename)
                files_processed_count += 1
                if process_markdown_file(filepath):
                    files_changed_count += 1
    
    print("\n--- Conversion Summary ---")
    print(f"Total Markdown files found: {files_processed_count}")
    print(f"Total Markdown files modified: {files_changed_count}")
    print("Done.")

if __name__ == "__main__":
    main()