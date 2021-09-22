
from model.recent import MobiUsers, NamedSearch, RecentSearch, db
from settings import logger


if __name__ == "__main__":
    logger.info("Initializing data base Connection  and creating data models...")
    db.create_all()
    logger.info("Command completed ......")