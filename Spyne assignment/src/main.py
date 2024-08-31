from flask import Flask
from api import upload_api, status_api
import database

app = Flask(__name__)

# Register API endpoints
app.register_blueprint(upload_api)
app.register_blueprint(status_api)

if __name__ == "__main__":
    database.init_db()
    app.run(host="0.0.0.0", port=5000)
