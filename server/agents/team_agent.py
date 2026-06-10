# agents/team_agent.py
import json
from services.llm_service import LLMService

class TeamAgent:
    def __init__(self, team_context):
        self.team_context = team_context
        self.team = team_context["team"]
        self.players = team_context["players"]
        self.coach = team_context["coach"]
        self.formation = team_context["formation"]
        self.formations = team_context.get("formations", [])
        self.tactical_profiles = team_context.get("tactical_profiles", [])
        self.llm = LLMService()

        # 用于提示词中的足球知识
        self.knowledge = {
            "formations": self.formations,
            "tactics": self.tactical_profiles
        }

    def decide(self, match_state):
        """
        根据当前比赛状态，使用 Qwen 智能体决定下一步事件：
        - tactic 战术
        - formation 阵型
        - event_type 事件类型（attack, shot, goal, defend, save, substitution 等）
        - player 参与球员
        - reason 理由
        """
        prompt = f"""
你是一支国家队足球智能体。

================
足球阵型知识
================

{json.dumps(self.knowledge['formations'], ensure_ascii=False)}

================
足球战术知识
================

{json.dumps(self.knowledge['tactics'], ensure_ascii=False)}

================
当前球队
================

{json.dumps(self.team_context, ensure_ascii=False)}

================
当前比赛状态
================

{json.dumps(match_state, ensure_ascii=False)}

请思考：

1. 当前选择什么战术
2. 是否调整阵型
3. 发起什么进攻
4. 哪个球员参与
5. 事件类型

只返回JSON，格式如下：

{{
    "tactic": "",
    "formation": "",
    "event_type": "",
    "player": "",
    "reason": ""
}}
不要解释，不要输出Markdown。
"""
        # 调用 LLMService（内部使用 Qwen）
        response = self.llm.chat(
            prompt=prompt,
        )

        # 解析智能体返回
        try:
            action = json.loads(response)
        except Exception:
            # 回退机制
            action = {
                "tactic": "balanced",
                "formation": self.formation["id"],
                "event_type": "attack",
                "player": self.players[0]["name"],
                "reason": "fallback"
            }

        return action