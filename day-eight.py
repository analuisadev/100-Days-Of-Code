from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
import time

class WhatsappBot: 
     def __init__(self):
        #My message 
        self.mensagem = 'Hello people, this is my first WhatsApp bot. Did you like it?'
        #The groups and people that the message will be sent to
        self.group = "mãe"
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(
            executable_path=r'./chromedriver.exe')
     def MessageSending(self):
            self.driver.get('https://web.whatsapp.com')
            time.sleep(30)
            group = self.driver.find_element_by_xpath('//span[@title="mãe"]')
            time.sleep(3)
            group.click()
            chat_box = self.driver.find_element_by_class_name('DuUXI')
            time.sleep(2)
            chat_box.click()
            chat_box.send_keys(self.mensagem)
            botao_enviar = self.driver.find_element_by_xpath(
                "//span[@data-icon='send']")
            time.sleep(2)
            botao_enviar.click()
            time.sleep(1)
            
bot = WhatsappBot()
bot.MessageSending()