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
	@app.route("/map20220407095431299920.html")
	def map20220407095431299920():
		return render_template("maps/map20220407095431299920.html")
	@app.route("/map20220407095617589617.html")
	def map20220407095617589617():
		return render_template("maps/map20220407095617589617.html")
	@app.route("/map20220407095818214573.html")
	def map20220407095818214573():
		return render_template("maps/map20220407095818214573.html")
	@app.route("/map20220407100004602678.html")
	def map20220407100004602678():
		return render_template("maps/map20220407100004602678.html")
	@app.route("/map20220407100010308508.html")
	def map20220407100010308508():
		return render_template("maps/map20220407100010308508.html")
	@app.route("/map20220407100037802550.html")
	def map20220407100037802550():
		return render_template("maps/map20220407100037802550.html")
	@app.route("/map20220407100043872452.html")
	def map20220407100043872452():
		return render_template("maps/map20220407100043872452.html")
	@app.route("/map20220407100114916199.html")
	def map20220407100114916199():
		return render_template("maps/map20220407100114916199.html")
	@app.route("/map20220407100129538059.html")
	def map20220407100129538059():
		return render_template("maps/map20220407100129538059.html")
	@app.route("/map20220409114723311155.html")
	def map20220409114723311155():
		return render_template("maps/map20220409114723311155.html")
	@app.route("/map20220409114808751979.html")
	def map20220409114808751979():
		return render_template("maps/map20220409114808751979.html")