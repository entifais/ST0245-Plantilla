from flask import Flask, render_template
app = Flask(__name__)
class maps():
	@app.route("/map20220407171119370186.html")
	def map20220407171119370186():
		return render_template("maps/map20220407171119370186.html")
	@app.route("/map20220408081250115225.html")
	def map20220408081250115225():
		return render_template("maps/map20220408081250115225.html")
	@app.route("/map20220408081344125294.html")
	def map20220408081344125294():
		return render_template("maps/map20220408081344125294.html")