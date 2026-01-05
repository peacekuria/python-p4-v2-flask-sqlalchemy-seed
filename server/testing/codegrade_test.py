# server/testing/codegrade_test.py

import pytest
from faker import Faker

from config import db, create_app
from models import Pet


@pytest.fixture
def app():
    """Create application for testing."""
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()


@pytest.fixture
def client(app):
    """Create a test client for the app."""
    return app.test_client()


class TestPetModel:
    """Tests for the Pet model."""
    
    def test_pet_model_exists(self):
        """Test that Pet model is defined."""
        assert Pet is not None
    
    def test_pet_has_id_column(self):
        """Test that Pet has an id column."""
        assert hasattr(Pet, 'id')
    
    def test_pet_has_name_column(self):
        """Test that Pet has a name column."""
        assert hasattr(Pet, 'name')
    
    def test_pet_has_species_column(self):
        """Test that Pet has a species column."""
        assert hasattr(Pet, 'species')
    
    def test_pet_tablename(self):
        """Test that Pet uses 'pets' as table name."""
        assert Pet.__tablename__ == 'pets'


class TestSeedData:
    """Tests for seeding the database."""
    
    def test_seed_creates_pets(self, app):
        """Test that seeding creates pet records."""
        fake = Faker()
        species = ['Dog', 'Cat', 'Chicken', 'Hamster', 'Turtle']
        
        with app.app_context():
            # Delete existing pets
            Pet.query.delete()
            
            # Create and add pets
            pets = []
            for n in range(5):
                pet = Pet(name=fake.first_name(), species=species[n % len(species)])
                pets.append(pet)
            
            db.session.add_all(pets)
            db.session.commit()
            
            # Verify pets were created
            all_pets = Pet.query.all()
            assert len(all_pets) == 5
    
    def test_seed_uses_faker(self):
        """Test that Faker generates realistic names."""
        fake = Faker()
        name = fake.first_name()
        assert isinstance(name, str)
        assert len(name) > 0
    
    def test_seed_delete_existing(self, app):
        """Test that seed deletes existing pets before adding new ones."""
        fake = Faker()
        
        with app.app_context():
            # Add initial pets
            initial_pet = Pet(name=fake.first_name(), species='Dog')
            db.session.add(initial_pet)
            db.session.commit()
            
            # Delete all and add new pets
            Pet.query.delete()
            pets = []
            for n in range(3):
                pet = Pet(name=fake.first_name(), species='Cat')
                pets.append(pet)
            db.session.add_all(pets)
            db.session.commit()
            
            # Verify only new pets exist
            all_pets = Pet.query.all()
            assert len(all_pets) == 3


class TestPetQueries:
    """Tests for Pet queries."""
    
    def test_filter_by_species(self, app):
        """Test filtering pets by species."""
        fake = Faker()
        
        with app.app_context():
            Pet.query.delete()
            
            # Add cats and dogs
            cat1 = Pet(name=fake.first_name(), species='Cat')
            cat2 = Pet(name=fake.first_name(), species='Cat')
            dog = Pet(name=fake.first_name(), species='Dog')
            
            db.session.add_all([cat1, cat2, dog])
            db.session.commit()
            
            # Filter by species
            cats = Pet.query.filter_by(species='Cat').all()
            dogs = Pet.query.filter_by(species='Dog').all()
            
            assert len(cats) == 2
            assert len(dogs) == 1
    
    def test_pet_count(self, app):
        """Test counting pets."""
        fake = Faker()
        
        with app.app_context():
            Pet.query.delete()
            
            # Add pets
            for _ in range(5):
                pet = Pet(name=fake.first_name(), species='Dog')
                db.session.add(pet)
            db.session.commit()
            
            # Count
            count = Pet.query.count()
            assert count == 5
    
    def test_pet_to_dict(self, app):
        """Test Pet to_dict method."""
        with app.app_context():
            pet = Pet(name='Fido', species='Dog')
            db.session.add(pet)
            db.session.commit()
            
            pet_dict = pet.to_dict()
            
            assert pet_dict['name'] == 'Fido'
            assert pet_dict['species'] == 'Dog'
            assert 'id' in pet_dict


class TestFlaskApp:
    """Tests for Flask app configuration."""
    
    def test_app_creation(self):
        """Test that Flask app can be created."""
        app = create_app()
        assert app is not None
    
    def test_app_has_db(self):
        """Test that app has database configured."""
        app = create_app()
        assert 'SQLALCHEMY_DATABASE_URI' in app.config
        assert 'sqlite://' in app.config['SQLALCHEMY_DATABASE_URI']
    
    def test_app_config_disables_track_modifications(self):
        """Test that app disables SQLALCHEMY_TRACK_MODIFICATIONS."""
        app = create_app()
        assert app.config.get('SQLALCHEMY_TRACK_MODIFICATIONS') is False


def test_codegrade_placeholder():
    """Codegrade placeholder test."""
    assert 1 == 1

