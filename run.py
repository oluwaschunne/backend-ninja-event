from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/about', methods=['GET'])
def about():
    data = {
        "Name": "Falope Oluwaseun",
        "Gender": "Male",
        "Github_url": "www.github.com/oluwaschunne/backend-ninja-event"
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)