# cqsdx_video_watching
自动观看cqsdx视频

本工具使用[Apache2.0开源](https://github.com/azkbbys/cqsdx_video_watching/blob/main/LICENSE)
## 前置准备
* 下载本工具源码
* 在[python官网](https://python.org)下载python3.x版本
* 在`cmd`中运行`pip install requests`，等待下载完成
## 使用方法
* 先进入观看视频页面，按下`Ctrl`+`Shift`+`I`或`F12`打开浏览器开发者工具，选择`网络`或`Network`选项卡，等待视频自行播放2分钟，等待新的名为`saveTime`的项目出现
* 往下翻找到`cookie`一栏，复制右侧内容，粘贴到`index.py`的cookie中，**不要删除原有的前后单引号**
* 浏览器的`saveTime`中找到`负载`选项卡，将`id`的值复制到`index.py`的id变量中，**不要删除原有的前后单引号**
* 保存后运行`index.py`即可，等待时间等于原视频时长
* 等待刷完后，手动在浏览器中使用倍速插件播放到视频最后，点击完成即可
