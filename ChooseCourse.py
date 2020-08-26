"""
Version: 1.0
Author: Nameless
Date: 2020-08-26
"""

from selenium import webdriver
import time 

class Choose():
    def __init__(self):
        self.browser = webdriver.Chrome(executable_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe")
        self.browser.get("http://202.115.133.173:805/Login.html")
        account = int(input("请输入学号:"))
        passwd =  str(input("请输入密码:"))
        time.sleep(3)
        self.browser.find_element_by_id("txtUser").send_keys(account)#学号
        self.browser.find_element_by_id("txtPWD").send_keys(passwd)#密码
        self.browser.find_element_by_id("ibtnLogin").click()#登录
        time.sleep(1)
    def switch(self,flag):
        if(flag == 1):
            self.choosePE()
        elif(flag == 2):
            self.chooseOP()
        else:
            return  


    def choosePE(self):
        #browser.find_element_by_xpath("//span[@class='nav_menu_04']").click()
        time.sleep(1)
        #browser.find_element_by_xpath("//a[@href='Default.aspx#bx']").click()
        time.sleep(1)
        #browser.find_element_by_xpath("//a[@href='Default.aspx#xx']").click()
        #browser.switch_to.alert.accept()
        time.sleep(1)
        #titles =  browser.find_elements_by_xpath("//div[@class='floatDiv50']//a//b")
    def chooseOP(self):
        self.browser.find_element_by_xpath("//span[@class='nav_menu_04']").click()
        time.sleep(1)
        self.browser.find_element_by_xpath("//a[@href='Default.aspx#bx']").click()
        time.sleep(1)
        self.browser.find_element_by_xpath("//a[@href='Default.aspx#xx']").click()
        self.browser.switch_to.alert.accept()
        time.sleep(1)
        titles =  self.browser.find_elements_by_xpath("//input[@class='btn_conn' and @chooseflg = 'true']/parent::div/parent::div/div/a/b")
        courses = self.browser.find_elements_by_xpath("//input[@class='btn_conn' and @chooseflg = 'true']")
        print("=="*20)
        print("现在可选课程为:")
        for i in range(len(titles)):
            print(i,'.',titles[i].text)
        print("=="*20)
        index = int(input("请输入你要选课程前的序号:"))
        courses[index].click()
        time.sleep(1)
        self.browser.find_element_by_xpath("//div[@id='facebox']/div/div[@class='content']/div[2]/ul[@id]/li/div[@class='floatDiv25']/input[@name='course_02_1']").click()
        self.browser.find_element_by_xpath("//div[@id='facebox']/div/div/div[@style]/input").click()

if __name__ == "__main__":
    banner = """
    ========================================================================
                                                                            
        /|    / /                                                           
       //|   / /  ___      _   __      ___     //  ___      ___      ___    
      // |  / / //   ) ) // ) )  ) ) //___) ) // //___) ) ((   ) ) ((   ) ) 
     //  | / / //   / / // / /  / / //       // //         \ \      \ \     
    //   |/ / ((___( ( // / /  / / ((____   // ((____   //   ) ) //   ) )   

    ========================================================================
        https://github.com/NameQuin/CDUTChooseClass
        https://gitee.com/namelessWss/get-courseof-cdut
    ========================================================================
    """
    print(banner)
    choose = Choose()
    flag = -1
    while(flag!=0):
        print("*"*30)
        print("1.选择体育课(还没写)")
        print("2.选择选修")
        print("0.退出")
        flag = int(input("请输入序号:"))
        choose.switch(flag)
