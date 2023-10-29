from login import SellerLogin
from search import SecondTab
from popup_notification import pop_ups
import math
import pandas as pd

our_account_bot = SellerLogin(url="https://bflconsumer.my.site.com/NDSDealer/s/login/")
our_account_bot.login()

product_bot = SecondTab()

high_price_model_list = []

file_path = "model_id.xlsx"
df = pd.read_excel(file_path)

my_list = df["Model CODE"].tolist()
model_ids = []
for x in my_list:
    if not math.isnan(x):
        model_ids.append(int(x))

for value in model_ids:
    product_bot.product_search(value)
    if not product_bot.selected:
        other_company_price = int(product_bot.offer_price)
        price_difference = abs(int(product_bot.our_price) - other_company_price)
        if price_difference > 20:
            high_price_model_list.append(value)
        else:
            our_account_bot.update_price(price=other_company_price, model_id=value)

if len(high_price_model_list) > 0:
    for mod_id in high_price_model_list:
        product_bot.product_search(mod_id)
        other_price = product_bot.offer_price
        difference = int(product_bot.our_price) - int(other_price)
        user_choice = pop_ups(mod_id=mod_id, difference=difference, other_price=other_price,
                              ours=product_bot.our_price)
        if user_choice:
            our_account_bot.update_price(price=int(other_price), model_id=mod_id)

our_account_bot.driver1.quit()
product_bot.driver2.quit()

