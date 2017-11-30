import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

from app.models import Website

class RunScript():
    """docstring for ClassName"""

    def __init__(self):
        self.chrome_options = Options()
        self.chrome_options.add_argument("disable-infobars")
        self.driver = webdriver.Chrome(chrome_options=self.chrome_options)
        # self.driver = webdriver.Chrome()
        self.urls = Website.objects.values_list('url').order_by('?')
        self.__call__()

    def __del__(self):
        self.driver.close()

    def __call__(self):
        for url in self.urls:
            self.driver.get(url[0])
            scheight = .1
            while scheight < 9.9:
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight/%s);" % scheight)
                scheight += .01
        return True

        
        
