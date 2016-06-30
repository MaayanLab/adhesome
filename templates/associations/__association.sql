{% set cur = get_cursor() %}
{{ (cur|query("select `{0}` from `datasets` where `Name`=?".format(typ), name)).data.0.0 }}
