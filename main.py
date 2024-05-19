import requests
from bs4 import BeautifulSoup
from googletrans import Translator


def get_words_and_definitions():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        english_word = soup.find('div', id='random_word').text.strip()
        english_definition = soup.find("div", id="random_word_definition").text.strip()

        translator = Translator()
        russian_word = translator.translate(english_word, dest='ru').text
        russian_definition = translator.translate(english_definition, dest='ru').text

        return {
            "russian_word": russian_word,
            "russian_definition": russian_definition
        }
    except:
        print("Произошла ошибка")


def word_game():
    print("Добро пожаловать в игру")
    print("Ваша задача угадать слово")

    while True:
        word_dict = get_words_and_definitions()
        word = word_dict.get("russian_word")
        word_definition = word_dict.get("russian_definition")

        print(f"Значение слова - {word_definition}")
        user = input("Ваше слово: ")

        if user == word:
            print("Вы угадали")
            break
        else:
            print("Вы не угадали, это слово -", word)

        play_again = input("Хотите сыграть еще? (y/n) ")
        if play_again.lower() != "y":
            print("Спасибо за игру!")
            break


word_game()