{% set cur = get_cursor() %}
{{ cur|query("select * from `predictions`") }}
