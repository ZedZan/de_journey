{{
    config(
        materialized='incremental',
        unique_key='customer_name'
    )
}}

with base as (
    select * from {{ ref('stg_sales') }}

    {% if is_incremental() %}
        where loaded_at > (select max(loaded_at) from {{ this }})
    {% endif %}
)

select
    customer_name,
    SUM(sale_amount) as total_amount,
    COUNT(sale_id) as sum_transactions
from base
group by customer_name