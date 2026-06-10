from fastapi import APIRouter

from services.data_loader import DataLoader
from services.team_builder import TeamBuilder

router = APIRouter()


@router.get("/teams")
def get_teams():

    return DataLoader.get_all_teams()

@router.get("/teams/{team_id}")
def get_team(team_id: str):
    return TeamBuilder.build(team_id)