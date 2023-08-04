import requests
import random
import datetime

api_ninja_key = ''
phrase_file = "folder_of_doom.txt"


def get_cat_fact():
    res = requests.get("https://catfact.ninja/fact").json()
    intro = random.choice([
        "Here's a cat fact. ",
        "Cat fact time. ",
        "Meow",
        "Meeeoooow"
    ])

    return [intro, res.get("fact")]


def get_joke():
    res = requests.get("https://v2.jokeapi.dev/joke/Any?type=single").json()
    intro = random.choice([
        "I have a joke for you. ",
        "Here's a joke. ",
        "Incoming funny. ",
        "hahaha ha haha. ",
    ])

    return [intro, res.get("joke")]


def get_random_phrase():
    intro = random.choice([
        "uhhh. ",
        "ding dong. ",
        "wee woo wee woo. "
    ])

    with open(phrase_file, "r") as file:
        return [intro, random.choice(file.readlines())]


def get_insult():
    res = requests.get("https://evilinsult.com/generate_insult.php?lang=en&type=json").json()
    return [res.get("insult", "")]


def get_random_fact():
    intro = random.choice([
        "Here's a random fact. "
    ])

    limit = 1
    api_url = 'https://api.api-ninjas.com/v1/facts?limit={}'.format(limit)
    response = requests.get(api_url, headers={'X-Api-Key': api_ninja_key})
    if response.status_code == requests.codes.ok:
        return [intro, response.json()[0].get("fact", "")]
    else:
        return f"Error: {response.text}"


def get_random_fact_for_today():
    today = datetime.date.today()
    day = today.day
    month = today.month

    events = []
    text = ''
    tries = 5

    while not events and tries:
        tries -= 1

        api_url = 'https://api.api-ninjas.com/v1/historicalevents?text={}&day={}&month={}&offset={}'.format(text, day, month, random.randint(0, 100))
        response = requests.get(api_url, headers={'X-Api-Key': api_ninja_key})
        if response.status_code == requests.codes.ok:
            events = response.json()
        else:
            print("got error")
            print("Error:", response.status_code, response.text)

    event_info = random.choice(events)
    return [f"Here's an event that happend today in {event_info.get('year', '')}. ", event_info.get("event", "")]


def get_rhymes(word):
    api_url = 'https://api.api-ninjas.com/v1/rhyme?word={}'.format(word)
    response = requests.get(api_url, headers={'X-Api-Key': api_ninja_key})
    if response.status_code == requests.codes.ok:
        return response.json()
    else:
        print("Error:", response.status_code, response.text)


def get_random_word():
    api_url = 'https://api.api-ninjas.com/v1/randomword'
    response = requests.get(api_url, headers={'X-Api-Key': api_ninja_key})
    if response.status_code == requests.codes.ok:
        word = response.json().get("word", "")
        rhymes = get_rhymes(word)

        message = "Here's a random word. " + word
        if rhymes:
            message += ". And some rhymes are " + " ".join( random.sample(rhymes, min(len(rhymes), 5)))
        else:
            message += ". This word has no rhymes. wow"


        return [message]
    else:
        print("Error:", response.status_code, response.text)


def get_joke2():
    api_url = random.choice([
        'https://api.api-ninjas.com/v1/jokes?limit=1',
        'https://api.api-ninjas.com/v1/dadjokes?limit=1'
    ])
    response = requests.get(api_url, headers={'X-Api-Key': api_ninja_key})
    if response.status_code == requests.codes.ok:
        return ["Here's a joke", response.json()[0].get("joke", "")]
    else:
        print("Error:", response.status_code, response.text)



