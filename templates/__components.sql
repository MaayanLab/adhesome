{% set substitutions %} {
	"official_symbol": "<a href='{{ base }}/components/[[ official_symbol ]].html'>[[ official_symbol ]]</a>",
	"links": "<span style='white-space: nowrap;'><a href='http://www.uniprot.org/uniprot/[[ swiss_prot_id ]]'><img src='{{ base }}/images/swiss_prot.png'></a>&nbsp;<a href='http://amp.pharm.mssm.edu/Harmonizome/gene/[[ official_symbol ]]'><img src='{{ base }}/images/harmonizome.png'></a>&nbsp;<a href='http://www.genecards.org/cgi-bin/carddisp.pl?gene=[[ official_symbol ]]'><img src='{{ base }}/images/genecards.png'></a>&nbsp;<a href='http://www.ncbi.nlm.nih.gov/gene/[[ gene_id ]]'><img src='{{ base }}/images/ncbi.png'></a></span>",
	"swiss_prot_id": "",
	"gene_id": ""
} {% endset %}
{% set cur = get_cursor() %}
{{ cur|query("select *, `Official Symbol` as `Links` from `components`")|apply(substitutions) }}
