from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options

opt = Options()
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")
driver = webdriver.Chrome(chrome_options= opt, executable_path = 'C:\\Users\\SURAJ MOOLYA\\Downloads\\chromedriver_win32\\chromedriver.exe')
#you have to update the above address with the address of the selenoid on your coumputer 
driver.get('https://accounts.google.com/ServiceLogin/webreauth?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ss=1&scc=1&authuser=0&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin')

username = driver.find_element_by_xpath('//*[@id="identifierId"]')
username.click()
username.send_keys('XXXXXXXXXXXXX')
#replace XXXXXXXXXXXX  by the email address of the by you which you want to send mail

next = driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/div[2]')
next.click()

sleep(5)
password = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
password.click()
password.send_keys('XXXXXXXXXXXX')
#replace XXXXXXXXX by the password of the above email addresss 

next = driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/div[2]')
next.click()

sleep(4)
compose = driver.find_element_by_xpath('/html/body/div[7]/div[3]/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div[1]/div/div')
compose.click()

sleep(10)
s = ''
f = open('D:\emails.txt','r')
#create a .txt file containing the list of email address to which you want send mail and update the address above with the address of the file.
for x in f:
    s = s + x + ','
recepients = driver.find_element_by_xpath('/html/body/div[17]/div/div/div/div[1]/div[3]/div[1]/div[1]/div/div/div/div[3]/div/div/div[4]/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[1]/td[2]/div/div/textarea')
recepients.click()
recepients.send_keys(s)
f.close()
sleep(10)
f = open('D:\subject.txt','r')
#create a .txt file containing the subject of the mail and update the address above with the address of the file.

subject = driver.find_element_by_xpath('/html/body/div[17]/div/div/div/div[1]/div[3]/div[1]/div[1]/div/div/div/div[3]/div/div/div[4]/table/tbody/tr/td[2]/form/div[3]/div/input')
subject.send_keys(f.read())
sleep(5)
body = driver.find_element_by_xpath('/html/body/div[17]/div/div/div/div[1]/div[3]/div[1]/div[1]/div/div/div/div[3]/div/div/div[4]/table/tbody/tr/td[2]/table/tbody/tr[1]/td/div/div[1]/div[2]/div[1]/div/table/tbody/tr/td[2]/div[2]/div')
body.click()
f.close()
f = open('D:\\body.txt','r')

#create a .txt file containing the body of the mail and update the address above with the address of the file.
body.send_keys(f.read())
f.close()

send = driver.find_element_by_xpath('/html/body/div[17]/div/div/div/div[1]/div[3]/div[1]/div[1]/div/div/div/div[3]/div/div/div[4]/table/tbody/tr/td[2]/table/tbody/tr[2]/td/div/div/div[4]/table/tbody/tr/td[1]/div/div[2]/div[1]')
send.click()
#email has been sent successfully
