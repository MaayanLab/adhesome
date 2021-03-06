{% set node_view %}
	create temp view `nodes_all` as
	select
		`components`.`Official Symbol`,
		`components`.`FA`,
		`neighbors`.`Neighbors`*1.0/(select max(`neighbors`.`Neighbors`) from `neighbors`)
	from `components`
	left join `neighbors`
	on `components`.`Official Symbol` = `neighbors`.`Official Symbol`
	where `neighbors`.`Neighbors` not null;
{% endset %}
{% set edge_view %}
	create temp view `edges_all` as
	select
		`Source`,
		`Target`,
		`PMID`
	from `edges`
	where
		`Source` in (select `Official Symbol` from `nodes_all`)
	and `Target` in (select `Official Symbol` from `nodes_all`);
{% endset %}
{% set res = config.cur|query_exec(node_view.format(name)), config.cur|query_exec(edge_view.format(name)) %}
{
	'nodes': {{ (config.cur|query("select * from `nodes_all`")).data }},
	'edges': {{ (config.cur|query("select * from `edges_all`")).data }}
}
{% set res = config.cur|query_exec("drop view `nodes_all`"), config.cur|query_exec("drop view `edges_all`") %}
