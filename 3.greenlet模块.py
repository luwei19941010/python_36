#-*-coding:utf-8-*-
# Author:Lu Wei

# import time
# from greenlet import greenlet
#
# def eat():
#     print('luwei is eating')
#     time.sleep(0.5)
#     g2.switch()
#     print('luwei finished eat')
#
# def sleep():
#     print('weilu is sleeping')
#     time.sleep(0.5)
#     print('weilu is finished sleep')
#     g1.switch()
#
# g1=greenlet(eat)
# g2=greenlet(sleep)
# g1.switch()

# import time
# import gevent
# print('time===',time.sleep)
# from gevent import monkey
# monkey.patch_all()
# s=time.time()
# def eat():
#     print('wusir is eating')
#     time.sleep(1)
#     # gevent.sleep(1)
#     print('time===', time.sleep)
#     print('wusir finished eat')
#
# def sleep():
#     print('小马哥 is sleeping')
#     time.sleep(1)
#     print('小马哥 finished sleep')
#
# g1 = gevent.spawn(eat)  # 创造一个协程任务
# g2 = gevent.spawn(sleep)  # 创造一个协程任务
# g1.join()   # 阻塞 直到g1任务完成为止
# g2.join()   # 阻塞 直到g1任务完成为止
# print('123')




# import time
# import  gevent
# from gevent import monkey
# monkey.patch_all()
#
# def eat():
#     print('luwei is eating')
#     time.sleep(1)
#     print('luwei finished eat')
#
# def sleep():
#     print('davidlu is sleep')
#     time.sleep(1)
#     print('davidlu finished sleep')
#
# g1=gevent.spawn(eat)
# g2=gevent.spawn(sleep)
# gevent.joinall([g1,g2])

#返回值
import time
import  gevent
from gevent import monkey
monkey.patch_all()

def eat():
    print('luwei is eating')
    time.sleep(1)
    print('luwei finished eat')
    return 'luwei ****'

def sleep():
    print('davidlu is sleep')
    time.sleep(1)
    print('davidlu finished sleep')
    return 'davidlu ****'

g1=gevent.spawn(eat)
g2=gevent.spawn(sleep)
gevent.joinall([g1,g2])

print(g1.value)
print(g2.value)
