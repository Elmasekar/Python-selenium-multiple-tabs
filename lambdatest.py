import os
import unittest
import sys
from selenium import webdriver

username = os.environ.get("LT_USERNAME")
access_key = os.environ.get("LT_ACCESS_KEY")


class FirstSampleTest(unittest.TestCase):

	# setUp runs before each test case
	def setUp(self):
		desired_caps = {
			'LT:Options': {
				"user": username,
				"accessKey": access_key,
				"build": "UnitTest-Selenium-Sample",
				"name": "UnitTest-Selenium-Test",
				"platformName": "Windows 11",
				"selenium_version": "4.0.0"
			},
			"browserName": "Chrome",
			"browserVersion": "latest",
		}

		self.driver = webdriver.Remote(
			command_executor="http://hub.lambdatest.com:80/wd/hub",
			desired_capabilities=desired_caps)


# tearDown runs after each test case

	def tearDown(self):
		self.driver.quit()

	def test_tabs():
		"""
		Create new tab, switch to it and switch back to old tab
		:return: None
		"""
		driver.get('https://www.lambdatest.com/')
		driver.maximize_window()
		driver.execute_script("window.open('about:blank','secondtab');")
		driver.switch_to.window("secondtab")
		driver.get('https://www.lambdatest.com/')
		driver.switch_to.window(1)
		assert success == True
	
if __name__ == "__main__":

	#run testcases
	unittest.main()
