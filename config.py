class Config:
    SECRET_KEY = 'H3ll0W0rld!'


class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''
    MYSQL_DB = 'primarykey'


config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}
