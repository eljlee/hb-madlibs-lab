"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]


@app.route('/')
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)


@app.route('/game')
def show_madlib_form():
    """Displays the madlib template to the user."""

    answer = request.args.get("answer")

    if answer == "no":
        return render_template("goodbye.html")

    else:
        return render_template("game.html")


@app.route('/madlib')
def show_madlib():
    """Takes user's choices and puts them into a madlib."""

    hexcode = request.args.get("hexcode")
    noun = request.args.get("noun")
    person = request.args.get("name")

    adjectives = request.args.getlist("adj")

    length = len(adjectives)

    # make list of all html files
    # call choice() on list of html files and store as variable
    # place ^ variable in render_template

    madlibs = ["madlib.html", "madlib2.html", "madlib3.html"]

    random_madlib = choice(madlibs)

    return render_template(random_madlib, hexcode=hexcode, noun=noun,
                           person=person, adjectives=adjectives, length=length)


if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True)
