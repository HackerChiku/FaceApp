from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "This is home page"

#variable rule
@app.route('/<name>')
def variable(name):
    return "This is variable {}".format(name)

@app.route('/blog/<int:blogid>')
def blog(blogid):
    return "This blogid is {}".format(blogid)

@app.route('/blog/<float:w>')
def weight(w):
    return "This weight is {}".format(w)


if __name__ == "__main__":
    app.run(debug=True)