from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined


app = Flask(__name__)
app.jinja_env.undefined = StrictUndefined
app.jinja_env.auto_reload = True

# Required to use Flask sessions and the debug toolbar
app.secret_key = "\xdd~\x08Ry\x16~|\n\xba\xa5\x86\x9e\xe3AX\xaf@?\xa8\xd9zA\xe9"


@app.route("/")
def index():

    return render_template("index.html")


@app.route("/application-form")
def application_form():

    positions = ["Software Engineer", "QA Engineer", "Product Manager"]

    return render_template("application-form.html", positions=positions)


@app.route("/application-success", methods=["POST"])
def application_success():

    firstname = request.form.get("firstname")
    lastname = request.form.get("lastname")
    name = "{} {}".format(firstname, lastname)

    position = request.form.get("position")

    salary = request.form.get("salary")
    salary = "${:6,}".format(int(salary))

    return render_template("application-response.html",
                            name=name,
                            position=position,
                            salary=salary)


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
