from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/pay", methods=["POST"])
def pay():
    # This is a MOCK page. No card details are validated, stored, or charged.
    name = request.form.get("name", "").strip() or "Customer"
    return render_template("success.html", name=name)


if __name__ == "__main__":
    import os

    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
