# server/models.py

from config import db


class Pet(db.Model):
    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    species = db.Column(db.String)

    def __repr__(self):
        return f'<Pet {self.id}, {self.name}, {self.species}>'

    def to_dict(self):
        """Convert Pet instance to dictionary for JSON serialization."""
        return {
            'id': self.id,
            'name': self.name,
            'species': self.species
        }

