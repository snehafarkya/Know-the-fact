from flask import Flask,flash,render_template, request 

app = Flask(__name__)
app.secret_key = "snega12233"
@app.route("/base")

def home():
   
    return render_template("index.html") 

@app.route("/choice.html", methods=['POST','GET'])
def ans():
    flash("You will eat " + str(request.form['inptext']) +" at "+ str(request.form['place'])) 
    return render_template("choice.html")

if __name__ == "__main__":
    app.run(debug=True)