# ImageTimeEdit



##你需要安装一个python3 

从python.org下载python3 然后执行 `pip install -r requirements.txt`
修改config.json

```
{
    "begin_date":"2018-6-18", //开始日期
    "end_date":"2018-6-25", //结束日期
    "rest_time_begin":"12:00:00",//休息时间开始
    "rest_time_end":"14:00:00", //休息时间结束
    "time_line_start":"10:00:00",//工作时间开始
    "time_line_end":"19:00:00"//工作时间结束
}
```
注意时间格式

#执行

将图片放在img文件夹
在项目目录执行python change.py
需要的图片将出现在res目录
