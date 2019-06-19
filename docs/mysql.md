## 使用flask-sqlacodegen快速生成orm对象

终端输入

```
flask-sqlacodegen --outfile models.py  --flask 'mysql://user:password@ip/database'
```

将models.py放入models文件夹，修改db，`from application import db`

## 数据库备份与恢复

mysql数据库备份整个库shell:mysqldump -u root -p major_db > major_db.sql

mysql恢复数据库:mysql -uroot -p major_db < major_db.sql


## 使用flask-migrate进行数据库迁移

在`manage.py`中已经添加了**MigrateCommand**