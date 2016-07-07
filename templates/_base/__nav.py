(
	("Home", ("home", "index.html", [])),
	("Components", ("components", "components.html", (
		("Network Graph", ("component", "all_components.html")),
	))),
	("Interactions", ("interactions", "interactions.html", [])),
	("Associations", ("associations", "associations.html", (
		{% for typ_ in config.typs %}
			("{{ config.typs[typ_] }}", ("{{ typ_ }}", "associations/{{ uri }}_{{ typ_ }}.html")),
		{% endfor %}
	))),
	("Predictions", ("predictions", "predictions.html", (
		("Process", ("process", "predictions/process.html")),
		("Intrinsic", ("intrinsic", "predictions/intrinsic.html")),
		("Associated", ("associated", "predictions/associated.html")),
		("All Components", ("all_components", "predictions/all_components.html")),
	))),
	("Downloads", ("downloads", "downloads.html", [])),
	("Contact", ("contact", "contact.html", [])),
)
