{% set substitutions %} {
	"genesym": "[% if adhesome %]<a href='{{ config.base }}/components/[[ genesym ]].html'>[[ genesym ]]</a>[% else %][[ genesym ]][% endif %]",
	"adhesome": ""
} {% endset %}
{{ config.cur|query("select *, `GeneSym` in (select `Official Symbol` from `components`) as adhesome from predictions_out")|apply(substitutions) }}
