{% set substitutions %} {
	"dataset": "<a href='{{ base }}/associations/[[ urlize(dataset) ]]_prot_att.html'>[[ dataset ]]</a>"
} {% endset %}
{% set cur = get_cursor() %}
{{ cur|query("select `Name` as `Dataset` from `datasets`")|apply(substitutions) }}
