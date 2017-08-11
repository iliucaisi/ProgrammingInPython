#!/usr/bin/python
import time
import fasteners

@fasteners.interprocess_locked('/tmp/tmp_lock_file')
def test():
	for i in range(10):
		print('I have the lock')
		time.sleep(1)

print('Waiting for the lock')
test()
