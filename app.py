from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Cấu hình PostgreSQL Render
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://render_r53v_user:xGzANkXkzDKwtTN9RzvbjZty5Nyk7mSG@dpg-d1nn9mc9c44c73ehm5l0-a.oregon-postgres.render.com:5432/render_r53v'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Mô hình dữ liệu đơn giản
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(100))

@app.route('/')
def home():
    return "Ứng dụng Flask đã kết nối PostgreSQL!"

@app.route('/add')
def add_note():
    note = Note(content='Test render')
    db.session.add(note)
    db.session.commit()
    return 'Đã thêm ghi chú!'

if __name__ == '__main__':
    app.run()
