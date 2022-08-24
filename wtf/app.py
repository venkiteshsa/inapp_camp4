from flask import Flask, render_template

from myformclass import NameForm

app = Flask(__name__)

#including a secret key fro preventing CSRF attacks in the app.config dic
app.config['SECRET_KEY'] = 'secret string'


@app.route("/wtf", methods = ['GET', 'POST'])
def wtf():
    #create an instance of the NameForm class from myformclass (.py)
    form = NameForm()
    name = None
    #checking if all the validators were passed and the form was submitted
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''

    return render_template("wtf.html", form=form, name=name)

if __name__ == "__main__":
    app.run(debug=True)