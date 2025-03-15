from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.google.com/maps/@12.9794048,77.6863744,14z?entry=ttu&g_ep=EgoyMDI1MDMxMi4wIKXMDSoASAFQAw%3D%3D")
sleep(2)

def searchplace():
    Place=driver.find_element(By.XPATH, "//input[@id='searchboxinput']")
    Place.send_keys("Chennai")
    Submit=driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[3]/div[8]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]/span[1]")
    Submit.click()
    sleep(5)
searchplace()

def directions():
    sleep(10)
    directions=driver.find_element(By.XPATH, "//span[@class='Cw1rxd google-symbols NhBTye G47vBd']")
    directions.click()
directions()

def find():
    sleep(6)
    find=driver.find_element(By.XPATH, "//input[@placeholder='Choose starting point, or click on the map...']")
    find.send_keys("Bangalore")
    sleep(6)
    search=driver.find_element(By.XPATH, "//div[@id='directions-searchbox-0']//span[@class='google-symbols'][contains(text(),'')]")
    search.click()
find()

def kilometeres():
    sleep(3)
    total_kilometers=driver.find_element(By.XPATH, "//div[@class='Fk3sm fontHeadlineSmall delay-light']")
    print("Total Kilometers", total_kilometers.text)
    sleep(5)
    Car=driver.find_element(By.XPATH, "//div[contains(text(),'324 km')]")
    print("Car Travel", Car.text)
    sleep(5)

    Train=driver.find_element(By.XPATH, "//div[contains(text(),'5 hr 10 min')]")
    print("Train",Train.text)
kilometeres()






