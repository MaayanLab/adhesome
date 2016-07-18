(
	{% if subpage %}
		{% for typ_ in config.typs %}
			("{{ config.typs[typ_] }}", ("{{ typ_ }}", "associations/{{ uri }}_{{ typ_ }}.html")),
		{% endfor %}
	{% endif %}
)