{% set substitutions %} {
	"file": "<a href='[[ url ]]'>[[ file ]]</a>",
	"url": ""
} {% endset %}
{{ config.cur|query("select * from `downloads`")|apply(substitutions) }}
