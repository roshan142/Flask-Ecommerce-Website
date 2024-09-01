from flask import Flask , render_template
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager , current_user


db = SQLAlchemy()
DB_NAME = "database.db"
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'testuser1002'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{path.join(app.root_path,DB_NAME)}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    from .views import views
    from .auth import auth
    from .models import User
    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    create_database(app)
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    return app
   

def add_sample_products():
    from .models import Product
    products = [
            Product (product_name="Women Floral Print Tiered Dress with Short Sleeves",gender="women", price=899, description="Product color might slightly vary due to photographic lighting sources or your monitor settings, We recommend you buy a size larger,Package contains: 1 dress, Machine wash cold,100% cotton.",photo="/static/img/1.avif"),
            Product(product_name="Printed V-Neck Fit & Flare Dress",gender="women", price=899, description="Package contains: 1 dress,Machine wash,Cotton.",photo="/static/img/2.avif"),
            Product(product_name="Women Floral Print Straight Kurta with Pants",gender="women", price=1299, description="For further wash care information, kindly refer to the label attached to the product,Notched neckline,Embroidered yoke with sequins,Package contains: 1 kurta, 1 pant,Machine wash,100% Cotton,Kurta & Bottomwear.",photo="/static/img/3.avif"),
            Product(product_name="Women Zip-Front Bomber Jacket",gender="women", price=799, description="We recommend you buy a size smaller,Package contains: 1 jacket,Machine wash,Cotton Blend.",photo="/static/img/4.avif"),
            Product (product_name="Woven Saree with Contrast Border",gender="women", price=899, description="Blouse piece length: 0.8 m,Saree length: 5.5 m,Package contains: 1 saree with blouse piece,The last image gives a detailed look of the blouse piece that comes with this saree (The model is wearing a blouse from our in-house wardrobe),Hand wash,Soft Silk.",photo="/static/img/5.avif"),
            Product(product_name="Women Solid Satin Sleep Shirt",gender="women", price=399, description="Package contains: 1 shirt,Machine wash,100% polyester.",photo="/static/img/6.avif"),
            Product(product_name="Women Quilted Button-Down Jacket",gender="women", price=799, description="Package contains: 1 jacket,Machine wash,Polyester Blend.",photo="/static/img/7.avif"),
            Product(product_name="Women Relaxed Fit Joggers",gender="women", price=499, description="3-pocket styling,Placement patch,Package contains: 1 joggers,Machine wash,70% organic cotton, 30% recycled polyester.",photo="/static/img/8.avif"),
            Product (product_name="Women Tie & Dye Round-Neck Shift Dress",gender="women", price=1699, description="Package contains: 1 dress,Machine wash,Viscose blend.",photo="/static/img/9.avif"),
            Product(product_name="Hoodie with Kangaroo Pockets",gender="women", price=599, description="Drawstring fastening waist,Ribbed hem cuffs,Package contains: 1 hoodie,Machine wash,Cotton Blend.",photo="/static/img/10.avif"),
            Product(product_name="Satin Floral Print Shift Dress - Green And Black",gender="women", price=1999, description="This green and black shift dress has a V-neck, floral print, and balloon sleeves. It is perfect for your evening catch-up. Made from Satin, it's immensely soft and comfortable to wear.",photo="/static/img/11.webp"),
            Product(product_name="Floral Shift Dress - Multicolour",gender="women", price=2499, description="Shift silhouette,Floral print,V-neck,Slightly stretchable,Short flutter sleeves with lace hem,2 pockets,Above knee length,Non-transparent.",photo="/static/img/12.webp"),
            Product (product_name="Box Pleat Ombre Dress - Green and Blue",gender="women", price=1199, description="This green and blue sleeveless ombre dress has a high-neck and box pleat detail. Made from Polyester Moss Lycra, it is soft and comfortable to wear.",photo="/static/img/13.webp"),
            Product(product_name="Men Lightly Washed Tapered Fit Jeans",gender="men", price=699, description="We recommend you buy a size larger,Package contains: 1 jeans,Machine wash,Denim,Mid Rise.",photo="/static/img/14.avif"),
            Product(product_name="Men Straight Fit Cargo Pants with Insert Pockets",gender="men", price=399, description="We recommend you buy a size smaller,Straight Fit,Package contains: 1 cargo pants,Hand wash,Mid Rise,Twill,Running.",photo="/static/img/15.avif"),
            Product(product_name="Men Track Pants with Insert Pockets",gender="men", price=399, description="Package contains: 1 track pants,Machine wash cold,52% cotton, 48% polyester.",photo="/static/img/16.webp"),
            Product (product_name="Checked Shirt with Patch Pocket",gender="men", price=599, description="Single-button squared cuffs,Curved hemline,Regular Fit,Package contains: 1 shirt,Machine wash,Cotton.",photo="/static/img/17.avif"),
            Product(product_name="Men Oversized Fit Round-Neck T-Shirt",gender="men", price=499, description="Cotton,Regular Fit,Round,Short sleeve,Medium,Package contains: 1 t-shirt,Oversized Solid Tshirt,Cotton Blend,Machine wash,Round.",photo="/static/img/18.avif"),
            Product(product_name="Checked Shirt with Patch Pocket",gender="men", price=599, description="Curved hemline,Single-button round cuffs,Regular Fit,Package contains: 1 shirt,Machine wash,Cotton.",photo="/static/img/19.avif"),
            Product(product_name="Heavy-Wash Slim Jeans",gender="men", price=799, description="Package contains: 1 jeans,Machine wash,Mid Rise,Cotton poly Lycra.",photo="/static/img/20.avif"),
            Product (product_name="Men Regular Fit Short Kurta",gender="men", price=499, description="Regular Fit,Package contains: 1 kurta,Hand wash,Cotton polyester blend.",photo="/static/img/21.avif"),
            Product(product_name="Textured Blazer, Waistocat and Trouser Set",gender="men", price=9999, description="Regular Fit,Machine wash,75% terylene, 25% rayon.",photo="/static/img/22.avif"),
            Product(product_name="Geometric Print Lounge Set",gender="men", price=799, description="We recommend you buy a size larger,Package contains: 1 shirt, 1 shorts,Hand wash,Cotton.",photo="/static/img/23.avif"),
            Product(product_name="Geometric Printed Regular Fit Lounge Wear Sets",gender="men", price=999, description="Crafted with cotton to provide utmost comfort,Machine wash,Rayon.",photo="/static/img/24.avif"),
            Product (product_name="Zip-Front Slim Fit Puffer Jacker",gender="men", price=1399, description="Zipper pockets,Placement logo applique,Slim Fit,Package contains: 1 jacket,Dry clean,100% nylon.",photo="/static/img/25.avif"),
            Product(product_name="Cotton Trucker Jacket with Pockets",gender="men", price=3999, description="Regular Fit,Package contains: 1 jacket,Machine wash,100% cotton,Universal.",photo="/static/img/26.avif"),
            Product(product_name="Brand Applique Regular Fit Hoodie",gender="men", price=1699, description="Drawstring fastening hood,Ribbed hem & cuffs,Kangaroo pockets,Regular Fit,Package contains: 1 hoodie,Machine wash,77% cotton, 14% polyester, 9% recycled polyester.",photo="/static/img/27.avif"),
            Product(product_name="Brand Print Slim Fit Hoodie with Kangaroo Pockets",gender="men", price=1199, description="Drawstring fastening hood,Ribbed hem & cuffs,Slim Fit,Package contains: 1 hoodie,Machine wash cold,60% cotton, 40% polyester.",photo="/static/img/28.avif"),   
    ]
    db.session.bulk_save_objects(products)
    db.session.commit()

def create_database(app):
    if not path.exists('web/' + DB_NAME):
        with app.app_context():
            db.create_all()
            add_sample_products()
        print('Created Database!')

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html',user=current_user), 404
    
