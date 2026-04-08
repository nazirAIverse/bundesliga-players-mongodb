from mongoengine import Document, StringField, IntField, FloatField

class Player(Document):
    meta = {"collection": "players"}

    name = StringField(required=True)
    age = IntField()
    height = FloatField()
    nationality = StringField()
    price = IntField()
    max_price = IntField()
    position = StringField()
    club = StringField()