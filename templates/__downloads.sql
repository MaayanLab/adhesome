{% set substitutions %} {
	"file": "<a href='[[ url ]]' target=_blank>[[ file ]]</a>",
	"url": ""
} {% endset %}
{{ config.cur|query("select * from `downloads`")|apply(substitutions) }}
