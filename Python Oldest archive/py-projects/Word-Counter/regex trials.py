import re
p=re.compile(r'\s+')
def is_matching(i_string):
	global p
	m=p.findall(i_string)
	print(len(m))
is_matching('000211 a a')

