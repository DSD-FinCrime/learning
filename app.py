from flask import Flask, request, render_template
'''instance of flask class, webserver gateway interface'''

app = Flask(__name__)

@app.route("/")
def welcome():
    return"welcome to learning flask , This is Rahul Here."

@app.route("/form",methods=['GET','POTST'])
def form():
    if request.method=="POST":
        pass
    return render_template('form.html')

if __name__ == "__main__":
    app.run(debug=True)

'''This is just a ractise code file'''
''hello''