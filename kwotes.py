from pyquery import PyQuery

def grabber(i=0):
    base_url = "http://principiadiscordia.com/memebombs/"
    url = base_url + "kwotes.pl?action=list&m=501&so=reverse&o=date&s=" + str(i)
    PQ = PyQuery(url)
    BQ = PQ("blockquote")
    for x in BQ:
        try:
           print x.text
        except:
            error = 1
            #this is not error handling... it's error ignoring.

    if len(BQ):
        grabber(i+500)

grabber()