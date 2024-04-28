from playhouse.postgres_ext import PostgresqlExtDatabase


# If not using docker, you probably want to set this to "localhost"
ENV_VALUES = {
# POSTGRES_HOST:"postgres",
"POSTGRES_HOST":"localhost",
"POSTGRES_NAME":"jesse_db",
"POSTGRES_PORT":5432,
"POSTGRES_USERNAME":"jesse_user",
"POSTGRES_PASSWORD":"password"
}
db = PostgresqlExtDatabase(
            ENV_VALUES['POSTGRES_NAME'],
            user=ENV_VALUES['POSTGRES_USERNAME'],
            password=ENV_VALUES['POSTGRES_PASSWORD'],
            host=ENV_VALUES['POSTGRES_HOST'],
            port=int(ENV_VALUES['POSTGRES_PORT']),
            sslmode=ENV_VALUES.get('POSTGRES_SSLMODE', 'disable'),
            #**options
        )

if __name__ == '__main__':
    # connect to the database
    db.connect()
    print(db)
