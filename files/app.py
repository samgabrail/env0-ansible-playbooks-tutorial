from flask import Flask, render_template
import psycopg2

app = Flask(__name__)

@app.route('/')
def index():
    conn = psycopg2.connect(
        dbname="myapp",
        user="myapp",
        password="myapppassword",
        host="192.168.56.103"  # IP of your database server
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM items")
    items = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', items=items)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
