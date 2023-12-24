import undetected_chromedriver as uc
from selenium import webdriver
import pickle
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
#from selenium.webdriver.chrome.options import ChromeOptions


# Function to perform long press on an element
def long_press(element):
    action = ActionChains(driver)
    action.click_and_hold(element).perform()
    # You can adjust the sleep time based on your needs
    driver.implicitly_wait(7)
    action.release(element).perform()

if __name__ == '__main__':
#    options = uc.ChromeOptions()
#    options.add_argument("--headless")


    
    options = uc.ChromeOptions()
    options.headless = False
    
#    options2 = webdriver.ChromeOptions()
    options.add_argument(r'--user-data-dir=C:\Users\Your_Name\AppData\Local\Google\Chrome\User Data\Default') # add your directory name insted of "Your name"
    
    driver = uc.Chrome(options=options,version_main=119)
    
    driver.get("https://www.flipkart.com/")    
    cookies = pickle.load(open("flipkartcookies2.pkl","rb"))
    time.sleep(4)
    #"Your diver.get requests goes here"
    # example:   driver.find_element(By.CSS_SELECTOR,"#container > div > div._2c7YLP.UtUXW0._6t1WkM._3HqJxg > div._1YokD2._2GoDe3 > div._1YokD2._3Mn1Gg.col-5-12._78xt5Y > div:nth-child(2) > div > ul > li > form > button").click()
    # sequence stack
  driver.quit()
