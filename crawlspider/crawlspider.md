#### 1.creat crawlspider
```shell
scrapy startproject demo
cd demo
scrapy genspider -t crawl demo_spider www.baidu.com

%% execute
scrapy crawl demo_spider
```

#### 2.settings.py
```python
ROBOTSTXT_OBEY = FALSE

USER_AGENT: 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'

DOWNLOAD_DELAY = 1

LOG_LEVEL = 'ERROR'
```

#### 3.start.py
```python
from scrapy import cmdline

cmdline.execute("scrapy crawl demo_spider".split())
```

<++>
