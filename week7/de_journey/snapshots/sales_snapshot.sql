{% snapshot sales_snapshot %}

{{
    config(
        target_schema = 'snapshots',
        unique_key = 'id',
        strategy = 'timestamp',
        updated_at = 'loaded_at',
    )
}}

select * from {{ source('de_journey_dw', 'sales') }}

{% endsnapshot %}