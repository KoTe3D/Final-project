import Functions_create_order
import Values

# Моренко Данила, 13-я когорта - Финальный проект. Инженер по тестированию плюс
def test_assert_cod_200():
    new_orgder = Functions_create_order.post_create_new_order(Values.user_body)
    save_track = Functions_create_order.save_track_order()
    receiving_an_order_by_track_request = Functions_create_order.get_receiving_an_order_by_track(save_track)

    assert receiving_an_order_by_track_request.status_code == 200
