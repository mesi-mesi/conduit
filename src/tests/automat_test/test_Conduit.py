from fuggvenyek import Fuggvenyek

import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestConduit(Fuggvenyek):

    def setup_method(self):
        s = Service(executable_path=ChromeDriverManager().install())
        o = Options()
        o.add_experimental_option('detach', True)
        self.browser = webdriver.Chrome(service=s, options=o)
        url = "http://localhost:1667/#/"
        self.browser.get(url)
        self.browser.fullscreen_window()

    def teardown_method(self):
        self.browser.quit()


    # TC1_Adatkezelés elfogadása
    def test_accept_cookie(self):
        self.accept_cookie()

    #TC2_Regisztráció
    def test_registration(self):
        self.accept_cookie()
        self.registration()

    # # # TC3_Bejelentkezés
    def test_login(self):
        self.accept_cookie()
        self.login()

    # # # TC4_Kijelentkezés
    def test_logout(self):
        self.accept_cookie()
        self.login()
        self.logout()

    # TC5_Több oldalas lista bejárása
    def test_data_listing(self):
        self.accept_cookie()
        self.login()
        self.multi_page_list()

    # # TC6_Új cikk létrehozása   Működik de a beviteli mezőket nem tudom ellenőrizni(value és text hibára fut)
    def test_new_article(self):
        self.accept_cookie()
        self.login()
        self.new_article()

    # # # TC7_Cikk módosítása
    def test_mod_article(self):
        self.accept_cookie()
        self.login()
        self.new_article()
        self.mod_article()

    # # # # TC8_Új cikk hozzászólás
    def test_new_comment(self):
        self.accept_cookie()
        self.login()
        self.new_article()
        self.new_comment()

    # # TC_9 Cikk törlése
    def test_article_del(self):
        self.accept_cookie()
        self.login()
        self.new_article()
        self.article_del()

    # TC_Adatok lementése felületről
    def test_saving_data_interface(self):
        self.accept_cookie()
        self.login()
        self.saving_data_interface()      # A tag szövegét nem teszi bele a csv fájlba, a sima tesztesetesben rendesen működik
