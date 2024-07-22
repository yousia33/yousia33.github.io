# 在main.ts中导入
```typescript

import { createApp } from 'vue'
import ElementPlus from 'element-plus' //导入模块
import 'element-plus/dist/index.css' //导入css样式
import App from './App.vue'

const app = createApp(App)

app.use(ElementPlus) //注册插件
app.mount('#app')

```

# 按钮模块

按钮的颜色通过type属性定义，属性通过plain，round，circle，disabled，loading定义

```typescript

<el-button>Default</el-button> //白色
<el-button type="primary">Primary</el-button> //主要按钮 蓝色
<el-button type="success">Success</el-button> //成功按钮 绿色
<el-button type="info">Info</el-button> ////信息按钮，灰色
<el-button type="warning">Warning</el-button>// 橙色
<el-button type="danger">Danger</el-button>// 红色

  <h3>按钮属性</h3>
        <el-button plain>朴素按钮</el-button>
        <el-button round>圆角按钮</el-button>
        <el-button circle>圆</el-button>
        <el-button disabled>禁用按钮</el-button>
        <el-button loading>加载中</el-button>

  <h3>尺寸</h3>
        <el-button size="large">大型按钮</el-button>
        <el-button>默认按钮</el-button>
        <el-button size="small">小型按钮</el-button>


```

# 图标

使用图标前需要导入并注册