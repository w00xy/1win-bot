from flask import Flask, request, jsonify

from database import db


app = Flask(__name__)


@app.route('/postback', methods=['POST'])
def postback():
    data = request.get_json()
    print(data)

    if "user_id" not in data:
        return jsonify(msg="Missing user_id"), 400

    user_id = data["user_id"]
    try:
        int(user_id)
    except Exception as e:
        return jsonify(msg="Wrong user_id. Must be Number")

    cur, con = db()

    try:
        con.execute("INSERT INTO win_users (user_id) VALUES (?)", (user_id, ))
        con.commit()
        msg = "Successful Insert"
    except Exception as e:
        con.rollback()
        msg = f"{e}"

    con.close()

    return jsonify(msg="Successful Insert")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port="5000")