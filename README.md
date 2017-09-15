## 简介
该项目爬取了github中流行的项目，并进行语言排名和图标分析，供开源爱好者参考

## 环境依赖
 - python 3.6.1
 - mongo 3.4.7

## 相关技术
 - scrapy
 - flask
 - Material Design Lite
 - vue

## 部署
安装python环境
http://www.runoob.com/python3/python3-tutorial.html

安装mongodb环境，可参考以下链接，使用默认端口27017
http://www.runoob.com/mongodb/mongodb-tutorial.html

```
git clone https://github.com/guanpengchn/github-popular.git
pip install -r requirements.txt
python app.py
``` 

访问浏览器
http://locolhost:5000

## 目录结构
├── README.md                   // help
├── app.py                      // web入口
├── requirements.txt            // python相关依赖
├── scrapy.cfg                  // scrapy配置文件
├── startSpider.py              // 开启爬虫脚本
├── templates                   // 页面模板
├── static                      // 静态资源
├── popular                     // 爬虫
└── doc                         // 相关文档

## 效果
mongodb中会生成
db名为popular，collection名为trending的数据
存储了从
https://github.com/trending
获取的数据
最后在网页上进行分析显示

![image](https://github.com/guanpengchn/github-popular/doc/content.png)
