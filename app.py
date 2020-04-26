from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/info")
def info():
    return render_template('/info/index.html')

@app.route("/info/rulebook")
def rulebook():
    return render_template('/info/rulebook/index.html')

@app.route("/info/trainmap")
def trainmap():
    return render_template('/info/trainmap/index.html')

@app.route("/info/welcome/")
def welcome():
    return render_template('/info/welcome/index.html')

@app.route("/info/welcome/01")
def welcome01():
    return render_template('/info/welcome/01/index.html')

@app.route("/info/welcome/02")
def welcome02():
    return render_template('/info/welcome/02/index.html')

@app.route("/info/welcome/03")
def welcome03():
    return render_template('/info/welcome/03/index.html')

@app.route("/dynmap")
def dynmap():
    return render_template('/dynmap/index.html')

@app.route("/our-story")
def ourstory():
    return render_template('/our-story/index.html')

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=80)
