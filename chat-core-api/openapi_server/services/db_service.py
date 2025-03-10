from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool
from variables import DATABASE_NAME, DATABASE_PASSWORD, DATABASE_USERNAME, INSTANCE_CONNECTION_NAME


class ChienowaNetDbService:
    """Service to manage database connections and sessions."""

    def __init__(self):
        """Initializes the database engine and session maker."""
        self.engine = create_engine(
            self._get_db_url_by_environment(), echo=False, poolclass=NullPool)
        self.Session = sessionmaker(bind=self.engine, autocommit=False)

    @contextmanager
    def start_session(self, commit=False):
        """Context manager for database sessions."""
        session = self.Session()
        try:
            if commit:
                session.commit()
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()

    def _get_db_url_by_environment(self):
        """Constructs the database URL using environment variables."""
        return (
            f"mysql+pymysql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}"
            f"@{INSTANCE_CONNECTION_NAME}:3306/{DATABASE_NAME}"
        )
