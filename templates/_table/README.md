# Table

Templates for creating a DataTable.

## Arguments

```
table: {
	"header": ['Your', 'Headers', 'Here'],
	"data": [(1,2,3),(4,5,6)]
}
```

## Components

`head` (no arguments): `{% include "_table/head.html" %}`
`body` (table = {{path}}): `{% include "_table/_body.html" %}`
`csv` (requires arguments): `{% include "_table/_csv.csv" %}`
`json` (requires arguments): `{% include "_table/_json.json" %}`
`scripts` (table = {{path}}): `{% include "_table/_scripts.html" %}`

## Extra requirements

Table expects a json `{{path}}_table.json` (you can generate this using the `json` component)
