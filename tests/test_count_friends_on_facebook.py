from helpers.facebook_helper import Facebook
from config import log

FB_EMAIL = 'email'
FB_PASS = 'password'


def test_count_friends(driver):
    fb = Facebook(driver)
    fb.open_home_page()
    fb.login(email=FB_EMAIL, password=FB_PASS)
    fb.open_profile()
    fb.open_friends_page()
    log.info('Number of friends (badge): {}'.format(fb.get_number_of_friends_badge()))
    fb.scroll_down()
    log.info('Number of friends counted by selenium: {}'.format(fb.count_friends()))
