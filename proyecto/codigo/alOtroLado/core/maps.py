from flask import Flask, render_template
app = Flask(__name__)
class maps():
	@app.route("/map20220505164549125735.html")
	def map20220505164549125735():
		return render_template("maps/map20220505164549125735.html")
	@app.route("/map20220505164848923118.html")
	def map20220505164848923118():
		return render_template("maps/map20220505164848923118.html")
	@app.route("/map20220505170636256622.html")
	def map20220505170636256622():
		return render_template("maps/map20220505170636256622.html")
	@app.route("/map20220505170740199483.html")
	def map20220505170740199483():
		return render_template("maps/map20220505170740199483.html")
	@app.route("/map20220505170754285881.html")
	def map20220505170754285881():
		return render_template("maps/map20220505170754285881.html")
	@app.route("/map20220505170817704913.html")
	def map20220505170817704913():
		return render_template("maps/map20220505170817704913.html")
	@app.route("/map20220506090426472178.html")
	def map20220506090426472178():
		return render_template("maps/map20220506090426472178.html")
	@app.route("/map20220506091807778594.html")
	def map20220506091807778594():
		return render_template("maps/map20220506091807778594.html")
	@app.route("/map20220506093157857947.html")
	def map20220506093157857947():
		return render_template("maps/map20220506093157857947.html")