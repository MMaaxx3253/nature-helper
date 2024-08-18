from defs import *
from flask import Flask, render_template,request, redirect
startup()
print("LOG beginning...")
print("")

app = Flask(__name__)

#Запуск страницы с контентом
@app.route('/')
def index():
    return render_template('index.html')


#Динамичные скиллы
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    return render_template('index.html', button_python=button_python)
def discd():
    button_discord = request.form.get('button_discord')
    return render_template('index.html', button_discord=button_discord)
def html_base():
    button_html = request.form.get('button_html')
    return render_template('index.html', button_html=button_html)
def diary():
    button_db = request.form.get('button_db')
    return render_template('index.html', button_db=button_db)


if __name__ == "__main__":
    app.run()
else:
    print("ERROR: Names does not match, exiting")
print("")
print("LOG ending, exit in 3 seconds...")
time.sleep(3)
exit