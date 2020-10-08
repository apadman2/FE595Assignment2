import os
import requests

f = open("C:/Users/vaiku/FE 595 Files/Assignments/Results2.txt", "w")
for j in range(50):
    r = requests.get('http://3.95.249.159:8000/random_company')
    alltext = r.text
    words = alltext.split('\n')

    for i in words:
        if 'Name:' in i:
            namestr = i
            namestr = namestr[16:-5]
            f.write(namestr + '\n')
        if 'Purpose' in i:
            allpurpose = i
            allpurpose = allpurpose[16:-5]
            f.write(allpurpose + '\n')

### Review of Vaikunth's code: 5/5 (Review performed by Aniruddh Padmanaban) ######

f.close()
