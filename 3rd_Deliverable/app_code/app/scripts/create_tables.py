from app.data.database import Base, engine
import os
import app.models

# WINDOWS
# $env:PYTHONPATH = "."
# python app/scripts/create_tables.py
# UNIX:
# PYTHONPATH=. python app/scripts/create_tables.py
os.remove("app_data.db")
Base.metadata.create_all(bind=engine)
