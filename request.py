# Строилов Дмитрий, 8-я когорта — Финальный проект. Инженер по тестированию плюс
import stand_request
import data

def test_track_send():
    resp_body = stand_request.post_new_order(data.order_body)
    resp={"t": resp_body.json()["track"]}
    response_order_by_track = stand_request.get_new_order(resp)
    assert response_order_by_track.status_code == 200


