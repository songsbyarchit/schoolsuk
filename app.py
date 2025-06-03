from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/meet-the-team')
def team():
    return render_template('meet-the-team.html')

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/stories')
def stories():
    return render_template('stories.html')

@app.route('/trial')
def trial():
    return render_template('trial.html')

@app.route('/dfe')
def dfe():
    return render_template('dfe.html')

@app.route('/webinar')
def webinar():
    return render_template('webinar.html')

if __name__ == '__main__':
    app.run(debug=True, port=5050)