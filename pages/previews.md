---
title: Previews
permalink: previews/
---

{% for post in site.pages %}
{% if post.preview %}
<div class=""><a href="{{ post.url }}">{{ post.title }}</a></div>
{% endif %}
{% endfor %}