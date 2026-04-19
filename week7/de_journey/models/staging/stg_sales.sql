with source as (
    select * from {{ source('de_journey_dw', 'sales') }}
),

renamed as (
    select
        id          as sale_id,
        name        as customer_name,
        sales       as sale_amount,
        date        as sale_date,
        loaded_at
    from source
)

select * from renamed