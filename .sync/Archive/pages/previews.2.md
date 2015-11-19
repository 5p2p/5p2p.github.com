---
title: Previews
type: previews
permalink: previews/
---

    {% for post in site.pages %}
        {% if post.preview %}

        <div class="postTitle"><a href="{{ post.url }}">{{ post.title }}</a></div>
        <div class="postStats">
        <div class="postPath"><i class="fa fa-folder-open" style="margin-right: 0.1rem;"></i> {{post.path}}</div>
        <i class="fa fa-clock-o"></i>
            {% if post.tag %}
            <div class="tags">
            <i class="fa fa-tag"></i>
            {% for tag in post.tag %}
                <a href="/{{tag}}" class="nobold">{{tag}}</a>
            {% endfor %}
            </div>
            {% endif %}
        </div>


        {% endif %}

    {% endfor %}