from app.data.database import Base, engine
import app.models

# WINDOWS
# $env:PYTHONPATH = "."
# python app/scripts/create_tables.py
# UNIX:
# PYTHONPATH=. python app/scripts/create_tables.py

Base.metadata.create_all(bind=engine)
