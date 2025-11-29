from flask import Flask, request, jsonify

app = Flask(__name__)

# Store the latest received data
data_storage = {}

# ESP32 sends data here
@app.route('/temperature', methods=['POST'])
def receive_temperature():
    content = request.get_json()
    if 'id' in content and 'temperature' in content:
        data_storage['id'] = content['id']
        data_storage['temperature'] = content['temperature']
        return jsonify({"status": "success", "received": content}), 200
    return jsonify({"status": "failed", "message": "Invalid data"}), 400

# Streamlit fetches data here
@app.route('/get_temperature', methods=['GET'])
def get_temperature():
    return jsonify(data_storage)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)