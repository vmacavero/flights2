from fastapi import FastAPI
from fast_flights import get_flights, FlightData, Passengers

app = FastAPI()

@app.get("/search")
def search_flights(origin: str, destination: str, date: str):
    # Configura i parametri di ricerca
    flight_data = FlightData(
        origin=origin,
        destination=destination,
        date=date,
        passengers=Passengers(adults=1)
    )
    # Esegui la ricerca
    results = get_flights(flight_data)
    return results
