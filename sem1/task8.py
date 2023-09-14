from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('base.html')


@app.route('/about/')
def about():
    return render_template('about.html')


@app.route('/contacts/')
def contact():
    return render_template('contacts.html')


@app.route('/clothes/')
def clothes():
    return render_template('clothes.html')

@app.route('/shoes/')
def shoes():
    return render_template('shoes.html')

@app.route('/clothes/jaket')
def jaket():
    return render_template('jaket.html')


if __name__ == '__main__':
    app.run(debug=True)
