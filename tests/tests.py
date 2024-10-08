import os
import requests
import time
import pytest
from pages.sbis_loc import FirstScenario, SecondScenario, ThirdScenario
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class TestsScenarios:
    """Тесты для трех сценариев."""

    @pytest.mark.first_scenario
    def test_first_scenario(self, web_browser):
        """Проверка первого сценария."""

        page = FirstScenario(web_browser)

        WebDriverWait(web_browser, 15).until(EC.presence_of_element_located((
            By.XPATH, '//div[contains(text(), "Контакты")]')))
        page.btn_contacts.click()

        WebDriverWait(web_browser, 15).until(EC.presence_of_element_located((
            By.CLASS_NAME, 'sbisru-Header-ContactsMenu__arrow-icon')))
        page.btn_all_contacts.click()

        WebDriverWait(web_browser, 15).until(EC.presence_of_element_located((
            By.XPATH, '//img[contains(@src, "logo.svg")]')))
        page.logo.click()

        # Получение всех идентификаторов окон (вкладок)
        browser_tabs = web_browser.window_handles

        # Переключение на последнюю вкладку (новую)
        web_browser.switch_to.window(browser_tabs[-1])

        # Поиск раздела "Сила в людях", до которого нужно проскроллить
        strength_in_people = web_browser.find_element(By.XPATH, '//p[contains(text(), "Сила в людях")]')

        # Прокрутка страницы до раздела
        web_browser.execute_script("arguments[0].scrollIntoView();", strength_in_people)

        # Проверка наличия блока "Сила в людях"
        assert page.strength_in_people.is_presented()

        WebDriverWait(web_browser, 15).until(EC.presence_of_element_located((
            By.XPATH, '//p[@class="tensor_ru-Index__card-text"]//a[@href="/about"]')))
        page.about_company.click()

        # Поиск раздела "Работаем" и прокрутка до него
        work = web_browser.find_element(By.XPATH, '//h2[contains(text(), "Работаем")]')
        web_browser.execute_script("arguments[0].scrollIntoView();", work)

        web_browser.implicitly_wait(10)

        # Поиск всех четырёх фотографий в разделе "Работаем", общий локатор для 4 фото.
        photos = web_browser.find_elements(By.XPATH, '//img[@width="270" and @height="192"]')

        # Получение высоты и ширины первой фотографии для сравнения
        first_photo_height = photos[0].get_attribute('height')
        first_photo_width = photos[0].get_attribute('width')

        # Проверка, что нашлось ровно 4 фотографии
        assert len(photos) == 4, f"Ожидалось 4 фотографии, найдено: {len(photos)}"

        # Проверка, что все фотографии имеют одинаковую высоту и ширину
        for photo in photos:
            height = photo.get_attribute('height')
            width = photo.get_attribute('width')

            # Сверяем высоту и ширину каждого фото с первой фотографией
            assert height == first_photo_height, f"Фото {photo} имеет другую высоту: {height}"
            assert width == first_photo_width, f"Фото {photo} имеет другую ширину: {width}"

    @pytest.mark.second_scenario
    def test_second_scenario(self, web_browser):
        """Проверка второго сценария."""

        page = SecondScenario(web_browser)

        WebDriverWait(web_browser, 15).until(EC.presence_of_element_located((
            By.XPATH, '//div[contains(text(), "Контакты")]')))

        page.btn_contacts.click()

        WebDriverWait(web_browser, 15).until(EC.presence_of_element_located((
            By.XPATH, '//*[@id="wasaby-content"]/div/div/div[2]'
                      '/div[1]/div[1]/div[1]/div[2]/ul/li[2]/div/div[2]/div[2]/span/span')))

        page.link_select_reg.click()

        WebDriverWait(web_browser, 15).until(EC.presence_of_element_located((
            By.XPATH, '//span[contains(text(), "37 Ивановская обл.")]')))

        page.select_reg.click()

        WebDriverWait(web_browser, 15).until(EC.presence_of_element_located((
            By.CLASS_NAME, 'sbisru-Header-ContactsMenu__arrow-icon')))

        page.btn_all_contacts.click()

        # Проверка, что в разделе Контакты указан регион Ивановская обл. и есть список партнеров
        assert page.reg_contacts.get_attribute('innerText') == 'Ивановская обл.'
        assert page.partner_1.is_presented() and page.partner_2.is_presented() and page.partner_3.is_presented()

        page.reg_contacts.click()

        web_browser.implicitly_wait(10)

        page.kamchatka_reg.click()

        time.sleep(1)

        # Проверка, что в разделе Контакты указан регион Камчатский край
        assert page.reg_contacts.get_attribute('innerText') == 'Камчатский край'
        # Проверка, что список партнеров изменился
        assert page.partner_1.get_attribute('title') != page.kam_reg_par.get_attribute('title')

        # Проверка, что URL и title содержат информацию выбранного региона
        assert "kamchatskij-kraj" in web_browser.current_url,\
            f"URL не содержит 'kamchatskij-kraj'. Текущий URL: {web_browser.current_url}"
        assert "Камчатский край" in web_browser.title,\
            f"title вкладки не содержит 'Камчатский край'. Текущий title: {web_browser.title}"

    def test_third_scenario(self, web_browser):
        """Проверка третьего сценария."""

        page = ThirdScenario(web_browser)

        # Проскролить до ссылки "Скачать локальные версии"
        page.link_down_loc_ver.scroll_to_element()

        WebDriverWait(web_browser, 15).until(EC.presence_of_element_located((
            By.XPATH, '//div[contains(text(), "Контакты")]')))

        page.link_down_loc_ver.click()

        WebDriverWait(web_browser, 15).until(EC.presence_of_element_located((By.XPATH, '//div[text()="СБИС Плагин"]')))

        page.sbis_plugin.click()

        WebDriverWait(web_browser, 15).until(EC.presence_of_element_located((By.XPATH, '//span[text()="Windows"]')))

        page.sbis_windows.click()

        WebDriverWait(web_browser, 15).until(EC.presence_of_element_located((
            By.XPATH, '//a[text()="Скачать (Exe 11.47 МБ) "]')))

        page.link_down_exe.click()

        # Ссылка на файл для скачивания
        link_plug = 'https://update.sbis.ru/Sbis3Plugin/master/win32/sbisplugin-setup-web.exe'

        # Указание папки для сохранения
        current_dir = os.path.dirname(os.path.abspath(__file__))  # Получаем текущую директорию
        download_dir = os.path.join(current_dir, "downloads")  # Папка для загрузки
        if not os.path.exists(download_dir):
            os.makedirs(download_dir)  # Создаём папку, если её нет

        # Вызов функции скачивания файла
        file_path = download_file(link_plug, download_dir)

        # Проверка, что файл был скачан и существует в директории
        assert os.path.exists(file_path), f"Файл {file_path} не был скачан."

        # Проверка размера файла
        expected_size_mb = 11.47  # Ожидаемый размер файла в МБ
        actual_size_mb = get_file_size_in_mb(file_path)

        # Проверяем, что размер совпадает
        assert abs(actual_size_mb - expected_size_mb) < 0.01, f"Размеры файлов не совпадают."


def download_file(link, download_dir):
    """Функция для скачивания файла в указанную директорию."""
    # Получаем имя файла из ссылки
    filename = link.split('/')[-1]
    file_path = os.path.join(download_dir, filename)  # Полный путь к файлу

    # Скачиваем файл
    print(f"Загрузка файла: {link}")
    r = requests.get(link, allow_redirects=True)

    # Сохраняем файл
    with open(file_path, 'wb') as f:
        f.write(r.content)

    print(f"Файл {filename} был сохранён в папку {download_dir}")
    return file_path


def get_file_size_in_mb(file_path):
    """Функция для получения размера файла в мегабайтах."""
    size_in_bytes = os.path.getsize(file_path)
    size_in_mb = size_in_bytes / (1024 * 1024)  # Конвертируем байты в мегабайты
    return size_in_mb
