from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class PodcastEpisode(Base):
    __tablename__ = 'podcast_episodes'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    host = Column(String, nullable=False)
