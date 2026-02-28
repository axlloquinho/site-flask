from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def pag_inicial():
    return render_template("inicial_pag.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
