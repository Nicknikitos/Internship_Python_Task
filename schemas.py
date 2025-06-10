from typing import Literal

from pydantic import BaseModel


class PodcastEpisodeSchema(BaseModel):
    title: str
    description: str
    host: str

    class Config:
        from_attributes = True


class AlternativeEpisode(BaseModel):
    target: Literal['title', 'description']
    prompt: str


class AlternativeResponse(BaseModel):
    original_episode: PodcastEpisodeSchema
    target: str
    prompt: str
    generated_alternative: str
