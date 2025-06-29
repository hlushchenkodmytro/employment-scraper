import time
import employment.constants as const

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from employment.exel_writing import writer
from employment.open_job_detail import ChildPageNavigator

class Employment(webdriver.Chrome):
    def __init__(self, teardown=False):
        self.teardown = teardown
        super(Employment, self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()
        self.vacancies = {"Job Title": [], "Requirements": []}  # Store job data

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)

    def cookie_skip(self):
        time.sleep(1)
        selection_element = self.find_element(By.ID, "ccmgt_explicit_accept")
        selection_element.click()

    def extract_vacancy_titles(self):
        job_title = []
        main_elements = self.find_elements(By.CSS_SELECTOR, 'a.res-1cv93ld')
        for element in main_elements:
            job_title.append(element)
        self.vacancies["Job Title"].extend(job_title)

    def report_requirements_all_pages(self, counter=None):
        self.count = 0
        if counter is None:
            counter = len(self.find_elements(By.CSS_SELECTOR, "li.res-1fosy9w a"))

        for page_index in range(counter):
            if page_index != 0:
                # Refresh page links before clicking
                page_links = self.find_elements(By.CSS_SELECTOR, "li.res-1fosy9w a")
                page_links[page_index].click()
                time.sleep(2)

            print(f"Page {page_index + 1} loaded")

            self.report_requirements()

    def report_requirements(self):
        child_pages_boxes = self.find_elements(By.CSS_SELECTOR, "a.res-1cv93ld")
        if not child_pages_boxes:
            child_pages_boxes = self.find_elements(By.CSS_SELECTOR, "a.res-1fudl87")

        for i in range(len(child_pages_boxes)):
            # child_pages_boxes = self.find_elements(By.CSS_SELECTOR, "a.res-1cv93ld")
            job_title = [child_pages_boxes[i].text]
            # Open job detail in a new tab
            child_pages_boxes[i].click()
            tabs = self.window_handles
            self.switch_to.window(tabs[1])

            # Parse job requirements
            page_navigation = ChildPageNavigator(self, count=self.count)
            page_navigation.extract_requirements()
            self.count = page_navigation.extract_requirements()

            if not page_navigation.requremnts_lists:
                self.close()
                self.switch_to.window(tabs[0])
                continue

            self.vacancies["Requirements"].extend(page_navigation.requremnts_lists)
            self.vacancies["Job Title"].extend(job_title)

            # Close detail tab and return
            self.close()
            self.switch_to.window(tabs[0])

    def save_to_excel(self):
        writer(self.vacancies)
