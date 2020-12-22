import odia
from indic-transliteration import sanscript
from indic-transliteration.sanscript import transliterate
text="Sweta Mohapatra"
mystr=transliterate(text,sanscript.ITRANS,sanscript.ORIYA)
mylist=[]
for letter in mystr:
    mylist.append(letter)
print(mylist)	