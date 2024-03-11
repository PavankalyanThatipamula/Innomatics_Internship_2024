from flask import Flask, render_template, request
import re

app = Flask(__name__, template_folder='templates', static_folder='templates', static_url_path='/static')


def validate_email(email):
    # Regex pattern for validating email addresses
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/match', methods=['POST', 'GET'])
def match():
    if request.method == 'POST':
        pattern = request.form['pattern']
        text = request.form['text']
        matches = re.findall(pattern, text)
        return render_template('index.html', matches=matches)
    else:
        return render_template('index.html')


@app.route('/validate_email', methods=['POST'])
def validate_email_route():
    email = request.form['email']
    if validate_email(email):
        return render_template('index.html', success=f'{email} is a valid email address.')
    else:
        return render_template('index.html', error=f'{email} is not a valid email address.')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
