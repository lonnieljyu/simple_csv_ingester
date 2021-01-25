# simple_tsv_ingester

## Setup

1. Install packages in Python environment  
Execute `pip install -r requirements.txt` 

2. Initialize database  
Execute `python initialize_db.py` to initialize the SQLite DB.  
There exists two tables in the DB: `customers` and `purchases`.  

3. Set Flask server's secret key  
Set a secure secret key in `application.secret_key` in `source/__init__.py`  

4. Run the Flask application  
Execute `python application.py`

5. Open browser to Flask website  
The default url is `http://127.0.0.1:5000/`