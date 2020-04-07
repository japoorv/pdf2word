import os
import os.path
import subprocess
from flask import Flask, request, render_template, url_for, redirect, send_file,send_from_directory

app = Flask(__name__)

def is_pdf(name):
    if (name[-4:]=='.pdf'):
        return True
    else :
        return False

@app.route("/")
def fileFrontPage():
    return render_template('fileform.html')

@app.route("/handleUpload", methods=['POST'])
def handleFileUpload():
    if 'photo' in request.files:
        photo = request.files['photo']
        if photo.filename != '' and is_pdf(photo.filename):
            curr_path=os.getcwd()
            name = str(len([name for name in os.listdir('.') if os.path.isfile(name)]))+'.pdf'
            photo.save(name)
            os.system('./abiword --to=doc '+ name)
            fileName = name[:-4]+'.doc'
            return send_from_directory(os.getcwd(),fileName,as_attachment=True,attachment_filename=photo.filename[:-4]+'.doc')

       # else :
       #     return redirect(url_for('fileErrPage'))
    #else :
     #   return redirect(url_for('fileErrPage'))

    return redirect(url_for('fileFrontPage'))
if __name__=='__main__':
        app.run()