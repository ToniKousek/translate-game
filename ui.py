import tkinter as tk
from languages import get_languages, random_language
from sentences import random_sentence

from main import translate_sentence, check_input
from constants import debug, TRANSLATE_URL, BEGIN_LIVES


def refresh_sentence():
    global sentence, language, translated_sentence
    sentence = random_sentence()
    language = random_language(supported_languages)
    translated_sentence = translate_sentence(sentence, language)
    sentence_widget.configure(text=translated_sentence)


def button_pressed():
    global lives, score
    checked_input = check_input(input.get(), supported_languages, language)
    match checked_input:
        case 0:
            pass
        case 1:
            print("Correct!")
            score += 1
            score_widget.configure(text=f"Score: {score}")
            refresh_sentence()
        case 2:
            print("Incorrect!")
            lives -= 1
            lives_widget.configure(text=f"Lives: {lives}")
        case _:
            raise NotImplementedError

    # check lives
    if lives <= 0:
        print("No lives left!")
        window.quit()


# setup game
if debug:
    print("Started!")
supported_languages = get_languages(TRANSLATE_URL)

lives = BEGIN_LIVES
score = 0

# setup tkinter ui
window = tk.Tk()

lives_widget = tk.Label(window, text=f"Lives: {lives}")
lives_widget.grid(column=0, row=0, padx=5, pady=5)
score_widget = tk.Label(window, text=f"Score: {score}")
score_widget.grid(column=1, row=0, padx=5, pady=5)

title = tk.Label(text="In what language is this sentence written in?")
title.grid(column=0, row=1, columnspan=2, padx=5, pady=5)

input = tk.StringVar(window)
menu = tk.OptionMenu(window, input, *tuple(supported_languages.keys()))
menu.grid(column=0, row=3, padx=5, pady=5)

button = tk.Button(window, text="Check input", command=button_pressed)
button.grid(column=1, row=3, padx=5, pady=5)

# get the sentence
sentence = random_sentence()
language = random_language(supported_languages)
translated_sentence = translate_sentence(sentence, language)
if debug:
    print(f"'{language}' selected")
    print(f"'{translated_sentence}' translated")

sentence_widget = tk.Label(window, text=translated_sentence)
sentence_widget.grid(column=0, columnspan=2, row=2, padx=5, pady=5)


window.mainloop()
