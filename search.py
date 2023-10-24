from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class SecondTab:
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver2 = webdriver.Chrome(options=self.chrome_options)
        self.first_iteration = True
        self.selected = True
        self.our_price = None
        self.price_list = None

    def product_search(self, value):
        self.driver2.get(f'https://www.bajajmall.in/emi-store/search.html?q={value}')
        time.sleep(2)

        if self.first_iteration:
            self.driver2.find_element(By.ID, value='wzrk-cancel').click()
            time.sleep(2)
            search = self.driver2.find_element(By.XPATH,
                                               value='//*[@id="searchformId"]/div[1]/div[4]/button/span/i/img')
            search.click()
        self.first_iteration = False
        time.sleep(2)

        product = self.driver2.find_element(By.XPATH,
                                            value='//*[@id="plp-view-type"]/div/div/div/section[2]/div[2]/div[2]/div/a')
        product.click()

        time.sleep(2)
        self.driver2.close()
        time.sleep(2)
        self.driver2.switch_to.window(self.driver2.window_handles[0])

        try:
            time.sleep(2)
            seller_list = self.driver2.find_element(By.XPATH, value='//*[@id="deliveryDetailsSection"]/div/div/div/'
                                                                    'div[7]/div/div/div[3]/span')
            seller_list.click()
            self.our_price = self.driver2.find_element(By.CSS_SELECTOR,
                                                       value='[data-id="732090"] .sellerOfferPrice').text.replace(
                '₹', '').replace(',', '')
            
            self.price_list = [price.text.replace(
                    '₹', '').replace(',', '') for price in self.driver2.find_elements(By.CLASS_NAME,
                                                                                      '[class="pdp-md-selname-text ft-med ws-nowrap sellerOfferPrice"]')]

            self.selected = self.driver2.find_element(By.CSS_SELECTOR, value='[data-sellerid="732090"]').is_selected()



        except:
            time.sleep(2)
            price_list = [self.driver2.find_element(By.CSS_SELECTOR,
                                                    '[class="ft-med-lt absolute-discount-calc-offer-price "]').text.
                          replace(',', '')]
            self.our_price = price_list[-1]
