import random
import time
from api_functions import (
    get_joke,
    get_cat_fact,
    get_random_phrase,
    get_insult,
    get_random_fact,
    get_random_word,
    get_joke2,
    get_random_fact_for_today,
)
from ha_api import (
    is_jokepod_playing,
    send_hoeass_tts,
)


jokepod_id = "media_player.chrispod_mini"
min_sleep_mins = 10
max_sleep_mins = 30


def wait():
    sleep_time = random.randint(min_sleep_mins, max_sleep_mins)
    print(f"Waiting {sleep_time} minutes...")
    time.sleep(sleep_time * 60)


def main():
    message_functions = [
        get_joke,
        get_cat_fact,
        get_random_phrase,
        get_insult,
        get_random_fact,
        get_random_word,
        get_joke2,
        get_random_fact_for_today,
    ]

    send_hoeass_tts("random speech started", jokepod_id)

    while True:
        wait()

        if is_jokepod_playing(jokepod_id):
            print(f"JokePod {jokepod_id} is currently playing. Skipping...")
            continue

        message_function = random.choice(message_functions)
        try:
            for message in message_function():
                if not send_hoeass_tts(message, jokepod_id):
                    send_hoeass_tts("nevermind, we got an error", jokepod_id)
        except Exception as e:
            send_hoeass_tts(f"Error getting message from {message_function.__name__}: {e}", jokepod_id)




if __name__ == "__main__":
    main()



