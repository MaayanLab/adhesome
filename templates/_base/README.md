# Base

Main page template: content available on all pages, layout and navigation.

This module is designed to be extended from base.

```
{% set page = "home" %}
{% extends "_base/_base.html" %}
{% block head %}{% endblock %}
{% block body %}{% endblock %}
{% block scripts %}{% endblock %}
```

## Arguments

`page`: Defines the current page uri, for nav selection
`title`: Page title, defaults to capitalized version of uri

## Blocks

`head`: Whatever extra you want to put in the head tag
`body`: Whatever you want as the content
`scripts`: Whatever extra scripts you want
