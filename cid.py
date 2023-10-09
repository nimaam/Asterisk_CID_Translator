from flask import Flask, request, jsonify

app = Flask(__name__)

def process_cid(cid):
    if len(cid) == 8:
        return '+9821' + cid
    elif cid.startswith('98'):
        return '+' + cid
    else:
        return 'Invalid CID'

@app.route('/cid-lookup', methods=['POST'])
def cid_lookup():
    try:
        data = request.get_json(force=True)  # Use force=True to parse JSON even if content type is not set to application/json
        cid = data.get('cid')
        result = process_cid(cid)
        return jsonify({'result': result}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

