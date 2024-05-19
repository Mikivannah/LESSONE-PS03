import requests
from bs4 import BeautifulSoup

def get_english_wods():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)


        soup = BeautifulSoup(response.content, 'html.parser')
        english_words = soup.find('div', id='random_word').text.strip()
        word_definition = soup.find("div",id="random_word_definition").text.strip()

        return {
            "english_words": english_words,
            "word_definition": word_definition
        }
    except:
        print("произошла ощибка")

def word_game():
    print("Добро пожаловать в игру")
    print("Ваша задача угадать слово")
    while True:
        word_dict = get_english_wods()
        word = word_dict.get("english_words")
        word_definition = word_dict.get("word_definition")

        print(f"Значение слова - {word_definition}")
        user = input("Ваше слово: ")
        if user == word:
            print("Вы угадали")
            break
        else:
            print("Вы не угадали, это слово-", word)

        play_again = input("Хотите сыграть еще? (y/n) ")
        if play_again.lower() != "y":
            print("Спасибо за игру!")
            break


word_game()