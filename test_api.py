import requests

URL_APP = "http://127.0.0.1:8000"
URL_ITEM_IT = URL_APP + "/items/"


# 32?q=%22ciccio%22

def get_items(item_id: int, q: str | None):
    call = URL_ITEM_IT + str(item_id)
    if q is not None:
        call += f"?q=%22{q}%22"
        return requests.get(call).json()


if __name__ == '__main__':
    response = get_items(12, "foo")
    print(response["result"])
