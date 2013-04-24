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
 {% if post.tags.size > 0 %}
> 关于 
    {% for tag in post.tags %}
<a href="/tag.html#{{ tag }}">{{ tag }}</a>
    {% endfor %}
  :
  {% else %}
> 我的LISt:
  {% endif %}
> {{ post.content }}
</br>

<hr/>
{% endfor %}

<br/>


<label>
> [View More LISblogs In LISt.]({{ site.baseurl }}all.html)
-----------------------------------------------------------

</label>
