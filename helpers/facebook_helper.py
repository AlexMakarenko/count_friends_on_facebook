from elementium.drivers.se import SeElements


class Facebook:
    def __init__(self, driver):
        self.driver = driver
        self.se = SeElements(browser=self.driver)

    def open_home_page(self):
        self.driver.get("https://www.facebook.com")

    def login(self, email, password):
        self.se.find('#email', wait=True, ttl=5).clear().write(email)
        self.se.find('#pass', wait=True, ttl=5).clear().write(password)
        self.se.find('#loginbutton', wait=True, ttl=5).click()

    def open_profile(self):
        self.se.xpath('//a[@title="Profile" or @title="Профиль"]', wait=True, ttl=5).click()

    def open_friends_page(self):
        self.se.xpath('//a[text()="Friends" or text()="Друзья"]', wait=True, ttl=5).click()

    def get_number_of_friends_badge(self):
        return self.se.xpath('//a[@name="All friends" or @name="Все друзья"]/span[2]', wait=True, ttl=5).text()

    def scroll_down(self):
        movies_block = self.se.find('#pagelet_timeline_medley_movies')
        count = 50
        while not len(movies_block):
            if count == 0:
                break
            else:
                self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
                count -= 1

    def count_friends(self):
        friends = self.se.xpath('//div[@data-testid="friend_list_item"]', wait=True, ttl=10)
        return len(friends)
