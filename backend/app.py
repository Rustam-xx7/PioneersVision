from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Backend OK"

@app.route("/user/<name>")
def hwlo(name):
    return f"welcom {name} !"

if __name__ == "__main__":
    app.run(debug=True)