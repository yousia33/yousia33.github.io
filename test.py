import threading  
  
def worker():  
    """线程要执行的函数"""  
    print("线程开始工作...")  
    # 模拟一些工作  
    for i in range(5):  
        print(f"线程中: {i}")  
    print("线程工作完成.")  
  
# 创建一个Thread对象  
t = threading.Thread(target=worker)  
  
# 启动线程  
t.start()  
  
# 主线程会继续执行以下代码  
for i in range(5):  
    print(f"主线程中: {i}")  
  
# 等待所有线程完成（在这个简单的例子中，我们只有一个线程，所以这一步是可选的）  
t.join()  
  
print("主线程结束.")