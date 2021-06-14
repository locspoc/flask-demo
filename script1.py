from flask import Flask, render_template

app=Flask(__name__) # instantiate class using name of python script

@app.route('/') #specify home page
def home():
    return render_template("home.html")

@app.route('/about/') #specify about page
def about():
    return render_template("about.html")

if __name__=="__main__":
    app.run(debug=True)