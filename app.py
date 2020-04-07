import os
import os.path
import subprocess
from flask import Flask, request, render_template, url_for, redirect

app = Flask(__name__)

def is_pdf(name):
    if (name[-4:]=='.pdf'):
        return True
    else :
        return False

@app.route("/download",methods=['POST'])
def download() :
    return '<a href="'+request.args['fileName']+'" download>Download converted file.</a>'
    

@app.route("/")
def fileFrontPage():
    return render_template('fileform.html')

@app.route("/handleUpload", methods=['POST'])
def handleFileUpload():
    if 'photo' in request.files:
        photo = request.files['photo']
        if photo.filename != '' and is_pdf(photo.filename):
            name = str(len([name for name in os.listdir('.') if os.path.isfile(name)]))+'.pdf'
            photo.save(os.path.join('./', name))
            os.system('abiword --to=doc'+ name)
            return '<a href="'+name[:-4]+'.doc'+'" download>Download converted file.</a>'
       # else :
       #     return redirect(url_for('fileErrPage'))
    #else :
     #   return redirect(url_for('fileErrPage'))

    return redirect(url_for('fileFrontPage'))

if __name__=='__main__':
        app.run()