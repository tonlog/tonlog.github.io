---
layout: index
title: lisblog
author: tonie
---


<h4>最新速递</h4>

{% for post in site.posts limit: 5 %}
+ <a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a>
  <label>{{ post.date | date_to_string }}</label>
{% endfor %}

> 我的LISt:

{% for post in site.posts limit: 2 %}

> {{ post.content | truncate: 100}}
</br>

{% endfor %}

<br/>

> [View More LISblogs In LISt.]({{ site.baseurl }}cat.html)
-----------------------------------------------------------
