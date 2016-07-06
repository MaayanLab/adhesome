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

`head` (no arguments): `{% include "_graph/head.html" %}`
`body` (graph = {{path}}, style=""): `{% include "_graph/_body.html" %}`
`json` (requires arguments): `{% include "_graph/_json.json" %}`
`scripts` (graph = {{path}}): `{% include "_graph/_scripts.html" %}`

## Extra requirements

Graph expects a json `{{path}}_graph.json` (you can generate this using the `json` component)
