from fuggvenyek import Fuggvenyek
from adatok import *
import time
import csv
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
        o.add_argument('--headless')
        o.add_argument('--no-sandbox')
        o.add_argument('--disable-dev-shm-usage')
        self.browser = webdriver.Chrome(service=s, options=o)
        url = "http://localhost:1667/"
        self.browser.get(url)
        self.browser.fullscreen_window()

    def teardown_method(self):
        self.browser.quit()

#   TC_01 Sütik elfogadása

    def test_accept_cookie(self):
        self.accept_cookie()

#   TC_02 Regisztráció az oldalra, megfelelő adatokkal
    def test_registration(self):
        self.accept_cookie()
        self.registration()

#    TC_03 Bejelentkezés megfelelő adatokkal
    def test_login(self):
        self.accept_cookie()
        self.login()

#   TC_04 Egyik felhasználó cikkeinek kilistázása/lista bejárása
    def test_data_listing(self):
        self.accept_cookie()
        self.login()
        self.data_listing()

#   TC_05 Több oldalas lista bejárása
    def test_multi_page_list(self):
        self.accept_cookie()
        self.login()
        self.multi_page_list()

#   TC_06 Új cikk létrehozása
    def test_new_article(self):
        self.accept_cookie()
        self.login()
        self.new_article()

#   TC_07 Új cikk címének módosítása
    def test_mod_article_title(self):
        self.accept_cookie()
        self.login()
        self.new_article()
        self.mod_title_article()

#   TC_08 Új cikk hozzászólása
    def test_new_comment(self):
        self.accept_cookie()
        self.login()
        self.new_article()
        self.new_comment()

#  TC_09 Új cikk törlése
    def test_article_del(self):
        self.accept_cookie()
        self.login()
        self.new_article()
        self.article_del()

#   TC_10 Bejelentkezés követően az első oldalon lévő cikkek szerzőinek a kigyűjtése csv fájlba
    def test_saving_data_interface(self):
        self.accept_cookie()
        self.login()
        self.saving_data_interface()

#   TC_11 Ismételt és sorozatos adatbevitel adatforrásból
    def test_import_data_from_file(self):
        self.accept_cookie()
        self.import_data_from_file()

#   TC_12 Kijelentkezés
    def test_logout(self):
        self.accept_cookie()
        self.login()
        self.logout()