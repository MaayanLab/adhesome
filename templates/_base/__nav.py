(
	("Home", ("home", "index.html", [])),
	("Components", ("components", "components.html", {{ evaluate("components/__nav.py", subpage=subpage) }})),
	("Interactions", ("interactions", "interactions.html", [])),
	("Associations", ("associations", "associations.html", {{ evaluate("associations/__nav.py", subpage=subpage) }})),
	("Predictions", ("predictions", "predictions.html", {{ evaluate("predictions/__nav.py", subpage=subpage) }})),
	("Downloads", ("downloads", "downloads.html", [])),
	("Contact", ("contact", "contact.html", [])),
)
