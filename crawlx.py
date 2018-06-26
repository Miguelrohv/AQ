from selenium import webdriver
from selenium.webdriver.firefox.options import Options

print("crawlx initiated...")
options = Options()
options.add_argument("--headless")
driver = webdriver.Firefox(firefox_options=options)
print("Headless Firefox initiated...")
#driver.set_window_size(1120, 550)
driver.get("http://www.olx.ph/computers?q=gtx+970&locationName=")
#driver.find_element_by_xpath("""/html/body/div[1]/div/div[2]/div[1]/div/div[2]/div[4]/div/div[1]/div[2]/a""").click()
posts = driver.find_elements_by_class_name("title")
print("site loaded...raw posts:",len(posts))
cnt = 0
for post in posts:
    if "970" in post.text:
        if "970m" not in post.text:
            print(post.text)
            cnt+=1
        else:
            pass
    else:
        pass
print("useful post:",cnt)
