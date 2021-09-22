import logging

logging.basicConfig(level=logging.NOTSET)
logger = logging.getLogger("  Mobi service message   ")

#connonction_string ="database_engine://user:password@host:port/database"


database = {
    "SQLALCHEMY_DATABASE_URI": "postgresql://user:password@host:port/database",
    "SQLALCHEMY_TRACK_MODIFICATIONS": False
}
