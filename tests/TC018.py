from data import email

def test_fourth(driver):
   driver.get("https://www.vpnunlimitedapp.com/en")
   email_fild = driver.find_element_by_xpath("//div[@class='footer_input_wrap']/input[@class='footer_input_form']")

   email_fild.send_keys(email)

   btn = driver.find_element_by_xpath("//div[@class='footer_input_wrap']/label[@class='footer_input_btn_label']")
   btn.click()

   print('User successfully receives email with information')