import uuid

import allure
from fuggvenyek import Fuggvenyek
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


class TestConduit(Fuggvenyek):

    def setup_method(self):
        s = Service(executable_path=ChromeDriverManager().install())
        o = Options()
        o.add_experimental_option('detach', True)
        o.add_argument('--headless')
        o.add_argument('--no-sandbox')
        o.add_argument('--disable-dev-shm-usage')
        self.browser = webdriver.Chrome(service=s, options=o)
        url = "http://localhost:1667/"
        self.browser.get(url)
        self.browser.fullscreen_window()

    def teardown_method(self):
        self.browser.quit()

    @allure.id('ATC_01')
    @allure.title('Adatkezelés elfogadása')
    def test_accept_cookie(self):
        self.accept_cookie()

    @allure.id('ATC_02')
    @allure.title('Regisztráció megfelelő adatokkal')
    def test_registration(self):
        self.accept_cookie()
        self.registration()

    @allure.id('ATC_03')
    @allure.title('Bejelentkezés regisztrált felhasználóval')
    def test_login(self):
        self.accept_cookie()
        self.login()

    @allure.id('ATC_04')
    @allure.title('Egyik felhasználó cikkeinek kilistázása/lista bejárása')
    def test_data_listing(self):
        self.accept_cookie()
        self.login()
        self.data_listing()

    @allure.id('ATC_05')
    @allure.title('Több oldalas lista bejárása')
    def test_multi_page_list(self):
        self.accept_cookie()
        self.login()
        self.multi_page_list()

    @allure.id('ATC_06')
    @allure.title('Cikk létrehozása')
    def test_new_article(self):
        self.accept_cookie()
        self.login()
        self.new_article()

    @allure.id('ATC_07')
    @allure.title('Saját cikk szövegének módosítása')
    def test_mod_article(self):
        self.accept_cookie()
        self.login()
        self.new_article()
        self.mod_article()

    @allure.id('ATC_08')
    @allure.title('Saját cikk hozzászólása')
    def test_new_comment(self):
        self.accept_cookie()
        self.login()
        self.new_article()
        self.new_comment()

    @allure.id('ATC_09')
    @allure.title('Saját cikk törlése')
    def test_article_del(self):
        self.accept_cookie()
        self.login()
        self.new_article()
        self.article_del()

    @allure.id('ATC_10')
    @allure.title('Bejelentkezést követően az első oldalon lévő cikkek szerzőinek a kigyűjtése txt fájlba')
    def test_saving_data_interface(self):
        self.accept_cookie()
        self.login()
        self.saving_data_interface()

    @allure.id('ATC_11')
    @allure.title('Ismételt és sorozatos adatbevitel adatforrásból (többszöri regisztráció)')
    def test_import_data_from_file(self):
        self.accept_cookie()
        self.import_data_from_file()

    @allure.id('ATC_12')
    @allure.title('Kijelentkezés')
    def test_logout(self):
        self.accept_cookie()
        self.login()
        self.logout()

