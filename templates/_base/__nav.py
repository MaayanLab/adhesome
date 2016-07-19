(
	("Introduction", ("introduction", "index.html", [])),
	("Components", ("components", "components.html", [])),
	("Interactions", ("interactions", "interactions.html", {{ evaluate("components/__nav.py") }})),
	("Associations", ("associations", "associations.html", {{ evaluate("associations/__nav.py", subpage=subpage, uri=uri) }})),
	("Predictions", ("predictions", "predictions.html", {{ evaluate("predictions/__nav.py") }})),
	("Downloads", ("downloads", "downloads.html", [])),
)
