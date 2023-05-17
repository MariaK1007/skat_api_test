import configuration
import requests
import data


# Функция на создание заказа
def post_new_order():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS,
                         json=data.orders_body)


# Сохраняем номер трека заказа в переменную
tracker = post_new_order().json()['track']


# Функция на получение заказа по треку заказа
def get_new_order():
    body = data.orders_body.copy()
    return requests.get(configuration.URL_SERVICE + configuration.CREATE_ORDERS_TRACK + str(tracker),
                        json=body)


# Тест на проверку кода 200
def test_create_order_get_success_response():
    body_response = get_new_order()
    assert body_response.status_code == 200
