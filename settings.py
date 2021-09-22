import logging

logging.basicConfig(level=logging.NOTSET)
logger = logging.getLogger("  Mobi service message   ")

#connonction_string ="database_engine://user:password@host:port/database"


database = {
    "SQLALCHEMY_DATABASE_URI": "postgresql://uniuser_1:12345@35.223.205.190:5432/mobikwik",
    "SQLALCHEMY_TRACK_MODIFICATIONS": False
}
