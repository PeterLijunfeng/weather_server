### 说明

获取天气信息，并发布服务。

- 通过配置文件获取城市信息
- 通过接口传入的省份 城市 站点编号获取信息
- 定时获取天气信息



天气信息包含7日内的气温，风力和降水等信息



### 依赖安装

```json
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```



### 数据库迁移&升级

```bash
flask db init 
flask db migrate -m "init_db"
flask db upgrade
```





### 启动定时任务

见文件 `crontab_synchroize.py`



### 服务启动&中止

```json
# Linux系统中
gunicorn -w 2 -b 0.0.0.0:7000 app:app -D

# windows系统中
# 先将虚拟环境安装在根目录下 venv文件夹中
weather_server.bat
```





### 接口文档

#### 获取指定城市的天气信息

**URL**    `/weather/<province>/<city>/<int:stationid>`

**方式**   GET

**返回参数**

```json
{
  "data": {
    "city": "xian", 
    "precipitation": {
      "hour": ["02:00", "05:00", "08:00", "11:00", "14:00", "17:00", "20:00", "23:00"], 
      "value": [ "-", "-", "-", "-", "-", "-", "-", "-"]
    }, 
    "province": "ASN", 
    "stationid": 57036, 
    "weather": [
      {
        "date": "2020-03-25", 
        "day": {"weather": {"img": "9999", "info": "9999", "temperature": "9999"}, 
          "wind": {"direct": "9999", "power": "9999"}}, 
        "night": {"weather": {"img": "http://image.nmc.cn/assets/img/w/40x40/4/1.png", "info": "\u591a\u4e91", "temperature": "12"}, 
          "wind": {"direct": "\u897f\u98ce", "power": "3~4\u7ea7"}}, 
        "pt": "2020-03-25 20:00"
      }, 
      {
        "date": "2020-03-26", 
        "day": {
          "weather": {
            "img": "http://image.nmc.cn/assets/img/w/40x40/4/2.png", 
            "info": "\u9634", 
            "temperature": "20"
          }, 
          "wind": {
            "direct": "\u897f\u5357\u98ce", 
            "power": "3~4\u7ea7"
          }
        }, 
        "night": {
          "weather": {
            "img": "http://image.nmc.cn/assets/img/w/40x40/4/7.png", 
            "info": "\u5c0f\u96e8", 
            "temperature": "7"
          }, 
          "wind": {
            "direct": "\u4e1c\u98ce", 
            "power": "\u5fae\u98ce"
          }
        }, 
        "pt": "2020-03-25 20:00"
      }, 
      ...
      }
    ]
  }, 
  "rst": "ok"
}
```



### 接口文档

#### 获取配置文件中城市的天气信息



**URL**    `/weather/latest`  

**方式**   GET

**返回参数**   同上

