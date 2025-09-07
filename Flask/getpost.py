from flask import Flask, render_template, request, redirect, url_for
import numpy as np

app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome User"

@app.route("/index")
def index():
    return render_template('index.html')
    # return "Welcome User index change to this that mm"

@app.route("/success/<score>")
def suecess(score):
    return "Your scores are: " + score
    # return "Welcome User index change to this that mm"

###############################VARIABLE RULE
##Changing the requirement to specify the input is a an int
@app.route("/success_n/<int:score>")
def success1(score):
    return "Your scores are: " + str(score)
    # return "Welcome User index change to this that mm"


###############################DYNAMIC RULES
###CASE 1
@app.route("/dynamic/<int:score>")
def dynamic1(score):
    if score > 30:
        res = "PASSED"
    else:
        res = "FAILED"
    
    return render_template('dynamic1.html', results = res)

###CASE 2A: Adding Comments and using if
@app.route("/dynamic2/<int:score>")
def dynamic2(score):
    
    return render_template('dynamic2.html', results = score)

###CASE 2A: Adding Comments and using for
@app.route("/dynamic3/<name>/<subjname>/<int:score>") #/<name>/<subjname>/<int:score>
def dynamic3(name,subjname,score): #name,subjname,score
    # dct = {'Name':'rach','Subject':'Eng', 'Score': 10}
    dct = {'Name':name,'Subject':subjname, 'Score': score}
    
    return render_template('dynamic3.html', results = dct)

##############################Dynamic URL
@app.route('/submit', methods = ['GET', 'POST'])
def submit():
    avg= 0
    if request.method == "POST":
        sci = float(request.form['science'])
        math = float(request.form['maths'])
        c = float(request.form['c'])
        ds = float(request.form['datascience'])
        avg = (sci+math+c+ds )/4

        if int(avg) > 30:
            return redirect(url_for('dynamic2',score = int(avg)))
        else:
            return redirect(url_for('success1',score = int(avg)))
    return render_template('getresult.html')



@app.route(rule ='/form', methods = ['GET','POST'])
def form():
    if request.method == "POST":
        nm = request.form['name']
        return f"Hello, {nm}!" ##name we got from form -> id mention
    
    return render_template('form.html')


if __name__ == "__main__":
    app.run(debug=True)