from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://www.google.com")
driver.back()
driver.forward()
driver.refresh()
print(driver.title)
print(driver.current_url)

product = driver.find_element(By.XPATH, "//a[@href='/products/shirt']")
product.click()

add_to_cart = driver.find_element(By.XPATH, "//button[text()='Добавить в корзину']")
add_to_cart.click()

cart_items = driver.find_elements(By.XPATH, "//td[@class='cart-item-name']")
assert len(cart_items) == 1, "В корзине должен быть только 1 товар"
assert cart_items[0].text == "Рубашка", "В корзину добавлен неправильный товар"

driver.quit()
