from Generator import *
from flask import Flask, render_template,request,flash

app=Flask(__name__)

@app.route("/home",methods=["PoST","GET"])

def home() :
    if request.method=="POST":
        output=str(genCheck())
        return render_template("home.html", output=output)
    else:
        
        return render_template("home.html",output="")


if __name__== "__main__":
    app.run(debug=False)