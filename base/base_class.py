import datetime


class Base():

    def __init__(self, driver):
        self.driver = driver

    """Method get current url"""

    def get_current_url(self):
        get_this = self.driver.current_url
        print("Current url is " + get_this)

    """Method assert word"""

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print ("Good value word")

    """Method Screenshot"""

    def screenshot(self):
        nowdate = datetime.datetime.utcnow().strftime('%Y.%m.%d.%H.%M.%S')
        name_screen = "screenshot " + nowdate + ".png"
        self.driver.save_screenshot('C:\\Users\\Anna\\PycharmProjects\\Project_white_wind\\screen\\' + name_screen)

    """Method assert url"""

    def assert_url(self, result):
        get_this = self.driver.current_url
        assert get_this == result
        print("Good value url")