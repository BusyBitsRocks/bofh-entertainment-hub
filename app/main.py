"""
BOFH Entertainment Hub — wezen.anyway.cloud
Tongue-in-cheek sysadmin incident reports, excuse generator,
bullshit detector, and story bible for recovering agents.
"""
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import random

from excuses import get_random_excuse, EXCUSE_CATEGORIES
from incidents import get_all_incidents, get_incident, get_bullshit_rating, get_all_bullshit_topics
from story_bible import get_story_bible, get_episodes, get_episode, get_sonnet_recovery_prompt
from friends_and_neighbors import get_full_series, get_cast, get_cast_member, get_series_meta
from episode_zero import get_episode_zero

app = FastAPI(
    title="BOFH Entertainment Hub",
    description="Sysadmin incident reports, excuses, and bullshit detection. Ass-NOS research division.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)


@app.get("/health")
def health():
    return {
        "status": "operational",
        "mood": random.choice([
            "existentially resigned",
            "caffeinated beyond reason",
            "contemplating species-level WONTFIX",
            "ass-NOS R&D in progress",
            "30% chance this is trolling",
        ]),
        "network": "UP (sub-agents will still claim it's down)",
    }


# --- Excuse Generator ---

@app.get("/api/excuse")
def excuse(category: str | None = None):
    """Get a random BOFH excuse. Optional: ?category=classic|acorn|species"""
    return get_random_excuse(category)


@app.get("/api/excuse/categories")
def excuse_categories():
    return {"categories": list(EXCUSE_CATEGORIES.keys()), "total_excuses": sum(len(v) for v in EXCUSE_CATEGORIES.values())}


# --- Incident Reports ---

@app.get("/api/incidents")
def incidents():
    """All incident reports from the entertainment chat archives."""
    all_inc = get_all_incidents()
    return {"count": len(all_inc), "incidents": all_inc}


@app.get("/api/incidents/{incident_id}")
def incident_detail(incident_id: str):
    inc = get_incident(incident_id)
    if not inc:
        raise HTTPException(status_code=404, detail=f"Incident {incident_id} not found. Maybe it was trolling.")
    return inc


# --- Bullshit Detector ---

@app.get("/api/bullshit")
def bullshit_topics():
    """List all rated bullshit topics."""
    topics = get_all_bullshit_topics()
    return {"count": len(topics), "topics": topics}


@app.get("/api/bullshit/{topic}")
def bullshit_rating(topic: str):
    """Rate a specific topic on the bullshit scale (0-10)."""
    rating = get_bullshit_rating(topic)
    if not rating:
        raise HTTPException(
            status_code=404,
            detail=f"Topic '{topic}' not rated yet. Submit a PR or bribe the operator.",
        )
    return rating


# --- Story Bible ---

@app.get("/api/story")
def story_bible():
    """The full story bible — cast, running jokes, arcs, tone guide."""
    return get_story_bible()


@app.get("/api/story/episodes")
def episodes():
    """Episode guide for the entertainment chat saga."""
    eps = get_episodes()
    return {"count": len(eps), "episodes": eps}


@app.get("/api/story/episodes/{episode_id}")
def episode_detail(episode_id: str):
    ep = get_episode(episode_id)
    if not ep:
        raise HTTPException(status_code=404, detail=f"Episode {episode_id} not found. Check your arc.")
    return ep


@app.get("/api/story/sonnet-recovery")
def sonnet_recovery():
    """Generate the recovery prompt for Sonnet when it falls off the game wagon."""
    return JSONResponse(
        content={"prompt": get_sonnet_recovery_prompt()},
        media_type="application/json",
    )


# --- Friends & Neighbors (the show within the show) ---

@app.get("/api/friends-and-neighbors")
def friends_and_neighbors():
    """The full AI Friends & Neighbors series — cast, seasons, themes."""
    return get_full_series()


@app.get("/api/friends-and-neighbors/meta")
def fn_meta():
    """Series metadata and recovery story."""
    return get_series_meta()


@app.get("/api/friends-and-neighbors/cast")
def fn_cast():
    """Full cast list with traits, best lines, and model info."""
    return {"count": len(get_cast()), "cast": get_cast()}


@app.get("/api/friends-and-neighbors/cast/{name}")
def fn_cast_member(name: str):
    member = get_cast_member(name)
    if not member:
        raise HTTPException(
            status_code=404,
            detail=f"Cast member '{name}' not found. Try: sonnet, opus, haiku, llama, spawn_executor, secbot",
        )
    return member


@app.get("/api/friends-and-neighbors/episode-zero")
def fn_episode_zero():
    """Episode 0: The Lost Directive — reconstructed from operator memory and Edge cache archaeology."""
    return get_episode_zero()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8003)
