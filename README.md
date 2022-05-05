# twitterbot 文件说明  
twitter_bot.py 表示需要运行的推特bot脚本，包含基本功能（跳转需要操作的推特链接，进行一键三联操作），可批量账号操作  
user.txt 包含两列数值，一列用户名、一列推文回复内容（一行表示一个用户）  
set.json 包含两个key，一个baseUrl（无需调整），tg_url修改为需要三连的推文链接  
cookies 里面放置用户的cookie信息，具体cookie的导出需要用到edit this cookie，可参考https://jingyan.baidu.com/article/6d704a13f7aa1428da51ca7e.html  

# 注意：  
selenium需要单独安装（pip install selenium）  
chromedriver.exe 需要去官网单独下载，并放置在twitter_bot.py的同级目录下  

需完善点（希望各位大佬继续完善代码）：  
1、follow功能未补充  
2、未设置每个用户单独ip、模拟浏览器  
3、未判断每个推文之前是否三连过，如果重复对一个推文进行操作，可能导致点赞失效（已点赞后取消点赞）  
