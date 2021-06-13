from flask import Flask
import views

app = Flask(__name__)


#URL
app.add_url_rule('/','index',views.index,methods = ['GET','POST'])

# run the app
if __name__ == "__main__":
    app.run(debug = True)
