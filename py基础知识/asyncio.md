适合处理需要等待的程序,面对很多任务决定执行哪一个任务

同时执行的任务只能有一个

# 概念

什么是协程coroutine？

一种轻量级线程

特点：

- 轻量级：协程的创建、切换和销毁的开销远小于线程，这使得协程在需要大量并发任务时更加高效。
- 非抢占式：协程的调度是由程序员控制的，而不是由操作系统自动调度。这意味着协程的执行顺序和时机完全取决于程序中的代码逻辑。
- 高并发：由于协程的轻量级特性，一个线程中可以创建大量的协程来并发执行多个任务，从而提高程序的并发处理能力。
- 状态保存：协程在切换时会自动保存当前的状态和上下文信息，以便在下次切换回来时能够从上次中断的地方继续执行。

## 携程函数

`async def` 开头的函数就是携程函数

调用携程函数，返回的是一个**携程对象coroutine object**而不会运行程序

如何运行 coroutine 的代码？
1. 进入async（进入event loop）
2. 吧coroutine 变成 task


入口函数 asyncio.run(coroutine对象)

**asyncio.run**是从同步变成异步的入口

asyncio.sleep() 等待几秒，返回的是coroutine对象

await可以将coroutine对象变成task
放回event loop里，同时告诉event loop需要等待这个task运行

task需要主动把控制权交回event loop


asyncio.create_task(corotine对象)
接受corotine对象返回task对象，将task注册到event loop里

如果await后跟的是task，不需要交还控制权给await

```python
import asyncio

async def func1():

	print('协程1')

async def func2():
	await asyncio.sleep(1)
	print('协程2')

async def  main():
	await func1()
	await func2()

asyncio.run(main()) # 运行到func2时会等待1s

```

```python
import asyncio

async def func1():

	print('协程1')

async def func2():
	await asyncio.sleep(1)
	print('协程2')

async def func3():
	await asyncio.sleep(2)
	print('协程3')


async def  main():
	await func1()
	await func2()
	await func3()

asyncio.run(main()) #运行到func2等待1s，func3等待2秒，不会一起等待，与异步的思想相悖

```

```python
import asyncio

async def func1():

	print('协程1')

async def func2():
	await asyncio.sleep(1)
	print('协程2')

async def func3():
	await asyncio.sleep(2)
	print('协程3')


async def  main(): 
	task1=asyncio.create_task(func1()) #通过asyncio.create_task()将corotine对象转化为task
	task2=asyncio.create_task(func2())
	task3=asyncio.create_task(func3())

	await task1 #await task,可以实现异步
	await task2
	await task3



asyncio.run(main()) #一共等待2s

```

使用asyncio.create_task()来并行执行协程。create_task()函数将协程封装成任务（Task），并立即返回，而不会等待协程完成。这样，main函数就可以同时启动func1、func2和func3的执行，而不是顺序地等待它们。
尽管在main函数中await是顺序的，但这并不妨碍协程本身的并行执行。总执行时间取决于最慢的协程完成所需的时间