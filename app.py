from flask import *
from pickle import *

app = Flask(__name__)
app.secret_key = "created_by_vedant"
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        f = open("model.pkl", "rb")
        model = load(f)
        f.close()   

        f = open("mms.pkl", "rb")
        mms = load(f)
        f.close()
        try:
              preci = float(request.form["preci"])
              max_temp = float(request.form["max_temp"])
              min_temp = float(request.form["min_temp"])
              wind = float(request.form["wind"])
              d = [[preci, max_temp, min_temp, wind]]
              nd = mms.transform(d)
              weather = model.predict(nd)
              msg = "Weather : " + str(weather[0])
			
              return render_template("home.html", msg=msg)
        except Exception as e:
            msg = "Issue " + str(e)
            return render_template("home.html", msg = msg)
    
    return render_template("home.html")

if __name__ == "__main__":
	app.run(debug=True, use_reloader=True)