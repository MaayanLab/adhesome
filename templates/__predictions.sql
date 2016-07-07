{% set substitutions %} {
	"preds": "[[ '%0.3f'|format(preds) ]]",
	"probas": "[[ '%0.3f'|format(probas) ]]"
} {% endset %}
{{ config.cur|query("select * from `predictions`")|apply(substitutions) }}
