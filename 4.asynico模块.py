#-*-coding:utf-8-*-
# Author:Lu Wei

import asyncio

#起一个任务
# async def demo():
#     print('start')
#     await asyncio.sleep(1)
#     print('end')
#
# loop=asyncio.get_event_loop()   #创建一个事件循环
# loop.run_until_complete(demo()) #把demo任务丢到事件循环中去执行

# #起多个任务，且没有返回值
# async  def demo():
#     print('start')
#     await asyncio.sleep(1)
#     print('end')
# loop=asyncio.get_event_loop()   #创建一个事件循环
# wait_obj=asyncio.wait([demo(),demo(),demo()])
# loop.run_until_complete(wait_obj)


# async def demo():
#     print('start')
#     await asyncio.sleep(1)
#     print('end')
#     return 123
# loop=asyncio.get_event_loop()
# t1=loop.create_task(demo())
# t2=loop.create_task(demo())
# wait_obj=asyncio.wait([t1,t2])
# loop.run_until_complete(wait_obj)
# tasks=[t1,t2]
# for i in tasks:
#     print(i.result())

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