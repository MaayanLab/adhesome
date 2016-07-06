{% set intrinsic_view %}
	create temp view `intrinsic_nodes` as
	select *
	from `components`
	where `FA`="Intrinsic Proteins";
{% endset %}
{% set intrinsic_edges_query %}
	select count(*)
	from `edges`
	where `Source`=(select `Official Symbol` from `intrinsic_nodes`)
	or `Target`=(select `Official Symbol` from `intrinsic_nodes`);
{% endset %}
{% set associated_view %}
	create temp view `associated_nodes` as
	select *
	from `components`
	where `FA`="Associated Proteins";
{% endset %}
{% set associated_edges_query %}
	select count(*)
	from `edges`
	where `Source`=(select `Official Symbol` from `associated_nodes`)
	or `Target`=(select `Official Symbol` from `associated_nodes`);
{% endset %}
{% set res = config.cur|query_exec(intrinsic_view), config.cur|query_exec(associated_view) %}
{
	'all': {{ (config.cur|query("select count(*) from `components`")).data.0.0 }},
	'all_interactions': {{ (config.cur|query("select count(*) from `edges`")).data.0.0 }},
	'intrinsic': {{ (config.cur|query("select count(*) from `intrinsic_nodes`")).data.0.0 }},
	'associated': {{ (config.cur|query("select count(*) from `associated_nodes`")).data.0.0 }},
	'intrinsic_interactions': {{ (config.cur|query(intrinsic_edges_query)).data.0.0 }},
	'associated_interactions': {{ (config.cur|query(associated_edges_query)).data.0.0 }}
}
{% set res = config.cur|query_exec("drop view `intrinsic_nodes`"), config.cur|query_exec("drop view `associated_nodes`") %}
