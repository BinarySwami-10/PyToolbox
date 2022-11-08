import json
import os ,threading

def worker(a,b):
	print(a+b)

import os
script_dir = os.path.dirname(__file__)
sublocator = os.path.join(script_dir, "classroom/alldatathreaded.json")
print (script_dir)

with open(sublocator,'r',) as f1:
    dicto=json.load(f1)

'''print(len(dicto['titles']))
for i in range(0,len(dicto['paragraphs'])):
	print(dicto['titles'][i])
	print(dicto['paragraphs'][i],'\n ------------------------------------- \n\n\n\n\n\n\n')'''


'''list1=['madadar']
void=['123213']
list1.extend()
print(list1)'''








'''for a in range(1,6):
	void.append(a)
	print(void,)
	list1.append(void)
	print(list1,'\n')'''

#	for b in range(10):
#		list1.append(0)
