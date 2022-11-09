
from email.utils import decode_rfc2231

d1 = {1:"a",2:"b",3:"c",4:"d"}
for clave,valor in d1.items():
    print(clave,valor)
d1[3]="Soy un cambio de valor"
d1[5]=["hola","que tal?"]
for clave,valor in d1.items():
    print(clave,valor)

