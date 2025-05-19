from fastapi import FastAPI
from fast_flights import get_flights, FlightData, Passengers

app = FastAPI()

@app.get("/search")
def search_flights(origin: str, destination: str, date: str):
    try:
        flight_data = FlightData(
            from_airport=origin,
            to_airport=destination,
            date=date
        )
        passengers = Passengers(adults=1)
        result = get_flights(
            flight_data=[flight_data],
            trip="one-way",
            seat="economy",
            passengers=passengers,
            fetch_mode="fallback"
        )
        return {"status": "ok", "results": result}
    except Exception as e:
        return {"status": "error", "message": str(e)}
