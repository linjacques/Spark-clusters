def read_data(spark, path):
    return spark.read.csv(path, header=True, inferSchema=True)

def write_data(df, path):
    df.write.csv(path, mode="overwrite")
