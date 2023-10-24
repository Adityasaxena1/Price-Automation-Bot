from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class SellerLogin:
    def __init__(self, url):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver1 = webdriver.Chrome(options=self.chrome_options)
        self.driver1.get(url)
        self.username = "e732090@bfl.com"
        self.password = "biligiri24"

    def login(self):
        time.sleep(2)
        username_input = self.driver1.find_element(By.CSS_SELECTOR, '[placeholder="Username"]')
        username_input.send_keys(self.username)
        password_input = self.driver1.find_element(By.CSS_SELECTOR, '[placeholder="Password"]')
        password_input.send_keys(self.password)
        login_button = self.driver1.find_element(By.CLASS_NAME, value="loginButton")
        login_button.click()
        time.sleep(10)
        price_management = self.driver1.find_element(By.XPATH, value='/html/body/div[3]/div[1]/div/div[2]/div/div/'
                                                                     'div/community_navigation-global-navigation-'
                                                                     'list/div/nav/ul/li[4]')
        price_management.click()
        time.sleep(2)
        self.driver1.close()
        self.driver1.switch_to.window(self.driver1.window_handles[0])
        time.sleep(10)
        list_button = self.driver1.find_element(By.CLASS_NAME, value='level2HeaderTitle')
        list_button.click()

    def update_price(self, price, model_id):
        self.driver1.maximize_window()
        search_input = self.driver1.find_element(By.ID, value="searchinput")
        search_input.clear()
        search_input.send_keys(model_id)
        search_input.send_keys(Keys.ENTER)
        time.sleep(1)
        price_button = self.driver1.find_element(By.CSS_SELECTOR, '[class="rupee stockInput"]')
        price_button.click()
        time.sleep(1)
        rate = self.driver1.find_element(By.CSS_SELECTOR, '[class="ag-input-field-input ag-text-field-input"]')
        rate.send_keys(price)
        save_button = self.driver1.find_element(By.CSS_SELECTOR, '[class="savebtn2W"]')
        save_button.click()
        time.sleep(2)
        try:
            close_img = self.driver1.find_element(By.CSS_SELECTOR, '[class="closeImg"]')
            close_img.click()
        except:
            time.sleep(2)
            close_img = self.driver1.find_element(By.CSS_SELECTOR, '[class="closeImg"]')
            close_img.click()




