#!/usr/bin/python
import time
import fasteners

def test():
	for i in range(10):
		with fasteners.InterProcessLock('/tmp/tmp_lock_file'):
			print('I have the lock')
			time.sleep(1)

test()
