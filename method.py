
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

promised_download=150
promised_upload=10

chrome_driver_path="YOUR CHROME DRIVER PATH"

TWITTER_EMAIL= "YOUR TWITTER EMAIL"
TWITTER_PASSWORD= "YOUR TWITTER PASSWORD"




class InternetSpeedTwitterBot:
  def __init__(self,driver_path):
    self.driver=webdriver.Chrome(executable_path=driver_path)
    self.up=0
    self.down=0
#--------------------------------------------------------------------------------------------------------------------#
  def get_internet_speed(self):
    
   self.driver.get("https://www.speedtest.net/result/14945486242") #the link to the website we want to scrap and  automate

   self.driver.implicitly_wait(20) 
    
   go_button = self.driver.find_element(By.XPATH,"//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]") #finding the go button

   go_button.click()

   self.driver.implicitly_wait(20)  
    
   self.up= (self.driver.find_element(By.CLASS_NAME,"result-data-large number result-data-value upload-speed")).text
   self.down=(self.driver.find_element(By.CLASS_NAME,"result-data-large number result-data-value download-speed")).text
  
#-----------------------------------------------------------------------------------------------------#
  
  def tweet_at_provider(self):
    
    #login:
    
    self.driver.get("https://twitter.com/i/flow/login?redirect_after_login=%2F%3Flang%3Dar")
    time.sleep(20)
    #sending the email
    email=self.driver.find_element(By.CLASS_NAME,"css-1dbjc4n r-18u37iz r-1pi2tsx r-1wtj0ep r-u8s1d r-13qz1uu")
    email.send_keys(TWITTER_EMAIL)
           

    next=self.driver.find_element(By.CLASS_NAME,"//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div")
    self.driver.implicitly_wait(20) 
    
    #sending the password 
    password=self.driver.find_element(By.XPATH,"//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]")
    password.send_keys(TWITTER_PASSWORD)
    
    #hiding password
    hide_password=self.driver.find_element(By.XPATH,"//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[2]/div/div/svg")
    hide_password.click()
    
    #confirming the login
    finally_login=self.driver.find_element(By.XPATH,"//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div")
    finally_login.click()

    self.driver.implicitly_wait(20) 

    #posting the compaiment:
    
    #finding the field where we will write
    writing=self.driver.find_element(By.CLASS_NAME,"public-DraftStyleDefault-block public-DraftStyleDefault-ltr") 

    #sending the compaiment as a keys
    writing.send_keys(f"Hey @bluejet , why my internet speed ({self.up}/{self.down}) when I pay for{promised_upload}/{promised_download}")

    #sending it 
    posting=self.driver.find_element(By.XPATH,"//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[3]")


    posting.send_keys(Keys.ENTER)

    self.driver.implicitly_wait(20) 

    self.driver.quit()
