from flask import Flask, render_template, request
import string

app = Flask(__name__)

def calculate_password_strength(password):
 
    score = 0

    if any(char.isdigit() for char in password):
        score += 1
    if any(char.islower() for char in password):
        score += 1
    if any(char.isupper() for char in password):
        score += 1
    if any(char in string.punctuation for char in password):
        score += 1

    return score

@app.route('/', methods=['GET', 'POST'])
def index():
    strength = None

    if request.method == 'POST':
        user_password = request.form['password']
        strength = calculate_password_strength(user_password)

    return render_template('index.html', strength=strength)

if __name__ == '__main__':
    app.run(debug=True)
