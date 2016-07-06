{% set substitutions %} {
	"file": "<a href='{{ config.base }}/[[ url ]]'>[[ file ]]</a>",
	"url": ""
} {% endset %}
{{ config.cur|query("select * from `downloads`")|apply(substitutions) }}
