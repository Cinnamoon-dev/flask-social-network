from app import app


@app.route("/")
def index():
    return "Hello World!"


@app.route("/<name>")
def hello_name(name: str):
    return "Hello, %r!" % name
