from typing import List

from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session
from google import generativeai as genai

from config import GEMINI_API_KEY
from database import get_db
from models import PodcastEpisode
from schemas import PodcastEpisodeSchema, AlternativeEpisode, AlternativeResponse


app = FastAPI()

genai.configure(api_key=GEMINI_API_KEY)


@app.get('/episodes', response_model=List[PodcastEpisodeSchema])
def get_episodes(db: Session = Depends(get_db)):
    episodes = db.query(PodcastEpisode).all()
    return episodes


@app.post('/episodes', response_model=PodcastEpisodeSchema)
def create_episode(episode: PodcastEpisodeSchema, db: Session = Depends(get_db)):
    existing_episode = db.query(PodcastEpisode).filter(PodcastEpisode.title == episode.title).first()
    if existing_episode:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Episode with title '{episode.title}' already exist."
        )

    new_episode = PodcastEpisode(
        title=episode.title,
        description=episode.description,
        host=episode.host
    )
    db.add(new_episode)
    db.commit()
    db.refresh(new_episode)
    return new_episode


@app.post('/episodes/{episode_id}/generate_alternative', response_model=AlternativeResponse)
def alternative_episode(episode_id: int, request: AlternativeEpisode, db: Session = Depends(get_db)):
    episode = db.query(PodcastEpisode).filter(PodcastEpisode.id == episode_id).first()
    if not episode:
        raise HTTPException(
            status_code=404,
            detail={'error": "Episode not found.'}
        )

    if request.target == 'title':
        original_text = episode.title
    elif request.target == 'description':
        original_text = episode.description
    else:
        raise HTTPException(
            status_code=400,
            detail='Invalid target'
        )

    prompt_text = request.prompt + " Original " + request.target + ": " + original_text

    try:
        model = genai.GenerativeModel(
            "gemini-2.0-flash")
        response = model.generate_content(prompt_text)
        alternative_text = response.text
    except Exception as e:
        raise HTTPException(status_code=500,
                            detail=f"AI generation failed: {e}")

    return AlternativeResponse(
        original_episode=PodcastEpisodeSchema.from_orm(episode),
        target=request.target,
        prompt=request.prompt,
        generated_alternative=alternative_text
    )
