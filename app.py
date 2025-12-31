from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "سلام! سایت من با پایتون ساخته شد 😎"

if __name__ == "__main__":
    app.run(debug=True)
