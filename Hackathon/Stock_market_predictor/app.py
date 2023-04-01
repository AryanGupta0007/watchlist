from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
DB_NAME = 'mydb.db'
db = SQLAlchemy()
app.config["SECRET KEY"] = "DSHSHSFHAHF HSFHSKHFS"
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "jlsjfl"
db.init_app(app=app)


class User(db.model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    password = db.Column(db.String(100))

    def __repr__(self):
        return f"{self.name} {self.id} {self.email} {self.password}"

@app.route('/home')
def home_page():
    return render_template('index.html')


@app.route('/login', methods=['POST', 'GET'])
def login_page():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        if credenitals_correct:
            return render_template('index.html')

        if false:
            flash('Incorrect Login Credentials ')
            return render_template('')

    elif request.method == 'GET':
        return render_template('login.html')

@app.route('/signup', method=['POST', 'GETs'])
def register_page():
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == 'POST':
        name = request.form.get('username')
        email = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        user = User.query.filter_by(email=email).first()
        if user:
            flash("Sorry a account with this email already Please login")
            return redirect(url_for("app.login_page"))
        if password1 == password2:
            new_user = User(name=name, email=email, password=password1)
            db.session.add(new_user)
            db.session.commit()
            flash('Account Created')
        return render_template('index.html')


if __name__ == '__main__':
    app.run()
