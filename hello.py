from flask import Flask

app = Flask(__name__)


# route goes here
@app.route("/")
def hello():
    return "Hello world!"


if __name__ == "__main__":
    app.run()
# app.run(0.0.0.0) if run locally ane exposed to public network
