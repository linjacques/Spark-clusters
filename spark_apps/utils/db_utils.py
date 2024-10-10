def get_postgres_connection_properties():
    jdbc_url = "jdbc:postgresql://<host>:<port>/<database>"
    
    properties = {
        "user": "<username>",
        "password": "<password>",
        "driver": "org.postgresql.Driver"
    }

    return jdbc_url, properties
