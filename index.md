---
layout: index
title: lisblog
author: tonie
---
<h3>欢迎到GitHub Pages.</h3>
<!---
<table>
	<tr><td>asd</td></tr>
	<tr><td>qwe</td></tr>
</table>

	<pre>
		<code>
			$ cd your_repo_root/repo_name
			$ git fetch origin
			$ git checkout gh-pages
		</code>
	</pre>

someasdiw
<img src="images/sprite_download.png" style="height:100px;width:100px" />--->

<h3>最近的</h3>
<table>
{% for post in site.posts limit: 6 %}
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
<br/>
{% for post in site.posts limit: 2 %}

> {{ post.content | truncate: 300 }}
<br/>

{% endfor %}

> [View More LISblogs In LISt.]({{ site.baseurl }}cat.html)
--------------------------------------------------
