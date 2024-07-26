
# 入口文件：index-html
```html
 <div id="app"></div> // 花盆
 <script type="module" src="/src/main.ts"></script> // 调用main.ts
```
# main.ts

```typescript
import './assets/main.css' //css样式

import { createApp } from 'vue' //引入createApp，创建应用平台（花盆）
import App from './App.vue' // 引入App根组件 （根基）

createApp(App).mount('#app') // 将根基放入花盆中，在 id=app 的div中,创建应用实例


```

App.vue是根基，components div是枝叶

# vue文件
一个.vue文件需要三种标签
1. template  结构
2. script   交互
3. style   样式

启动：npm run dev
