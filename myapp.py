from flask import Flask, render_template
from markupsafe import Markup
from reddit_scanner import get_data
from waitress import serve

app = Flask(__name__)


@app.route("/")
def home():
    df = get_data()
    if df is None:
        return render_template("home.html", df="Failed to get data")
    return render_template("home.html", df=Markup(df.to_html()))


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8080)
