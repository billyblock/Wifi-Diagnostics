import os 
import speedtest
import re
import csv

def pingTest():
    # google
    ip = '8.8.8.8'

    response = os.popen('ping ' + ip).read()
    
    # Extract relevant lines directly
    lost = response.split("Lost =")[1].split(" (")[0].strip()
    max_ping = response.split("Maximum =")[1].split("ms")[0].strip()
    avg_ping = response.split("Average =")[1].split("ms")[0].strip()
    
    test = [lost, max_ping, avg_ping]
    return test

def speedTest():
    try:
        speedTest = speedtest.Speedtest()

        download = speedTest.download() / 1048576
        upload = speedTest.upload() / 1048576
        test = [round(download,2), round(upload,2)]
        return test
        
    except speedtest.SpeedtestException as e:
        print("An error occurred during speed test:", str(e))
    
def getAccessPointBSSID():
    response = os.popen('netsh wlan show networks mode=bssid').read()
    bssid = re.search(r'BSSID 1\s*:\s*([0-9a-fA-F:]+)', response).group(1)
    return bssid

def writeToCSV(index, pingTest, speedTest, previousBSSID, currentBSSID, bssidChanged):
    with open('data/info' + str(index) + '.csv', mode='w') as csvfile:
        fieldnames = ['packetsLost',
            'maximumPing', 
            'averagePing', 
            'downloadSpeed', 
            'uploadSpeed',
            'previousBSSID',
            'currentBSSID',
            'bssidChanged']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({'packetsLost': pingTest[0],'maximumPing': pingTest[1], 'averagePing': pingTest[2],
                         'downloadSpeed': speedTest[0], 'uploadSpeed': speedTest[1],
                         'previousBSSID': previousBSSID,'currentBSSID': currentBSSID, 'bssidChanged': bssidChanged})

def main():
    while True:
        for i in range(10):
                currentBSSID = getAccessPointBSSID()
                
                pTest = pingTest()
                sTest = speedTest()
                
                previousBSSID = currentBSSID
                currentBSSID = getAccessPointBSSID()
                bssidChanged = False
                
                if currentBSSID != previousBSSID: 
                    bssidChanged = True
                else:
                    bssidChanged = False
                    
                writeToCSV(i, pTest, sTest, previousBSSID, currentBSSID, bssidChanged)
                print("Information printed to CSV file! \n")
                
        
main()