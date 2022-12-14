# -*- coding: utf-8 -*-
"""corpus.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hpV7hMZtYWWxa7Gi8sEJe3WhRdZQiRov
"""

import spacy
import requests
import re
from bs4 import BeautifulSoup
#criar uma variável para armazenar no modelo
nlp=spacy.load("en_core_web_sm")
print("ok")

# Leonardo Luize

#A página web (url) deve apontar para uma página web em inglês contendo, não menos que 1000 palavras.
#O texto desta página deverá ser transformado em um array de senteças.

site1 = requests.get("https://en.wikipedia.org/wiki/English_Wikipedia")
site2 = requests.get("https://en.wikipedia.org/wiki/Marilyn_Monroe")
site3 = requests.get("https://en.wikipedia.org/wiki/British_English")
site4 = requests.get("https://en.wikipedia.org/wiki/Elvis_Presley")
site5 = requests.get("https://en.wikipedia.org/wiki/Spanish_conquest_of_Pet%C3%A9n")

print("ok")

def get_site_texts(site):
  return BeautifulSoup(site.text, 'html.parser').find_all('p')[2].get_text()

site_text1 = get_site_texts(site1)
site_text2 = get_site_texts(site2)
site_text3 = get_site_texts(site3)
site_text4 = get_site_texts(site4)
site_text5 = get_site_texts(site5)

print("ok")

def gerar_array_sentencas(txt):
  doc = nlp(txt)
  return [doc.orth_ for doc in doc if not doc.is_punct]

print("\nsite1:")
print(gerar_array_sentencas(site_text1))

print("\nsite2:")
print(gerar_array_sentencas(site_text2))

print("\nsite3:")
print(gerar_array_sentencas(site_text3))

print("\nsite4:")
print(gerar_array_sentencas(site_text4))

print("\nsite5:")
print(gerar_array_sentencas(site_text5))