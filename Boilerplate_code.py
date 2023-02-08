#Importing flask module in the project
from flask import Flask, render_template

#Create an object of the Flask class
app = Flask(__name__)

#The route() function of the Flask class 
@app.route("/SA")

def class_activity():
    name = "Aman"
    return render_template("Index.html", student_name = name)

app.run(debug = True)