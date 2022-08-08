from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

if __name__ == '__main__':
   path = 'C:\Program Files (x86)\chromedriver.exe'
   driver = webdriver.Chrome(path)
   driver.get('http://www.pbclibrary.org/raton/mousercise.htm')


   try:
      #nivel0
      link_locator = (By.XPATH, "//input[@type='submit']")
      link = WebDriverWait(driver, 10).until(EC.presence_of_element_located(link_locator))
      link.click()


      #niveles del 1 al 16
      for i in range (2, 17):
         x_path = "//a[@href='m2.htm']"
         path = x_path.replace('2', str(i))
         link_locator = (By.XPATH, path)
         link = WebDriverWait(driver, 10).until(EC.presence_of_element_located(link_locator))
         link.click()

      #niveles del 17 al 20
      for i in range(17, 21):
         x_path = "//form[@action='m17.htm']"
         path = x_path.replace('17', str(i))
         link_locator = (By.XPATH, path)
         link = WebDriverWait(driver, 10).until(EC.presence_of_element_located(link_locator))
         link.click()

      # niveles del 21 al 22
      for i in range(21, 23):
         x_path = "//a[@href='m2.htm']"
         path = x_path.replace('2', str(i))
         link_locator = (By.XPATH, path)
         link = WebDriverWait(driver, 10).until(EC.presence_of_element_located(link_locator))
         link.click()

      #nivel 23
      for i in range (1, 12):
         name = 'b0'
         name = name.replace('0', str(i))
         link_locator = (By.NAME, name)
         link = WebDriverWait(driver, 10).until(EC.presence_of_element_located(link_locator))
         link.click()

      name = 'advance'
      link_locator = (By.NAME, name)
      link = WebDriverWait(driver, 10).until(EC.presence_of_element_located(link_locator))
      link.click()

      #nivel 24
      for i in range(4, 8):
         x_path = "//img[@src='images/but4.gif']"
         x_path = x_path.replace('4', str(i))
         link_locator = (By.XPATH, x_path)
         link = WebDriverWait(driver, 10).until(EC.presence_of_element_located(link_locator))
         link.click()

      link_locator = (By.XPATH, "//input[@type='button']")
      links = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(link_locator))
      for link in links:
         link.click()

      x_path = "//img[@src='images/continue.gif']"
      link_locator = (By.XPATH, x_path)
      link = WebDriverWait(driver, 10).until(EC.presence_of_element_located(link_locator))
      link.click()

      #nivel25
      x_path = "//img[@src='images/firecracker.gif']"
      link_locator = (By.XPATH, x_path)
      links = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(link_locator))
      action = ActionChains(driver)
      for link in links:
         action.double_click(link).perform()

      x_path = "//img[@src='images/continue.gif']"
      link_locator = (By.XPATH, x_path)
      link = WebDriverWait(driver, 10).until(EC.presence_of_element_located(link_locator))
      link.click()

      #nivel26 al 31
      for i in range(26, 32):
         x_path = "//a[@href='m2.htm']"
         path = x_path.replace('2', str(i))
         link_locator = (By.XPATH, path)
         link = WebDriverWait(driver, 10).until(EC.presence_of_element_located(link_locator))
         link.click()

      #nivel32
      x_path = "//a[@href='javascript:doAlert()']"
      link_locator = (By.XPATH, x_path)
      link = WebDriverWait(driver, 10).until(EC.presence_of_element_located(link_locator))
      link.click()
      #switch to alert
      alert = Alert(driver)
      alert.accept()

      #nivel33
      x_path = "//a[@href='m33.htm']"
      link_locator = (By.XPATH, x_path)
      link = WebDriverWait(driver, 10).until(EC.presence_of_element_located(link_locator))
      link.click()

      #nivel34
      name = "sample"
      link_locator = (By.NAME, name)
      links = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(link_locator))
      for link in links:
         link.click()
      #continue button
      x_path = "//img[@src='images/continue.gif']"
      link_locator = (By.XPATH, x_path)
      link = WebDriverWait(driver, 10).until(EC.presence_of_element_located(link_locator))
      link.click()

      #nivel 35
      name = "sample"
      link_locator = (By.NAME, name)
      links = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(link_locator))
      for link in links:
         link.click()
      #continuar
      link_locator = (By.XPATH, "//input[@type='submit']")
      link = WebDriverWait(driver, 10).until(EC.presence_of_element_located(link_locator))
      link.click()

      # nivel 36
      name = "sample"
      link_locator = (By.NAME, name)
      links = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(link_locator))
      for link in links:
         link.click()
      # continue button
      x_path = "//img[@src='images/continue.gif']"
      link_locator = (By.XPATH, x_path)
      link = WebDriverWait(driver, 10).until(EC.presence_of_element_located(link_locator))
      link.click()

      #nivel37
      name = "sample"
      link_locator = (By.NAME, name)
      link = WebDriverWait(driver, 10).until(EC.presence_of_element_located(link_locator))
      link.click()
      # continuar
      link_locator = (By.XPATH, "//input[@type='submit']")
      link = WebDriverWait(driver, 10).until(EC.presence_of_element_located(link_locator))
      link.click()

      #nivel38
      name = 'theChoices'
      link_locator = (By.NAME, name)
      select = Select(WebDriverWait(driver, 10).until(EC.presence_of_element_located(link_locator)))
      select.select_by_visible_text('Cinco')
      # continue button
      x_path = "//img[@src='images/continue.gif']"
      link_locator = (By.XPATH, x_path)
      link = WebDriverWait(driver, 10).until(EC.presence_of_element_located(link_locator))
      link.click()

      # nivel39
      x_path = "//select"
      link_locator = (By.XPATH, x_path)
      select = Select(WebDriverWait(driver, 10).until(EC.presence_of_element_located(link_locator)))
      select.select_by_visible_text('Bote')
      # continuar
      link_locator = (By.XPATH, "//input[@type='submit']")
      link = WebDriverWait(driver, 10).until(EC.presence_of_element_located(link_locator))
      link.click()

      #nivel40
      name = 'theChoices'
      link_locator = (By.NAME, name)
      select = Select(WebDriverWait(driver, 10).until(EC.presence_of_element_located(link_locator)))
      select.select_by_visible_text('Seis')
      # continue button
      x_path = "//img[@src='images/continue.gif']"
      link_locator = (By.XPATH, x_path)
      link = WebDriverWait(driver, 10).until(EC.presence_of_element_located(link_locator))
      link.click()

      # nivel41
      x_path = "//select[@size='3']"
      link_locator = (By.XPATH, x_path)
      select = Select(WebDriverWait(driver, 10).until(EC.presence_of_element_located(link_locator)))
      select.select_by_visible_text('Deep Dish')
      # continuar
      link_locator = (By.XPATH, "//input[@type='submit']")
      link = WebDriverWait(driver, 10).until(EC.presence_of_element_located(link_locator))
      link.click()

      #nivel41(?)
      name = 'fname'
      link_locator = (By.NAME, name)
      link = WebDriverWait(driver, 10).until(EC.presence_of_element_located(link_locator))
      link.send_keys('Pedro')

      name = 'lname'
      link_locator = (By.NAME, name)
      link = WebDriverWait(driver, 10).until(EC.presence_of_element_located(link_locator))
      link.send_keys('Guerrero')

      # continuar
      link_locator = (By.XPATH, "//input[@type='submit']")
      link = WebDriverWait(driver, 10).until(EC.presence_of_element_located(link_locator))
      link.click()

   except:
      driver.quit()






