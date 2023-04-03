import time
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

    def accept_cookie(self):
        accept = WebDriverWait(self.browser, 5).until(EC.presence_of_element_located(
            (By.XPATH, '//button [@class="cookie__bar__buttons__button cookie__bar__buttons__button--accept"]')))
        assert self.browser.find_element(By.XPATH,
                                         '//button [@class="cookie__bar__buttons__button cookie__bar__buttons__button--accept"]').text == 'I accept!'
        accept.click()

    def login(self):
        sign_in_button = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'ion-compose')))
        sign_in_button.click()
        assert self.browser.current_url == 'http://localhost:1667/#/login'

        email_sign_in = self.browser.find_element(By.XPATH, '//input [@placeholder="Email"]')
        email_sign_in.send_keys('varadimesi@gmail.com')
        assert email_sign_in.get_attribute("value") == 'varadimesi@gmail.com'

        password_sign_in = self.browser.find_element(By.XPATH, '//input [@placeholder="Password"]')
        password_sign_in.send_keys('TesztElek01')
        assert password_sign_in.get_attribute("value") == 'TesztElek01'

        sign_in_account = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.XPATH,
                                            '//button [@class="btn btn-lg btn-primary pull-xs-right"]')))
        sign_in_account.click()

        user_name = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.XPATH, '//a [@href="#/@user_emese/" and @class="nav-link"]')))
        assert user_name.text == 'user_emese'

    def new_article(self):
        new_article_button = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '//i [@class="ion-compose"]')))
        new_article_button.click()
        time.sleep(3)

        assert self.browser.current_url == 'http://localhost:1667/#/editor'

        article_title = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Article Title"]')))
        article_title.send_keys('Gaudeamus igitur')

        article_about = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '//input[@placeholder="What\'s this article about?"]')))

        article_about.send_keys('Gaudeamus igitur songs')

        article_write = self.browser.find_element(By.XPATH,
                                                  '//fieldset/textarea [@placeholder="Write your article (in markdown)"]')
        article_write.send_keys(
            'Gaudeamus igitur iuvenes dum sumus \nGaudeamus igitur iuvenes dum sumus \nPost iucundam iuventutem post molestam senectutem \nNos habebit humus nos habebit humus')

        enter_tags = self.browser.find_element(By.XPATH, '//input[@placeholder="Enter tags"]')
        enter_tags.send_keys('vita')

        publish_article = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located(
                (By.XPATH, '//button [@type="submit" and @class="btn btn-lg pull-xs-right btn-primary"]')))
        publish_article.click()

        new_article = self.browser.title
        self.browser.save_screenshot(f'New_article{new_article}.png')
        assert self.browser.current_url == 'http://localhost:1667/#/articles/gaudeamus-igitur'

    def registration(self):
        sign_up = self.browser.find_elements(By.XPATH, '//li/a [@class="nav-link"]')[1]
        sign_up.click()
        assert self.browser.current_url == 'http://localhost:1667/#/register'

        username = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.XPATH, '//input [@placeholder="Username"]')))
        username.send_keys('user_emese')

        email = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.XPATH, '//input [@placeholder="Email"]')))
        email.send_keys('varadimesi@gmail.com')

        password = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.XPATH, '//input [@placeholder="Password"]')))
        password.send_keys('TesztElek01')

        sign_up_account = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.XPATH, '//button [@class="btn btn-lg btn-primary pull-xs-right"]')))
        sign_up_account.click()

        ok_button = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.XPATH, '//button [@class="swal-button swal-button--confirm"]')))
        ok_button.click()

        assert self.browser.current_url == 'http://localhost:1667/#/'

    def logout(self):
        logout_button = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.XPATH, '//i[@class="ion-android-exit"]')))
        assert logout_button.is_displayed()
        logout_button.click()

        logout = self.browser.title
        self.browser.save_screenshot(f'Logout_{logout}.png')

    def data_listing(self):
        nisil_tag = self.browser.find_elements(By.XPATH, '//a [@class="tag-pill tag-default" and text() = "nisil"]')[1]
        assert nisil_tag.get_attribute("text") == "nisil"
        print(nisil_tag.text)
        nisil_tag.click()

        time.sleep(3)
        nisil = self.browser.title
        self.browser.save_screenshot(f'List_{nisil}.png')

    def mod_article(self):
        edit_article_button = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.XPATH, '//i [@class="ion-edit"]')))
        assert edit_article_button.is_displayed()
        edit_article_button.click()

        article_title_mod = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Article Title"]')))
        article_title_mod.click()
        article_title_mod.clear()
        assert article_title_mod.get_attribute("value") == ''

        article_title_mod.send_keys('OMNIA SOL TEMPERATA')

        article_about_mod = self.browser.find_element(By.XPATH, '//input[@placeholder="What\'s this article about?"]')
        article_about_mod.click()
        article_about_mod.clear()
        assert article_about_mod.get_attribute("value") == ''

        article_about_mod.send_keys('Carmen: OMNIA SOL TEMPERATA ')

        article_write_mod = self.browser.find_element(By.XPATH,
                                                      '//fieldset/textarea [@placeholder="Write your article (in markdown)"]')
        article_write_mod.click()
        article_write_mod.clear()
        assert article_write_mod.get_attribute("value") == ''

        article_write_mod.send_keys(
            'Omnia Sol temperat \npurus et subtilis; \nnovo mundo reserat \nfacies Aprilis, \nad amorem properat\nanimus herilis, \net iocundis imperat \ndeus puerilis.')

        tag_del = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.XPATH, '//i [@class="ti-icon-close"]')))
        tag_del.click()

        enter_tags_mod = self.browser.find_element(By.XPATH, '//input[@placeholder="Enter tags"]')
        enter_tags_mod.send_keys('fons')

        publish_article_button = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located(
                (By.XPATH, '//button [@type="submit" and @class="btn btn-lg pull-xs-right btn-primary"]')))
        publish_article_button.click()

        new_article = self.browser.title
        self.browser.save_screenshot(f'New_article{new_article}.png')

    def new_comment(self):
        new_comment = self.browser.find_element(By.XPATH,
                                                '//textarea [@placeholder="Write a comment..." and @class="form-control"]')
        new_comment.send_keys('Juvenes dum sumus')

        post_comment_button = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.XPATH, '//button [@class="btn btn-sm btn-primary"]')))

        post_comment_button.click()
        time.sleep(3)

        comment = self.browser.find_element(By.XPATH, '//p [@class="card-text"]')

        assert comment.text == 'Juvenes dum sumus'

    def article_del(self):
        delete_article_button = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.XPATH, '//i[@class="ion-trash-a"]')))
        delete_article_button.click()
        time.sleep(3)
        assert self.browser.current_url == 'http://localhost:1667/#/'

    def multi_page_list(self):

        page_link_button = self.browser.find_elements(By.XPATH, '//a [@class="page-link"]')
        osszeg = 0
        for i in range(page_link_button.__len__()):
            page_link_button = self.browser.find_elements(By.XPATH, '//a [@class="page-link"]')[i]
            assert page_link_button.is_displayed()
            page_link_button.click()
            time.sleep(5)

            i += 1
            # print(f'i értéke {i}')
            article = self.browser.find_elements(By.XPATH, '// div[@ class="article-preview"]')
            for j in range(article.__len__()):
                article = self.browser.find_elements(By.XPATH, '// div[@ class="article-preview"]')[j]
                j += 1

            # print(f'j értéke: {j}')
            osszeg += j
            # print(f' {osszeg} ')
        print(f'Jelenleg {osszeg} cikk található az oldalon')

    def saving_data_interface(self):

        article = self.browser.find_elements(By.XPATH, '// div[@ class="article-preview"]')[0]
        article.click()

        time.sleep(5)
        assert self.browser.current_url != "http://localhost:1667/#/"

        szerzo = self.browser.find_element(By.CLASS_NAME, 'author')

        with open('interface_data.csv', 'a', encoding='UTF-8') as file_szoveg:
            file_szoveg.writelines(f'A szerző neve: {szerzo.text}\n')

        szoveg = self.browser.find_element(By.XPATH, '//p')

        with open('interface_data.csv', 'a', encoding='UTF-8') as file_szoveg:
            file_szoveg.writelines(f'A cikk szövege: {szoveg.text}\n')

        tag = self.browser.find_elements(By.CLASS_NAME, "tag-pill tag-default")

        for i in range(tag.__len__()):
            tag = self.browser.find_elements(By.XPATH, '//a[@class="tag-pill tag-default"]')[i]
            time.sleep(5)
            print(tag.text)
            with open('interface_data.csv', 'a', encoding='UTF-8') as file_szoveg:
                file_szoveg.writelines(f'A cikk tagje: {tag.text}\n')
                time.sleep(5)
