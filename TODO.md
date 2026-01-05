# TODO: Fix Flask-SQLAlchemy Seed Project

## Issues Found:
1. Circular import between app.py and models.py
2. Duplicate db definition in app.py
3. Incomplete models.py without proper Flask app context
4. Basic seed.py that doesn't use Faker
5. Placeholder test that doesn't test anything meaningful

## Plan:
- [x] 1. Create config.py with Flask app and db configuration to break circular imports
- [x] 2. Update models.py to import db from config and define Pet model
- [x] 3. Fix app.py to properly import from config
- [x] 4. Update seed.py to use Faker for generating 10 random pets
- [x] 5. Add comprehensive tests in codegrade_test.py
- [x] 6. Run tests to verify everything works

## Summary:
- Created `server/config.py` with Flask app factory and database configuration
- Updated `server/models.py` to import db from config and define Pet model with to_dict method
- Simplified `server/app.py` to use config module
- Updated `server/seed.py` to use Faker for generating 10 random pets with species from a list
- Added comprehensive tests in `server/testing/codegrade_test.py` (15 tests)
- All 15 tests pass
- Seed script successfully seeds 10 pets to the database

