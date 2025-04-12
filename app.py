from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/reset-password')
def reset():
    return render_template('reset-password.html')

@app.route('/dashboard', methods=['POST'])
def dashboard():
    # Add auth logic here
    return render_template('dashboard.html')

@app.route('/send-reset-link', methods=['POST'])
def send_reset():
    email = request.form['email']
    # Logic to send reset email
    return "Reset link sent to " + email

if __name__ == '__main__':
    app.run(debug=True)
