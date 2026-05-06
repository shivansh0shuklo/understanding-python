from flask import Flask,render_template
app = Flask(__name__)

posts   =[
    {
        'author':'shivansh',
        'title':'a hollow mind',
        'content':'blog post 1',
        'date':'10-04-26'
    },
    {
        'author':'rohit',
        'title':'a kind heart',
        'content':'blog post 2',
        'date':'10-05-26'
    }
]
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',posts=posts)

@app.route("/about")
def about():
    return render_template('about.html',title='ABOUT')

if (__name__ == '__main__'):
    app.run(debug=True)  