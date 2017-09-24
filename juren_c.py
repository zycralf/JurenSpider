#! /usr/bin/env python
#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time  
from selenium.common.exceptions import NoSuchElementException
import urllib

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC
import selenium.webdriver.support.ui as ui

from selenium import webdriver
    
class JUREN:
    def __init__(self,baseUrl,section):
        self.chapter_url=baseUrl
        #self.driver = webdriver.PhantomJS()
        #self.driver = webdriver.Chrome()
        self.n=section
        self.p=1
        
    def save_f(self,url, image_name):
        try:
            image=urllib.urlopen(url).read()
            f = open(image_name, 'wb')
            f.write(image)
            f.close()
        except Exception, et:
            print(et)
    
    def is_visible(self,driver,locator, timeout=2):
        try:
            ui.WebDriverWait(driver, timeout,0.5).until(EC.visibility_of_element_located((By.XPATH, locator)))
            return True
        except TimeoutException:
            return False
    

    def catch(self):
        #chapter_url="http://www.57mh.com/118/"
        #driver = webdriver.PhantomJS()
        driver = webdriver.Chrome()
        driver.implicitly_wait(4) 
        driver.get(self.chapter_url)

        n=self.n
        p=self.p

        
        if self.is_visible(driver,'/html/body/div[2]/div/h2/a'):
            driver.maximize_window()
            driver.execute_script("window.scrollTo(0, 1450);")
        
        
        #driver.maximize_window()
        #driver.execute_script("window.scrollTo(0, 1450);")
                
        driver.find_element_by_css_selector("#chpater-list-1 > ul:nth-child(1)").click()
        
        pages=driver.find_elements_by_css_selector("#chpater-list-1 > ul:nth-child(1) > li > a")
        
        
        for each in pages:
            each.click()
            driver.switch_to_window(driver.window_handles[1])
            dir_path = driver.find_element_by_css_selector("body > div.w996.title.pr > h2").text
            dir_path='E:/Python_kankei/' + dir_path +'/' 

            os.makedirs(dir_path)
            
            while True:
                image_url=driver.find_element_by_css_selector('#manga').get_attribute('src')
                file_name=dir_path+bytes(p)+'.jpg'
                self.save_f(image_url,file_name)
                p=p+1
                print type(driver.find_element_by_css_selector("#next"))
                driver.find_element_by_css_selector("#next").click()
                try:
                    driver.find_element_by_css_selector('#pb')
                    break
                except NoSuchElementException:
                    print "ok"
            n=n-1
            driver.close()
            driver.switch_to_window(driver.window_handles[0])
            


chapter="http://www.57mh.com/118/"
sec=94
juren = JUREN(chapter,sec)
juren.catch()
            

        





