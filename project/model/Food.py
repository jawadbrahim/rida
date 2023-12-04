from database.postgres import db

class Food(db.Model):
    category=db.Column(db.String(250))
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250))
    description = db.Column(db.Text)
    picture = db.Column(db.String(500))
    ingredients = db.Column(db.String(1000))
   

    
    
