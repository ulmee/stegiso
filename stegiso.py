#все необходимые импорты
import base64
import time
import pycdlib
#подготавливаем наши тексты
with open('/home/ul/stegist1.txt','rb') as stegist1:# открываем файл
    print('#Читаем файл')
    for line1 in stegist1.readlines(2):
        print(line1)#читаем содержимое
    for line2 in stegist1.readlines(2):
        print(line2)#читаем содержимое

enc_line1=base64.b64encode(line1)
print(enc_line1)
enc_line2=base64.b64encode(line2)
print(enc_line2)
with open('/home/ul/stegist2.txt','rb') as stegist2:
    print('#Читаем файл')
    for line3 in stegist2.readlines(2):
        print(line3)
    for line4 in stegist2.readlines(2):
        print(line4)
enc_line3=base64.b64encode(line3)
print(enc_line3)
enc_line4=base64.b64encode(line4)
print(enc_line4)
with open('/home/ul/up.txt','ab') as up:
    up.write(enc_line1)
    up.write(enc_line3)
with open('/home/ul/down.txt','ab') as down:
    down.write(enc_line2)
    down.write(enc_line4)
time.sleep(5)

#вносим все в структуру iso
iso=pycdlib.PyCdlib()
iso.new(rock_ridge='1.09')
iso.add_directory(iso_path='/A1',rr_name='a1')
iso.add_directory(iso_path='/B1',rr_name='b1')
iso.add_directory(iso_path='/B1/B2',rr_name='b1b2')
iso.add_directory(iso_path='/A1/A2',rr_name='a1a2')
iso.add_file('/home/ul/stegistup.txt', iso_path='/A',rr_name='a')
iso.add_file('/home/ul/stegistdown.txt', iso_path='/B',rr_name='b')
iso.write('papastegisto.iso')
