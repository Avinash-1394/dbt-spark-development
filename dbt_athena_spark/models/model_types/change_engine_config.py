def model(dbt, spark_session):
    dbt.config(
        materialized="table",
        engine_config={
            "CoordinatorDpuSize": 1,
            "MaxConcurrentDpus": 3,
            "DefaultExecutorDpuSize": 1,
        },
    )

    data = [(1,), (2,), (3,), (4,)]

    df = spark_session.createDataFrame(data, ["A"])

    return df
