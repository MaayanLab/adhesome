{% set substitutions %} {
	"dataset": "<a href='{{ config.base }}/associations/[[ dataset|urlize ]]_prot_att.html'>[[ dataset ]]</a>"
} {% endset %}
{{ config.cur|query("select `Name` as `Dataset` from `datasets`")|apply(substitutions) }}
