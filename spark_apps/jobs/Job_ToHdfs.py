from pyspark.sql import SparkSession
from spark_apps.utils.db_utils import get_postgres_connection_properties

def run(spark: SparkSession):
    # Récupérer les propriétés de connexion PostgreSQL
    jdbc_url, properties = get_postgres_connection_properties()

    # Lire les données de PostgreSQL
    df = spark.read.jdbc(url=jdbc_url, table="public.my_table", properties=properties)

    # Afficher les premières lignes pour vérifier
    df.show()

    # Spécifier le chemin HDFS où les données doivent être écrites
    hdfs_path = "hdfs://namenode:9000/user/hadoop/my_table_data"

    # Écrire les données dans HDFS au format Parquet
    df.write.mode("overwrite").parquet(hdfs_path)
