# 七，cpython、GIL
# Python(CPython)将Python源码编译成CPython字节码，再由虚拟机解释执行这些字节码。
# python将py文件编译成为PyCodeObject，再将这个对象写入某文件就成为了pyc文件，文件中包含python的magic number(来说明
# 编译时使用的python版本号)、源文件的mtime(使pyc和py文件保持同步)、编译出的code对象
# Python Virtual Machine，简写为PVM，当有字节码文件之后，就会被发送到PVM里来执行。
# 这里注意，PVM并不是指的一个独立的程序，是不需要安装的。可以把PVM理解为Python的运行引擎，是一个迭代运行字节码指令的大循环，
# 一个个的完成操作，直到结束。
# 从技术角度看，PVM才是“解释器”的最后一步。
# Python有多个解释器实现。分别用C，Java，C＃和Python编写的CPython，Jython，IronPython和PyPy是最受欢迎的。GIL仅存在
# 于CPython的原始Python实现中
# GIL：⼜叫全局解释器锁，每个线程在执⾏的过程中都需要先获取GIL，保证同⼀时刻只有⼀个线程在运⾏，⽬的是解决多线程
# 同时竞争程序中的全局变量⽽出现的线程安全问题。

