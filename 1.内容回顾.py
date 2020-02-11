#-*-coding:utf-8-*-
# Author:Lu Wei

#锁 -都可以维护线程之间的数据安全
    #互斥锁 ：一把锁不能在一个线程中连续acquire，开销小
    #递归锁 ：一把锁可以连续在一个线程中acquire多次，acquire多少次就release多少次，开销大


    #死锁现象
        #1.在某些线程中出现陷入阻塞并且永远无法结束阻塞的情况就是死锁现象
        #出现死锁：
            #多把锁+交替使用
            #互斥锁在一个线程中连续acquire
    #避免死锁
        #在一个线程中只有一把锁，并且每一次acquire后都要release

#队列
    #先进先出 Queue
    #后进先出 LifoQueue
    #优先级  PriorityQueue

#池
    #1.是单独开启线程进程还是池？
        #如果只是开启一个子线程做一件事情，就可以单独开线程。
        #有大量的任务等待程序去做，要到达一定的并发数，开启线程池
        #根据你程序的IO操作可以判定是用池还是不用池？
            #socket 大量的阻塞IO，recv ， recvfrom socketserver 原生的线程。
            #爬虫的时候 池
    #2.回调函数
        #执行完子线程任务之后直接调用对应的回调函数
        #抓取网页 需要等待数据传输和网络上的响应高IO的--子线程
        #分析网页 没有什么IO操作，这个操作没有必要子线程完成，交给回调函数统一执行

            #关键点
                #1.存在IO操作的事情
                #2.基本不存在IO操作的事情
                #obj=submit(IO操作对应的函数)
                #obj.add_done_callback(计算型的事情)

    #3.
        #tp=ThreadPoolExecutor(cpu*5)
        #obj=tp.submit()
        #obj
            #1.获取返回值 obj.result()是一个阻塞方法
            #2.绑定回调函数 obj.add_done_callback(子线程执行完毕之后要执行的代码对应的函数)
        #ret=tp.map(需要在子线程执行函数名，iterable)
            #1.迭代ret，总是能得到所有的返回值

        #shutdown
            #tp.shutdown()

#进程池 和线程池都有锁
    #所有在线程中能工作的基本都不能在进程中工作
    #所有在进程中能工作的基本在线程总都能工作