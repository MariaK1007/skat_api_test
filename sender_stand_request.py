import requests
import configuration


# Функция на создание заказа
def post_new_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS,
                         json=order_body)


# Функция на получение заказа по треку заказа
def get_new_order(track):
    tracker = {'t': track}
    return requests.get(configuration.URL_SERVICE + configuration.CREATE_ORDERS_TRACK,
                        params=tracker)
