from flask import render_template, request
from app import app
from controller import getCategory, getProduct, getUser, addCategory

# index
@app.route('/')
def index():
    return render_template('index.html')

# user
@app.route('/user')
def user(type=None):
    data = getUser()
        
    return render_template('user.html', data=data)

# product
@app.route('/product')
def product(type=None):
    data = getProduct()
        
    return render_template('product.html', data=data)

# category
@app.route('/category', methods=['POST','GET'])
def category():

    if request.method == 'POST':
        name = request.form['category']
        addCategory(name=name)
        
    data = getCategory()
    return render_template('category.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)