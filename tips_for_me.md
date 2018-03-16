full.py文件的改进工作
- 从research下来菜单读取研究类型，后面就可以自动爬了
- 那么自动爬，就每一页都需要判断是否遇上`<title>Page not found - Williams InstituteWilliams Institute</title>`
  ` import requests
    import re
    
    url = 'https://williamsinstitute.law.ucla.edu/category/research/***/page/***'
    html = requests.get(url)
    if re.search(r'<title>Page not found', html.txt) != None
      then start collecting
      else goto another category`
  ——话说Python有`return`这种东西吗
- 页面有pdf文件则记录并下载
- 文件编码
  * Python 3 里面直接是 `open('filename.txt', 'a', encoding = 'uft-8')`
  * Python 2 则是
   ` import sys
     reload(sys)
     sys.setdefauldencoding('utf-8')`
