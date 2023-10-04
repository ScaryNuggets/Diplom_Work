
import configurations
import requests
import data
def post_new_order(body):
    return requests.post(configurations.URL_SERVICE + configurations.CREATE_USER_ORDER,
                         json=body)
def get_new_order(track):
    return requests.get(configurations.URL_SERVICE+configurations.GETS_NEW_ORDER,
                        params=track);

