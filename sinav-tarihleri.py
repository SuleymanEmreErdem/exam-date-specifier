#!/usr/bin/env python
import requests as req
from bs4 import BeautifulSoup as bs
 
def butun_programlar(fakulte):
    url = f"https://dersprogramiyukle.atilim.edu.tr/20222023baharfinal/{fakulte}/index_files/sheet001.htm"
    response = req.get(url)
    soup = bs(response.content, "html.parser")
    tlist = soup.text.split("\n\n")
    tlist = [a.replace("\xa0","") for a in tlist]
    return tlist

fakulteler = ["servis", "gsod", "fef", "gstmf", "saglik", "isletme", "muhendislik", "sivil"]

print("Bu uygulama sayesinde hukuk fakültesi hariç final tarihlerine, ders kodlarını girerek ulaşabilirsin.\n")
num = int(input("Kaç dersin var? "))

print("\nDers kodlarını gir:\n")
for _ in range(num):
	ders = input()
	for fakulte in fakulteler:
		tlist = butun_programlar(fakulte)
		for ind, text in enumerate(tlist):
			if ders in text:
				print(text)
