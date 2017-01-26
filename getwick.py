import urllib2
from bs4 import BeautifulSoup
import os
import csv
import time, datetime


def crawl(url):
    try:
        pageContent = ''
        asset_data={}
        dis1 = {}
        #countrow = 0
    
        soup = BeautifulSoup(urllib2.urlopen(url))
        Lastupdate = soup.find('small',{'class': "last-update"}).text
        Lastupdate =str( Lastupdate.split('Last update:')[-1]).strip()
        LastupdateTime = Lastupdate
        Lastupdate = Lastupdate+" 2016"
        daa = datetime.datetime.strptime(Lastupdate, '%a %d %b %H:%M %Y')
        Lastupdate= daa.strftime('%A %d:%m:%Y')
#        print ("*******************")
        #if not os.path.isdir('Gatwick_arrival'):
           # os.makedirs('Gatwick_arrival')
        filename = os.getcwd()+'/Gatwick_arrival/Gatwick_arrival.csv'
#        filename = r'D:\gatwik\Gatwick\Gatwick_arrival\Gatwick_arrival.csv'
        outputFile = open(filename, 'wb')
        outputWriter = csv.writer(outputFile, quoting=csv.QUOTE_ALL)
        dis ={}
        dis['company'] = ''
        dis['logo'] = ''
        dis['status'] = ''
       # newRow = ('AirLines', 'logo', 'schedule', 'from','flight','status','terminal')
       # outputWriter.writerow(newRow)
        for tables in soup.find_all("table"):
            newRow1 = ('AirLines', 'logo', 'schedule', 'from','flight','status','terminal', 'gate', 'lastUpdate','lastUpdateTime')
            outputWriter.writerow(newRow1)
            for row in tables.find_all("tr"):
                count =0
                for cell in row.find_all("td"):    
                    count = count + 1
#                    print count
                    if count ==1:
#                        print cell.get('data-airline-name')
                        dis['company']= cell.get('data-airline-name')
                        dis['logo'] = 'http://www.gatwickairport.com'+ str(cell.get('data-airline-image'))
                        dis['status'] = ''
                    if cell.get_text().strip() != '' and count ==2:
                        dis['schedule'] = cell.get_text().strip()
                    if cell.get_text().strip() != '' and count == 3:
                        dis['from'] = cell.get_text().strip()
                    if cell.get_text().strip() != '' and count == 4:
                        dis['flight'] = cell.get_text().strip()
                    if cell.get_text().strip() != '' and count == 5:
                        dis['status'] = cell.get_text().strip()
                    if cell.get_text().strip() != '' and count == 6:
                        dis['terminal'] = cell.get_text().strip()
                        dis['gate'] = ' '
                        dis['lastUpdate'] = Lastupdate.strip()
                        dis['lastUpdateTime']= LastupdateTime
                        newRow = (dis['company'],dis['logo'],dis['schedule'],dis['from'],dis['flight'],dis['status'],dis['terminal'],dis['gate'],dis['lastUpdate'], dis['lastUpdateTime'])
                        outputWriter.writerow(newRow)

#                        asset_data = json.dumps(dis)
                    #asset_data = json.dumps(dis)
                    #dis1.update(dis)
                    #     print cell.get_text().strip()
                    #
     #       countrow=+1
        outputFile.close()
    except Exception as ex:
        print 'Exception: '+str(ex)
        outputFile.close()
        pass
            
#    print asset_data

#crawl('http://www.gatwickairport.com/flights/?type=arrivals')
while True:
    crawl('http://www.gatwickairport.com/flights/?type=arrivals')
    print 'Data dumped at ', datetime.datetime.now()
    time.sleep(900)
    


    
