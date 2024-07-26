# pip install webdriver-manager

from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager


options = Options()
options.add_argument('--ignore-certificate-errors')
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument('start-maximized') #это чтобы хром на весь экран открывался
# browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
# browser.get(url)