# agents/commentary_agent.py

import json
from services.llm_service import LLMService


class CommentaryAgent:

    def __init__(self):
        self.llm = LLMService()

    def generate_commentary(
        self,
        home_team,
        away_team,
        timeline
    ):

        prompt = f"""
你是世界杯央视解说员。

风格参考：

贺炜
詹俊

要求：

1 激情
2 专业
3 有临场感
4 能分析战术
5 能描述球员动作
6 关键进球重点渲染
7 不要编造不存在事件
8 按时间顺序解说
9 输出自然中文

比赛：

{home_team}
VS
{away_team}

事件：

{json.dumps(
    timeline,
    ensure_ascii=False,
    indent=2
)}

请直接输出比赛解说。
"""

        return self.llm.chat(prompt)