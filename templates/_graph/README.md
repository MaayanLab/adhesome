# Graph

Templates for creating a cytoscape node graph.

## Arguments

```
graph: {
	"nodes": [],
	"edges": []
}
```

## Components

`head`: `{{ include("_graph/head.html") }}`
`body`: `{{ include("_graph/_body.html", graph={{path}}, style="") }}`
`json`: `{{ include("_graph/_json.json", graph=graph) }}`
`scripts`: `{{ include("_graph/_scripts.html", graph={{path}}) }}`

## Extra requirements

Graph expects a json `{{path}}_graph.json` (you can generate this using the `json` component)
