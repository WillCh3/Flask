from flask import Flask, render_template

alunos = {'Will': 9.5, 'José': 4.5, 'Taty': 9.5, 'Bryann': 8.4, 'Wyan': 7.9}


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', alunos = alunos)


if __name__ == '__main__':
    app.run(debug=True)