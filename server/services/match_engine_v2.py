import random

from agents.coach_agent import CoachAgent


class MatchEngine:

    def simulate(
        self,
        home_agent,
        away_agent
    ):

        timeline = []

        home_score = 0
        away_score = 0

        home_coach = CoachAgent(
            home_agent.context
        )

        away_coach = CoachAgent(
            away_agent.context
        )

        minute = 1

        while minute <= 90:

            home_decision = home_agent.decide(
                {
                    "minute": minute,
                    "my_score": home_score,
                    "opponent_score": away_score
                }
            )

            away_decision = away_agent.decide(
                {
                    "minute": minute,
                    "my_score": away_score,
                    "opponent_score": home_score
                }
            )

            if random.random() < 0.5:

                team = home_agent
                decision = home_decision

            else:

                team = away_agent
                decision = away_decision

            event = {
                "minute": minute,
                "team": team.team["name"],
                "action": decision["action"],
                "player": decision["target_player"],
                "reason": decision["reason"]
            }

            if decision["action"] == "shot":

                if random.random() < 0.3:

                    event["action"] = "goal"

                    if team == home_agent:
                        home_score += 1
                    else:
                        away_score += 1

            timeline.append(event)

            if minute in [60, 75]:

                coach_result = home_coach.decide_tactical_change(
                    minute,
                    home_score,
                    away_score
                )

                if coach_result.get("change"):

                    timeline.append(
                        {
                            "minute": minute,
                            "team": home_agent.team["name"],
                            "action": "formation_change",
                            "formation": coach_result["formation"],
                            "reason": coach_result["reason"]
                        }
                    )

                coach_result = away_coach.decide_tactical_change(
                    minute,
                    away_score,
                    home_score
                )

                if coach_result.get("change"):

                    timeline.append(
                        {
                            "minute": minute,
                            "team": away_agent.team["name"],
                            "action": "formation_change",
                            "formation": coach_result["formation"],
                            "reason": coach_result["reason"]
                        }
                    )

            minute += random.randint(3, 8)

        return {
            "score": f"{home_score}-{away_score}",
            "timeline": timeline
        }