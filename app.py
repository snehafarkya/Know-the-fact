from tkinter.font import BOLD
from flask import Flask,flash,render_template, request 
import random

app = Flask(__name__)
app.secret_key = "snega12233"


@app.route("/")
def home():
    a= random.randrange(1,6)
    return render_template("index.html") 

@app.route("/choice.html", methods=['POST','GET'])
def ans(): 
    num = str(request.form['num'])
    if num == '1':
       flash("You will eat " + str(request.form['inptext']) +" at "+ str(request.form['place']) + ". You entered: "+ str(request.form['num']))
       flash("HAHA! Funny😄")  
       flash("Did you know 🤔? \n ")
       flash("Glaciers and ice sheets hold about 69 percent of the world's freshwater.")
    elif num == '2':
        flash("You will eat " + str(request.form['inptext']) +" at "+ str(request.form['place']) + ". You entered: "+ str(request.form['num']))  
        flash("HAHA! Funny😄")  
        flash("Did you know 🤔? \n "  +" ")
        flash("Climate change is causing flowers to change color.")
    elif num == '3':
        flash("You will eat " + str(request.form['inptext']) +" at "+ str(request.form['place']) + ". You entered: "+ str(request.form['num']))  
        flash("HAHA! Funny😄")  
        flash("Did you know 🤔? \n "  +" ")
        flash("North Korea and Cuba are the only places you can't buy Coca-Cola.")
    elif num == '4':
        flash("You will eat " + str(request.form['inptext']) +" at "+ str(request.form['place']) + ". You entered: "+ str(request.form['num']))  
        flash("HAHA! Funny😄")  
        flash("Did you know 🤔? \n "  +" ")
        flash("The hottest chili pepper in the world is so hot it could kill you.")
    elif num == '5':
        flash("You will eat " + str(request.form['inptext']) +" at "+ str(request.form['place']) + ". You entered: "+ str(request.form['num']))  
        flash("HAHA! Funny😄")  
        flash("Did you know 🤔? \n "  +" T")
        flash("he world's most densely populated island is the size of two soccer fields.")
    elif num == '6':
        flash("You will eat " + str(request.form['inptext']) +" at "+ str(request.form['place']) + ". You entered: "+ str(request.form['num']))  
        flash("HAHA! Funny😄")  
        flash("Did you know 🤔? \n "  +" ")
        flash("The world's quietest room is located at Microsoft's headquarters in Washington state.")
    else:
        flash("Enter the number in given range!")
    return render_template("choice.html")

if __name__ == "__main__":
    app.run(debug=True)