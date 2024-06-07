from flask import Flask, jsonify, request
import requests
import json

app = Flask(__name__)

# Define the URL and headers for the API request
url = 'https://us-east-1.aws.data.mongodb-api.com/app/data-oubqqaw/endpoint/data/v1/action/findOne'
headers = {
    'Content-Type': 'application/json',
    # API Key
    'Access-Control-Request-Headers': '*'
}

@app.route('/findOne', methods=['GET'])
def find_one():
    data = {
        "collection": "questions",
        "database": "VoirDireDB",
        "dataSource": "VoirdireDB",
        "projection": {"_id": 1}
    }
    
    response = requests.post(url, headers=headers, data=json.dumps(data))
    
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": f"Request failed with status code {response.status_code}: {response.text}"}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)
