{% set cur = get_cursor() %}
{% set node_view %}
	create temp view `nodes_{0}` as
	select
		`components`.`Official Symbol`,
		`components`.`FA`,
		`neighbors`.`Neighbors`*1.0/(select max(`neighbors`.`Neighbors`) from `neighbors`)
	from `components`
	left join `neighbors`
	on `components`.`Official Symbol`=`neighbors`.`Official Symbol`
	where `neighbors`.`Neighbors` not null
	and (`components`.`Official Symbol`="{0}"
	or `components`.`Official Symbol` in (
		select `Target`
		from `edges`
		where `Source`="{0}")
	or `components`.`Official Symbol` in (
		select `Source`
		from `edges`
		where `Target`="{0}"));
{% endset %}
{% set edge_view %}
	create temp view `edges_{0}` as
	select
		`Source`,
		`Target`,
		`PMID`
	from `edges`
	where
		`Source` in (select `Official Symbol` from `nodes_{0}`)
	and `Target` in (select `Official Symbol` from `nodes_{0}`);
{% endset %}
{% set res = cur|query_exec(node_view.format(name)), cur|query_exec(edge_view.format(name)) %}
{
	'nodes': {{ (cur|query("select * from nodes_{0}".format(name))).data }},
	'edges': {{ (cur|query("select * from edges_{0}".format(name))).data }}
}
{% set res = cur|query_exec("drop view `nodes_{0}`".format(name)), cur|query_exec("drop view `edges_{0}`".format(name)) %}
