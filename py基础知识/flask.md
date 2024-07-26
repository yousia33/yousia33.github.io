# HTTP方法

@app.route("/login",methods=["POST","GET"])


## 在html页面输入——form

<form action="#" method="post">
  <input type = "submit" value="submit">
</form>

## 检查是GET还是POST

```python
from flask import request

...

@app.route("/login",methods=["POST","GET"])
def login():
  if request.method == "POST"
    return template_render()
  else:
    return template_render()

```

# Sessions

在 Flask 中，session 对象是一个非常有用的特性，它允许你在用户的多个请求之间存储和检索信息。这通常用于跟踪用户的登录状态、保存用户的偏好设置或者存储任何需要在多个页面或请求之间持久保存的数据。

 ```python

 from flask import session

  @app.route("/login",methods=["POST","GET"])
def login():
  
  if request.method == "POST"
  user = request.form["nm"]
  session["user"] = user
    return template_render()
  else:
    return template_render()

另一个路由中：
  if "user" in session
    return ...

```

添加： session[key] = value
删除： session.pop(key，None)

PERMANENT_SESSION_LIFETIME 是 Flask 框架中一个用于配置 session 持久性时间的参数。在 Flask 应用中，这个参数决定了 session 将在客户端（通常是用户的浏览器）中保持有效的时间长度。默认情况下，Flask 的 session 会在浏览器关闭后立即过期，但通过设置 PERMANENT_SESSION_LIFETIME，可以改变这个行为，使得 session 能够在浏览器关闭后仍然保持有效一段时间。



# flash message

在 Flask 中，flash 消息是一种在多个请求之间传递消息给用户的机制，特别是用于在用户完成某些操作（如登录、提交表单等）后，向用户显示一次性的通知或错误消息。这些消息通常显示在模板的某个部分，如导航栏下方或页面顶部，直到下一个请求发生并且可能的新消息覆盖了它们。

 `from flask import Flask, flash, render_template, get_flashed_messages`

在视图函数中，你可以使用 flash() 函数来发送一个 flash 消息。这个函数接受两个参数：消息内容和消息的分类（可选）。

 ```python
@app.route('/login', methods=['GET', 'POST'])  
def login():  
    # 假设这里有一些登录逻辑  
    if login_successful:  
        flash('登录成功！', 'success')  
        return redirect(url_for('home'))  
    # 登录失败的情况  
    flash('用户名或密码错误！', 'error')  
    return render_template('login.html')
 ```

 在template中显示flash消息

 ```html

{% with messages = get_flashed_messages(with_categories=true) %}  
  {% if messages %}  
    <ul class="flashes">  
    {% for category, message in messages %}  
      <li class="{{ category }}">{{ message }}</li>  
    {% endfor %}  
    </ul>  
  {% endif %}  
{% endwith %}

 ```