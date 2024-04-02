from typing import Any
from fastapi import FastAPI, Depends
from pyspark.sql import SparkSession

app = FastAPI()


# Dependency
def get_spark():
    return  SparkSession.builder.appName("fastapi-pyspark-demo01").getOrCreate()


@app.get("/", response_model=None)
def read_root(spark: SparkSession = Depends(get_spark)) -> Any:
    return {"status": "up", "spark": spark is not None}


@app.get("/items", response_model=None)
def read_items(spark: SparkSession = Depends(get_spark)) -> Any:
    df = (
        spark.read.format("csv")
        .option("header", "true")
        .option("inferSchema", "true")
        .load("/data/business-operations-survey-2023-business-practices.csv")
    )

    return {"items": df.take(10)}
