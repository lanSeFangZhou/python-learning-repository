# 六、并发编程：asyncio、threading
# threading.Thread () 创建
# 在python中，主线程是第一个启动的线程。
# ~父线程:如果启动线程A中启动了一个线程B，A就是B的父线程。
# ~子线程：B就是A的子线程。
# 一个线程中调用另一个线程的join方法，调用者被阻塞，直到调用线程被终止
# ~run（）：用以表示线程活动的方法
# ~start（）：启动线程
# ~join（）：等待至线程终止
# ~isAlive（）：返回线程是否活动的
# ~getName（）：返回线程名称
# ~setName() : 设置线程名称
# python的threading模块提供了RLock锁解决方法。在某一时间只能让一个线程操作的语句放到RLock的acquire方法和release方法之间，
# 即acquire相当于给RLack上锁，而release相当于解锁
