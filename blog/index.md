---
layout: default
title: Blog
permalink: /blog/
---
<section class="blog-index">
  <h2>Neueste Beiträge</h2>
  <ul class="blog-index__list">
    {% for post in site.posts %}
      <li class="blog-index__item">
        <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
        <span class="blog-index__meta">{{ post.date | date: '%d.%m.%Y' }}</span>
        <p class="blog-index__excerpt">{{ post.excerpt | strip_html | truncate: 200 }}</p>
      </li>
    {% endfor %}
  </ul>
</section>
