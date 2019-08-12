from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html", title="Home")


@app.route('/about')
def about():
    return render_template("about.html", title="About")


@app.route('/membership')
def membership():
    return render_template("membership.html", title="Memberships")


@app.route('/contact')
def contact():
    return render_template("contact.html", title="Contact Us")
