import pyshorteners
d=input('Enter the url: ')
def shortener(d):
    s=pyshorteners.Shortener()
    print(s.tinyurl.short(d))
shortener(d)