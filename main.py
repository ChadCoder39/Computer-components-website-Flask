from flask import Flask, redirect


app = Flask(__name__)
app.secret_key = '11122'


# redirect to main page
@app.route("/")
def root():
    return redirect("/start_page")

# Imports all the @app routes from ./routes folder (must be declared after the "app" variable!)
from routes.__routes__ import *


if __name__ == "__main__":
    app.run(debug=True)