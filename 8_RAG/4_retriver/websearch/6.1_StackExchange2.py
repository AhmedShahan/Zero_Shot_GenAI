import requests

res = requests.get("https://api.stackexchange.com/2.3/sites")
sites = res.json()["items"]

for site in sites:
    print(f"{site['name']} → site=\"{site['api_site_parameter']}\"")
'''
Stack Overflow → site="stackoverflow"
Server Fault → site="serverfault"
Super User → site="superuser"
Meta Stack Exchange → site="meta"
Web Applications → site="webapps"
Web Applications Meta → site="webapps.meta"
Arqade → site="gaming"
Arqade Meta → site="gaming.meta"
Webmasters → site="webmasters"
Webmasters Meta → site="webmasters.meta"
Seasoned Advice → site="cooking"
Seasoned Advice Meta → site="cooking.meta"
Game Development → site="gamedev"
Game Development Meta → site="gamedev.meta"
Photography → site="photo"
Photography Meta → site="photo.meta"
Cross Validated → site="stats"
Cross Validated Meta → site="stats.meta"
Mathematics → site="math"
Mathematics Meta → site="math.meta"
Home Improvement → site="diy"
Home Improvement Meta → site="diy.meta"
Meta Super User → site="meta.superuser"
Meta Server Fault → site="meta.serverfault"
Geographic Information Systems → site="gis"
Geographic Information Systems Meta → site="gis.meta"
TeX - LaTeX → site="tex"
TeX - LaTeX Meta → site="tex.meta"
Ask Ubuntu → site="askubuntu"
Ask Ubuntu Meta → site="meta.askubuntu"

'''