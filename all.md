---
layout: index
title: All LISblog
author: tonie
---
<a id="forkme_banner" href="/">Home Page</a>
{% include div_left.textile %}
  <ul>
  {% for post in site.posts %}
    <li>
      <a href="{{site.baseurl}}{{post.url}}">{{ post.title }}</a>
      <ul>
        <li style="list-style:none;">
          written @{{ post.date | date_to_string }} 
          {% if post.tags.size > 0 %}
            with tags: 
            {% for tag in post.tags %}
              {{ tag }}
            {% endfor %}
          {% endif %}
        </li>
      </ul>
    </li>
  {% endfor %}
  </ul>
{% include div_right.textile %}
