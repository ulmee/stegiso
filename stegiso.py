#all imports
import time
import pycdlib
#preparing our texts
stegist1=open('/home/ul/stegist1.txt','r')
stegist2=open('/home/ul/stegist2.txt','r')
#creating a new file that constist of 1 part of 1 and 2 file
stegistup=open('/home/ul/stegistup.txt','a+')
steg11=stegist1.readlines(4)
print(steg11,file=stegistup)
stegistup.close()
stegistup=open('/home/ul/stegistup.txt','a')
steg21=stegist2.readlines(2)
print(steg21,file=stegistup)
stegistup.close()
#creating one more new file that constist of 2 part of 1 and 2 file
stegistdown=open('/home/ul/stegistdown.txt','a+')
steg12=stegist1.readlines(3)
print(steg12,file=stegistdown)
stegistdown.close()
stegistdown=open('/home/ul/stegistdown.txt','a')
steg22=stegist2.readlines(2)
print(steg22,file=stegistdown)
stegistdown.close()
stegist1.close()
stegist2.close()
#preparing our files
iso=pycdlib.PyCdlib()
iso.new(rock_ridge='1.09')
iso.add_directory(iso_path='/A1',rr_name='a1')
iso.add_directory(iso_path='/B1',rr_name='b1')
iso.add_directory(iso_path='/B1/B2',rr_name='b1b2')
iso.add_directory(iso_path='/A1/A2',rr_name='a1a2')
iso.add_file('/home/ul/stegistup.txt', iso_path='/A',rr_name='a')
iso.add_file('/home/ul/stegistdown.txt', iso_path='/B',rr_name='b')
iso.write('papastegisto.iso')
