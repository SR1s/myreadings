# About
This project aim to build a service for users to make they notes while they viewing webpage which have something needed to record.

# Dependency
Flask
Flask-SQLAlchemy
MySQL

# 部署
1. 初次部署请运行myreadings/db_rebuild.py创建数据库
2. 更改配置文件myreadings/config/local_config.py，填写正确的数据库参数
3. 将myreadings/config/myreadings.ngix文件复制到/ect/ngix/site-available中，并在/ect/ngix/site-enabled中创建软链接链接到此文件
3. 将myreadings/config/uwsgi_cofig.xml中的pathonpath标签中的值改为项目所在文件夹路径
4. 在/etc/rc.local文件中添加/usr/local/bin/uwsgi -x <your_project_path>/myreadings/config/uwsgi_config.xml使uwsgi开机自动启动
5. 重启ngix或重启服务器，即可生效
