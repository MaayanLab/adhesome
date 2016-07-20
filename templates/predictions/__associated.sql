{% set substitutions %} {
	"genesym": "<a href='{{ config.base }}/components/[[ genesym ]].html'>[[ genesym ]]</a>"
} {% endset %}
{{ config.cur|query("select * from `predictions_out` where GeneSym in (select `Official Symbol` from `components` where `FA`='Associated Proteins')")|apply(substitutions) }}
