from flask import Flask, render_template
app = Flask(__name__)
print("on file ")
class maps():
	print("on class")
	@app.route("/map20220407094736325610.html")
	def map20220407094736325610():
		return render_template("maps/map20220407094736325610.html")
	@app.route("/map20220407095004226860.html")
	def map20220407095004226860():
		return render_template("maps/map20220407095004226860.html")