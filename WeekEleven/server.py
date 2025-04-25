from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/demo')
def demo():
    title = 'helloo'
    desc = 'This is a demo page with data passed from the backend.'
    
    if (title == 'hello'):
        title = 'COSC1104'
    
    return render_template(template_name_or_list='index.html', title=title, desc=desc)

if __name__ == '__main__':
    app.run(port=5555, debug=True)