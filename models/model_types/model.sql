{{ config(materialized="table") }}
select 1 as column_1, 2 as column_2, '{{ run_started_at.strftime("%Y-%m-%d") }}' as run_date