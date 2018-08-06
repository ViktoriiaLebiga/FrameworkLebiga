from waiting import wait
from allure.constants import AttachmentType
import allure

empty = ' '
invalid_email = '1238mmj'
empty_message = 'The "E-mail" field is required.'
invalid_message = 'The "E-mail" field must contain a valid email address.'

def test_empty_fild_message(driver):
   driver.get("https://www.vpnunlimitedapp.com/en")
   email_fild = driver.find_element_by_xpath("//div[@class='footer_input_wrap']/input[@class='footer_input_form']")

   email_fild.send_keys(empty)
   btn = driver.find_element_by_xpath("//div[@class='footer_input_wrap']/label[@class='footer_input_btn_label']")
   btn.click()
   message = driver.find_element_by_xpath("//p[@class='form-error']").text
   wait(driver)

   assert message == empty_message
   with allure.MASTER_HELPER.step('Error'):
      allure.MASTER_HELPER.attach('screen_shot', driver.get_screenshot_as_png(), type=AttachmentType.PNG)

   print('User cannot receive email. Show valid error message')

def test_inv_email_fild_message(driver):
   driver.get("https://www.vpnunlimitedapp.com/en")
   email_fild = driver.find_element_by_xpath("//div[@class='footer_input_wrap']/input[@class='footer_input_form']")
   email_fild.send_keys(invalid_email)
   btn2 = driver.find_element_by_xpath("//div[@class='footer_input_wrap']/label[@class='footer_input_btn_label']")
   btn2.click()
   message2 = driver.find_element_by_xpath("//p[@class='form-error']").text
   wait(driver)

   assert message2 == invalid_message, "User cannot receive email. Show valid error message"
   #print('User cannot receive email. Show valid error message')
