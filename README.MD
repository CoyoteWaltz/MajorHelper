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
---docs(后端api文档，数据库操作文档，数据表创建脚本，数据库备份)
---venv(已删除，本地开发改用anaconda3了，在创建的flask环境中)
application.py
manage.py
www.py
requirements.txt(python所需依赖的包，pip install -r requirements.txt)
```