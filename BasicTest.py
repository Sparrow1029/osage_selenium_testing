import time
import unittest
import requests

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC


class LandingPageTest(unittest.TestCase):

    opts = Options()
    opts.headless = True
    BASE_URL = "https://osagepartners.com"

    def setUp(self):
        # create a new Firefox session
        self.driver = webdriver.Firefox(options=self.opts)
        self.driver.maximize_window()

        # Check that site is reachable
        r = requests.get(self.BASE_URL)
        assert r.status_code == 200
        print(f"{r.status_code} OK: Site is reachable")

        # navigate to landing page
        self.get_page_with_timeout()

    def test_homepage_links(self):
        driver = self.driver
        self.assertTrue(
            EC.presence_of_element_located((By.CLASS_NAME, "panel")))
        links = driver.find_elements_by_class_name("panel")
        self.assertIsNotNone(links)
        prevUrl = driver.current_url
        links[0].click()
        self.assertNotEqual(self.driver.current_url, prevUrl)
        driver.back()
        try:
            back_success = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "panel")))
        except TimeoutException:
            self.fail(msg="Back button didn't work.")

        links = driver.find_elements_by_class_name("panel")
        self.assertIsNotNone(links)
        prevUrl = driver.current_url
        links[1].click()
        self.assertNotEqual(self.driver.current_url, prevUrl)

    def test_university_partners_homepage(self):
        driver = self.driver
        link = driver.find_element_by_class_name("right")
        assert link is not None
        link.click()
        self.assertEqual(driver.current_url, "https://oup.vc/")

        search = driver.find_element_by_id("s")
        assert search is not None

        search.send_keys("investors")
        print(search.text)
        search.submit()
        # search.send_keys(Keys.RETURN)
        try:
            search_success = WebDriverWait(driver, 5).until(
                EC.title_contains("You searched for"))
        except TimeoutException:
            self.fail(msg="Search failed.")
        # time.sleep(3)

        assert driver.current_url == "https://oup.vc/?s=investors"
        # self.assertEquals(driver.current_url, "https://oup.vc/?s=investors")

    def tearDown(self):
        # Close the browser window
        self.driver.quit()

    def get_page_with_timeout(self, url=BASE_URL):
        """
        Helper function to force connection without 'pending' wait
        :param url: Url to request
        """
        driver = self.driver
        driver.set_page_load_timeout(10)

        t = time.time()

        try:
            driver.get(self.BASE_URL)
        except TimeoutException:
            driver.execute_script("window.stop();")
        print("Request time taken:", time.time() - t)


if __name__ == '__main__':
    unittest.main(verbosity=2)
