from defs import *
from flask import Flask, render_template,request, redirect
import codecs
startup()
print("LOG beginning...")
print("")

app = Flask(__name__)

#Запуск страницы с контентом
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/eng',methods=['GET','POST'])
def eng():
    return render_template('english.html')
    
@app.route('/rus',methods=['GET','POST'])
def rus():
    return render_template('russian.html')

@app.route('/submit', methods=['GET','POST'])
def submit_form():
    email = request.form['email']
    comment = request.form['comment']
    with codecs.open('forms.text', 'a', 'utf-8') as f:
            f.write(email+'\n')
            f.write(comment+'\n')
            f.write("-------------"+'\n')
    return render_template('submit.html',
                           email=email,
                           comment=comment
                           )

if __name__ == "__main__":
    app.run()
print("")
print("LOG ending, exit in 3 seconds...")
time.sleep(3)
exit