from flask import Flask, render_template
app = Flask(__name__)
class maps():
	@app.route("/map20220510163349564694.html")
	def map20220510163349564694():
		return render_template("maps/map20220510163349564694.html")