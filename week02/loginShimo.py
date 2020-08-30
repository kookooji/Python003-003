from time import sleep

from selenium import webdriver


class LoginShinmo:
    def login(self):
        bro = webdriver.Chrome(executable_path= '../chromedriver')
        bro.get('https://shimo.im/welcome')
        bro.maximize_window()
        try:
            bro.find_element_by_xpath('//nav[@class="wrapper"]/div[3]/a[2]/button').click()
        except AttributeError as e:
            print(e)
        sleep(1)
        try:
            bro.find_element_by_xpath('//*[@class="StyledLogin-sc-2oZUsG bZrWhJ"]/div[1]/div[1]/div/input').send_keys('mobileOrEmail')
            bro.find_element_by_xpath('//*[@class="StyledLogin-sc-2oZUsG bZrWhJ"]/div[1]/div[2]/div/input').send_keys('password')
            bro.find_element_by_xpath('//*[@class="sm-button submit sc-1n784rm-0 bcuuIb"]').click()
        except AttributeError as e:
            print(e)

        sleep(5)
        bro.close()


if __name__ == '__main__':
    shimo = LoginShinmo()
    shimo.login()
