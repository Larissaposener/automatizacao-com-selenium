#equipe larissa 202108575127 e willian andré 202108655007

from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path=r"C:\Users\Larissa Posener\OneDrive\Área de Trabalho\chromedriver.exe")
driver.get("https://www.youtube.com")


driver.find_element_by_name("search_query").send_keys("Lady Gaga")

searchButton = driver.find_element_by_xpath('/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/button')
searchButton.click()

time.sleep(4)
driver.close()

