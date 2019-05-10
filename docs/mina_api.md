# 分流助手（小程序）后端api文档

## 接口api

### 0.通配交互内容

```
request:
    header: {
  	    'content-type': 'application/json' // 默认值
    },

response:
    data : {}
    msg : ""
    code : ""       //业务状态码：2xxx = 正常, 4xxx = 有错误
    extra : 正式环境没有extra
```

### 1.专业定位

#### 1.1 标签选择页面

```
type : "GET"
url : "http://{{server ip}}:8080/v1/locate"
data = None
response : {
    data : {
        "interest" : [
            {"i_id" : 1, "i_content" : xxx},
            {"i_id" : 2, "i_content" : xxx},
            ...
        ]
    },
    msg : "ok",  // 请求状态描述，调试用
    code: 200, // 业务自定义状态码
    <!-- extra : { // 全局附加数据，字段、内容不定，调试用
        type: 1,
        desc: "成功！"
    } -->

}
```

#### 1.2 搜索页面

```
method : "GET"        // 兴趣标签是通过GET
url : "http://{{server ip}}:8080/v1/locate/search"

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
    code: 2001, // 业务自定义状态码
    <!-- extra : { // 全局附加数据，字段、内容不定，调试用
        type: 1,
        desc: "成功！"
    } -->

}
```

```
method : "POST"        // 搜索框用表单from提交
url : "http://{{server ip}}:8080/v1/locate/search"
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
    code: 2000, // 业务自定义状态码
    extra : { // 全局附加数据，字段、内容不定，调试用
        type: 1,
        desc: "成功！"
    }

}

response : {         //未搜索到，返回错误信息
    msg : "not found", // 没有失败的情况
    code: 4001, // 业务自定义状态码
    extra : { // 全局附加数据，字段、内容不定，调试用
        type: 1,
        desc: "失败！没有收录该专业"
    }
}

```

#### 1.3 详细页

```
method : "GET"
url : "http://{{server ip}}:8080/v1/detail/<int:id>"
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
    <!-- extra : { // 全局附加数据，字段、内容不定，调试用
        type: 1,
        desc: "成功！"
    } -->
}

response : {    // id不在数据库中
    msg : "数据库中未找到"
    code : 4004
}
```

### 2.专业一览

#### 2.1 大类-学院-专业

```
method : "GET"
url : "http://{{server ip}}:8080/v1/general"
data = None
response : {    // 返回大类{学院{专业}}
    data : {        // 这个数据有点庞大
        "category" : [  // list
            "理工大类" : {
                "college" : [        // list
                    "计算机工程与科学学院" : {
                        "major" : [  // list
                            {
                                "m_id" : 5,
                                "m_name" : "计算机科学与技术"
                            },
                            {
                                "m_id" : 42,
                                "m_name" : "智能科学与技术"
                            },
                            ...
                        ],
                    "环境科学与工程学院" : {
                        "major" : [
                            {
                                "m_id" : 15,
                                "m_name" : "环境工程"
                            },
                            {
                                "m_id" : 13,
                                "m_name" : "化学工程与工艺"
                            },
                            ...
                        ],
                    }
                ]
            },
            "人文大类" : {
                "college" : [
                    "xxx" : {
                        "major" : [
                            {
                                ...
                            }
                        ]
                    },
                    "yyy" : {
                        "major" : [
                            {
                                ...
                            },
                        ]
                    }
                ]
            }
        ]
    },
    msg : "ok", // 没有失败的情况
    code: 2001, // 业务自定义状态码
}
```

#### 2.2 前端最自豪的界面

```
// 当前大类的专业近三年排位百分比
method : "GET"
url : "http://{{server ip}}:8080/v1/general/rank"
data = {
    "c_id" : 1              // 当前类别的id
}
response : {    // 返回专业近三年排位
        data : [
            {
                "m_name" : xxx,
                "f_rank" : 32.1,
                "s_rank" : 34.1,
                "t_rank" : 30.1
            },
            {
                "m_name" : yyy,
                "f_rank" : 22.1,
                "s_rank" : None,        //如果是新专业的话还没测试能否发送None类型
                "t_rank" : None
            },
        ]
    msg : "ok", // 没有失败的情况
    code: 2001, // 业务自定义状态码
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