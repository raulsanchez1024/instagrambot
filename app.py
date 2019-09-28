from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time

class Instagrambot:
  def __init__(self, username, password):
    self.username = username
    self.password = password
    self.bot = webdriver.Firefox(executable_path='/Users/raul/Downloads/geckodriver')

  def login(self):
    bot = self.bot
    bot.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
    time.sleep(3)
    username = bot.find_element_by_name('username')
    password = bot.find_element_by_name('password')
    username.clear()
    username.send_keys(self.username)
    password.send_keys(self.password)
    password.send_keys(Keys.RETURN)
    time.sleep(3)

  def like_post(self, hashtag):
    bot = self.bot
    bot.get('https://www.instagram.com/explore/tags/' + hashtag + '/')
    time.sleep(3)
    for i in range(1,3):
      bot.execute_script('window.scrollTo(0, document.body.scrollHeight)')
      posts = bot.find_elements_by_class_name('v1Nh3')
      links = [elem.find_element_by_tag_name('a').get_attribute('href')
            for elem in posts]
      print(links)
      for link in links:
        bot.get(link)
        try:
          time.sleep(5)
          bot.find_element_by_class_name('fr66n').click()
          time.sleep(5)
        except:
          print('Something went wrong')

ib = Instagrambot('<username>', '<password>')
ib.login()
ib.like_post('<hashtag>')
