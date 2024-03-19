from dotenv import load_dotenv
import os

load_dotenv()

sqlite_uri = r"sqlite:///./db.sqlite"
sqlite_test = r"sqlite:///./testdb.sqlite"


class Config:
    """Base config class"""
    SECRET_KEY = os.environ["SECRET_KEY"]
    SQL_ALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(Config):
    """Development config"""
    SQLALCHEMY_DATABASE_URI = sqlite_uri
    SQL_ALCHEMY_ECHO = True


class TestConfig(Config):
    """Testing config"""
    SQLALCHEMY_DATABASE_URI = sqlite_uri
    SQL_ALCHEMY_ECHO = False
    TESTING = True

