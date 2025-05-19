from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
import logging
from flights import search_flights

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "✅ API pronta. Usa /search per cercare voli."}

@app.get("/search")
def search(
    origin: str = Query(..., description="Codice IATA aeroporto di partenza (es. BRI)"),
    destination: str = Query(..., description="Codice IATA aeroporto di arrivo (es. STN)"),
    date: str = Query(..., description="Data in formato YYYY-MM-DD")
):
    logger.info("📡 Chiamata ricevuta a /search con:")
    logger.info(f"✈️ origin: {origin}")
    logger.info(f"🎯 destination: {destination}")
    logger.info(f"📅 date: {date}")

    try:
        results = search_flights(origin, destination, date)
        logger.info(f"✅ {len(results)} risultati trovati.")
        return JSONResponse(content=results)
    except Exception as e:
        logger.error(f"❌ Errore durante la ricerca: {str(e)}")
        return JSONResponse(status_code=500, content={"status": "error", "message": str(e)})
