from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/skills')
def skills():
    return render_template('skills.html')

@app.route('/contact', methods=['GET','POST'])
def contact():

    if request.method == 'POST':

        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']

        conn = sqlite3.connect('database.db')
        cur = conn.cursor()

        cur.execute("INSERT INTO contact(name,email,subject,message) VALUES (?,?,?,?)",
        (name,email,subject,message))

        conn.commit()
        conn.close()

    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)