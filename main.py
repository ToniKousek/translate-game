import time
import requests

from languages import get_languages, random_language
from sentences import random_sentence

from constants import debug, TRANSLATE_URL, FRONTEND_LANGUAGE, BEGIN_LIVES

"""
TODO:
- error handling for database
"""

high_score = 0
lives = BEGIN_LIVES


def print_languages(languages: list[str]):
    print(f"There are {len(languages)} languages supported:")
    for language in languages:
        print(f"{language}{' '*4}", end="")
    print(end="\n")


def translate_sentence(sentence: str, language: tuple[str, str]):
    payload = {
        "q": sentence,
        "source": FRONTEND_LANGUAGE,
        "target": language[1],
    }
    response = requests.post(f"{TRANSLATE_URL}translate", params=payload)
    if debug:
        print(response.text)
    return response.json()["translatedText"]


def get_input(
    languages: dict[str, str],
    translated_sentence: str,
    correct_language: tuple[str, str],
):
    global high_score, lives

    while True:
        print("What language do you think is this sentence?")
        print(translated_sentence)
        selected = input().lower().strip()
        output = check_input(selected, languages, correct_language)
        match output:
            case 0:
                print("That isn't a supported language\n")
            case 1:
                print("That is correct!")
                print("SCORE ++")
                high_score += 1
                break
            case 2:
                print("That is not the right language!")
                lives -= 1
                print(f"Current lives: {lives}\n")
                print(f"The correct language is: {correct_language[0]}")

            case _:
                print("There has been an error!")
                print("Exiting!")
                exit(1)

        if lives <= 0:
            print("You ran out of lives!")
            print(f"Score is {high_score}")
            print("Exiting!")
            time.sleep(3)
            exit(1)


def check_input(
    input: str,
    languages: dict[str, str],
    correct_language: tuple[str, str],
):
    """Checks the input of the user.\n
    returns Literal[0] if input is not in the language list\n
    returns Literal[1] if input is correct\n
    returns Literal[2] if input isn't correct"""

    if input not in list(languages.keys()):
        return 0
    if input == correct_language[0].lower():
        return 1
    else:
        return 2


if __name__ == "__main__":
    if debug:
        print("Started!")
    supported_languages = get_languages(TRANSLATE_URL)
    print_languages(list(supported_languages.keys()))

    while True:
        print(f"Next game!\nScore: {high_score}\nLives: {lives}")
        sentence = random_sentence()
        language = random_language(supported_languages)
        translated_sentence = translate_sentence(sentence, language)
        if debug:
            print(f"'{language}' selected")
            print(f"'{translated_sentence}' translated")
        get_input(supported_languages, translated_sentence, language)
