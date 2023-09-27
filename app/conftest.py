import os

# changes MODE variable (db URI) in .env when pytest is running
os.environ["MODE"] = "TEST"
