{% set cur = get_cursor() %}
{% set substitutions %} {
	"file": "<a href='{{ base }}/[[ url ]]'>[[ file ]]</a>",
	"url": ""
} {% endset %}
{% set cur = get_cursor() %}
{{ cur|query("select * from `downloads`")|apply(substitutions) }}
