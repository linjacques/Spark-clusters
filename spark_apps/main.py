from spark_apps.jobs import job_postgres_to_hdfs
from spark_apps.config.spark_config import create_spark_session

def main():

    spark = create_spark_session()

    # Exécuter le job pour extraire de PostgreSQL et charger vers HDFS
    job_postgres_to_hdfs.run(spark)

    spark.stop()

if __name__ == "__main__":
    main()
