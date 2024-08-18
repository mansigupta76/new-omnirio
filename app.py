from flask import Flask, render_template, request, jsonify
# from flask_cors import CORS

app = Flask(__name__)
# CORS(app,origins=["*"])


@app.route('/api/data', methods=['POST'])
def handle_data():
    if request.method == 'POST':
        data = request.json
        email = data.get("email")
        # Process data here
        return jsonify({ "data": email})
    else:
        return jsonify({"message": "Send a POST request to this endpoint"})



if __name__ == '__main__':
    app.run(debug=True,port=5001)
