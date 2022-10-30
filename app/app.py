from flask import render_template, request
from app import app
from controller import getCategory


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<type>')
def route(type=None):
    data = []
    if type == 'user':
        pass
    elif type == 'product':
        pass
    elif type == 'category':
        print(getCategory())

    return render_template(type + '.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)