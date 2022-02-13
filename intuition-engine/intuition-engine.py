from flask import Flask

app = Flask(__name__)

@app.route("/")
def main_page():
    return """
		<html><head><title>Intuition Engine</title></head><body><div><form><input type="text" id="searchbox"><input type="submit"></form></div><br><ht><div id="content"></div></body></html>
		"""

@app.route("/gematria")


@app.route("/video")


@app.route("/text")
