# Bootstrap是什么
Bootstrap是一个流行的前端开发框架，由美国Twitter公司的设计师Mark Otto和Jacob Thornton合作基于HTML、CSS、JavaScript开发。

利用其提供的Sass变量和大量mixin、响应式栅格系统、可扩展的预制组件等快速开发网站原型。

引用本地的boostrap,js在body的最后面引用，也可以使用在线的CDN links来使用boostrap

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="bootstrap-5.3.3-dist/css/bootstrap.min.css">
    <title>Document</title>
</head>
<body>
    
    <link rel="stylesheet" href="bootstrap-5.3.3-dist/js/bootstrap.bundle.min.js">
</body>
</html>

```

# 容器

容器 container 是 Bootstrap 中最基本的布局元素，在使用默认网格系统时是必需的。容器用于容纳、填充和（有时）将内容居中。虽然容器可以嵌套，但大多数布局不需要嵌套容器。

Containers are the most basic layout element in Bootstrap and are required when using our default grid system. Containers are used to contain, pad, and (sometimes) center the content within them. While containers can be nested, most layouts do not require a nested container.

有两个容器类：
- .container 创建**固定宽度**的响应式页面
- .container-fluid 会根据屏幕宽度同比例放大缩小 宽度width始终是100%
- .container-{breakpoint}, which is width: 100% until the specified breakpoint

.container 的 固定宽度：

| 屏幕尺寸 | 超级小<576px | 小>=576px | 中等>=768px | 大>=992px | 特大>=1200px | 超级大>=1400px |  
| :--: | :--: | :--: | :--: | :--: | :--: | :--: |  
| 容器宽度 | 100% | 540px | 720px | 960px | 1140px | 1320px |

区别：

| 属性/类别 | .container | .container-fluid |  
| --- | --- | --- |  
| **宽度** | 根据屏幕大小设置固定宽度 | 宽度始终为100%，占据整个视口 |  
| **响应式** | 支持响应式布局，宽度会随屏幕大小变化 | 同样支持响应式布局，但宽度始终保持100% |  
| **内边距** | 容器左右两侧默认有15px的内边距 | 容器本身没有默认内边距，但内部元素可以添加 |  
| **内容对齐** | 内容在容器中通常居中显示 | 内容在容器中占据整个宽度，无特定对齐方式 |  
| **媒体查询** | 使用了媒体查询来定义不同屏幕宽度下的固定宽度 | 不使用媒体查询，始终保持100%宽度 |  
| **用途** | 用于创建固定宽度并支持响应式布局的容器 | 用于创建全屏宽度、流式布局的容器 |  
| **高度** | 高度均可设置为自动（auto）或指定值 | 高度均可设置为自动（auto）或指定值 |  

.container-{breakpoint}：

| 屏幕尺寸 | .container | .container-sm | .container-md | .container-lg | .container-xl | .container-xxl | .container-fluid |  
| --- | --- | --- | --- | --- | --- | --- | --- |  
| <576px | 100% | 100% | 100% | 100% | 100% | 100% | 100% |  
| ≥576px | 540px | 540px | 100% | 100% | 100% | 100% | 100% |  
| ≥768px | 720px | 720px | 720px | 100% | 100% | 100% | 100% |  
| ≥992px | 960px | 960px | 960px | 960px | 100% | 100% | 100% |  
| ≥1200px | 1140px | 1140px | 1140px | 1140px | 1140px | 100% | 100% |  
| ≥1400px | 1320px | 1320px | 1320px | 1320px | 1320px | 1320px | 100% |