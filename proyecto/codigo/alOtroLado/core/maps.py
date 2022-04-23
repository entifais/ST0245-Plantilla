from flask import Flask, render_template
app = Flask(__name__)
class maps():
	@app.route("/map20220418094140147118.html")
	def map20220418094140147118():
		return render_template("maps/map20220418094140147118.html")
	@app.route("/map20220420124049508619.html")
	def map20220420124049508619():
		return render_template("maps/map20220420124049508619.html")
	@app.route("/map20220422225354989095.html")
	def map20220422225354989095():
		return render_template("maps/map20220422225354989095.html")
	@app.route("/map20220422225614370999.html")
	def map20220422225614370999():
		return render_template("maps/map20220422225614370999.html")
	@app.route("/map20220422225640232081.html")
	def map20220422225640232081():
		return render_template("maps/map20220422225640232081.html")
	@app.route("/map20220422231215450600.html")
	def map20220422231215450600():
		return render_template("maps/map20220422231215450600.html")
	@app.route("/map20220422231303240456.html")
	def map20220422231303240456():
		return render_template("maps/map20220422231303240456.html")
	@app.route("/map20220422231324758524.html")
	def map20220422231324758524():
		return render_template("maps/map20220422231324758524.html")
	@app.route("/map20220422231838380711.html")
	def map20220422231838380711():
		return render_template("maps/map20220422231838380711.html")
	@app.route("/map20220422231928504566.html")
	def map20220422231928504566():
		return render_template("maps/map20220422231928504566.html")