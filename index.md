---
layout: default
title: lisblog
author: tonie
---


## {{ page.title }}

{{ page.tags }}


latest
=======

{{ page.author }}

{% for post in site.posts %}
+ {{ post.date | date_to_string }}
	[{{ post.title }}]({{ site.baseurl }}{{ post.url }})
{% endfor %} 