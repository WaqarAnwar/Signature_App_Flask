 
from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)
 
@app.route('/', methods=['GET', 'POST'])
def signature_app():
    if request.method == 'GET':
        return render_template("signature.html")
    
if __name__ == '__main__':
    app.run()