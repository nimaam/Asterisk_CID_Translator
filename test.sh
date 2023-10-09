#!/bin/bash

# Define the CID to test
CID=$1

# Check if CID argument is provided
if [ -z "$CID" ]; then
    echo "Error: CID not provided."
    exit 1
fi

# Send a POST request to the Flask API endpoint and print the response
RESPONSE=$(curl -s -X POST -H "Content-Type: application/json" -d "{\"cid\": \"$CID\"}" http://localhost:5000/cid-lookup)

# Print the full response for debugging
echo "API Response: $RESPONSE"

# Extract the result field from the JSON response
RESULT=$(echo "$RESPONSE" | grep -o '"result":"[^"]*' | awk -F ':"' '{print $2}')

# Check if the result is empty (indicating an error)
if [ -z "$RESULT" ]; then
    echo "Error: Invalid response from the API."
    exit 1
fi

# Display the modified CID
echo "Modified CID: $RESULT"

