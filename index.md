---
layout: index
title: lisblog
author: tonie
---


<h3>最近的</h3>

{% for post in site.posts limit: 5 %}
+ <a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a>
  <label>{{ post.date | date_to_string }}</label>
{% endfor %}

{% for post in site.posts limit: 2 %}

> {{ post.content}}
</br>

{% endfor %}

<br/>

> [View More LISblogs In LISt.]({{ site.baseurl }}cat.html)
-----------------------------------------------------------
