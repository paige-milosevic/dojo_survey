from flask import Flask, render_template, session, redirect, request

app = Flask(__name__)
app.secret_key='Paige Rocks'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    return redirect('/success')

@app.route('/success')
def sucess():
    return render_template('sucess.html')

if __name__=='__main__':
    app.run(debug=True)