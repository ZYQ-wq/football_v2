import json

from services.llm_service import LLMService


class CoachAgent:

    def __init__(self, team_context):

        self.context = team_context

        self.llm = LLMService()

    def decide_tactical_change(
        self,
        minute,
        goals_for,
        goals_against
    ):

        prompt = f"""
你是一名足球主教练。

球队信息：

{json.dumps(self.context, ensure_ascii=False)}

比赛时间:

{minute}

比分:

{goals_for}:{goals_against}

球队可选阵型:

{self.context["team"]["formations"]}

请决定是否调整阵型。

返回：

{{
    "change": true,
    "formation":"4-4-2",
    "reason":"xxxx"
}}

或者

{{
    "change": false
}}

只返回JSON。
"""

        result = self.llm.chat(prompt)

        try:
            return json.loads(result)
        except:
            return {
                "change": False
            }