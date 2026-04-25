from flask import Flask, render_template, request, redirect, url_for, session
from models import db, PasswordEntry
from encryption import initialize_key, encrypt_val, decrypt_val

app = Flask(__name__)

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vault.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "SECURE_SECRET_KEY_KRISHNA" # Needed for login sessions
db.init_app(app)

# SET YOUR MASTER PASSWORD HERE
MASTER_PASSWORD = "admin" 

# Initialize Encryption Key and Database
initialize_key()
with app.app_context():
    db.create_all()

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form.get('master_password') == MASTER_PASSWORD:
            session['logged_in'] = True
            return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/')
def index():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    entries = PasswordEntry.query.all()
    return render_template('index.html', entries=entries)

@app.route('/add', methods=['POST'])
def add_password():
    website = request.form.get('website')
    username = request.form.get('username')
    password = request.form.get('password')
    
    # Encrypt before saving
    encrypted_pw = encrypt_val(password)
    
    new_entry = PasswordEntry(website=website, username=username, encrypted_password=encrypted_pw)
    db.session.add(new_entry)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)