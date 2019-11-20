import requests


def catapi():
    try:
        r = requests.get('https://api.thecatapi.com/v1/images/search')
        r.raise_for_status()
        list = r.json()
        cat = list[0]['url']
        return cat


    except Exception as err:
        print(f'Other error occurred: {err}')
        return None

def rubapi():
    try:
        r = requests.get('https://api.exchangerate-api.com/v4/latest/RUB')
        r.raise_for_status()
        dict_rub = r.json()
        eur = dict_rub['rates']['EUR']
        return eur

    except Exception as err:
        print(f'Other error occurred: {err}')
        return None

def kanyeapi():
    try:
        r = requests.get('https://api.kanye.rest')
        r.raise_for_status()
        kanye_dict = r.json()
        kanye = kanye_dict['quote']
        return kanye

    except Exception as err:
        print(f'Other error occurred: {err}')
        return None
