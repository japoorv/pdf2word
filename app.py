import os
from flask import Flask, request, render_template, url_for, redirect

app = Flask(__name__)

def is_pdf(name):
    if (name[-4:]=='.pdf'):
        return True
    else 
        return False
        
@app.route("/")
def fileFrontPage():
    return render_template('fileform.html')
    
@app.route("/handleUpload", methods=['POST'])
def handleFileUpload():
    if 'photo' in request.files:
        photo = request.files['photo']
        if photo.filename != '' and is_pdf(photo.filename):
            photo.save(os.path.join('./', '1.pdf'))
        else 
            
    return redirect(url_for('fileFrontPage'))

if __name__=='__main__':
        app.run()