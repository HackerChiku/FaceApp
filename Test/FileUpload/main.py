from flask import Flask, app
import views
app = Flask(__name__)


# Url
app.add_url_rule('/','index',views.index,methods = ['GET','POST'])

# Run
if __name__ == "__main__":
    app.run(debug = True)