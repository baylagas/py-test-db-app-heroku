from flask import Flask, render_template
from logic.person_logic import PersonLogic

app = Flask(__name__)


@app.route("/")
def home():
    logic = PersonLogic()
    result = logic.getAllPerson()
    return render_template("index.html", personArray=result)


if __name__ == "__main__":
    app.run(debug=True)
