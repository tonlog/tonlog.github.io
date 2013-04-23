---
layout: index
title: lisblog
author: tonie
---
<h3>欢迎到GitHub Pages.</h3>

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
<img src="images/sprite_download.png" style="height:100px;width:100px" />

<br/>
{% for post in site.posts %}

> [{{ post.title }}]({{ site.baseurl }}{{ post.url }})

{% endfor %}

