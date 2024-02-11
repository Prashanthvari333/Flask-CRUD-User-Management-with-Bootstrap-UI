from flask import Flask, render_template, request,url_for,redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5433/UsersData'
db = SQLAlchemy(app)

# Define your model
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    phone = db.Column(db.String(20))

# Create the database tables
#db.create_all()

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/prashu')
def prashu():
    return "Hai.. sruthi"

@app.route("/sruthi")
def sruthi():
    return "<h1> Sruthi wants to say hi to you </h1>"

@app.route('/home')
def home():
    data = db.session.query(Users).all()
    return render_template("home.html",users=data)

@app.route('/demo')
def demo():
    return render_template("demo.html")

@app.route('/add', methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        name = request.form.get('name')
        phone = request.form.get('phone')
        new_user = Users(name=name, phone=phone)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('home'))
    return "Please submit the form."
@app.route('/edit/<string:id>')
def edit(id):
    # Query the user by id
    user = db.session.query(Users).filter_by(id=id).first()
    
    if user is None:
        return "User not found", 404  # Return 404 Not Found if user not found
    
    # Print user details
    print("User ID:", user.id)
    print("User Name:", user.name)
    print("User Phone:", user.phone)
    
    return '<h1>Edit page {0}</h1>'.format(id)
@app.route('/delete/<string:id>')
def delete(id):
    # Query the user by id
    user = db.session.query(Users).filter_by(id=id).first()
    # Print user details
    print("User ID:", user.id)
    print("User Name:", user.name)
    print("User Phone:", user.phone)
    return "<h1> this is delete page ..!{0}</h1>".format(id)
    #return redirect(url_for('home'))

if __name__ == '__main__':
    with app.app_context():
        # Create the database tables
        db.create_all()
    app.run(debug=True)
