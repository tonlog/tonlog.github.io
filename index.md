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

{% for post in site.posts limit: 2 %}
<hr/>
> 我的LISt:
  <li>
    {% for tag in post.tags %}
    {{ tag }}
    {% endfor %}
  </li>
> {{ post.content }}
</br>

<hr/>
{% endfor %}

<br/>


<label>
> [View More LISblogs In LISt.]({{ site.baseurl }}all.html)
-----------------------------------------------------------

</label>
