

# StepStone Job Scraper

A simple Python script that scrapes developer job listings from [StepStone](https://www.stepstone.de/jobs/developer/in-trier?radius=100&searchOrigin=Resultlist_top-search) in the Trier area and saves the data (job titles and requirements) into an Excel file.

##   Installation

Make sure Python and pip are installed on your machine.

1. Install the required libraries:

```bash
pip install selenium
pip install openpyxl
```

2. Install [Google Chrome](https://www.google.com/chrome/) if you haven’t already.

3. Download the appropriate version of [ChromeDriver](https://sites.google.com/chromium.org/driver/) for your Chrome browser.

4. Place the `chromedriver.exe` file in the **same folder** as the Python script.

##  How to Use

1. Run the script:

```bash
python your_script_name.py
```

2. The script will:

   * Open the StepStone job listings page for developers in Trier.
   * Scrape:

     * **Job titles**
     * **Job requirements**
   * Save the extracted data into an Excel file.

## Notes

* Website structure may change. In particular, **CSS selectors** like:

```python
elements = driver.find_elements(By.CSS_SELECTOR, 'a.res-1cv93ld')
```

may stop working if the site's HTML layout is updated.

* If you encounter errors, inspect the page using your browser’s Developer Tools (F12), find the new selectors, and update the script accordingly.

## 📄 Output

The script will generate an Excel file containing a list of job titles and their corresponding requirements.

---


