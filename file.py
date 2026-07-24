from flask import Flask , render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', name = 'Home')

@app.route("/about")
def about():
    return render_template('about.html', name = 'ABOUT')    


@app.route("/courses")
def curses():
    return render_template('courses.html', name = 'courses')    


@app.route("/booking")
def booking():
    return render_template('booking.html', name = 'booking')    


@app.route("/contact")
def contact():
    return render_template('contact.html', name = 'contact')    


if __name__ == '__main__':
    app.run(debug=True)