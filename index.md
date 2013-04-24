---
layout: index
title: lisblog
author: tonie
---

{% for post in site.posts limit: 2 %}

> {{ post.content}}
</br>

{% endfor %}

<br/>

<h3>最近的</h3>

{% for post in site.posts limit: 5 %}
+ <a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a>
  <label>{{ post.date | date_to_string }}</label>
{% endfor %}


> [View More LISblogs In LISt.]({{ site.baseurl }}cat.html)
-----------------------------------------------------------
