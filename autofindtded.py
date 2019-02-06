from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as req



url =  'http://www.ball-lock.com/detail.php?id=1101202'

webopen = req(url)
page_html = webopen.read()
webopen.close()

page_soup = soup(page_html,'html.parser')
#print(page_soup.title)
    

#--------------------  1 t-ded --------------------------------
data = page_soup.find(class_ = 'detail')
data_ref = page_soup.find('span',{'style':'font-size:13px;color:#000000;font-weight:bold;'})
T_ded = data.text
T_dedref = data_ref.text
T_dedref001 = (T_dedref[6:27])
print("posted by (shewshew): {}TIME:{} ".format(T_ded,T_dedref001))

#---------------------------------------------------------------





















    

    
    
    



