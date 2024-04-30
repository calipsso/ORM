from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://urici3i0icy8cuufham5:FrtbL6FqnCsROZMWocDBkgoOeoZC7R@b81s1xhecmfxnpmteb27-postgresql.services.clever-cloud.com:50013/b81s1xhecmfxnpmteb27"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

from Authors import Author

@app.route("/authors/", methods=['GET'])
def getAuthors():
    authors = Author.query.all()
    return authors



if __name__ == "__main__":
    app.run(debug=True)