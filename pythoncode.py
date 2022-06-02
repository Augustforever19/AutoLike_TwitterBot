from selenium import webdriver #To automate web browser interaction ,i am using chrome webdriver
from selenium.webdriver.common.keys import keys
from tkinter import *
from time import sleep
import pyautogui #Automate liking on twitter website

window=TK() #initializing the tkinter object
window.geometry('700*600') #width and height of the window
#Email
emails=Label(window,text='Enter E-mail ID',font='Times 24 Bold')
emails.grid(row=0,column=0)
entry1=Entry(window) #to provide the email input
entry1.grid(row=0,column=6)
#Password
Passwords=Label(window,text='Enter E-mail ID',font='Times 24 Bold')
Passwords.grid(row=2,column=0)
entry2=Entry(window) #to provide the email input
entry2.grid(row=2,column=6)
#Hashtag
hashtags=Label(window,text='Enter E-mail ID',font='Times 24 Bold')
hashtags.grid(row=4,column=0)
entry3=Entry(window) #to provide the email input
entry3.grid(row=4,column=6)

#button
b1=Button(window,text='GO',command.execute,width=12,bg='gray')
b1.grid(row=7,column=6)
window.mainloop()


#Twitter Class
class twitter:
    def __init__(self,username,password):
        self.username=username
        self.password=password
        self.bot=webdriver.chrome(execute_path='#path of web-driver')
        
    def login(self):
        bot=self.bot
        bot.get('https://twitter.com/i/flow/login')
        sleep(5)
        emails=bot.find_element_by_name('session[Username_or_email]')
        passwords=bot.find_element_by_name('session[password]')
        emails.clear()
        passwords.clear()
        emails.send_keys(self.username)
        passwords.send_keys(self.password)
        passwords.send_keys(keys.RETURN)
        sleep(10)
    def like_tweet(self,entry3):
        bot=self.bot
        bot.get('url'+str(entry3)+'url')
        while True:
            pyautogui.click(pyautogui.locateCenterOnScreen('1.png'))
            sleep(5)
            bot.execute_script('window.ScrollTo(0,document.body.ScrollHeight)')
            sleep(5)
def execute():
    log=twitter(str(entry1.get()),str(entry2.get()))
    log.login()
    log.like_tweet(entry3.get())
    
execute()