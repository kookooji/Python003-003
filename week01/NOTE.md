学习笔记
反思：
通过本周的学习，让我更清楚的认识了自己的不足（太菜了）。特别是在写作业的时候，有时候写个for循环，逻辑总弄错，花了好长时间调试。还是得多练，自己之前比较懒，练的比较少，写的很不顺手。基础也要加强。

收获：
1、又复习了一遍git的基本操作和流程（git init->git remote add origin git@github.com:xxse/xx.git->git --config global 参数名 参数值-> git clone -> 编写代码->git add. ->git commit -m "" ->git push -u origin）
2、requests库的基本操作（requests.get()）
3、bs4的应用。BeautifulSoup(response.text.'html.paser')，find_all('tag_name',attrs={'attr':value})，find_all方法在遇到多个标签相同的情况下，还可以加limit参数，并使用下标（从0开始）获取特定位置标签内置的属性（text等）“urls.find_all('li',limit=3)[2].text”
4、Scrapy框架的使用
核心组件：引擎（engine），调度器（），爬虫（），下载器，管道，
自己理解的每一个组件的作用
引擎的作用：负责数将据流交给某一个组件处理。例如request请求交给调度器，reponse交给爬虫解析。
调度器：将请求压入栈中，提交给引擎，再由引擎提交给下载器
下载器：处理Request请求，下载资源，并通过下载中间件，最后通过下载中间件将reponse响应提交给引擎
爬虫：发起请求，对response进行解析，提取数据
管道：pipeline和items。在爬虫程序中，items中将需要提取的数据定义成Scrapy.Field()。然后爬虫将item提交到pipeline中，对数据进行清洗，存取。




