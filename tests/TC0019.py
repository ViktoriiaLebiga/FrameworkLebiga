from waiting import wait
empty = ' '
invalid_email = '1238mmj'
empty_message = 'The "E-mail" field is required.'
invalid_message = 'The "E-mail" field must contain a valid email address.'

def test_fifth(driver):
   driver.get("https://www.vpnunlimitedapp.com/en")
   email_fild = driver.find_element_by_xpath("//div[@class='footer_input_wrap']/input[@class='footer_input_form']")

   email_fild.send_keys(empty)
   btn = driver.find_element_by_xpath("//div[@class='footer_input_wrap']/label[@class='footer_input_btn_label']")
   btn.click()
   message = driver.find_element_by_xpath("//p[@class='form-error']").text
   wait(driver)

   assert message == empty_message
   print('User cannot receive email. Show valid error message')

def test_fifth2(driver):
   driver.get("https://www.vpnunlimitedapp.com/en")
   email_fild = driver.find_element_by_xpath("//div[@class='footer_input_wrap']/input[@class='footer_input_form']")
   email_fild.send_keys(invalid_email)
   btn2 = driver.find_element_by_xpath("//div[@class='footer_input_wrap']/label[@class='footer_input_btn_label']")
   btn2.click()
   message2 = driver.find_element_by_xpath("//p[@class='form-error']").text
   wait(driver)

   assert message2 == invalid_message
   print('User cannot receive email. Show valid error message')
