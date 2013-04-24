---
layout: index
title: All LISblog
author: tonie
---
<a id="forkme_banner" href="/">Home Page</a>
{% include div_left.textile %}
  {% for post in site.posts %}
    <li>
      <a href="{{site.baseurl}}{{post.url}}">{{ post.title }}</a>
      <ul>
        <li>
          {{ post.date | date_to_string }}
        </li>
      </ul>
    </li>
  {% endfor %}
{% include div_right.textile %}
