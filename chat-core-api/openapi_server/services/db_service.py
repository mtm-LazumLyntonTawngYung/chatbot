import logging
from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool


class ChienowaNetDbService:

    def __init__(self):
        url = self.get_db_url_by_environment()
        self.engine = create_engine(url, echo=False, poolclass=NullPool)
        self.Session = sessionmaker(bind=self.engine, autocommit=False)

    @staticmethod
    def get_db_url_by_environment():
        url = 'mysql+pymysql://root:root@localhost:3306/g_system01_dev'
        return url

    @contextmanager
    def start_session(self, commit=False):
        session = None
        try:
            session = self.Session()
            try:
                yield session
                if commit:
                    session.commit()
            except Exception as e:
                logging.info(e)
                session.rollback()
                raise
        finally:
            if session is not None:
                session.close()
