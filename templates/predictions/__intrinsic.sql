{% set predictions_query %}
	select
		`GeneSym`,
		printf("%0.3f", `Out of Fold Probability`) as `Probability`,
		`GeneSym` as `Links`
	from `predictions`
	where
		`Known` = 0
	and `Out of Fold Prediction` = 1
	and `Model` = "intrinsic";
{% endset %}
{% set substitutions %} {
	"links": "<span style='white-space: nowrap;'><a href='http://amp.pharm.mssm.edu/Harmonizome/gene/[[ genesym ]]'><img src='{{ config.base }}/images/harmonizome.png' alt='View on Harmonizome'></a>&nbsp;<a href='http://www.genecards.org/cgi-bin/carddisp.pl?gene=[[ genesym ]]'><img src='{{ config.base }}/images/genecards.png' alt='View on GeneCards'></a>&nbsp;<a href='http://www.ncbi.nlm.nih.gov/gene/[[ genesym ]]'><img src='{{ config.base }}/images/ncbi.png' alt='View on NCBI'></a></span>"
} {% endset %}
{{ config.cur|query(predictions_query)|apply(substitutions) }}
