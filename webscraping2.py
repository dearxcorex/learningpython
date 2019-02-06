from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as req




url = 'https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168'


webopen = req(url)
page_html = webopen.read()
webopen.close()


page_soup = soup(page_html,'html.parser')
#print(page_soup.title.text)
belle = page_soup.find(id="seven-day-forecast")  #find html  top tag
belle_dearx =  belle.findAll(class_='tombstone-container')
tonight = belle_dearx[1]


period = tonight.find(class_="period-name").get_text()
short_desc = tonight.find(class_="short-desc").get_text()
temp = tonight.find(class_="temp").get_text()


print(period)
print(short_desc)
print(temp)


img = tonight.find('img')
desc = img('title')
print(desc)

period_tags = seven_day.select(".tombstone-container .period-name")
periods = [pt.get_text() for pt in period_tags]
print(periods)
