from flask import Flask, request

app = Flask(__name__)

def process_cid(cid):
    if len(cid) == 10 and cid.startswith('21'):
        return '+98' + cid
    elif len(cid) == 11 and cid.startswith('0') and cid[1:].isdigit():
        return '+98' + cid[1:]
    elif len(cid) == 8:
        return '+9821' + cid
    elif cid.startswith('98'):
        return '+' + cid
    elif cid.startswith('00'):
        return '+' + cid[2:]
    else:
        return 'Invalid CID'

@app.route('/lookup/', methods=['GET', 'POST'])
def cid_lookup():
    try:
        if request.method == 'POST':
            # Parse JSON data from POST request
            data = request.get_json(force=True)  # Use force=True to parse JSON even if content type is not set to application/json
            did_number = data.get('did')
        elif request.method == 'GET':
            # Get the 'did' parameter from the URL for GET requests
            did_number = request.args.get('did')

        # Check if the 'did' parameter is present
        if did_number:
            # Process the 'did' number and modify CID
            modified_cid = process_cid(did_number)
            return modified_cid, 200

        # Return an error message if 'did' parameter is missing
        return 'DID number not provided.', 400

    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

