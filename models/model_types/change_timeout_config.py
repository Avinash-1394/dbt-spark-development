def model(dbt, spark_session):
    dbt.config(materialized="table", timeout=15)

    data = [(1,), (2,), (3,), (4,)]

    df = spark_session.createDataFrame(data, ["A"])

    return df
