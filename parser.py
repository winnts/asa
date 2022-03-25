from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://minfin.com.ua/currency/mb/")
assert "Межбанк: курс доллара на межбанке Украины онлайн" in driver.title

elemUsdBuy = driver.find_element(By.XPATH, value="(//td[@data-title='Доллар'])[1]")
elemUsdSell = driver.find_element(By.XPATH, value="(//td[@data-title='Доллар'])[2]")
elemEurBuy = driver.find_element(By.XPATH, value="(//td[@data-title='Евро'])[1]")
elemEurSell = driver.find_element(By.XPATH, value="(//td[@data-title='Евро'])[2]")
usd_sell = elemUsdSell.text.split(' ')[0]
usd_buy = elemUsdBuy.text.split(' ')[0]
eur_buy = elemEurBuy.text.split(' ')[0]
eur_sell = elemEurSell.text.split(' ')[0]

driver.close()

# while True:
#     currency = str(input('Please input type of currency (usd_sell, usd_buy, eur_sell, eur_buy): '))
#     if currency == 'usd_sell':
#         currency = usd_sell
#         print("USD, " + str(currency))
#     elif currency == 'usd_buy':
#         currency = usd_buy
#         print("USD, " + str(currency))
#     elif currency == 'eur_sell':
#         currency = eur_sell
#         print("EUR, " + str(currency))
#     elif currency == 'eur_buy':
#         currency = eur_buy
#         print("EUR, " + str(currency))
#     elif currency == 'stop':
#         break
#     else:
#         breakpoint()