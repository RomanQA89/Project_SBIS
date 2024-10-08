from pages.base import WebPage
from pages.elements import WebElement


class FirstScenario(WebPage):
    """Локаторы для первого сценария."""

    def __init__(self, web_driver, url=''):
        url = 'https://sbis.ru/'
        super().__init__(web_driver, url)

    # Кнопка Контакты
    btn_contacts = WebElement(xpath='//div[contains(text(), "Контакты")]')

    # Ссылка на все офисы в России
    btn_all_contacts = WebElement(class_name='sbisru-Header-ContactsMenu__arrow-icon')

    # Логотип Тензор
    logo = WebElement(xpath='//img[contains(@src, "logo.svg")]')

    # Блок Сила в людях
    strength_in_people = WebElement(xpath='//p[contains(text(), "Сила в людях")]')

    # Ссылка Подробнее о компании
    about_company = WebElement(xpath='//p[@class="tensor_ru-Index__card-text"]//a[@href="/about"]')


class SecondScenario(WebPage):
    """Локаторы для второго сценария."""

    def __init__(self, web_driver, url=''):
        url = 'https://sbis.ru/'
        super().__init__(web_driver, url)

    # Кнопка Контакты
    btn_contacts = WebElement(xpath='//div[contains(text(), "Контакты")]')

    # Ссылка на все офисы в России
    btn_all_contacts = WebElement(class_name='sbisru-Header-ContactsMenu__arrow-icon')

    # Ссылка выбора региона
    link_select_reg = WebElement(xpath='//*[@id="wasaby-content"]/div/div/div[2]'
                                       '/div[1]/div[1]/div[1]/div[2]/ul/li[2]/div/div[2]/div[2]/span/span')
    # Выбор своего региона из списка
    select_reg = WebElement(xpath='//span[contains(text(), "37 Ивановская обл.")]')

    # Обозначение региона в разделе Контакты
    reg_contacts = WebElement(xpath='//*[@id="container"]/div[1]/div/div[3]/div[2]/div[1]/div/div[2]/span/span')

    # Список партнеров для Ивановской обл.
    partner_1 = WebElement(xpath='//div[@title="СБИС - Иваново"]')
    partner_2 = WebElement(xpath='//div[@title="Сервис ТВ-Инфо"]')
    partner_3 = WebElement(xpath='//div[@title="Ванесс"]')

    # Локатор для ссылки выбора региона Камчатский край
    kamchatka_reg = WebElement(xpath='//span[text()="41 Камчатский край"]')

    # Партнер для региона Камчатский край
    kam_reg_par = WebElement(xpath='//div[@title="СБИС - Камчатка"]')


class ThirdScenario(WebPage):
    """Локаторы для третьего сценария."""

    def __init__(self, web_driver, url=''):
        url = 'https://sbis.ru/'
        super().__init__(web_driver, url)

    # Ссылка Скачать локальные версии
    link_down_loc_ver = WebElement(xpath='//a[@href="/download"]')

    # Выбор СБИС Плагина
    sbis_plugin = WebElement(xpath='//div[text()="СБИС Плагин"]')

    # Выбор для Windows
    sbis_windows = WebElement(xpath='//span[text()="Windows"]')

    # Ссылка для скачивания Веб-установщика
    link_down_exe = WebElement(xpath='//a[text()="Скачать (Exe 11.47 МБ) "]')
