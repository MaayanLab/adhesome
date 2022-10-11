{% set predictions_query %}
	select
		`GeneSym`,
		printf("%0.3f", `Out of Fold Probability`) as `Probability`,
		`GeneSym` as `Links`
	from `predictions`
	where
		`Known` = 0
	and `Out of Fold Prediction` = 1
	and `Model` = "associated";
{% endset %}
{% set substitutions %} {
	"links": "<span style='white-space: nowrap;'><a href='{{ config.harmonizome_base }}/gene/[[ genesym ]]' target=_blank><img src='{{ config.base }}/images/harmonizome.png' alt='View on Harmonizome'></a>&nbsp;<a href='https://www.genecards.org/cgi-bin/carddisp.pl?gene=[[ genesym ]]' target=_blank><img src='{{ config.base }}/images/genecards.png' alt='View on GeneCards'></a>&nbsp;<a href='https://www.ncbi.nlm.nih.gov/gene/?term=[[ genesym ]]' target=_blank><img src='{{ config.base }}/images/ncbi.png' alt='View on NCBI'></a></span>"
} {% endset %}
{{ config.cur|query(predictions_query)|apply(substitutions) }}
