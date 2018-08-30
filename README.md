# douban_movie_250

本项目用于爬虫学习，包含多个爬取豆瓣电影250的玩具爬虫。

### 安装依赖（dependency）

  ```bash
  # 进入`douban-movie-250`根目录安装依赖
  bash install.sh
  ```
### 爬虫（crawler）

- beautifulsoup crawler: 使用beautifulsoup4及urllib

  ```bash
  # 进入`beautifulsoup`，爬取数据并打印最终结果
  python bs_movie250.py
  ```

- scrapy crawler: 使用scrapy爬虫框架

  ```bash
  # 进入`scrapy/movie250/movie250/run`，爬取数据
  bash run.sh
  # 处理爬到的数据，打印最终结果
  python output.py
  ```
- selenium crawler: 使用selenium及Chromedriver

  ```bash
  # 进入`selenium`，爬取并打印数据
  python test.py
  ```
