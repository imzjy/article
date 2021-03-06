<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="//cdn.staticfile.org/twitter-bootstrap/3.3.1/css/bootstrap.css" rel="stylesheet">
    <link href="//cdn.staticfile.org/font-awesome/4.2.0/css/font-awesome.css" rel="stylesheet">
    <link href="//cdn.staticfile.org/fontdiao/0.0.8/css/fontdiao.css" rel="stylesheet">
    <title>博客文章 - 周继元</title>
    <style type="text/css">
    .article-list li {
        margin-bottom: 15px;
    }
    .article-list small {
        color: silver;
        margin-left: 10px;
    }
    .rss {
        font-size: 16px;
        margin-top: 20px;
    }
    </style>
</head>

<body>
    <div class="container">
        <div class="row">
            <div class="col-md-offset-2 col-md-8">

                <header class="page-header">
                    <h1>周继元的博客 <small class="pull-right rss"><a href="/rss.xml" target="_blank">RSS</a></small> </h1>
                </header>

                <section>
                    <div>
                        <ul class="article-list list-unstyled">
                            ${aritcle_list}
                        </ul>
                    </div>
                </section>

                <footer>
                    <!--Links -->
                    <ul class="list-inline">
                        <li>
                            <a href="http://blog.imzjy.com" target="_blank">
                                <i class="fa fa-rss fa-lg"></i>
                            </a>
                        </li>
                        <li>
                            <a href="https://github.com/imzjy" target="_blank">
                                <i class="fa fa-github-square fa-lg"></i>
                            </a>
                        </li>
                        <li>
                            <a href="http://www.flickr.com/photos/jatsz" target="_blank">
                                <i class="fa fa-flickr fa-lg"></i>
                            </a>

                        </li>
                        <li>
                            <a href="http://book.douban.com/people/jcu" target="_blank">
                                <i class="fa icon-douban fa-lg"></i>
                            </a>
                        </li>
                        <li>
                            <a href="http://www.linkedin.com/pub/jerry-chou/49/462/633" target="_blank">
                                <i class="fa fa-linkedin-square fa-lg"></i>
                            </a>
                        </li>
                        <li>
                            <a href="mailto:imjatsz@gmail.com" target="_blank">
                                <i class="fa fa-envelope-o fa-lg"></i>
                            </a>
                        </li>
                        <li class="pull-right fa-lg">
                            <span>zjy@2015</span>
                        </li>
                    </ul>
                </footer>
            </div>
        </div>
    </div>
</body>
</html>
