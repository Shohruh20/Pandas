# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1XtQhFzLXus-mXfHplFS6FhKTOTYtRCpU
"""

import pandas as pd
df = pd.DataFrame ({'ism':['Shoxrux','Nurmuhammad','Merojiddin','Shuxrat', 'Muhammadaziz','Oybek','Shoyat','Mohichexra','Xurshid','Ibrohim'],
                    'Familya':['Salimov','Jumanazarov','Bahtiyorjonov','Shamsiddinov','Rozaliyev','Akramov','Maqsudov','Yusupaliyeva','Odilov','Burxonov'],
                    'Yoshi':['19','19','19','19','19','19','19','20','19','19'],
                    'Kursi':['2','2','2','2','2','2','2','2','2','2']
                    })
print (df)

df.to_excel('Sessiya.xlsx',index=False, sheet_name='sheet1')