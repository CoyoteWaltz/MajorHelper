# 测试程序
====
## 启动
export ops_config=local | production && python manage.py runserver

## 文件目录说明

```
---api(api接口)
    ---v1
        index.py
---common(公用部分，自己写的包，数据库模型)
    ---libs
    ---models
---config
---venv
application.py
manage.py
www.py
requirements.txt
```