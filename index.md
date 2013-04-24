---
layout: index
title: lisblog
author: tonie
---
<h3>欢迎到GitHub Pages.</h3>

{% for post in site.posts limit: 2 %}

> {{ post.content}}
</br>
-------------------------------

{% endfor %}
<br/>

<h3>最近的</h3>
<table>
{% for post in site.posts limit: 5 %}
<tr>
	<td>
		<a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a>
	</td>
	<td>
		<label>{{ post.date | date_to_string }}</label>
	</td>
</tr>

{% endfor %}
</table>

> [View More LISblogs In LISt.]({{ site.baseurl }}cat.html)
-----------------------------------------------------------
