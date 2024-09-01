from flask import  Blueprint , render_template , request , redirect , url_for , flash , jsonify
from flask_login import login_required,current_user
from . import db
from .models import User,Cart,Product
import random
from sqlalchemy import func


views = Blueprint("views",__name__)

@views.route('/', methods=['GET','POST'])
def home():
      url = "home"
      product = Product.query.order_by(func.random()).all()
      return render_template('home.html',product=product,user=current_user,url=url)

@views.route('/contact', methods=['GET','POST'])
def contact():
      url = "contact"
      return render_template('contact.html',user=current_user,url=url)

@views.route('/add-to-cart/<int:product_id>')
@login_required
def add_to_cart(product_id):
    product = Product.query.get_or_404(product_id)
    cart_item = Cart.query.filter_by(user_link=current_user.id, product_link=product.id).first()
    if cart_item:
        cart_item.quantity += 1
    else:
        cart_item = Cart(user_link=current_user.id, product_link=product.id, quantity=1)
        db.session.add(cart_item)
    db.session.commit()
    flash(f'Added {product.product_name} to cart.')
    return redirect(url_for('views.cart'))

@views.route('/remove_from_cart/<int:product_id>', methods=['POST'])
@login_required
def remove_from_cart(product_id):
    cart_item = Cart.query.filter_by(user_link=current_user.id, product_link=product_id).first()
    
    if cart_item:
            db.session.delete(cart_item)
            db.session.commit()
            flash('Item removed from cart successfully.', 'success')
    else:
        flash('Item not found in your cart.', 'warning')
    return redirect(url_for('views.cart'))

@views.route('/update_quantity', methods=['POST'])
@login_required
def update_quantity():
    data = request.get_json()  # Get JSON data from the request
    product_id = data.get('product_id')
    quantity = data.get('quantity')

    if not product_id or not quantity:
        return jsonify({'success': False, 'message': 'Invalid input data'}), 400

    # Find the cart item with the matching product ID
    cart_item = Cart.query.filter_by(product_link=product_id).first()

    if cart_item:
            # Update the quantity in the database
            cart_item.quantity = quantity
            db.session.commit()
            return jsonify({'success': True, 'message': 'Quantity updated successfully'})
    else:
        return jsonify({'success': False, 'message': 'Item not found in cart'}), 404

@views.route('/product/<int:product_id>', methods=['GET','POST'])
def product_view(product_id):
    url = "home"
    random_number = random.randint(0,5)
    product = Product.query.get_or_404(product_id)
    return render_template('products.html',product_view=product,user=current_user,random_number=random_number,url=url)





@views.route('/order-success', methods=['GET','POST'])
@login_required
def order_success():
    cart_item = Cart.query.filter_by(user_link=current_user.id).all()
    if cart_item:
            for i in cart_item:
                db.session.delete(i)
                db.session.commit()
    url = "checkout"
    random_number = random.randint(10000000, 99999999)
    return render_template('order_success.html',user=current_user,random_number=random_number,url=url)

@views.route('/cart', methods=['GET','POST'])
@login_required
def cart():
    url = "cart"
    cart_items = Cart.query.filter_by(user_link=current_user.id).all()
    total = sum(item.product.price * item.quantity for item in cart_items)
    return render_template('cart.html', cart_items=cart_items, total=total,user=current_user,url=url)




@views.route('/checkout', methods=['GET','POST'])
@login_required
def checkout():
    url = "checkout"
    cart_items = Cart.query.filter_by(user_link=current_user.id).all()
    total = sum(item.product.price * item.quantity for item in cart_items)
    return render_template('checkout.html', cart_items=cart_items, total=total,user=current_user,url=url)

@views.route('/search', methods=['GET'])
def search():
    url = "home"
    query = request.args.get('query')  # Get the search query from the form
    if query:
        # Filter products based on the search query (e.g., by name or description)
        results = Product.query.filter(Product.product_name.ilike(f'%{query}%')).all()
    else:
        results = []

    return render_template('search_result.html', query=query, results=results,user=current_user,url=url)



