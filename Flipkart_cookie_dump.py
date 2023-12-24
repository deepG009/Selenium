import undetected_chromedriver as uc
import pickle
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
#from selenium.webdriver.chrome.options import ChromeOptions

if __name__ == '__main__':
#    options = uc.ChromeOptions()
#    options.add_argument("--headless")
    options = uc.ChromeOptions()
    options.headless = False
    driver = uc.Chrome(options=options,version_main=119)
    

    driver.get("https://www.flipkart.com/")
    driver.find_element(By.CSS_SELECTOR,"body > div.fbDBuK._3CYmv5 > div > div > div > div._3skCyB > div > form > div._22Dgdy._29BEA8 > input").send_keys('8329318571')
    driver.find_element(By.CSS_SELECTOR,"body > div.fbDBuK._3CYmv5 > div > div > div > div._3skCyB > div > form > div.YLloxs > button").click()
#    WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"#container > div > div.q8WwEU > div > div > div > div > div.css-1dbjc4n.r-13awgt0 > div > div.css-1dbjc4n.r-13awgt0.r-1iqfa7g.r-60vfwk > div > div._2NhoPJ > header > div._2msBFL > div:nth-child(2) > div > div > ul > a:nth-child(9) > li")))
    time.sleep(25)
    cookies = driver.get_cookies()
    pickle.dump(cookies,open("flipkartcookies3.pkl","wb"))

driver.quit()
