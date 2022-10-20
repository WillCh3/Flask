from crypt import methods
from flask import Flask, render_template, request

app = Flask(__name__)

notas = {}

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        if request.form.get('aluno') and request.form.get('nota'):
            notas[request.form.get('aluno')]= request.form.get('nota')
    return render_template('index.html', notas= notas)


if __name__ == '__main__':
    app.run(debug=True)