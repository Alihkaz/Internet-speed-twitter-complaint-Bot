#

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from method import InternetSpeedTwitterBot


promised_download=150
promised_upload=10

chrome_driver_path="YOUR CHROME DRIVER PATH"

TWITTER_EMAIL= "YOUR TWITTER EMAIL"
TWITTER_PASSWORD= "YOUR TWITTER PASSWORD"


#-----------------------------------------------------------------------------------------------------------#

twitter_bot=InternetSpeedTwitterBot(chrome_driver_path)# here the parameter or the variable is the driver path which have to be filled ,
                                                        #and we provide a value for that parameter which is the chrome_driver_path once we called the class ! 

twitter_bot.get_internet_speed()


twitter_bot.tweet_at_provider()




   









