import pyrebase
from flask import *
from datetime import datetime
from pytz import timezone


config = {
    "apiKey": "AIzaSyBavssQSz59apFNPAp8f1SvCJNX2nsi8JU",
    "authDomain": "gallery-ed37a.firebaseapp.com",
    "databaseURL": "https://gallery-ed37a-default-rtdb.asia-southeast1.firebasedatabase.app",
    "projectId": "gallery-ed37a",
    "storageBucket": "gallery-ed37a.appspot.com",
    "messagingSenderId": "32337441535",
    "appId": "1:32337441535:web:d059b311ccb8707d0312ca",
    "measurementId": "G-S8ZP49B45K"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

# insert
# db.child("test").push({"1": "google"})

# update
# db.child("img_url").child("person").update({"1": "google2"})

# select
# company = db.child("name").child("name").get()

# remove



app = Flask(__name__)



def get_now():
    now_str = datetime.now(timezone('Asia/Seoul')).strftime('%Y%m%d_%H%M%S')

    return now_str



@app.route('/', methods=['POST', 'GET'])
def main():
    if request.method == 'POST':
        text = request.form['img_file']
        now_str = get_now()
        if text != '':
            db.child("img_url").child("person").update({now_str:text})
            return render_template('index.html', todo=now_str)
        
        else :
            return render_template('index.html', todo="check again, no value")
        
    return render_template('index.html', todo="no working")


if __name__ == '__main__':
    app.run(debug=True)
