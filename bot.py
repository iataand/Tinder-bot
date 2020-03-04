from selenium import webdriver
from time import sleep
from secrets import username, password


class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get("https://tinder.com")
        sleep(4)

        button = self.driver.find_element_by_xpath(
            '//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button')
        button.click()

        baseWindow = self.driver.window_handles[0]
        self.driver.switch_to_window(self.driver.window_handles[1])

        usernameBox = self.driver.find_element_by_xpath('//*[@id="email"]')
        passwordBox = self.driver.find_element_by_xpath('//*[@id="pass"]')

        usernameBox.send_keys(username)
        passwordBox.send_keys(password)

        loginButton = self.driver.find_element_by_xpath(
            '//*[@id="u_0_0"]')
        loginButton.click()

        self.driver.switch_to_window(baseWindow)

        sleep(4)
        allowButton = self.driver.find_element_by_xpath(
            '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        allowButton.click()

        notInteresed = self.driver.find_element_by_xpath(
            '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
        notInteresed.click()

    def like(self):
        likeButton = self.driver.find_element_by_xpath(
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        likeButton.click()

    def closePopup(self):
        notInt = self.driver.find_element_by_xpath(
            '//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        notInt.click()

    def closeMatch(self):
        close = self.driver.find_element_by_xpath(
            '//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        close.click()

    def autoSwipe(self):
        while True:
            sleep(3)
            try:
                self.like()

            except Exception:
                try:
                    self.closePopup()
                except Exception:
                    self.closeMatch()


bot = TinderBot()
bot.login()
bot.autoSwipe()
