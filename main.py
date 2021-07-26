from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

browser = "D:\Hobby\chromedriver.exe"
driver = webdriver.Chrome(browser)
wait = WebDriverWait(driver, 300)
productPage = "https://shopee.co.id/Fantech-Multimedia-Office-Keyboard-K3M-i.194833069.5750292631?adsid=0&campaignid=0&position=7"

# Login with qr code
def login():
		driver.maximize_window()
		driver.get("https://shopee.co.id/buyer/login")
		wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/div/div[2]/div/div/form/div/div[1]/div/div[2]/a')))
		driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div/div/form/div/div[1]/div/div[2]/a').click()
		wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="main"]/div/div[2]/div[1]/div[1]/div/ul/li[2]/div/div/div/div[1]/img')))

# Go to product page
def buyProduct(link):
		driver.get(link)
		wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/div/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[5]/div/div/button[2]')))
		driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[5]/div/div/button[2]').click()

def checkout():
		# Wait for the popup to disappear and click the checkout button
		time.sleep(3.5)
		driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[2]/div/div[3]/div[2]/div[7]/button[4]').click()
		# Wait for the popup (again)
		time.sleep(3.5)
		# Payment method
		driver.find_element_by_xpath('//*[@id="main"]/div/div[3]/div[2]/div[4]/div[1]/div/div[3]').click()
		# Bank Transfer
		driver.find_element_by_xpath('//*[@id="main"]/div/div[3]/div[2]/div[4]/div[1]/div/div[1]/div[2]/span[2]/button').click()
		# BRI
		driver.find_element_by_xpath('//*[@id="main"]/div/div[3]/div[2]/div[4]/div[1]/div/div[2]/div[1]/div[2]/div[4]').click()
		
def main(link):
		login()
		buyProduct(link)
		checkout()

main(productPage)