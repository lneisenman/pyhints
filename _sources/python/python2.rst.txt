===============
Python Trivia 2 
===============

Passing Parameter Lists
=======================

Here is an example of passing parameter value lists and keyword-argument lists. This can be used to pass parameters to a function that calls another function without the calling function having to explicitly know the names of the parameters of the called function.

.. code-block:: py3

	def testfcn(n=1, a=2, b=3):
		print("n = %d, a = %d, b = %d" % (n, a, b))
		
		
	def call_testfcn(*argv, **kwargs):
		testfcn(*argv, **kwargs)
		if len(argv) > 0:
		    for value in argv:
		        print(value)
		if (len(kwargs) > 0):
		    for key in kwargs.iterkeys():
		        print(key, kwargs[key])
		

	if __name__ == '__main__':
		call_testfcn()
		call_testfcn(n=3)
		call_testfcn(a=3, b=1)
		test = [4, 5]
		call_testfcn(*test)
		test = {'a':3, 'b':1}
		call_testfcn(**test)
		test1 = [4, 5]
		test2 = {'b':6}
		call_testfcn(*test1, **test2)


