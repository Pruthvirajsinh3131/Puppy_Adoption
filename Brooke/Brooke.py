from selenium import webdriver
from CommonElements.Elements import Adopt
from CommonElements.Elements import ViewDetails
from CommonElements.Elements import AdditionalProducts
from CommonElements.Elements import Details
from CommonElements.Elements import Payment
from CommonElements.Elements import Order
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://spartantest-puppies.herokuapp.com/")

view_details = ViewDetails(driver)
view_details.Brook_ViewDetails()
time.sleep(2)

adopt = Adopt(driver)
adopt.ClickAdopt()
time.sleep(2)

additional_product = AdditionalProducts(driver)
additional_product.ChewToy()
additional_product.TravelCarrier()
time.sleep(2)
additional_product.CompleteTheAdoption()
time.sleep(2)

details = Details(driver)
details.Name("Vala")
details.Address("Warsaw")
details.Email("abc@123abc.com")
time.sleep(2)

payment = Payment(driver)
payment.Check()
time.sleep(2)

place_order = Order(driver)
place_order.Order()
time.sleep(2)

driver.close()
driver.quit()
