from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict

app = FastAPI(title="Ticket Price Tracker - Client Server")

#models
class Concert(BaseModel):
    id: int
    artist: str
    city: str
    date: str
    best_price: float

class TrackedEvent(BaseModel):
    concert_id: int

#stand in database 
CONCERTS: Dict[int, Concert] = {
    1: Concert(id=1, artist="Taylor Swift", city="Arlington", date="2026-05-01", best_price=250.0),
    2: Concert(id=2, artist="Olivia Rodrigo", city="Houston", date="2026-06-10", best_price=180.0),
}

TRACKED: Dict[int, Concert] = {}  #key = concert_id

#endpoints

@app.get("/concerts", response_model=List[Concert])
def list_concerts(artist: str | None = None, city: str | None = None):
    results = list(CONCERTS.values())
    if artist:
        results = [c for c in results if artist.lower() in c.artist.lower()]
    if city:
        results = [c for c in results if city.lower() in c.city.lower()]
    return results

@app.post("/track")
def track_concert(req: TrackedEvent):
    concert = CONCERTS.get(req.concert_id)
    if concert is None:
        return {"status": "error", "message": "Concert not found"}
    TRACKED[req.concert_id] = concert
    return {"status": "ok", "tracked_count": len(TRACKED)}

@app.get("/tracked", response_model=List[Concert])
def list_tracked():
    return list(TRACKED.values())

#demo: manually simulates a price drop
@app.post("/simulate_price_drop/{concert_id}")
def simulate_price_drop(concert_id: int, new_price: float):
    concert = CONCERTS.get(concert_id)
    if concert is None:
        return {"status": "error", "message": "Concert not found"}
    old_price = concert.best_price
    concert.best_price = new_price
    CONCERTS[concert_id] = concert
    if concert_id in TRACKED and new_price < old_price:
        #irl system would send an email or notification, we just return a message here
        return {
            "status": "ok",
            "message": f"Price dropped from {old_price} to {new_price} for {concert.artist} in {concert.city}"
        }
    return {"status": "ok", "message": "Price updated but no tracked alert"}
