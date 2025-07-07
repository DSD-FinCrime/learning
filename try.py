from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('form.html')

@app.route("/order",methods=["POST"])
def order():
    name = request.form['name']
    drink = request.form['drink']
    return f"order placed by {name} for {drink}"

if __name__=="__main__":
    app.run()