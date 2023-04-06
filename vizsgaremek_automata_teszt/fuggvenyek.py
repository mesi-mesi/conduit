import time
import csv
from adatok import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from datetime import datetime


class Fuggvenyek:
    # függvény az adatkezelésről
    def accept_cookie(self):
        accept = WebDriverWait(self.browser, 5).until(EC.presence_of_element_located(
            (By.XPATH, '//button [@class="cookie__bar__buttons__button cookie__bar__buttons__button--accept"]')))

        assert accept.text == 'I accept!'

        accept.click()

    # függvény a regisztrációról
    def registration(self):
        sign_up = self.browser.find_elements(By.XPATH, '//li/a [@class="nav-link"]')[1]
        sign_up.click()
        assert self.browser.current_url == 'http://localhost:1667/#/register'

        username = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.XPATH, '//input [@placeholder="Username"]')))
        username.send_keys(user["name"])

        email = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.XPATH, '//input [@placeholder="Email"]')))
        email.send_keys(user["email"])

        password = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.XPATH, '//input [@placeholder="Password"]')))
        password.send_keys(user["password"])

        sign_up_account = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.XPATH, '//button [@class="btn btn-lg btn-primary pull-xs-right"]')))
        sign_up_account.click()

        ok_button = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.XPATH, '//button [@class="swal-button swal-button--confirm"]')))
        ok_button.click()

        user_name = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.XPATH, '//a [@href="#/@user_emese/" and @class="nav-link"]')))

        assert user_name.text == user["name"]

    # függvény bejelentkezésről
    def login(self):
        sign_in_button = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'ion-compose')))
        sign_in_button.click()
        assert self.browser.current_url == 'http://localhost:1667/#/login'

        email_sign_in = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.XPATH, '//input [@placeholder="Email"]')))

        email_sign_in.send_keys(user["email"])

        password_sign_in = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.XPATH, '//input [@placeholder="Password"]')))
        password_sign_in.send_keys(user["password"])

        sign_in_account = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.XPATH,
                                            '//button [@class="btn btn-lg btn-primary pull-xs-right"]')))
        sign_in_account.click()

        user_name = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.XPATH, '//a [@href="#/@user_emese/" and @class="nav-link"]')))

        assert user_name.text == user["name"]

    # függvény egy felhasználó cikkeinek kilistázásához
    def data_listing(self):
        first_user = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'author')))
        #first_user = self.browser.find_element(By.XPATH, '// a[@class="author"]')
        first_user.click()
        time.sleep(5)
        assert self.browser.current_url != 'http://localhost:1667/#/'

        article = self.browser.find_elements(By.XPATH, '// div[@ class="article-preview"]')
        last_article = self.browser.find_elements(By.XPATH, '// div[@ class="article-preview"]')[-1]

        for j in range(article.__len__()):
            article = self.browser.find_elements(By.XPATH, '// div[@ class="article-preview"]')[j]
            j += 1

        assert article.text != ""
        assert last_article.text == article.text

    # függvény több oldalas lista bejárására, a Conduit oldal összes cikk bejárása
    def multi_page_list(self):

        page_link_button = self.browser.find_elements(By.XPATH, '//a [@class="page-link"]')
        osszeg = 0

        for i in range(page_link_button.__len__()):
            page_link_button = self.browser.find_elements(By.XPATH, '//a [@class="page-link"]')[i]
            assert page_link_button.is_displayed()
            page_link_button.click()
            time.sleep(5)
            i += 1

            article = self.browser.find_elements(By.XPATH, '// div[@ class="article-preview"]')
            for j in range(article.__len__()):
                article = self.browser.find_elements(By.XPATH, '// div[@ class="article-preview"]')[j]
                j += 1

            osszeg += j
        print(f'Jelenleg {osszeg} cikk található az oldalon')
