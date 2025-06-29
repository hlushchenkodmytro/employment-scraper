from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By

class ChildPageNavigator:
    def __init__(self, driver, count):
        self.driver1 = driver
        self.count = count
        self.vacancy_cards = self.collect_vacancy_pages()

    def collect_vacancy_pages(self):
        # Get all vacancy cards on the page
        return self.driver1.find_elements(By.CSS_SELECTOR, "span.job-ad-display-1cat3iu li")

    def extract_requirements(self):
        self.requremnts_lists = []
        requremnts_text = ""
        for card in self.vacancy_cards:
            requremnts_text += card.text + " "
            print(card.text)  # Print basic info from the card

        self.requremnts_lists.append(requremnts_text)
        self.count += 1
        print(f"""
        Parsed requirement block number: {self.count}
        """)
        return self.count