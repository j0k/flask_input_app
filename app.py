from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/<name>", methods=['GET', 'POST'])
def welcome(name):
    input = request.form.get("input")
    output = special_f(input)
    return render_template("welcome.html", output=output)

def special_f(text: str):
    return "{0} {1}".format(text, "world!")

if __name__ == '__main__':
    app.run(debug=True)
