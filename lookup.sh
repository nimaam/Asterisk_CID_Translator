#!/bin/bash

# Define the DID number to test
DID_NUMBER=$1

# Check if DID number argument is provided
if [ -z "$DID_NUMBER" ]; then
    echo "Error: DID number not provided."
    exit 1
fi

# Send a POST request to the Flask API endpoint and extract the result
RESPONSE=$(curl -s -X POST -H "Content-Type: application/json"  "http://localhost:5000/lookup/?did=$DID_NUMBER")
MODIFIED_DID=$(echo "$RESPONSE" | awk -F'"result":' '{print $2}' | tr -d '[:space:]' | tr -d '"')

# Check if the result is empty (indicating an error)
if [ -z "$MODIFIED_DID" ]; then
    echo "Error: Invalid response from the API."
    exit 1
fi

# Display the modified DID
echo "$MODIFIED_DID"

