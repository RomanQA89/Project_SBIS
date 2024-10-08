Тестовое задание по автоматизации 3 сценариев сайта https://sbis.ru/ компании Тензор.
При проектировании автоматизированных тестов быд применен паттерн PageObject и фреймворки Selenium Webdriver, Pytest.

Папка pages содержит следующие файлы:

- elements.py - функции для взаимодействия с элементами страницы сайта при проведении автотестов;
- base.py - функции для получения главной страницы сайта и пути текущей страницы;
- sbis_loc.py - функции для взаимодействия с url страниц и локаторы для элементов сайта.

Папка tests содержит файл:

- tests.py - UI автотесты, 3 тестовых сценария.

Также имеются такие файлы, как:

- conftest.py - фикстуры для работы с браузером;
- pytest.ini - маркеры для параметризации;
- requirements.txt - используемые при тестировании библиотеки PyCharm.

Инструменты для тестирования:

- PyCharm - воспроизведение автотестов.

Для подготовки к запуску автотестов необходимо установить необходимые библиотеки PyCharm с помощью вводимой команды в консоли терминала:

       pip install -r requirements.txt
   
Также необходимо скачать актуальную версию драйвера для вашего браузера для успешного прохождения автотестов.

Для запуска автотестов необходимо вводить команды в консоли терминала и указывать путь к веб-драйверу, например --driver-path C:\Chrome-selenium\chromedriver.exe

Для запуска всех тестовых сценариев:

       python -m pytest -v --driver Chrome --driver-path <chromedriver_directory>\<chromedriver_file> tests\tests.py -k TestsScenarios

В моём случае была например команда:

       python -m pytest -v --driver Chrome --driver-path C:\Chrome-selenium\chromedriver.exe tests\tests.py -k TestsScenarios

Для запуска теста 1-го сценария:

       python -m pytest -v --driver Chrome --driver-path <chromedriver_directory>\<chromedriver_file> tests\tests.py -k test_first_scenario

Для запуска теста 2-го сценария:

       python -m pytest -v --driver Chrome --driver-path <chromedriver_directory>\<chromedriver_file> tests\tests.py -k test_second_scenario

Для запуска теста 3-го сценария:

       python -m pytest -v --driver Chrome --driver-path <chromedriver_directory>\<chromedriver_file> tests\tests.py -k test_third_scenario



Автотесты также можно запускать с помощью фикстур pytest для всех 3-х сценариев:

Первый сценарий:

       python -m pytest -v --driver Chrome --driver-path <chromedriver_directory>\<chromedriver_file> tests\tests.py -k first_scenario
       
Второй сценарий:

       python -m pytest -v --driver Chrome --driver-path <chromedriver_directory>\<chromedriver_file> tests\tests.py -k second_scenario

Третий сценарий:

       python -m pytest -v --driver Chrome --driver-path <chromedriver_directory>\<chromedriver_file> tests\tests.py -k third_scenario


Окружение: Google Chrome Версия 129, Windows 11 Home (64 бит), Python 3.11
