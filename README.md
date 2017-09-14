## 介绍
该项目使用了scrapy爬虫，爬取github中最流行的项目，并进行语言排名

## 使用
```
git clone https://github.com/guanpengchn/github-popular.git
scrapy crawl popular -o items.json
``` 

## 效果
会在根目录写入github.com.html和items.json文件，保存了获取到的信息
