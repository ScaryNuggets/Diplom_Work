import configurations
import requests
import data
def post_new_order(body):
    return requests.post(configurations.URL_SERVICE + configurations.CREATE_USER_ORDER,  # подставляем полный url
                         json=body)
def get_new_order():
    return requests.get(configurations.URL_SERVICE+configurations.GETS_NEW_ORDER+str(response.json().get('track')))

def positive_assert(track):
    # Проверяется, что код ответа равен 200
    assert response2.status_code == 200