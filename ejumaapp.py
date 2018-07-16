from flask import Flask

app = Flask(__main__)

@app.route('/')
def index():
    return "<h1>it worked</h1>"

if __name__=='__main__':
    import os
    app.run(host='0.0.0.0', debug=True, os.environ.get('PORT',8000))
    
