from fastapi import FastAPI
from flights.main import find_flights

app = FastAPI()

@app.get("/search")
def search_flights(origin: str, destination: str, date: str):
    try:
        # Esegui la ricerca voli con i parametri forniti
        results = find_flights(origin=origin, destination=destination, date=date)
        return {"status": "ok", "results": results}
    except Exception as e:
        return {"status": "error", "message": str(e)}
