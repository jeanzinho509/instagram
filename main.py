from selenium.webdriver.firefox.service import Service
from selenium.webdriver import Firefox


class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        service = Service(r'C:\Users\devgl\OneDrive\Área de Trabalho\geckodriver\geckodriver.exe')
        self.driver = Firefox(service=service)

    def login(self):
        driver = self.driver
        driver.get('https://www.instagram.com')

gleycBot = InstagramBot('gleyctavaress', 'suasenha')
gleycBot.login()