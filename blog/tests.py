from django.test import TestCase, LiveServerTestCase
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
import unittest
import time

class FormTesting(LiveServerTestCase):
    def testFormLogin(self):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        
        driver.get(self.live_server_url+'/accounts/login/')
        
        username = driver.find_element_by_id('id_login')
        password = driver.find_element_by_id('id_password')
        submit = driver.find_element_by_id('login_btn')
        
        username.send_keys("GustavoFring")
        password.send_keys("LosPollosHermanos")
        
        submit.click()
        
        assert "AnimaCritic - Uma Comunidade CESAR School" in driver.title
        
        
        
    def testFormSignUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        
        driver.get(self.live_server_url+'/accounts/signup/')
        
        username = driver.find_element_by_id('id_username')
        email = driver.find_element_by_id('id_email')
        password1 = driver.find_element_by_id('id_password1')
        password2 = driver.find_element_by_id('id_password2')
        submit = driver.find_element_by_id('signup_btn')
        
        username.send_keys('AlguemNovo')
        email.send_keys('AlguemNovo@gmail.com') 
        password1.send_keys('Senha12345') 
        password2.send_keys('Senha12345')
        
        submit.click()
        
        assert "AnimaCritic - Uma Comunidade CESAR School" in driver.title
                
        
    def testLogout(self):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        
        driver.get(self.live_server_url+'/accounts/signup/')
        
        username = driver.find_element_by_id('id_username')
        email = driver.find_element_by_id('id_email')
        password1 = driver.find_element_by_id('id_password1')
        password2 = driver.find_element_by_id('id_password2')
        submit = driver.find_element_by_id('signup_btn')
        
        username.send_keys('AlguemNovo')
        email.send_keys('AlguemNovo@gmail.com') 
        password1.send_keys('Senha12345') 
        password2.send_keys('Senha12345')
        
        submit.click()
        
        driver.get(self.live_server_url+'/accounts/logout/')
        
        submit = driver.find_element_by_id('logout_btn')
        
        submit.click()
        
        assert "AnimaCritic - Uma Comunidade CESAR School" in driver.title  
          
    
    def testAddPost(self):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        
        driver.get(self.live_server_url+'/accounts/login/')
        
        username = driver.find_element_by_id('id_login')
        password = driver.find_element_by_id('id_password')
        submit = driver.find_element_by_id('login_btn')
        
        username.send_keys("GustavoFring")
        password.send_keys("LosPollosHermanos")
        
        submit.click()
        
        driver.get(self.live_server_url+'/new_post/')

        post_title = driver.find_element_by_id('id_title') 
        summary = driver.find_element_by_id('id_summary')
        slug = driver.find_element_by_id('id_slug')
        content = driver.find_element_by_id('id_content')
        submit = driver.find_element_by_id('post_btn')
        
        post_title.send_keys('Titulo')
        summary.send_keys('Resumo') 
        slug.send_keys('Slug') 
        content.send_keys('Conteudo')
        
        submit.click()

        assert "AnimaCritic - Uma Comunidade CESAR School" in driver.title
        
        driver.close()

            