from flask import render_template, request
from app import app
from controller import getCategory, getProduct, getUser, addCategory, addUser, addProduct

# index
@app.route('/')
def index():
    return render_template('index.html')

# user
@app.route('/user', methods=['POST','GET'])
def user():

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        avatar = request.form['avatar']
        # add user to db
        addUser(name=name, email=email, avatar=avatar, password=password, username=username)

    data = getUser()
    return render_template('user.html', data=data)

# category
@app.route('/category', methods=['POST','GET'])
def category():

    if request.method == 'POST':
        name = request.form['category']
        addCategory(name=name)
        
    data = getCategory()
    return render_template('category.html', data=data)


# product
@app.route('/product', methods=['POST','GET'])
def product():

    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        price = float(request.form['price'])
        image = request.form['image']
        category_id = request.form['category_id']
        owner_id = request.form['owner_id']

        addProduct(name=name, description=description, price=price, image=image, category_id=category_id, owner_id=owner_id)

    data = getProduct()
    return render_template('product.html', data=data)
if __name__ == '__main__':
    app.run(debug=True)