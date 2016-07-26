# Clustergrammer

Templates for passing a clustergrammer.

## Arguments

```
clustergrammer: {
	"title": "Your title here",
	"uri": "your_uri_here",
	"description": "Your long description here"
}
```

## Components

`head`: `{{ include("_clustergrammer/_head.html") }}`
`body`: `{{ include("_clustergrammer/_body.html", clustergrammer=clustergrammer) }}`
`scripts`: `{{ include("_clustergrammer/_scripts.html", clustergrammer=clustergrammer) }}`

## Extra requirements

Clustergrammer expects a json `{{uri}}.json` with a clustergrammer generated json.
See `/process/process_matrix.py` for more information.
