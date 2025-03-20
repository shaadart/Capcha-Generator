from flask import Flask, render_template, request, redirect, url_for, session, send_file
from captcha.image import ImageCaptcha
import random
import string
import io

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for session management

# Generate random captcha text
def generate_captcha_text(length=5):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

#this is how it works!
# Generate captcha image
def generate_captcha_image(text):
    image = ImageCaptcha()
    data = image.generate(text)
    return data

@app.route('/')
def index():
    captcha_text = generate_captcha_text()
    session['captcha_text'] = captcha_text
    return render_template('index.html')

@app.route('/captcha')
def captcha():
    captcha_text = session.get('captcha_text', '')
    data = generate_captcha_image(captcha_text)
    return send_file(data, mimetype='image/png')

@app.route('/refresh_captcha')
def refresh_captcha():
    captcha_text = generate_captcha_text()
    session['captcha_text'] = captcha_text
    return {"success": True}


@app.route('/verify', methods=['POST'])
def verify():
    user_input = request.form.get('captcha_input')
    if user_input == session.get('captcha_text'):
        return '<h2>Captcha Verified Successfully!</h2>'
    else:
        return '<h2>Incorrect Captcha. Try Again!</h2><br><a href="/">Go Back</a>'

if __name__ == '__main__':
    app.run(debug=True)
