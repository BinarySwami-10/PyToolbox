def test1(arg):
	a=1
	c=arg

	def fn1(te):
		# nonlocal c
		nonlocal c
		c='fenane'
		print(c+' => from fn1')

		def pou(num):
			nonlocal c
			c='petane'
			print(c+' => from pou')
		pou('init')

	fn1(333)
	print(c,' => from test1')



	return arg

print(test1(400))
