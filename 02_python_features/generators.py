# 生成器（generator）也是一种迭代器，在每次迭代时返回一个值，直到抛出 StopIteration 异常。
# 含有 yield 关键字的函数，调用该函数时会返回一个生成器
# 我们可以使用 close() 方法来关闭一个生成器。生成器被关闭后，再次调用 next() 方法，不管能否遇到 yield 关键字，都会抛出 StopIteration 异常

