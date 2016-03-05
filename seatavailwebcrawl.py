
import requests
from bs4 import BeautifulSoup
import pynotify
from time import sleep

try:
    trainno=input('Enter Train Number :- ')
    date=raw_input('Enter Date of Journey in "YYYY-MM-DD" format :- ')
    ars=raw_input('Enter Arrival Station Code :- ')
    deps=raw_input('Enter Departure Station code :- ')
    cls=raw_input('Enter Class Code eg SL-Sleeper 3A-Third AC etc :-')
    x='XXX'
    ars.lower()
    deps.lower()
    url='http://www.railyatri.in/seat-availability/'+(str)(trainno)+'-'+ars+'-'+deps+'?'+'journey_class='+cls+'&journey_date='+date+'&quota=GN'
    while x[0]=='A':
        sc=requests.get(url)
        soup=BeautifulSoup(sc.content,'lxml')
        for row in soup.find_all('div',attrs={"id" : "first1"}):
            x=row.text

        pynotify.init('test')
        n = pynotify.Notification('        Availability - '+str(x))
        n.show()

    pynotify.init('test')
    n = pynotify.Notification('        Availability - '+str(x))
    n.show()

    
except requests.exceptions:
    pynotify.init('test')
    n = pynotify.Notification('Connection Issue','No internet found')
    n.show()

    
