from fastapi import APIRouter, HTTPException
from src.services.upper_winds_service import upper_winds_service

router = APIRouter()


@router.get("/upper-winds/stations")
async def get_stations():
    try:
        stations = upper_winds_service.get_all_stations()
        if not stations:
            raise HTTPException(status_code=404, detail="No valid stations found")
        return stations
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/upper-winds/station/{icao_code}")
async def get_upper_winds_station(icao_code: str):
    try:
        data = upper_winds_service.get_upper_winds_data(icao_code)
        if not data:
            raise HTTPException(status_code=404, detail="Data not found")
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/upper-winds")
async def get_all_upper_winds():
    try:
        data = upper_winds_service.get_all_upper_winds_data()
        if not data:
            raise HTTPException(status_code=404, detail="No data found")
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
