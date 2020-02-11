#-*-coding:utf-8-*-
# Author:Lu Wei

# #1.
# import threading
# import time
# def _wait():
# 	time.sleep(3)
# # flag a
# t = threading.Thread(target=_wait,daemon = False)
# t.start()
# # flag b
#
# #3s
#
#
# #2
# import threading
# import time
# def _wait():
# 	time.sleep(60)
# # flag a
# t = threading.Thread(target=_wait,daemon = True)
# t.start()
# # flag b
#
# #马上

#3
# import threading
# import time
# def _wait():
# 	time.sleep(60)
# # flag a
# t = threading.Thread(target=_wait,daemon = True)
# t.start()
# t.join()
# # flag b

#60


#4
# import threading
# loop = int(1E7)
# def _add(loop:int = 1):
# 	global number
# 	for _ in range(loop):
# 		number += 1
# def _sub(loop:int = 1):
# 	global number
# 	for _ in range(loop):
# 		number -= 1
# number = 0
# ta = threading.Thread(target=_add,args=(loop,))
# ts = threading.Thread(target=_sub,args=(loop,))
# ta.start()
# ts.start()
# ta.join()
# ts.join()
# print(number)
#

#
# import threading
# loop = int(1E7)
# def _add(loop:int = 1):
# 	global number
# 	for _ in range(loop):
# 		number += 1
# def _sub(loop:int = 1):
# 	global number
# 	for _ in range(loop):
# 		number -= 1
# number = 0
# ta = threading.Thread(target=_add,args=(loop,))
# ts = threading.Thread(target=_sub,args=(loop,))
# ta.start()
# ta.join()
# ts.start()
# ts.join()
# print(number)

# import threading,time
# loop = int(1E7)
# def _add(loop:int = 1):
# 	global numbers
# 	for _ in range(loop):
# 		numbers.append(0)
#
#
# def _sub(loop:int = 1):
#     global numbers
#     for _ in range(loop):
#         while not numbers:
#             # print(123)
#             time.sleep(1E-8)
#         numbers.pop()
# numbers = [0]
# ta = threading.Thread(target=_add,args=(loop,))
# ts = threading.Thread(target=_sub,args=(loop,))
# ta.start()
# ta.join()
# print(len(numbers))
# ts.start()
# ts.join()
# print(len(numbers))


import threading,time
loop = int(1E7)
def _add(loop:int = 1):
	global numbers
	for _ in range(loop):
		numbers.append(0)


def _sub(loop:int = 1):
    global numbers
    for _ in range(loop):
            while not numbers:
                print(123)
                time.sleep(1E-8)
            numbers.pop()

numbers = [0]
ta = threading.Thread(target=_add,args=(loop,))
ts = threading.Thread(target=_sub,args=(loop,))
ta.start()
ts.start()
ta.join()
ts.join()
print(len(numbers))