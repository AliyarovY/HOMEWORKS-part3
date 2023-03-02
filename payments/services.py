import requests
import json
import os


def yookassa_pay(amount):
    # создание словаря с параметрами запроса и передача его в метод requests.post
    url = 'https://api.yookassa.ru/v3/payments'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {os.getenv("API_KEY")}'
    }
    data = {
        'amount': {
            'value': f'{amount}',
            'currency': 'RUB'
        },
        'description': 'Оплата',
        'confirmation': {
            'type': 'embedded',
        }
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))

    # Получение данных о созданном счете
    if response.status_code == 200:
        payment_id = response.json()['id']
        url = f'https://api.yookassa.ru/v3/payments/{payment_id}'
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            payment_data = response.json()

    # Проверка статуса платежа и получение подтверждения оплаты
    if payment_data['status'] == 'waiting_for_capture':
        url = f'https://api.yookassa.ru/v3/payments/{payment_id}/capture'
        response = requests.post(url, headers=headers)
        return response.status_code == 200
