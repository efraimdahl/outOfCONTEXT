import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions
from textblob import TextBlob

#Scrapes comments from URL
#runs analysis on Toxicity from the given comments
#returns an aggregate Toxicity measure
def analyse(url):
    data=[]
    textdata = []
    with Chrome(executable_path="./chromedriver.exe") as driver:
        wait = WebDriverWait(driver,15)
        driver.get(url)

        driver.maximize_window()
        time.sleep(5)

        try:
         # Extract the elements storing the video title and
         # comment section.
         title = driver.find_element_by_xpath('//*[@id="container"]/h1/yt-formatted-string').text
         comment_section = driver.find_element_by_xpath('//*[@id="comments"]')

        except exceptions.NoSuchElementException:
            # Note: Youtube may have changed their HTML layouts for
            # videos, so raise an error for sanity sake in case the
            # elements provided cannot be found anymore.
            print("this is error")
            error = "Error: Double check selector OR "
            error += "element may not yet be on the screen at the time of the find operation"
            print(error)

        # Scroll into view the comment section, then allow some time
        # for everything to be loaded as necessary.
        driver.execute_script("arguments[0].scrollIntoView();", comment_section)
        time.sleep(7)

        # Scroll all the way down to the bottom in order to get all the

        # elements loaded (since Youtube dynamically loads them).
        last_height = driver.execute_script("return document.documentElement.scrollHeight")
        count = 0
        while count<=5:
            # Scroll down 'til "next load".
            driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
            # Wait to load everything thus far.
            time.sleep(2)
            # Calculate new scroll height and compare with last scroll height.
            new_height = driver.execute_script("return document.documentElement.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

            # One last scroll just in case.
            driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
            count+=1
        try:
            comment_elems = driver.find_elements_by_xpath('//*[@id="content-text"]')
        except exceptions.NoSuchElementException:
            error = "Error: Double check selector OR "
            error += "element may not yet be on the screen at the time of the find operation"
            print(error)
        for comment in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#content"))):
            textdata.append(comment.text)


    for comment in textdata:
        #print(comment)
        analysis = TextBlob(comment)
        #print(analysis.sentiment)
        #print(analysis.sentiment.polarity)
        data.append(analysis.sentiment.polarity)
    print("recorded polarity", sum(data)/len(data))
    return sum(data)/len(data)

#print(analyse("https://www.youtube.com/watch?v=xj363_Udjio"))






    