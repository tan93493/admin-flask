from flask import Flask, jsonify
from flask_cors import CORS
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from models import db, Product, Category

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your-secret-key'

db.init_app(app)

# Flask-Admin
admin = Admin(app, name="Admin Panel", template_mode="bootstrap4", url='/')
admin.add_view(ModelView(Product, db.session))
admin.add_view(ModelView(Category, db.session))

@app.route('/api/books')
def get_books():
    books = Product.query.all()
    return jsonify([{'id': b.id, 'name': b.name, 'price': b.price} for b in books])

# Tạo bảng nếu chưa có
with app.app_context():
    db.create_all()
    print("✅ Database created.")

if __name__ == '__main__':
    app.run(debug=True)
