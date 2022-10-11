{% set substitutions %} {
	"source": "<a href='{{ config.base }}/interactions/[[ source ]].html'>[[ source ]]</a>",
	"target": "<a href='{{ config.base }}/interactions/[[ target ]].html'>[[ target ]]</a>",
	"pmid": "<select onchange='window.open(this.options\\[this.selectedIndex\\].value,\"_blank\")'><option value=''>Source Article(s)</option>[% for i in pmid.split(' ') %]<option value='https://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=pubmed&dopt=Abstract&list_uids=[[ i ]]'>[[ i ]]</option>[% endfor %]</select>"
} {% endset %}
{% if name %}
	{{ config.cur|query("select * from `interactions` where `Source`=? or `Target`=?", name, name)|apply(substitutions) }}
{% else %}
	{{ config.cur|query("select * from `interactions`")|apply(substitutions) }}
{% endif %}
