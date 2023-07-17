# Translate game

Uses [Libre translate](https://libretranslate.com/)

## Installing:

- Install the latest python interpreter
- Tested on Python==3.10.5
- Clone this repository

```
git clone https://github.com/ToniKousek/translate-game.git
cd translate-game
```

- Download packages

```
pip install -r requirements.txt
```

- Setup Libre translate

```
libretranslate
```

- Wait until the download finishes and it says `Running on http://127.0.0.1:5000`

## To play in terminal, run:

```
libretranslate --disable-files-translation --disable-web-ui
python main.py
```

## To play with a UI:

```
libretranslate --disable-files-translation --disable-web-ui
python ui.py
```

UI is coded in [tkinter](https://docs.python.org/3/library/tkinter.html)
