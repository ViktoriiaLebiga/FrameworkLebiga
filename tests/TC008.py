def test_third(driver):
   driver.get("https://www.vpnunlimitedapp.com/en")
   box = driver.find_elements_by_xpath("//div[@class='xl-4 md-12 sm-12 our_benefits_box']")

   assert len(box) == 6
   print('Six blocks with benefits are present')