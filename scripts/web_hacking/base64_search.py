'''
This script searches inside of a file and extracts potential
Base64 encoded strings that are 12 characters in length or longer.
If any potential Base64 strings are found, the script will print out
the decoded version of those strings.
'''
import base64
import re
import sys

def find_base64_strings(file_path):
    try:
        # Read the content of the file
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
 
        # Define a regular expression pattern to find strings inside single or double quotes
        quote_pattern = re.compile(r'["\'](.*?)["\']', re.MULTILINE | re.DOTALL)
        # Define a regular expression pattern for potential Base64 strings
        base64_pattern = re.compile(r'[A-Za-z0-9+/=]{20,}', re.MULTILINE)
        # Find all quoted strings in the content
        quoted_strings = quote_pattern.findall(content)
        # Find all potential Base64 strings in the content
        potential_base64_strings = base64_pattern.findall(content)
        # Combine quoted strings and potential Base64 strings
        all_strings = quoted_strings + potential_base64_strings
        # Initialize list for valid Base64 strings
        valid_base64_strings = []

        # Validate and decode potential Base64 strings
        for base64_string in all_strings:
            try:
                # Base64 strings should be a multiple of 4 in length
                if len(base64_string) % 4 == 0 and len(base64_string) > 11:
                    decoded_bytes = base64.b64decode(base64_string, validate=True)
                    decoded_string = decoded_bytes.decode('utf-8', errors='ignore')
                    valid_base64_strings.append((base64_string, decoded_string))
            except Exception:
                # Ignore invalid Base64 strings
                continue
        
        # Print the valid Base64 strings and their decoded values
        if valid_base64_strings:
            print("Valid Base64 strings found:")
            for original, decoded in valid_base64_strings:
                print(f"Original: {original}")
                print(f"Decoded: {decoded}")
                print()
        else:
            print("No valid Base64 strings found in the file.")
    
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Check if a file path was provided as an argument
    if len(sys.argv) != 2:
        print("Usage: python base64_search.py <path_to_file>")
    else:
        # Get the file path from command line argument
        file_path = sys.argv[1]
        find_base64_strings(file_path)
