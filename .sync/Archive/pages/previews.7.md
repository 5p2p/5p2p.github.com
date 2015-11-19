---
title: Previews
permalink: putta/
---

    {% for post in site.pages %}
        <div> post.path </div>
        {% if post.preview %}

        <div class=""><a href="{{ post.url }}">{{ post.title }}</a></div>

        {% endif %}

    {% endfor %}