import requests

api_key = ""
ha_url = "http://10.0.0.10:8123"

ha_headers = {
    "Authorization": f"Bearer {api_key}",
    "content-type": "application/json",
}

def ha_get(resource, data={}):
    return requests.get(ha_url + resource, headers=ha_headers, json=data)


def ha_post(resource, data={}):
    return requests.post(ha_url + resource, headers=ha_headers, json=data)


def get_entity_status(entity_id):
    return ha_get(f"/api/states/{entity_id}").json()


def send_hoeass_tts(message, entity_id):
    print(message)
    data = {
        "entity_id": entity_id,
        "message": message,
    }

    res = ha_post("/api/services/tts/google_translate_say", data=data)
    print(res.text)
    return res.status_code == 200


def is_jokepod_playing(entity_id):
    states = get_entity_status(entity_id)
    return states.get("state") == "playing"
