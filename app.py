from flask import Flask, render_template, jsonify
app = Flask(__name__)

@app.route("/")
def func():
    return render_template("index.html")

@app.route("/factorial/<int:n>")
def fact(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return str(fact)

@app.route("/sum/<int:a>/<int:b>")
def sum(a,b):
    sum = a+b
    result = {
        "First number" : a,
        "Second number" : b,
        "sum" : sum
    }
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug= True, port = 8000)