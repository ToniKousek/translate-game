from random import choice
import requests
from constants import debug


def get_languages(TRANSLATE_URL: str):
    response = requests.get(f"{TRANSLATE_URL}languages")
    if debug:
        print(response.text)
    response_jsoned = response.json()

    supported_languages: dict[str, str] = {}
    for language in response_jsoned:
        supported_languages.update({language["name"].lower(): language["code"]})

    return supported_languages


def random_language(languages: dict[str, str]):
    # the choice function does not support dictionaries
    # workaround with only the keys inside choice function
    chosen_key = choice(list(languages.keys()))
    return (chosen_key, languages[chosen_key])
