
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        return WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(locator))

    def click_on_element(self, locator):
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    def set_text_on_element(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    def drag_and_drop_on_element(self, locator_one, locator_two):
        draggable = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(locator_one))
        droppable = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(locator_two))
        action_chains = ActionChains(self.driver)
        action_chains.drag_and_drop(draggable, droppable).perform()

    def get_value(self, locator):
        element = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(locator))
        value = element.text
        return value

    def element_is_not_displayed(self, locator):
        return WebDriverWait(self.driver, 15).until(EC.invisibility_of_element_located(locator))

    def get_current_url(self):
        return self.driver.current_url

    def element_is_present(self, locator):
        return WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(locator))




