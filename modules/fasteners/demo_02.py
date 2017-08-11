#!/usr/bin/python
import time
import fasteners

def test():
	a_lock = fasteners.InterProcessLock('/tmp/tmp_lock_file')
	for i in range(10):
		gotten = a_lock.acquire(blocking=False)
		try:
			if gotten:
				print('I have the lock')
				time.sleep(0.2)
			else:
				print('I do not have the lock')
				time.sleep(0.1)
		finally:
			if gotten:
				a_lock.release()

test()
