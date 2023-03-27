import pandas as pd


def model(dbt, session):
    dbt.config(materialized="incremental")
    df = dbt.ref("model")

    if dbt.is_incremental:
        max_from_this = f"select max(run_date) from {dbt.this}"
        df = df.filter(df.run_date >= session.sql(max_from_this).collect()[0][0])

    return df
