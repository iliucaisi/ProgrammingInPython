#!/usr/local/bin/python3
def make_fun():
	n = 0

	def func_to_return(arg):
		nonlocal n
		print(n, arg, end=": ")
		#print('%s %s : ' % (n, arg))
		arg += 1
		n += arg
		return n
	return func_to_return

x = make_fun()
y = make_fun()

for i in range(5):
	print(x(i))

print("=" * 10)

for i in range(10, 15):
	print(y(i))



