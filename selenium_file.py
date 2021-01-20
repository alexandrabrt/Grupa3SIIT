from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
# browser = webdriver.Edge(r"C:\Users\LenovoE14\Downloads\edgedriver\msedgedriver.exe")

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get('https://www.cel.ro/index.php?main_page=login')

get_element1 = driver.find_element_by_id('firstname')
get_element1.send_keys('Ana')

get_element2 = driver.find_element_by_id('lastname')
get_element2.send_keys('Maria')

get_element3 = driver.find_element_by_name('email_address')
get_element3.send_keys('test1010@test.ro')

get_element4 = driver.find_element_by_id('customers_gender')
get_element4.send_keys('Doamna')

get_element5 = driver.find_element_by_id('telephone')
get_element5.send_keys('0721345678')

get_element6 = driver.find_element_by_id('street_address')
get_element6.send_keys('Iasi1')

get_element7 = driver.find_element_by_id('entry_suburb')
get_element7.send_keys('Ploiesti')

from selenium.webdriver.common.keys import Keys
html = driver.find_element_by_tag_name('html')
html.send_keys(Keys.END)

get_element8 = driver.find_element_by_xpath('//*[@id="cont_nou"]/tbody[2]/tr[1]/td/div[2]/label/input')
get_element8.click()

get_element1.submit()

driver.get('https://www.cel.ro/telefoane-mobile/telefon-mobil-huawei-p30-lite-128gb-dual-sim-4g-peacock-blue-pMCE7NjArPg-l/')
# get_element_to_cart = driver.find_element_by_id('main-add-to-cart')
get_element_to_cart = driver.find_element_by_xpath('//*[@id="main-add-to-cart"]')
print(get_element_to_cart)
get_element_to_cart.click()

select_element = driver.find_element_by_xpath('//*[@id="body_cos_produse"]/tr/td/div[2]/div[2]/div/div/div/div/input')
select_element.click()
select_element.send_keys('3')


