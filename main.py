import csv
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
#-------------------------------------------------------------------------------
# Setup
Username = 0
Email = 1
URL = 2

    

with open('data.csv', 'r') as csv_file:

    csv_reader = csv.reader(csv_file)

#-------------------------------------------------------------------------------
# Web Automation

    for line in csv_reader:

        driver = webdriver.Chrome()
        driver.get('https://gainweb.org/submit.php')
        driver.maximize_window()
        time.sleep(5)

        freelink = driver.find_element("xpath", '/html/body/div[5]/div[4]/div[2]/form/table/tbody/tr[1]/td/div/div[1]/table/tbody/tr[3]/td[1]/input')
        freelink.click()
        time.sleep(5)

        username_field = driver.find_element("xpath", '//*[@id="OWNER_NAME"]')
        username_field.send_keys(line[0])
        time.sleep(3)

        Email_field = driver.find_element("xpath", '//*[@id="OWNER_EMAIL"]')
        Email_field.send_keys(line[1])
        time.sleep(3)

        URL_field = driver.find_element("xpath", '//*[@id="URL"]')
        URL_field.send_keys(line[2])
        time.sleep(3)

        Title_field = driver.find_element("xpath", '//*[@id="TITLE"]')
        Title_field.send_keys(line[3])
        time.sleep(3)

        Description_field = driver.find_element("xpath", '//*[@id="DESCRIPTION"]')
        Description_field.send_keys(line[4])
        time.sleep(3)
  
        element=driver.find_elements(By.NAME, ('CATEGORY_ID'))
        print('ok')
        drp=Select(element[0])
        drp.select_by_visible_text("|   |   |___Internet and Web")
        time.sleep(4)

        agree = driver.find_elements(By.NAME, 'AGREERULES')
        agree[0].click()
        time.sleep(10)

        submit = driver.find_elements(By.XPATH, '/html/body/div[5]/div[4]/div[2]/form/table/tbody/tr[13]/td/input')
        submit[0].click()


#---------------------------------------------------------------------------------------------------------------------------------------------

with open('data.csv', 'r') as csv_file:

    csv_reader = csv.reader(csv_file)




    for line in csv_reader:

            driver = webdriver.Chrome()
            driver.get('http://www.addlinkzfree.com/submit.php')
            driver.maximize_window()
            time.sleep(5)

            freelink = driver.find_element("xpath", '//*[@id="content"]/table/tbody/tr/td/form/table[1]/tbody/tr/td/table/tbody/tr[4]/td[1]/input')
            freelink.click()
            time.sleep(5)

            username_field = driver.find_element("xpath", '//*[@id="content"]/table/tbody/tr/td/form/table[2]/tbody/tr/td/table/tbody/tr[4]/td[2]/input')
            username_field.send_keys(line[0])
            time.sleep(3)

            Email_field = driver.find_element("xpath", '//*[@id="content"]/table/tbody/tr/td/form/table[2]/tbody/tr/td/table/tbody/tr[5]/td[2]/input')
            Email_field.send_keys(line[1])
            time.sleep(3)

            URL_field = driver.find_element("xpath", '//*[@id="content"]/table/tbody/tr/td/form/table[2]/tbody/tr/td/table/tbody/tr[2]/td[2]/input')
            URL_field.send_keys(line[2])
            time.sleep(3)

            Title_field = driver.find_element("xpath", '//*[@id="content"]/table/tbody/tr/td/form/table[2]/tbody/tr/td/table/tbody/tr[1]/td[2]/input')
            Title_field.send_keys(line[3])
            time.sleep(3)

            Description_field = driver.find_element("xpath", '//*[@id="content"]/table/tbody/tr/td/form/table[2]/tbody/tr/td/table/tbody/tr[3]/td[2]/textarea')
            Description_field.send_keys(line[4])
            time.sleep(3)

            # Category_field = driver.find_element("xpath", '//*[@id="container"]/table/tbody/tr/td/form/table[2]/tbody/tr/td/table/tbody/tr[6]/td[2]/select')
            # Category_field.send_keys(line[7])
            

            element=driver.find_elements(By.NAME, ('CATEGORY_ID'))
            print('ok')
            drp=Select(element[0])
            drp.select_by_visible_text("|   |___Web Design & Development")
            time.sleep(4)

            # agree = driver.find_elements(By.NAME, 'AGREERULES')
            # agree[0].click()
            # time.sleep(10)

            submit = driver.find_elements(By.XPATH, '//*[@id="content"]/table/tbody/tr/td/form/table[2]/tbody/tr/td/table/tbody/tr[8]/td[2]/input')
            submit[0].click()

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

with open('data.csv', 'r') as csv_file:

    csv_reader = csv.reader(csv_file)

#-------------------------------------------------------------------------------
# Web Automation

    for line in csv_reader:

        driver = webdriver.Chrome()
        driver.get('https://www.canadawebdir.com/submit.php')
        driver.maximize_window()
        time.sleep(5)

        freelink = driver.find_element("xpath", '//*[@id="option3"]')
        freelink.click()
        time.sleep(5)

        username_field = driver.find_element("xpath", '//*[@id="ownername"]')
        username_field.send_keys(line[0])
        time.sleep(3)

        Email_field = driver.find_element("xpath", '//*[@id="owneremail"]')
        Email_field.send_keys(line[1])
        time.sleep(3)

        URL_field = driver.find_element("xpath", '//*[@id="url"]')
        URL_field.send_keys(line[2])
        time.sleep(3)

        Title_field = driver.find_element("xpath", '//*[@id="title"]')
        Title_field.send_keys(line[3])
        time.sleep(3)

        Description_field = driver.find_element("xpath", '//*[@id="description"]')
        Description_field.send_keys(line[4])
        time.sleep(3)

        # Category_field = driver.find_element("xpath", '//*[@id="container"]/table/tbody/tr/td/form/table[2]/tbody/tr/td/table/tbody/tr[6]/td[2]/select')
        # Category_field.send_keys(line[7])
        

        element=driver.find_elements(By.NAME, ('CATEGORY_ID'))
        print('ok')
        drp=Select(element[0])
        drp.select_by_visible_text("|   |   |___Internet and Web Skills")
        time.sleep(4)

        agree = driver.find_elements(By.NAME, 'AGREERULES')
        agree[0].click()
        time.sleep(10)

        submit = driver.find_elements(By.XPATH, '//*[@id="send"]')
        submit[0].click()



#-------------------------------------------------------------------------------

with open('data.csv', 'r') as csv_file:

    csv_reader = csv.reader(csv_file)

    for line in csv_reader:

        driver = webdriver.Chrome()
        driver.get('http://www.1abc.org/submit.php')
        driver.maximize_window()
        time.sleep(5)

        freelink = driver.find_element("xpath", '//*[@id="container"]/table/tbody/tr/td/form/table[1]/tbody/tr/td/table/tbody/tr[4]/td[1]/input')
        freelink.click()
        time.sleep(5)

        username_field = driver.find_element("xpath", '//*[@id="container"]/table/tbody/tr/td/form/table[2]/tbody/tr/td/table/tbody/tr[4]/td[2]/input')
        username_field.send_keys(line[0])
        time.sleep(3)

        Email_field = driver.find_element("xpath", '//*[@id="container"]/table/tbody/tr/td/form/table[2]/tbody/tr/td/table/tbody/tr[5]/td[2]/input ')
        Email_field.send_keys(line[1])
        time.sleep(3)

        URL_field = driver.find_element("xpath", '//*[@id="container"]/table/tbody/tr/td/form/table[2]/tbody/tr/td/table/tbody/tr[2]/td[2]/input')
        URL_field.send_keys(line[2])
        time.sleep(3)

        Title_field = driver.find_element("xpath", '//*[@id="container"]/table/tbody/tr/td/form/table[2]/tbody/tr/td/table/tbody/tr[1]/td[2]/input')
        Title_field.send_keys(line[3])
        time.sleep(3)

        Description_field = driver.find_element("xpath", '//*[@id="container"]/table/tbody/tr/td/form/table[2]/tbody/tr/td/table/tbody/tr[3]/td[2]/textarea')
        Description_field.send_keys(line[4])
        time.sleep(3)
  
        element=driver.find_elements(By.NAME, ('CATEGORY_ID'))
        print('ok')
        drp=Select(element[0])
        print('ok')

        drp.select_by_visible_text('|   |___Web Development')
        time.sleep(4)


        submit = driver.find_elements(By.XPATH, '/html/body/div/div/table/tbody/tr/td/form/table[2]/tbody/tr/td/table/tbody/tr[8]/td[2]/input')
        submit[0].click()

#---------------------------------------------------------------------------------------------------------------------------------------------


with open('data.csv', 'r') as csv_file:

    csv_reader = csv.reader(csv_file)

#-------------------------------------------------------------------------------
# Web Automation

    for line in csv_reader:

        driver = webdriver.Chrome()
        driver.get('http://www.abstractdirectory.com/submit.php')
        driver.maximize_window()
        time.sleep(5)

        freelink = driver.find_element("xpath", '/html/body/div/div[3]/div[2]/table/tbody/tr[1]/td/blockquote/table/tbody/tr[4]/td[1]/input')
        freelink.click()
        time.sleep(5)


        Title_field = driver.find_element("xpath", '/html/body/div/div[3]/div[2]/table/tbody/tr[2]/td[2]/input')
        Title_field.send_keys(line[3])
        time.sleep(3)

        URL_field = driver.find_element("xpath", '/html/body/div/div[3]/div[2]/table/tbody/tr[3]/td[2]/input')
        URL_field.send_keys(line[2])
        time.sleep(3)


        Description_field = driver.find_element("xpath", '/html/body/div/div[3]/div[2]/table/tbody/tr[4]/td[2]/textarea')
        Description_field.send_keys(line[4])
        time.sleep(3)

        username_field = driver.find_element("xpath", '/html/body/div/div[3]/div[2]/table/tbody/tr[5]/td[2]/input')
        username_field.send_keys(line[0])
        time.sleep(3)

        Email_field = driver.find_element("xpath", '/html/body/div/div[3]/div[2]/table/tbody/tr[6]/td[2]/input')
        Email_field.send_keys(line[1])
        time.sleep(3)

        element=driver.find_elements(By.NAME, ('CATEGORY_ID'))
        print('ok')
        drp=Select(element[0])
        drp.select_by_visible_text("|   |___Web Hosting")
        time.sleep(4)

        # agree = driver.find_elements(By.NAME, 'AGREERULES')
        # agree[0].click()
        # time.sleep(10)

        submit = driver.find_elements(By.XPATH, '/html/body/div/div[3]/div[2]/table/tbody/tr[9]/td[2]/input')
        submit[0].click()
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

with open('data.csv', 'r') as csv_file:

    csv_reader = csv.reader(csv_file)

#-------------------------------------------------------------------------------
# Web Automation

    for line in csv_reader:

        driver = webdriver.Chrome()
        driver.get('https://d-i-r.com/submit.php')
        driver.maximize_window()
        time.sleep(5)

        freelink = driver.find_element("xpath", '/html/body/div[5]/div[2]/div[2]/form/table/tbody/tr[1]/td/div/div[1]/table/tbody/tr[1]/td[1]/input')
        freelink.click()
        time.sleep(5)


        Title_field = driver.find_element("xpath", '//*[@id="TITLE"]')
        Title_field.send_keys(line[3])
        time.sleep(3)
    
        URL_field = driver.find_element("xpath", '//*[@id="URL"]')
        URL_field.send_keys(line[2])
        time.sleep(3)
        

        element=driver.find_elements(By.NAME, ('CATEGORY_ID'))
        print('ok')
        drp=Select(element[0])
        drp.select_by_visible_text("|   |___Web Hosting")
        time.sleep(4)


        Description_field = driver.find_element("xpath", '//*[@id="DESCRIPTION"]')
        Description_field.send_keys(line[4])
        time.sleep(3)

        
        username_field = driver.find_element("xpath", '//*[@id="OWNER_NAME"]')
        username_field.send_keys(line[0])
        time.sleep(3)

        Email_field = driver.find_element("xpath", '//*[@id="OWNER_EMAIL"]')
        Email_field.send_keys(line[1])
        time.sleep(3)

        agree = driver.find_elements(By.NAME, 'AGREERULES')
        agree[0].click()
        time.sleep(10)

        submit = driver.find_elements(By.XPATH, '/html/body/div[5]/div[2]/div[2]/form/table/tbody/tr[12]/td/input')
        submit[0].click()
#------------------------------------------------------------------------------------------------------------------------------------

with open('data.csv', 'r') as csv_file:

    csv_reader = csv.reader(csv_file)

#-------------------------------------------------------------------------------
# Web Automation

    for line in csv_reader:

        driver = webdriver.Chrome()
        driver.get('https://www.qualityinternetdirectory.com/submit.php')
        driver.maximize_window()
        #time.sleep(5)

        freelink = driver.find_element("xpath", '/html/body/div[6]/div[2]/div/form/table/tbody/tr[1]/td/table/tbody/tr[2]/td[1]/input')
        freelink.click()
        time.sleep(5)

        Title_field = driver.find_element("xpath", '/html/body/div[6]/div[2]/div/form/table/tbody/tr[3]/td[2]/input')
        Title_field.send_keys(line[3])
        time.sleep(3)

        URL_field = driver.find_element("xpath", '/html/body/div[6]/div[2]/div/form/table/tbody/tr[4]/td[2]/input')
        URL_field.send_keys(line[2])
        time.sleep(3)


        Description_field = driver.find_element("xpath", '/html/body/div[6]/div[2]/div/form/table/tbody/tr[5]/td[2]/textarea')
        Description_field.send_keys(line[4])
        time.sleep(3)

        username_field = driver.find_element("xpath", '/html/body/div[6]/div[2]/div/form/table/tbody/tr[8]/td[2]/input')
        username_field.send_keys(line[0])
        time.sleep(3)

        Email_field = driver.find_element("xpath", '/html/body/div[6]/div[2]/div/form/table/tbody/tr[9]/td[2]/input')
        Email_field.send_keys(line[1])
        time.sleep(3)



        # Category_field = driver.find_element("xpath", '//*[@id="container"]/table/tbody/tr/td/form/table[2]/tbody/tr/td/table/tbody/tr[6]/td[2]/select')
        # Category_field.send_keys(line[7])
        

        element=driver.find_elements(By.NAME, ('CATEGORY_ID'))
        print('ok')
        drp=Select(element[0])
        drp.select_by_visible_text("|   |   |___Internet and Web Skills")
        time.sleep(4)

        agree = driver.find_elements(By.NAME, 'AGREERULES')
        agree[0].click()
        time.sleep(10)

        submit = driver.find_elements(By.XPATH, '/html/body/div[6]/div[2]/div/form/table/tbody/tr[13]/td/input')
        submit[0].click()



#-----------------------------------------------------------------------------------------------------------------------------------------------


with open('data.csv', 'r') as csv_file:

    csv_reader = csv.reader(csv_file)

#-------------------------------------------------------------------------------
# Web Automation

    for line in csv_reader:

        driver = webdriver.Chrome()
        driver.get('https://www.usalistingdirectory.com/submit.php')
        driver.maximize_window()
        time.sleep(5)

        regular_links = driver.find_element("xpath", '/html/body/div[6]/div[2]/div[2]/form/table/tbody/tr[1]/td/table/tbody/tr[2]/td[1]/input')
        regular_links.click()
        time.sleep(5)

        Title_field = driver.find_element("xpath", '/html/body/div[6]/div[2]/div[2]/form/table/tbody/tr[3]/td[2]/input')
        Title_field.send_keys(line[3])
        time.sleep(3)

        URL_field = driver.find_element("xpath", '/html/body/div[6]/div[2]/div[2]/form/table/tbody/tr[4]/td[2]/input')
        URL_field.send_keys(line[2])
        time.sleep(3)

        Description_field = driver.find_element("xpath", '/html/body/div[6]/div[2]/div[2]/form/table/tbody/tr[5]/td[2]/textarea')
        Description_field.send_keys(line[4])
        time.sleep(3)

        username_field = driver.find_element("xpath",'/html/body/div[6]/div[2]/div[2]/form/table/tbody/tr[8]/td[2]/input')
        username_field.send_keys(line[0])
        time.sleep(3)

        Email_field = driver.find_element("xpath", '/html/body/div[6]/div[2]/div[2]/form/table/tbody/tr[9]/td[2]/input')
        Email_field.send_keys(line[1])
        time.sleep(3)

  

        # Category_field = driver.find_element("xpath", '//*[@id="container"]/table/tbody/tr/td/form/table[2]/tbody/tr/td/table/tbody/tr[6]/td[2]/select')
        # Category_field.send_keys(line[7])
        

        element=driver.find_elements(By.NAME, ('CATEGORY_ID'))
        print('ok')
        drp=Select(element[0])
        drp.select_by_visible_text("|   |   |___Internet and Web Skills")
        time.sleep(4)

        agree = driver.find_elements(By.NAME, 'AGREERULES')
        agree[0].click()
        time.sleep(10)

        submit = driver.find_elements(By.XPATH, '/html/body/div[6]/div[2]/div[2]/form/table/tbody/tr[13]/td/input')
        submit[0].click()



#-------------------------------------------------------------------------------
    