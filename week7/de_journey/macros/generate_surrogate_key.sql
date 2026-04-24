{% macro generate_surrogate_key(column_names) %}
    MD5(CAST(
        {{ column_names | join(" || '-' || ") }}
    AS STRING))
{% endmacro %}