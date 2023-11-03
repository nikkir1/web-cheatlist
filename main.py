from flask import Flask, render_template
import sqlite3

app = Flask(__name__)
DATABASE = 'project.db'

def query_db(query, args=(), one=False):
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    cur.execute(query, args)
    rv = cur.fetchall()
    cur.close()
    con.close()
    return (rv[0] if rv else None) if one else rv

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/sql')
def show_sql_injections():
    rows = query_db('SELECT * FROM sql')
    return render_template('sql.html', sql_injections=rows)

@app.route('/writeups')
def writeups():
    conn = sqlite3.connect('project.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM writeup")
    writeups = cursor.fetchall()
    conn.close()
    return render_template('writeups.html', writeups=writeups)

if __name__ == '__main__':

    app.run(debug=True)
