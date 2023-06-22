# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Ders 6 : Kütüphanelerin Yüklenmesi
# Libraries

import pandas as pd     # Kütüphane eklemek için import anahtar kelimesi kullanılır.
import numpy as np      # Kütüphane isimlerinde kısaltma yapmak için as anahtar kelimesi kullanılır.
import matplotlib.pyplot  as mp


# ------- Coding Scope ------- 


# Veri Yükleme 

veriler = pd.read_csv("veriler.csv")
print(veriler) 



# Veri Ön İşleme 

boy = veriler[["boy"]]  #Veri kaynağı bir listeye dönüştürülmüş ve üzerinde filtreleme işlemi yapılmıştır.
print(boy)

boyKilo = veriler[["boy","kilo"]]
print(boyKilo)