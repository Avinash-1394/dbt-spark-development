def model(dbt, spark_session):
    dbt.config(
        materialized="table",
        table_type="iceberg",
        on_schema_change='append_new_columns',
        format="parquet",
        polling_interval=5,  # in seconds
        timeout=100,  # time out in seconds
        table_properties={
            "format-version": "2"
        },
        engine_config={
            "CoordinatorDpuSize": 1,
            "MaxConcurrentDpus": 2,
            "DefaultExecutorDpuSize": 1,
        }
    )

    import time
    
    time.sleep(15)
    data = [(1, "a"), (2, "b"), (3, "c")]
    cols = ["num", "alpha"]
    df = spark_session.createDataFrame(data, cols)

    return df
