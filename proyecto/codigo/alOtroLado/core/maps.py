from flask import Flask, render_template
app = Flask(__name__)
class maps():
	@app.route("/map20220418094140147118.html")
	def map20220418094140147118():
		return render_template("maps/map20220418094140147118.html")