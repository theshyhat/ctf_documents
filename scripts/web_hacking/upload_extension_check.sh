#!/bin/bash

#
# This is a script to enumerate which file extensions are allowed to be uploaded to a webform
# (in those sitations where it isn't obvious)
# Don't forget to adjust to adjust the UPLOAD_URL and ERROR_MESSAGE variables
# The EXTENSIONS list can be modified if a match can't be found initially
#

# MODIFY THIS!! URL of the web application upload page 
UPLOAD_URL="http://upl0ads.securezone.nyx/index.php"

# MODIFY THIS!! The error message the app returns if the extension is not allowed
ERROR_MESSAGE="Extension not allowed"

# List of file extensions to test (add as many as needed)
EXTENSIONS=("txt" "php" "gif" "jpg" "phar" "png" "html" "zip" "exe")

# Color codes
RED='\033[0;31m'
NC='\033[0m' # No Color (reset to default)

# Loop through each extension and try uploading a file
for ext in "${EXTENSIONS[@]}"
do
    # Create a dummy file with the current extension
    FILENAME="sample.$ext"
    echo "Testing upload for file with .$ext extension..."

    # Create a simple file to upload (you can adjust the content as needed)
    echo "This is a test file with $ext extension" > "$FILENAME"

    # Attempt to upload the file using curl (modify the form parameters as needed)
    RESPONSE=$(curl -s -F "file=@$FILENAME" $UPLOAD_URL)

    # Check if the response contains ERROR_MESSAGE variable
    if echo "$RESPONSE" | grep -q "$ERROR_MESSAGE"; then
        echo "Rejected: $ext"
    else
        echo -e "${RED}Accepted: $ext${NC}"
    fi

    # Remove the temporary file after the test
    rm "$FILENAME"
done
