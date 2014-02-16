from flask import Flask
app = Flask(__name__)

@app.route("/blo")
def hello2():
	return "Hello 2"

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()
