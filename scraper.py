from selenium import webdriver

MAX_PAGE_NUM = 5
MAX_PAGE_DIG = 3
driver = webdriver.Firefox()

with open('results.csv', 'w') as f:
    f.write("Title, Excerpt \n")

for i in range(1, MAX_PAGE_NUM + 1):
    page_num = (MAX_PAGE_DIG - len(str(i))) * "0" + str(i)
    url = "https://pmnv.herokuapp.com/" + page_num + ".html"

    driver.get(url)

    title = driver.find_elements_by_xpath('//div[@title="post-title"]')
    excerpt = driver.find_elements_by_xpath('//span[@class="text-preview"]')

    num_page_items = len(title)
    with open('results.csv', 'a') as f:
        for i in range(num_page_items):
            f.write(title[i].text + "," + excerpt[i].text + "\n")

driver.close()
