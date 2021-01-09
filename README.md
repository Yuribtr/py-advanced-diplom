# Дипломная работа


## Solution
** Before using pls rename a file "default_keys.py" to "keys.py" and put inside your VK tokens and DB info. Also, please make rebuild=True at VKinderBot __init__ for creating tables. After first launch, you have to revert this option to rebuild=False.
!!!Warning!!! Option rebuild=True will drop ALL tables in given DB each time when application starts.  


1. Bot uses 2 tokens (group token for chat conversations with clients, personal token for making search of users)
2. Bot can receive and remember some client's preferences (country, search history, lists of rated users) which stored in DB
3. Bot controlled by text commands or screen buttons. Bot shows prompts of acceptable commands 
4. Bot can mark VK users as liked, disliked or banned. Bot can show previously rated users
5. Bot and it's components have console logging and some unittests via moked server
6. Bot can speak almost simultaneously with any number of users. There will be delays in commands processing because bot works in single thread
7. Bot can understand commands synonyms, which can be extended
8. Bot supports timeout of client activity and close session if client is absent

Block diagram of main work flow:
![alt text](https://raw.githubusercontent.com/Yuribtr/py-advanced-diplom/master/block_diagram.png?raw=true)

DB diagram:
![alt text](https://raw.githubusercontent.com/Yuribtr/py-advanced-diplom/master/db_diagram.jpg?raw=true)


## VKinder
Все слышали про известное приложение для знакомств - Tinder. Приложение предоставляет простой интерфейс для выбора понравившегося человека. Сейчас в Google Play более 100 миллионов установок.

Используя данные из VK нужно сделать сервис намного лучше чем Tinder, а именно: чат-бота "VKinder". 
Бот должен искать людей, подходящих под условия, на основании информации о пользователе из VK:
- возраст,
- пол,
- город,
- семейное положение.

У тех людей, которые подошли по требованиям пользователю, получать топ-3 популярных фотографии с аватара. Популярность определяется по количеству лайков и комментариев.

За основу можно взять [код из файла basic_code.py](basic_code.py)

## Входные данные
Имя пользователя или его id в ВК, для которого мы ищем пару.
- если информации недостаточно нужно дополнительно спросить её у пользователя.

## Выходные данные
JSON-файл с 10 объектами, где у каждого объекта перечислены топ-3 фотографии и ссылка на аккаунт.

## Требование к сервису:
1. Код программы удовлетворяет`PEP8`.
2. Получать токен от пользователя с нужными правами.
3. Программа декомпозирована на функции/классы/модули/пакеты.
4. Результат программы записывать в БД.
5. Люди не должны повторяться при повторном поиске.
6. Реализовать тесты на базовую функциональность.
7. Не запрещается использовать внешние библиотеки для vk.


## Дополнительные требования (не обязательны для получения диплома):
1. В vk максимальная выдача при поиске 1000 человек. Подумать как это ограничение можно обойти.
2. Добавить возможность ставить/убирать лайк, выбранной фотографии.
3. Можно усложнить поиск добавив поиск по интересам. Разбор похожих интересов(группы, книги, музыка, интересы) нужно будет провести с помощью анализа текста.
4. У каждого критерия поиска должны быть свои веса. То есть совпадение по возрасту должны быть важнее общих групп. Интересы по музыке важнее книг. Наличие общих друзей важнее возраста. И так далее.
5. Добавлять человека в избранный список, используя БД.
6. Добавлять человека в черный список чтобы он больше не попадался при поиске, используя БД.
7. К списку фотографий из аватарок добавлять список фотографий, где отмечен пользователь.
