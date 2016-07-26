# Table

Templates for creating a DataTable.

## Arguments

```
table: {
	"header": ['Your', 'Headers', 'Here'],
	"data": [(1,2,3),(4,5,6)],
	"order": "[[ 1, \"desc\" ]]"
}
```

## Components

`head`: `{{ include("_table/head.html") }}`
`body`: `{{ include("_table/_body.html", table=path) }}`
`csv`: `{{ include("_table/_csv.csv", table=table) }}`
`json`: `{{ include("_table/_json.json", table=table) }}`
`scripts`: `{{ include("_table/_scripts.html", table=table) }}`

## Extra requirements

Table expects a json `{{path}}_table.json` (you can generate this using the `json` component)
