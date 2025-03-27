from flask import Flask,render_template,request,redirect
import mysql.connector
app = Flask(__name__)

con = mysql.connector.connect(
    host="localhost",
    user="abhinav",
    password="asd123."
    database="abhinav"
)
cursor = con.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users(name TEXT,age INTEGER)")
@app.route("/",methods=['GET','POST'])
def index():
    if request.method=="POST":
        name=request.form.get("name")
        age=request.form.get("age")
        print(name,age)
        cursor = con.cursor()
        cursor.execute("INSERT INTO users(name,age) values(%s,%s)",(name,age))
        
        con.commit()
        con.close()
        return redirect("/")
    return render_template("index.html")

app.run()