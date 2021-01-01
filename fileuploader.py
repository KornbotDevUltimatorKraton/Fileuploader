from flask import *  
import os 
app = Flask(__name__)
app.secret_key = os.urandom(64)
PATH = "/home/"
FILE = "/Fileuploader/static/app/uploads/"
@app.route('/')  
def upload():  
    return render_template("file_upload_form.html")  
 
@app.route('/success', methods = ['POST'])  
def success():  
    if request.method == 'POST':  
        f = request.files['file'] 
        print(f)
        print(f.filename)  
        f.save(PATH +"kornbotdev"+FILE+f.filename)
          
        return render_template("success.html", name = f.filename)  
  
if __name__ == '__main__':  
    app.run(debug = True)  
