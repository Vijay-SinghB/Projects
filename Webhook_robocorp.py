from flask import Flask, request, render_template, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
<html>
<head>
    <title>Get Username</title>
</head>
<body>
    <h1>What's your name?</h1>
    <form method="POST">
        <input type="text" name="name">
        <input type="submit" value="Submit">
    </form>
</body>
</html>
    '''
    
@app.route('/', methods=['POST'])
def process_form():
    name = request.form['name']
    message = f'Hello, {name}!'
    return f'<script>alert("{message}"); window.location.href="/";</script>'
    
if __name__ == '__main__':
    app.run(port=5005)
