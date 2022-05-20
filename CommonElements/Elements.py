from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import random


class Adopt():
    def __init__(self, driver):
        self.driver = driver
        self.Name_ID = "order_name"
        self.Address_ID = "order_address"
        self.Emai_ID = "order_email"

    def ClickAdopt(self):
        self.driver.find_element(By.XPATH, "//input[@value='Adopt Me!']").click()


class ViewDetails(Adopt):

    def Brook_ViewDetails(self):
        self.driver.find_element(By.XPATH, "//form[@action='/puppies/4']").click()

    def Hanna_ViewDetails(self):
        self.driver.find_element(By.XPATH, "//form[@action='/puppies/3']").click()

    def Maggie_ViewDetails(self):
        self.driver.find_element(By.XPATH, "//form[@action='/puppies/1']").click()

    def Ruby_ViewDetails(self):
        self.driver.find_element(By.XPATH, "//form[@action='/puppies/8']").click()

    def Sparky_ViewDetails(self):
        self.driver.find_element(By.XPATH, "//form[@action='/puppies/9']").click()

    def Spud_ViewDetails(self):
        self.driver.find_element(By.XPATH, "//form[@action='/puppies/2']").click()

    def Tipsy_ViewDetails(self):
        self.driver.find_element(By.XPATH, "//form[@action='/puppies/6']").click()

    def Topsy_ViewDetails(self):
        self.driver.find_element(By.XPATH, "//form[@action='/puppies/5']").click()

    def Twinkie_ViewDetails(self):
        self.driver.find_element(By.XPATH, "//form[@action='/puppies/7']").click()

    def Random_Click(self):
        elements = self.driver.find_elements(By.XPATH, "//input[@class='rounded_button']")
        r1 = random.choice(elements)
        r1.click()

class AdditionalProducts(Adopt):
    def CollarLeash(self):
        self.driver.find_element(By.XPATH, "//input[@id='collar']").click()

    def ChewToy(self):
        self.driver.find_element(By.XPATH, "//input[@id='toy']").click()

    def TravelCarrier(self):
        self.driver.find_element(By.XPATH, "//input[@id='carrier']").click()

    def FirstVetVisit(self):
        self.driver.find_element(By.XPATH, "//input[@id='vet']").click()

    def Random_Checkbox(self):
        checkboxs = self.driver.find_elements(By.XPATH, "//input[@type='checkbox']")
        for i in range(3):
            i = random.choice(checkboxs)
            i.click()

    def CompleteTheAdoption(self):
        self.driver.find_element(By.XPATH, "//input[@value='Complete the Adoption']").click()

    def AdoptAnotherPuppy(self):
        self.driver.find_element(By.XPATH, "//input[@value='Adopt Another Puppy']").click()


class Details(Adopt):
    def Name(self, name):
        self.driver.find_element(By.ID, self.Name_ID).send_keys(name)

    def Address(self, address):
        self.driver.find_element(By.ID, self.Address_ID).send_keys(address)

    def Email(self, email):
        self.driver.find_element(By.ID, self.Emai_ID).send_keys(email)


class Payment(Adopt):
    def Check(self):
        dropdow = Select(self.driver.find_element(By.XPATH, "//select[@id='order_pay_type']"))
        dropdow.select_by_visible_text("Check")

    def CreaditCard(self):
        dropdow1 = Select(self.driver.find_element(By.XPATH, "//select[@id='order_pay_type']"))
        dropdow1.select_by_visible_text("Credit card")


class Order(Adopt):
    def Order(self):
        self.driver.find_element(By.XPATH, "//input[@name='commit']").click()
