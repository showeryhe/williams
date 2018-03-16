full.py文件的改进工作
- 从research下来菜单读取研究类型，后面就可以自动爬了
- 那么自动爬，就每一页都需要判断是否遇上`<title>Page not found - Williams InstituteWilliams Institute</title>`——话说Python有`return`这种东西吗
- 页面有pdf文件则记录并下载
