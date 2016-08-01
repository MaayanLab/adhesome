{% set substitutions %} {
	"name": "<a href='{{ config.base }}/associations/[[ name|urlize ]]_prot_prot.html'>[[ name ]]</a>"
} {% endset %}
{{ config.cur|query("select `Name`, `Description` from `datasets`")|apply(substitutions) }}
