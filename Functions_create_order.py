import Configuration
import requests
import Values


# POST запрос для создания заказа
def post_create_new_order(body):

    return requests.post(Configuration.URL_SERVICE + Configuration.CREATE_NEW_ORDER,
                         json=body,
                         headers=Values.headers1)

response_create_new_order = post_create_new_order(Values.user_body)


# Сохранение номера заказа
def save_track_order():
    save_track = response_create_new_order

    return save_track.json()['track']

track_number = save_track_order()


# GET запрос на получение заказа по его номеру
def get_receiving_an_order_by_track(track_number):

    return requests.get(Configuration.URL_SERVICE + Configuration.RECEIVING_AN_ORDER_BY_TRACK + str(track_number))

response_receiving_an_order_by_track = get_receiving_an_order_by_track(track_number)
