# 分流助手（小程序）后端api文档

## 接口api

### 1.专业定位

#### 1.1 标签选择页面
```
type : "GET"
url : "http://localhost:8787/v1/locate"
data = None
response : {
    data : {
        "interest" : [
            {"i_id" : 1, "i_content" : xxx},
            {"i_id" : 1, "i_content" : xxx},
            ...
        ]
    },
    msg : "ok",  // 请求状态描述，调试用
    code: 200, // 业务自定义状态码
    extra : { // 全局附加数据，字段、内容不定，调试用
        type: 1,
        desc: "成功！"
    }

}
```

#### 1.2 搜索页面

```
type : "GET"        // 兴趣标签是通过GET
url : "http://localhost:8787/v1/locate/search"

data : {
    "fid" : 2,      // 第一个兴趣标签的编号
    "sid" : 5,      // 第一个兴趣标签的编号
    "tid" : 4,      // 第一个兴趣标签的编号
}
response : {
    data = {    // 返回兴趣匹配到的部分专业
        "major" : [
            {"m_id" : 1, "m_name" : "工业设计"},
            {"m_id" : 4, "m_name" : "城乡规划"},
            ...
        ]
    },
    msg : "ok", // 没有失败的情况
    code: 200, // 业务自定义状态码
    extra : { // 全局附加数据，字段、内容不定，调试用
        type: 1,
        desc: "成功！"
    }

}
```

```
type : "POST"        // 搜索框用表单from提交
url : "http://localhost:8787/v1/locate/search"
data = {
    "content" : "xxxx"
}
response : {         //搜索到，返回全部专业id和名称
    data : {
        "major" : [
            {"m_id" : 1, "m_name" : "工业设计"},
            {"m_id" : 4, "m_name" : "城乡规划"},
            ...
        ]
    },
    msg : "ok", // 没有失败的情况
    code: 200, // 业务自定义状态码
    extra : { // 全局附加数据，字段、内容不定，调试用
        type: 1,
        desc: "成功！"
    }

}

response : {         //未搜索到，返回错误信息
    data : {
    },
    msg : "not found", // 没有失败的情况
    code: 404, // 业务自定义状态码
    extra : { // 全局附加数据，字段、内容不定，调试用
        type: 1,
        desc: "失败！没有收录该专业"
    }

}
```

### 1.3详细页

```
type : "GET"
url : "http://localhost:8787/v1/detail/<int:id>"
data = None
response : {    // id正确，返回详细信息
    data : {
        "m_name" : "xxx",
        "intro" : "内容为很长的文段",
        "course" : "内容为字符串",
        "salary" : "文段",
        "rank_precent" : 30.12  //浮点数
    },
    msg : "ok", // 没有失败的情况
    code: 200, // 业务自定义状态码
    extra : { // 全局附加数据，字段、内容不定，调试用
        type: 1,
        desc: "成功！"
    }
}

response : {    // id不在数据库中
    msg : "数据库中未找到"
    code : 404
}
```

## 数据库所需文档格式

### 1.专业信息

    专业名称,学院大类,专业介绍,薪资,近一年排名

### 2.兴趣标签

    兴趣名称,txt或者csv文件，一行为一个标签
    e.g.
    管理
    机器人
    ...

### 3.兴趣对应专业

    专业名,兴趣(顺序无所谓),用保存为csv类型文件(用excel编辑)
    e.g.
    工业设计,艺术
    工业设计,动手能力
    环境工程,化学
    ...




### ps
vscode中使用git提交至github：前提，github帐号已经登录了,新的repo要git init，然后git remote add origin (repository的ssh)