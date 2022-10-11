{% set substitutions %} {
	"official_symbol": "<a href='{{ config.base }}/interactions/[[ official_symbol ]].html'>[[ official_symbol ]]</a>",
	"links": "<span style='white-space: nowrap;'><a href='https://www.uniprot.org/uniprot/[[ swiss_prot_id ]]' target=_blank><img src='{{ config.base }}/images/swiss_prot.png' alt='View on UniProt'></a>&nbsp;<a href='{{ config.harmonizome_base }}/gene/[[ official_symbol ]]' target=_blank><img src='{{ config.base }}/images/harmonizome.png' alt='View on Harmonizome'></a>&nbsp;<a href='https://www.genecards.org/cgi-bin/carddisp.pl?gene=[[ official_symbol ]]' target=_blank><img src='{{ config.base }}/images/genecards.png' alt='View on GeneCards'></a>&nbsp;<a href='https://www.ncbi.nlm.nih.gov/gene/[[ gene_id ]]' target=_blank><img src='{{ config.base }}/images/ncbi.png' alt='View on NCBI'></a></span>",
	"swiss_prot_id": "",
	"gene_id": ""
} {% endset %}
{{ config.cur|query("select *, `Official Symbol` as `Links` from `components`")|apply(substitutions) }}
