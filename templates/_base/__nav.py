(
	("Home", ("home", "index.html", [])),
	("Components", ("components", "components.html", {{ evaluate("components/__nav.py") }})),
	("Interactions", ("interactions", "interactions.html", [])),
	("Associations", ("associations", "associations.html", {{ evaluate("associations/__nav.py", subpage=subpage, uri=uri) }})),
	("Predictions", ("predictions", "predictions.html", {{ evaluate("predictions/__nav.py") }})),
	("Downloads", ("downloads", "downloads.html", [])),
	("Contact", ("contact", "contact.html", [])),
)
