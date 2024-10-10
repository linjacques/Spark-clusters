from spark_apps.jobs import job_data_processing, job_data_analysis
from spark_apps.config.spark_config import create_spark_session

def main():
    spark = create_spark_session()

    job_data_processing.run(spark)

    job_data_analysis.run(spark)

    spark.stop()


if __name__ == "__main__":
    main()
