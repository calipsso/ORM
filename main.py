from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify
from flask import request

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://urici3i0icy8cuufham5:FrtbL6FqnCsROZMWocDBkgoOeoZC7R@b81s1xhecmfxnpmteb27-postgresql.services.clever-cloud.com:50013/b81s1xhecmfxnpmteb27"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

from Authors import Author
from Member import Member

@app.route("/authors/", methods=['GET'])
def getAuthors():
    authors = Author.query.all()

    author_list = [
        {"author_id": author.author_id, "name": author.name, "bio": author.bio}
        for author in authors
    ]
    #author_list = [aut.to_dict() for aut in authors] pri tejto moznosti treba dorobit funkciu to_dict do file author
    return jsonify (author_list)

@app.route("/members/all", methods=['GET'])
def getMembers():
    members=Member.query.all()

    member_list = [mem.to_dict() for mem in members] # pri tejto moznosti treba dorobit funkciu to_dict do file author
    return jsonify (member_list)

@app.route("/member/id", methods=["GET"])
def getMemID():
    member_id = request.args.get("member_id")

    if member_id:
        memID = Member.query.filter_by(member_id=member_id)
    else:
        return jsonify({"Zadaj minimalne jeden parameter, title alebo name autora."}), 400

    member_list = [
        {"member_id":memID.member_id, "first_name": memID.first_name, "last_name": memID.last_name, "email":memID.email, "registration_date":memID.registration_date, "password": memID.password  }
        for memID in memID
    ]
    return jsonify(member_list)


@app.route("/member/inputMEM", methods=["POST"])
def insertMem():
    data = request.json

    first_name = data.get('first_name')
    last_name = data.get('last_name')
    email = data.get('email')
    registration_date = data.get("registration_date")
    password = data.get('password')

    if not (first_name and last_name and email and password):
        return jsonify({"error": "Missing required fields"}), 400


    new_member = Member(first_name=first_name, last_name=last_name, email=email, registration_date=registration_date, password=password)


    db.session.add(new_member)
    db.session.commit()

    return jsonify({"message": "Member registered successfully"}), 200

if __name__ == "__main__":
    app.run(debug=True)