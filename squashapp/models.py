from squashapp import db, app

class Player(db.Model):
    id = db.Column(Db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nulable=False)
    last_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    
