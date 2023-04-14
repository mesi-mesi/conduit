import time
import csv
import uuid

from adatok import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import allure


class Fuggvenyek:
    # függvény az adatkezelésről

    def accept_cookie(self):
        accept = WebDriverWait(self.browser, webdriver_timeout).until(EC.presence_of_element_located(
            (By.XPATH, '//button [@class="cookie__bar__buttons__button cookie__bar__buttons__button--accept"]')))

        assert accept.text == 'I accept!'
        assert accept.is_enabled()
        assert len(self.browser.find_elements(By.ID, 'cookie-policy-panel')) != 0

        accept.click()
        time.sleep(5)

        assert len(self.browser.find_elements(By.ID, 'cookie-policy-panel')) == 0

    # függvény a regisztrációról

    def registration(self):
        self.registration_with_param(user["name"], user["email"], user["password"])

    # függvény a regisztráció paramétereiről

    def registration_with_param(self, reg_username, reg_email, reg_password):
        sign_up = WebDriverWait(self.browser, webdriver_timeout).until(
            EC.presence_of_element_located((By.XPATH, '//a [@href="#/register"]')))

        sign_up.click()
        time.sleep(2)
        assert self.browser.current_url == 'http://localhost:1667/#/register'

        username = WebDriverWait(self.browser, webdriver_timeout).until(
            EC.presence_of_element_located((By.XPATH, '//input [@placeholder="Username"]')))
        email = WebDriverWait(self.browser, webdriver_timeout).until(
            EC.presence_of_element_located((By.XPATH, '//input [@placeholder="Email"]')))
        password = WebDriverWait(self.browser, webdriver_timeout).until(
            EC.presence_of_element_located((By.XPATH, '//input [@placeholder="Password"]')))
        sign_up_account = WebDriverWait(self.browser, webdriver_timeout).until(
            EC.presence_of_element_located((By.XPATH, '//button [@class="btn btn-lg btn-primary pull-xs-right"]')))

        username.send_keys(reg_username)
        email.send_keys(reg_email)
        password.send_keys(reg_password)
        sign_up_account.click()

        ok_button = WebDriverWait(self.browser, webdriver_timeout).until(
            EC.presence_of_element_located((By.XPATH, '//button [@class="swal-button swal-button--confirm"]')))

        ok_button.click()

        user_name = WebDriverWait(self.browser, webdriver_timeout).until(
            EC.presence_of_element_located((By.XPATH, '//a [@href="#/@' + reg_username + '/" and @class="nav-link"]')))

        assert user_name.text == reg_username

    # függvény bejelentkezésről

    def login(self):
        self.login_with_param(user["name"], user["email"], user["password"])

    def login_with_param(self, login_username, login_email, login_password):
        sign_in_button = WebDriverWait(self.browser, webdriver_timeout).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'ion-compose')))
        sign_in_button.click()
        assert self.browser.current_url == 'http://localhost:1667/#/login'

        email_sign_in = WebDriverWait(self.browser, webdriver_timeout).until(
            EC.presence_of_element_located((By.XPATH, '//input [@placeholder="Email"]')))
        password_sign_in = WebDriverWait(self.browser, webdriver_timeout).until(
            EC.presence_of_element_located((By.XPATH, '//input [@placeholder="Password"]')))
        sign_in_account = WebDriverWait(self.browser, webdriver_timeout).until(
            EC.presence_of_element_located((By.XPATH,
                                            '//button [@class="btn btn-lg btn-primary pull-xs-right"]')))

        email_sign_in.send_keys(login_email)
        password_sign_in.send_keys(login_password)
        sign_in_account.click()

        user_name = WebDriverWait(self.browser, webdriver_timeout).until(
            EC.presence_of_element_located(
                (By.XPATH, '//a [@href="#/@' + login_username + '/" and @class="nav-link"]')))

        assert user_name.text == user["name"]

    # függvény egy felhasználó cikkeinek kilistázásához
    def data_listing(self):
        first_user = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'author')))
        first_user.click()
        time.sleep(5)
        assert self.browser.current_url != 'http://localhost:1667/#/'

        articles = self.browser.find_elements(By.XPATH, '// div[@ class="article-preview"]')
        last_article = self.browser.find_elements(By.XPATH, '// div[@ class="article-preview"]')[len(articles) - 1]

        for j in range(len(articles)):
            article = self.browser.find_elements(By.XPATH, '// div[@ class="article-preview"]')[j]
            assert article.text != ""

        assert last_article.text == article.text

    # függvény több oldalas lista bejárására, a Conduit oldal összes cikk bejárása
    def multi_page_list(self):
        page_link_buttons = self.browser.find_elements(By.XPATH, '//a [@class="page-link"]')

        last_page_link_button = self.browser.find_elements(By.XPATH, '//a [@class="page-link"]')[
            len(page_link_buttons) - 1]

        for i in range(len(page_link_buttons)):
            page_link_button = self.browser.find_elements(By.XPATH, '//a [@class="page-link"]')[i]

            assert page_link_button.is_displayed()
            page_link_button.click()
            time.sleep(5)

            articles = self.browser.find_elements(By.XPATH, '// div[@ class="article-preview"]')
            last_article = self.browser.find_elements(By.XPATH, '// div[@ class="article-preview"]')[len(articles) - 1]

            for j in range(len(articles)):
                article = self.browser.find_elements(By.XPATH, '// div[@ class="article-preview"]')[j]

            assert article.get_attribute('value') == last_article.get_attribute('value')

        assert page_link_button.get_attribute('value') == last_page_link_button.get_attribute('value')

    # függvény új cikk létrehozására

    def new_article(self):
        title = first_new_article["article_title"] + ' ' + str(uuid.uuid4())

        new_article_button = WebDriverWait(self.browser, webdriver_timeout).until(
            EC.presence_of_element_located((By.XPATH, '//i [@class="ion-compose"]')))
        new_article_button.click()
        time.sleep(2)

        assert self.browser.current_url == 'http://localhost:1667/#/editor'

        article_title = WebDriverWait(self.browser, webdriver_timeout).until(
            EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Article Title"]')))
        article_about = WebDriverWait(self.browser, webdriver_timeout).until(
            EC.presence_of_element_located((By.XPATH, '//input[@placeholder="What\'s this article about?"]')))
        article_write = self.browser.find_element(By.XPATH,
                                                  '//fieldset/textarea [@placeholder="Write your article (in markdown)"]')
        publish_article = WebDriverWait(self.browser, webdriver_timeout).until(
            EC.presence_of_element_located(
                (By.XPATH, '//button [@type="submit" and @class="btn btn-lg pull-xs-right btn-primary"]')))
        enter_tags = self.browser.find_element(By.XPATH, '//input[@placeholder="Enter tags"]')

        article_title.send_keys(title)
        article_about.send_keys(first_new_article["about"])
        article_write.send_keys(first_new_article["article"])
        enter_tags.send_keys(first_new_article["tag"])
        publish_article.click()

        saved_article_title = WebDriverWait(self.browser, webdriver_timeout).until(
            EC.presence_of_element_located(
                (By.XPATH, '//div [@class="container"]/h1')))
        saved_article_write = WebDriverWait(self.browser, webdriver_timeout).until(
            EC.presence_of_element_located(
                (By.XPATH, '//div [@class="row article-content"]/div/div/p')))

        assert title == saved_article_title.get_attribute('innerText')
        assert first_new_article["article"] == saved_article_write.get_attribute('innerText')

    #  függvény új cikk címének módósítása

    def mod_article(self):
        edit_article_button = WebDriverWait(self.browser, webdriver_timeout).until(
            EC.presence_of_element_located((By.XPATH, '//i [@class="ion-edit"]')))
        assert edit_article_button.is_displayed()
        edit_article_button.click()

        article_text = WebDriverWait(self.browser, webdriver_timeout).until(EC.presence_of_element_located(
            (By.XPATH, '//fieldset/textarea [@placeholder="Write your article (in markdown)"]')))
        article_text.click()
        article_text.clear()

        article_text.send_keys(mod_article["article"])

        publish_article_button = WebDriverWait(self.browser, webdriver_timeout).until(
            EC.presence_of_element_located(
                (By.XPATH, '//button [@type="submit" and @class="btn btn-lg pull-xs-right btn-primary"]')))
        publish_article_button.click()
        time.sleep(2)

        modified_article_text = WebDriverWait(self.browser, webdriver_timeout).until(
            EC.presence_of_element_located(
                (By.XPATH, '//div [@class="row article-content"]/div/div/p')))

        assert mod_article["article"] == modified_article_text.get_attribute('innerText')

    #  függvény új cikk hozzászólása
    def new_comment(self):
        new_comment = self.browser.find_element(By.XPATH,
                                                '//textarea [@placeholder="Write a comment..." and @class="form-control"]')
        new_comment.send_keys(first_comment["comment"])

        post_comment_button = WebDriverWait(self.browser, webdriver_timeout).until(
            EC.presence_of_element_located((By.XPATH, '//button [@class="btn btn-sm btn-primary"]')))

        post_comment_button.click()
        time.sleep(3)

        comment = self.browser.find_element(By.XPATH, '//p [@class="card-text"]')

        assert comment.text == first_comment["comment"]

    # függvény új cikk törlésére
    def article_del(self):
        saved_article_title = WebDriverWait(self.browser, webdriver_timeout).until(
            EC.presence_of_element_located(
                (By.XPATH, '//div [@class="container"]/h1')))

        delete_article_button = WebDriverWait(self.browser, webdriver_timeout).until(
            EC.presence_of_element_located((By.XPATH, '//i[@class="ion-trash-a"]')))
        delete_article_button.click()
        time.sleep(3)
        assert self.browser.current_url == 'http://localhost:1667/#/'

        your_feed_btn = WebDriverWait(self.browser, webdriver_timeout).until(
            EC.presence_of_element_located((By.CLASS_NAME, "nav-link")))
        time.sleep(2)

        articles_title = self.browser.find_elements(By.XPATH, '//a [@class="preview-link"]/h1')

        for article_title in articles_title:
            assert saved_article_title != article_title

    # függvény adatok lementése felületről
    def saving_data_interface(self):

        time.sleep(2)
        szerzok = self.browser.find_elements(By.CLASS_NAME, 'author')
        szerzo_lista = list()
        with open('interface_data.txt', 'w') as file_szoveg:
            for szerzo in szerzok:
                szerzo_lista.append(szerzo)
                file_szoveg.write(f'Cikk szerzoje: {szerzo.text}\n')
        time.sleep(5)

        with open('interface_data.txt', 'r') as csv_szoveg:
            assert len(szerzo_lista) == len(list(csv_szoveg))
            assert len(szerzo_lista) != 0

    # függvény kilépésről

    def logout(self):
        logout_button = WebDriverWait(self.browser, webdriver_timeout).until(
            EC.presence_of_element_located((By.XPATH, '//i[@class="ion-android-exit"]')))
        assert logout_button.is_displayed()
        logout_button.click()

        sign_in_button = WebDriverWait(self.browser, webdriver_timeout).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'ion-compose')))
        assert sign_in_button.is_displayed()

    # függvény ismételt és sorozatos adatbevitel adatforrásból

    def import_data_from_file(self):
        time.sleep(5)
        with open('registration_data.csv', 'r') as registration_data:
            registration_reader = csv.reader(registration_data, delimiter=',')
            next(registration_reader)
            for reg in registration_reader:
                self.registration_with_param(reg[0], reg[1], reg[2])
                time.sleep(2)

                self.logout()