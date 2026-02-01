from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector
import os
app = Flask(__name__, static_folder="static", template_folder="templates")
app.secret_key = "lostandfound123"

#db = mysql.connector.connect(
    #host="localhost",
   # user="root",
   # password="Radhika1@",
    #database="lostfound"
#)
#cursor = db.cursor(buffered=True)
#def reconnect_db():
 #   global db, cursor
  #  if not db.is_connected():
   #     db.reconnect(attempts=3, delay=2)
    #    cursor = db.cursor(buffered=True)


# ---------------- LOGIN PAGE ----------------
@app.route("/")
def login_page():
    return render_template("index.html")



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT",5000)))
