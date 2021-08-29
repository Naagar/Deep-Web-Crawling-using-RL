Deep-Deep: Adaptive Crawler
===========================

## stopword.txt for the English texts

Deep-Deep is a Scrapy-based crawler which uses Reinforcement Learning methods
to learn which links to follow.

It is called Deep-Deep, but it doesn't use Deep Learning, and it is not only
for Deep web. Weird.

For keywords and relevancy crawlers, the following files will be created
in the result folder:

Presentation   
------------

 RL_WebCrawling_Presentation.pptx

Running
-------

In order to run the spider, you need some seed urls and a relevancy function
that will provide reward value for each crawled page. There are some scripts
# start a crawl where reward is given by a classifier that returns a score with textt match (wiki and NVD) method.

Requirements
------------

requirement.txt



Main Notebook
-------------
'ir_security_risk_ver_8.py' # .ipynb for Jupytor notebook

For headless browser run
    --------
'web_scrapping_headless.py'



Using trained model
-------------------

You can use deep-deep to just run adaptive crawls, updating link model and
collecting crawled data at the same time. But in some cases it is more
efficient to first train a link model with deep-deep, and then use this model
in another crawler. Deep-deep uses a lot of memory to store page and link features, and more CPU to update the link
model. So if the link model is general enough to freeze it, you can run
a more efficient crawl. Or you might want to just use deep-deep link model
in an existing project.

Note that in order to use default scrapy
queue, a float link score is converted to an integer priority value.

Note that in some rare cases the model might fail to generalize from
the crawl it was trained on to the new crawl.


Model explanation
-----------------

get_urls.py

get_reward.py

main.py

can save a model explanation to pickle, html,
or print it in the terminal. But it is hard to analyze because character
ngram features are used.

will produce an html file for each
crawled page, where explanations for all link scores will be shown.


Testing
-------

To run tests (A2C),  execute the following command from the
        ----------

'A2C_test_3.py'

