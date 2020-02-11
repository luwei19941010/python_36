### day36

#### 1.今日内容

```
#进程 资源分配的最小单位
#线程 CPU执行的最小的单位

#只要是线程里的代码就都被CPU执行就行
#线程是由 操作系统调度，由操作系统负责切换的
	#操作系统对IO操作的感知更加灵敏
#协程：
	#用户级别的，由我们自己写的python代码控制切换
	#是操作系统不可见的
#cpython解释器下	---协程和线程都不能利用多核，都是在一个CPU上轮流执行
	#由于多线程本身就不能利用多核
	#所以即便是开启了多个线程也只能在一个cpu上执行
	#协程如果把所有的任务的io操作都规避掉，只剩下需要使用cpu的操作
	#就意味着协程就可以做到提高cpu利用率的效果

```

```
#使用携程的好处
1.一个线程中的阻塞都被其他的各种任务沾满了
2.让操作系统觉得这个线程很忙
  尽量的减少这个线程进入阻塞的状态
  提高了单线程对CPU的利用率
3.多个任务在同一个线程中执行
  也达到了一个并发的效果
  规避了每一个任务的io操作
  减少了线程的个数，减轻了操作系统的负担
```

#### 2.协程模块介绍

协程：能够在一个线程下的多个任务之间来回切换，那么每一个任务都是一个协程

两种切换方式：

​			1.原生python完成，yield 	asyncio

​			2.C语言完成的python模块	greenlet   gevent模块



##### 2.1greenlet

```
import time
from greenlet import greenlet

def eat():
    print('luwei is eating')
    time.sleep(0.5)
    g2.switch()
    print('luwei finished eat')

def sleep():
    print('weilu is sleeping')
    time.sleep(0.5)
    print('weilu is finished sleep')
    g1.switch()

g1=greenlet(eat)
g2=greenlet(sleep)
g1.switch()
```

##### 2.2.gevent

```
#关于gevent monkey.patch_all()
#由于gevent模块不认识类似time.sleep这些IO阻塞，在编译代码时会将这些IO阻塞重写，替换成gevent模块能够认识的IO阻塞。
举例：
import time
import gevent
print('time===',time.sleep)
from gevent import monkey
monkey.patch_all()
s=time.time()
def eat():
    print('wusir is eating')
    time.sleep(1)
    # gevent.sleep(1)
    print('time===', time.sleep)
    print('wusir finished eat')
g1 = gevent.spawn(eat)  # 创造一个协程任务
g2.join()   # 阻塞 直到g1任务完成为止
print('123')


结果：
time=== <built-in function sleep> 		#重写之前为内置模块
wusir is eating
time=== <function sleep at 0x0000000002C79598>	#重写之后为对象
wusir finished eat
123
```



```
import time
import gevent
from gevent import monkey	
monkey.patch_all()					#重写IO阻塞
s=time.time()
def eat():
    print('wusir is eating')
    time.sleep(1)
    # gevent.sleep(1)				#gevent可以认识的IO阻塞
    print('wusir finished eat')

def sleep():
    print('小马哥 is sleeping')
    time.sleep(1)
    print('小马哥 finished sleep')

g1 = gevent.spawn(eat)  # 创造一个协程任务	
g2 = gevent.spawn(sleep)  # 创造一个协程任务
g1.join()   # 阻塞 直到g1任务完成为止		
g2.join()   # 阻塞 直到g1任务完成为止
print('123')

```



```
#多个协程任务 gevnet.jionall([g1,g2])
import time
import  gevent
from gevent import monkey
monkey.patch_all()

def eat():
    print('luwei is eating')
    time.sleep(1)
    print('luwei finished eat')

def sleep():
    print('davidlu is sleep')
    time.sleep(1)
    print('davidlu finished sleep')

g1=gevent.spawn(eat)
g2=gevent.spawn(sleep)
gevent.joinall([g1,g2])
```

```
#多协程任务 取协程返回值
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
```

##### 2.3asyncio

###### 2.3.1起一个协程任务

```

#起一个任务
async def demo():			#协程函数
    print('start')
    await asyncio.sleep(1)	 #await标识符类似for，看到await函数就知道需要切换
    print('end')

loop=asyncio.get_event_loop()   #创建一个事件循环
loop.run_until_complete(demo()) #把demo任务丢到事件循环中去执行
```

###### 2.3.2启动多个协程任务，没有返回值

```
#起多个任务，且没有返回值
async  def demo():
    print('start')
    await asyncio.sleep(1)
    print('end')
loop=asyncio.get_event_loop()   #创建一个事件循环
wait_obj=asyncio.wait([demo(),demo(),demo()]) #将协程任务放入列表中
loop.run_until_complete(wait_obj)
```

###### 2.3.3启动多个任务并且有返回值

```
# 启动多个任务并且有返回值
async def demo():
    print('start')
    await asyncio.sleep(1)
    print('end')
    return 123
loop=asyncio.get_event_loop()
t1=loop.create_task(demo())
t2=loop.create_task(demo())
wait_obj=asyncio.wait([t1,t2])
loop.run_until_complete(wait_obj)
tasks=[t1,t2]
for i in tasks:
    print(i.result())
```



###### 2.3.4谁先回来先取谁的结果

```
#谁先执行完成就先取谁的结构
async  def demo(i):
    print('start')
    await asyncio.sleep(10-i)
    print('end')
    return i,123

async def main():
    task_l=[]
    for i in range(10):
        task=asyncio.ensure_future(demo(i))
        task_l.append(task)
    for ret in asyncio.as_completed(task_l):
        res=await ret
        print(res)
loop=asyncio.get_event_loop()
loop.run_until_complete(main())
```

