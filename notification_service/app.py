
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/notify', methods=['GET'])
def notify():
    print("conversion completed")
    return jsonify({"message": "Conversion completed successfully!"})

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5004)
