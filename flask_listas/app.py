from flask import Flask, render_template

app = Flask(__name__)

frutas = ['banana', 'maçã', 'mamão', 'abacate', 'laranja', 'limão']

@app.route('/')
def index():
    return render_template('index.html', frutas= frutas)


if __name__ == '__main__':
    app.run(debug=True)