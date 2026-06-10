# server/api/simulate.py
from fastapi import APIRouter
from services.team_builder import TeamBuilder
from services.data_loader import DataLoader
from agents.team_agent import TeamAgent
from services.match_engine_v3 import MatchEngine

router = APIRouter()

@router.post("/simulate")
def simulate_match(payload: dict):

    # 用户选择的两支国家队
    home_id = payload["home_team"]
    away_id = payload["away_team"]

    # 读取全局战术和阵型知识（使用 DataLoader 自带的方法）
    formations = DataLoader.load_all_formations()
    tactical_profiles = DataLoader.load_all_tactical_profiles()

    # 构建两支队伍上下文
    home_context = TeamBuilder.build(home_id)
    away_context = TeamBuilder.build(away_id)

    # 把战术和阵型知识加入 team_context
    home_context["formations"] = formations
    home_context["tactical_profiles"] = tactical_profiles

    away_context["formations"] = formations
    away_context["tactical_profiles"] = tactical_profiles

    # 初始化智能体
    home_agent = TeamAgent(home_context)
    away_agent = TeamAgent(away_context)

    # 创建比赛引擎并模拟比赛
    engine = MatchEngine()
    result = engine.simulate(
        home_agent,
        away_agent
    )

    return result