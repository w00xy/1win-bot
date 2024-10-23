import asyncio
from flask import Flask, request, jsonify

from database.orm_query import save_user_id_db

app = Flask(__name__)

@app.route("/postback", methods=["POST"])
async def handle_postback():
    user_id = request.form.get("user_id")
    
    if not user_id:
        return jsonify({"error": "Missing user_id"}, 400)
    
    try: 
        await save_user_id_db(user_id)
    except Exception as ex:
        return jsonify({"error": "Failed generation"}, 400)
    
    return jsonify({'message': 'User registered successfully'}), 200


if __name__ == '__main__':
  # Запускаем Flask-приложение
  app.run(debug=True)