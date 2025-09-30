---
layout: default
title: Kategorien
permalink: /blog/categories/
---
<section class="blog-categories">
  <h2>Kategorien</h2>
  <ul class="blog-categories__list">
    {% assign grouped = site.posts | group_by_exp: 'post', 'post.categories | join: ","' %}
    {% for group in grouped %}
      {% assign categories = group.name | split: ',' %}
      <li class="blog-categories__item" id="{{ categories | join: '-' }}">
        <h3 class="blog-categories__title">{{ categories | join: ', ' }}</h3>
        <ul class="blog-categories__posts">
          {% for post in group.items %}
            <li><a href="{{ post.url | relative_url }}">{{ post.title }}</a> · {{ post.date | date: '%d.%m.%Y' }}</li>
          {% endfor %}
        </ul>
      </li>
    {% endfor %}
  </ul>
</section>
