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

    #   ATC_01 Adatkezelés elfogadása
    # @allure.id('ATC_01')
    # @allure.title('Adatkezelés elfogadása')
    # @allure.description('Sütik elfogadása')
    def test_accept_cookie(self):
        self.accept_cookie()


    #   ATC_02 Regisztráció megfelelő adatokkal
    # @allure.id('ATC_02')
    # @allure.title('Regisztráció megfelelő adatokkal')
    # @allure.description('Regisztrációhoz szükséges adatokat az adatok.py fájlból származnak.')
    def test_registration(self):
        self.accept_cookie()
        self.registration()

    #   ATC_03 Bejelentkezés megfelelő adatokkal
    # @allure.id('ATC_03')
    # @allure.title('Bejelentkezés megfelelő adatokkal')
    # @allure.description('Regisztrációnál létrehozott felhasználóval bejelentkezés')
    def test_login(self):
        self.accept_cookie()
        self.login()

    #   ATC_04 Egyik felhasználó cikkeinek kilistázása/lista bejárása
    # @allure.id('ATC_04')
    # @allure.title('Egyik felhasználó cikkeinek kilistázása/lista bejárása')
    def test_data_listing(self):
        self.accept_cookie()
        self.login()
        self.data_listing()

    #   ATC_05 Több oldalas lista bejárása
    # @allure.id('ATC_05')
    # @allure.title('Több oldalas lista bejárása')
    def test_multi_page_list(self):
        self.accept_cookie()
        self.login()
        self.multi_page_list()

    #   ATC_06 Cikk létrehozása
    # @allure.id('ATC_06')
    # @allure.title('Cikk létrehozása')
    def test_new_article(self):
        self.accept_cookie()
        self.login()
        self.new_article()

    #   ATC_07 Saját cikk címének módosítása
    # @allure.id('ATC_07')
    # @allure.title('Saját cikk címének módosítása')
    def test_mod_article_title(self):
        self.accept_cookie()
        self.login()
        self.new_article()
        self.mod_title_article()

    #   ATC_08 Saját cikk hozzászólása
    # @allure.id('ATC_08')
    # @allure.title('Saját cikk hozzászólása')
    def test_new_comment(self):
        self.accept_cookie()
        self.login()
        self.new_article()
        self.new_comment()

    #   ATC_09 Saját cikk törlése
    # @allure.id('ATC_09')
    # @allure.title('Saját cikk törlése')
    def test_article_del(self):
        self.accept_cookie()
        self.login()
        self.new_article()
        self.article_del()

    #   ATC_10 Bejelentkezést követően az első oldalon lévő cikkek szerzőinek a kigyűjtése csv fájlba
    # @allure.id('ATC_10')
    # @allure.title('Bejelentkezést követően az első oldalon lévő cikkek szerzőinek a kigyűjtése csv fájlba')
    def test_saving_data_interface(self):
        self.accept_cookie()
        self.login()
        self.saving_data_interface()

    #   ATC_11 Ismételt és sorozatos adatbevitel adatforrásból (többszöri regisztráció)
    # @allure.id('ATC_11')
    # @allure.title('Ismételt és sorozatos adatbevitel adatforrásból (többszöri regisztráció)')
    def test_import_data_from_file(self):
        self.accept_cookie()
        self.import_data_from_file()

    #   ATC_12 Kijelentkezés
    # @allure.id('ATC_12')
    # @allure.title('Kijelentkezés')
    def test_logout(self):
        self.accept_cookie()
        self.login()
        self.logout()