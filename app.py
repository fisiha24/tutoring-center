from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message

app = Flask(__name__)

# --- ቅንብሮች ---
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'Fisihamelkie6@gmail.com'
app.config['MAIL_PASSWORD'] = 'የእርስዎ_16_አሃዝ_App_Password' # እዚህ ጋር ኮድህን አስገባ

db = SQLAlchemy(app)
mail = Mail(app)

# --- የዳታቤዝ መዋቅር ---
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    grade = db.Column(db.Integer, nullable=False)
    address = db.Column(db.String(100), nullable=False)
    subject = db.Column(db.String(50), nullable=False)

with app.app_context():
    db.create_all()

# --- ገጾች (Routes) ---
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

@app.route('/register.html', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # መረጃን ከፎርሙ መቀበል እና በዳታቤዝ ማስቀመጥ
        new_student = Student(
            fullname=request.form.get('fullname'),
            email=request.form.get('email'),
            phone=request.form.get('phone'),
            grade=request.form.get('grade'),
            address=request.form.get('address'),
            subject=request.form.get('subject')
        )
        db.session.add(new_student)
        db.session.commit()
        return "ምዝገባው ተሳክቷል!"
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)