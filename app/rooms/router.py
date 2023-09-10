from fastapi import APIRouter

# room is the subset of hotel and I use hotels prefix
router = APIRouter(prefix="/hotels", tags=["Rooms"])
