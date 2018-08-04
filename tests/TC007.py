def test_second(driver):
   driver.get("https://www.vpnunlimitedapp.com/en")
   video_btn = driver.find_element_by_xpath("//div[@class='videoSection']/descendant::div[@class='pulse2']")

   video_btn.click()
   driver.find_element_by_xpath("//div[@class='videoWrapper']/video[@loop='loop']")

   print('Video opened on over the page')