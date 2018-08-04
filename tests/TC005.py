def test_first(driver):
   driver.get("https://www.vpnunlimitedapp.com/en")
   vpn_buisiness = driver.find_element_by_xpath("//a[@class='vpn_for_business']")
   vpn_buisiness.click()

   driver.find_elements_by_xpath("//head[title='Business VPN by KeepSolid']")
   print ('The new tab opens the Business VPN website')