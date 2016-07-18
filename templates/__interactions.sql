{% set substitutions %} {
	"source": "<a href='{{ config.base }}/components/[[ source ]].html'>[[ source ]]</a>",
	"target": "<a href='{{ config.base }}/components/[[ target ]].html'>[[ target ]]</a>",
	"pmid": "<select onchange='window.location=this.options\\[this.selectedIndex\\].value;'><option value=''>View PMID...</option>[% for i in pmid.split(' ') %]<option value='http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=pubmed&dopt=Abstract&list_uids=[[ i ]]'>[[ i ]]</option>[% endfor %]</select>"
} {% endset %}
{% if name %}
	{{ config.cur|query("select * from `interactions` where `Source`=? or `Target`=?", name, name)|apply(substitutions) }}
{% else %}
	{{ config.cur|query("select * from `interactions`")|apply(substitutions) }}
{% endif %}
