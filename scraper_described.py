#main config
from selenium import webdriver

#variables to maximum page quantity & for digit size (so.. 2 equals a two digit page number. example: 01, 02, 03 ....)
MAX_PAGE_NUM = 27
MAX_PAGE_DIG = 2

#calling on Firefox
driver = webdriver.Firefox()

#creating a csv and making columns in it
with open('results.csv', 'w') as f:
    f.write("Title, Excerpt, \n")

#generating page numbering
for i in range(1, MAX_PAGE_NUM + 1):
    page_num = (MAX_PAGE_DIG - len(str(i))) * "0" + str(i)
    
    # URL for the data source
    url = "https://pmnv.herokuapp.com/" + page_num
    
    #pointing Firefox to the URL
    driver.get(url)

    #selecting items on the page (title is located in a h1 element and exerpt is in a div)
    title = driver.find_elements_by_xpath('//h1[@class="title gradient-effect"]')
    excerpt = driver.find_elements_by_xpath('//div[@class="post-excerpt"]')

    # Look at the page, collect and writ to a csv file:
    num_page_items = len(title)
    with open('results.csv', 'a') as f:
        for i in range(num_page_items):
            f.write(title[i].text + "," + excerpt[i].text + "\n")

#clean-up // close browser after completion 
driver.close()