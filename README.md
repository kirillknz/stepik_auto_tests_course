# Readme
## Для рецензии задания "запуск автотестов для разных языков интерфейса"

### Умышленно оставлен Firefox для запуска

Комананда для запуска:
```sh
   pytest --language=es --browser_name=chrome test_items.py
```
- languages - en, ru, fr & etc
- browser_name - chrome, firefox
- для увеличения времени ожидания в файле _test_items.py_ следует убрать _'#'_ у time.sleep(30) 

## Шаги в сценарии 

- Открытие страницы на языке из параметров
- Проверка кнопки корзины
- Закрытие браузера




# _Автоматизация тестирования с помощью Selenium и Python_

![N|Solid](https://selenium-python.com/wp-content/uploads/2017/11/cropped-logo-mini.png)

В рамках задачи были выполнены цели:

- Разработка тестового сценария
- Оформление файла README.md
- Создание репозитория\добавление файлов
- ✨Удовлетворение от результата✨

> ***Все работы производились в PyCharm (Python, Selenium WebDriver), VCS для работы с Git***
- [Selenium WebDriver](https://www.selenium.dev/documentation/webdriver/)
- [PyCharm](https://www.jetbrains.com/ru-ru/pycharm/)
- [VCS](https://www.jetbrains.com/help/pycharm/enabling-version-control.html)

## Справочники, библиотеки


| Libary           | README                                             |
|------------------|----------------------------------------------------|
| Selenium         | [selenium.dev/documentation][PlDb]                   |
| Python           | [python.org/library][PlGh] |
| CSS Diner        | [flukeout.github.io][PlGd]                |
| CSS Selector     | [www.w3schools.com][PlOd]                 |



## Installation Selenium (Windows)

Загрузить [Python](https://www.python.org/downloads/) для Windows

Затем установить Selenium WebDriver с помощью Pip:
```sh
   pip install selenium  
```

Если приведенная выше команда вызывает ошибку, вы можете выполнить команду pip с помощью флага -m . *Флаг -m обозначает имя модуля и позволяет передать модуль во время вызова Python*:
```sh
   python -m pip install selenium  
```
### _Это вовсе не конец. Файл будет пополняться_ 
![progress](http://www.yarntomato.com/percentbarmaker/button.php?barPosition=28&leftFill=%23FF0000 "progress")



[![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Courier+Prime&size=30&color=000000&lines=Good+luck)](https://git.io/typing-svg)





[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)


   [PlDb]: <https://www.selenium.dev/documentation/>
   [PlGh]: <https://docs.python.org/3/library/index.html>
   [PlGd]: <https://flukeout.github.io/#>
   [PlOd]: <https://www.w3schools.com/cssref/trysel.asp?selector=b:only-child>
