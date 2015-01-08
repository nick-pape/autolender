import datetime
import statistics
from urllib.request import urlopen

#default latency check, 20 pings
#returns mean - 2 standard deviations
def latencyCheckDefault():
    return latencyCheck(20)

#returns mean ping in microseconds 10^-6
def latencyCheck(n):
    pingTimes = []
    for i in range(0,n):
        startTime = datetime.datetime.now()
        #ping LendingClub here
        #TODO change this to one of Nick's networking methods
        urlopen("http://api.openweathermap.org/data/2.5/weather?q=London,uk").read()
        endTime = datetime.datetime.now()
        pingTimes.append((endTime - startTime).microseconds)
    return statistics.mean(pingTimes)-2*statistics.stdev(pingTimes,None);

print(latencyCheck(6))    
        
    
