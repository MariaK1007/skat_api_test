import sender_stand_request
import data


# Функция на сохранение трека заказа
def get_order_track():
    response_body = sender_stand_request.post_new_order(data.order_body)
    return response_body.json()['track']


# Тест на проверку кода 200
def test_get_order_by_track():
    track = get_order_track()
    body_response = sender_stand_request.get_new_order(track)
    assert body_response.status_code == 200