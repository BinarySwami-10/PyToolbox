import bs4
from bs4 import BeautifulSoup as soup
import xml
import html5lib
import time

def print_all_items(list):
	for i in list:
		print(i)

def del_numbers(string_in):
	processed=string_in.split()
	pure=[]
	# for i in range(len(processed)):
	# 	if ( processed[i].isalpha()==True ):
	# 		pure.append(processed[i])

	# 		# processed[i]=''
	return pure

def open_file(name):
	file = open(filename, 'r')
	content = file.read()
	file.close()
	return content

filename = 'sample.sgm'
text=open_file(filename)

timer=time.monotonic_ns()
text_blocks=soup(text,'html5lib').findAll('text')
print(time.monotonic_ns()-timer)

t_string=text_blocks[60]
test='asasasas asdasd asdsadgfbxc'
# print(t_string.text.split())
giga_dictonary={'a':'as'}
# giga_dictonary
print (giga_dictonary.__setitem__('s','er'))
print(giga_dictonary)



