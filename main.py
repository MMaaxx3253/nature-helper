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

@app.route('/eng')
def index():
    return render_template('english.html')
    
@app.route('/rus')
def index():
    return render_template('russian.html')

@app.route('/submit',methods=['POST'])
def submit_form():
    email = request.form['email']
    comment = request.form['comment']
    with open('forms.txt', 'a',) as f:
            f.write(email+'\n')
            f.write(comment+'\n')
    return render_template('forms.text',
                           email=email,
                           comment=comment
                           )

if __name__ == "__main__":
    app.run()
else:
    print("ERROR: Names does not match, exiting")
print("")
print("LOG ending, exit in 3 seconds...")
time.sleep(3)
exit