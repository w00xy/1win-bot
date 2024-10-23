import requests


def send_postback(user_id=None, endpoint='http://127.0.0.1:5000/postback'):
    """Отправляет POST-запрос на указанный endpoint с данными user_id.

    Args:
    user_id (int): ID пользователя.
    endpoint (str, optional): URL endpoint Flask-приложения. Defaults to 'http://your_flask_app/postback'.
    """
    data = {'user_id': user_id}
    response = requests.post(endpoint, json=data)

    if response.status_code == 200:
        print(f'User ID {user_id} successfully sent to {endpoint}')
    else:
        print(f'Error sending user ID {user_id} to {endpoint}: {response.text}')

    print("\n", response.json())
    print(f"\n\n {response.text}")


send_postback(user_id=1234444)
