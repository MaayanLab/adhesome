{% set cur = get_cursor() %}
{% set substitutions %} {
	"source": "<a href='{{ base }}/components/[[ source ]].html'>[[ source ]]</a>",
	"target": "<a href='{{ base }}/components/[[ target ]].html'>[[ target ]]</a>",
	"pmid": "<span style='white-space: nowrap'>[% for i in pmid.split(' ') %] <a href='http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=pubmed&dopt=Abstract&list_uids=[[ i ]]'><img src='{{ base }}/images/ncbi.png' alt='View PubMed Article ([[ pmid ]])' /></a>&nbsp;[% endfor %]</span>"
} {% endset %}
{% if name %}
	{{ cur|query("select * from `interactions` where `Source`=? or `Target`=?", name, name)|apply(substitutions) }}
{% else %}
	{{ cur|query("select * from `interactions`")|apply(substitutions) }}
{% endif %}
