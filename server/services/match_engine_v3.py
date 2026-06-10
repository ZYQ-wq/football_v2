# services/match_engine_v3.py

import random


class MatchEngine:

    def simulate(
        self,
        home_agent,
        away_agent
    ):

        timeline = []

        home_score = 0
        away_score = 0

        for minute in range(1, 91, 5):

            acting_agent = random.choice(
                [home_agent, away_agent]
            )

            match_state = {
                "minute": minute,
                "home_score": home_score,
                "away_score": away_score,
                "last_event":
                    timeline[-1]
                    if timeline
                    else None
            }

            try:

                decision = acting_agent.decide(
                    match_state
                )

            except Exception as e:

                decision = {
                    "intent": "attack",
                    "player": "Unknown",
                    "formation":
                        acting_agent.formation["name"],
                    "tactic": "default",
                    "reason": str(e)
                }

            team_name = (
                acting_agent.team["name"]
            )

            player = decision.get(
                "player",
                "Unknown"
            )

            intent = decision.get(
                "intent",
                "attack"
            )

            formation = decision.get(
                "formation",
                acting_agent.formation["name"]
            )

            tactic = decision.get(
                "tactic",
                ""
            )

            reason = decision.get(
                "reason",
                ""
            )

            if intent == "attack":

                timeline.append({
                    "minute": minute,
                    "team": team_name,
                    "player": player,
                    "event_type": "attack",
                    "commentary":
                        f"{player} 发起进攻",
                    "formation": formation,
                    "tactic": tactic,
                    "score":
                        f"{home_score}-{away_score}"
                })

                shot_prob = 0.45

                if random.random() < shot_prob:

                    timeline.append({
                        "minute": minute,
                        "team": team_name,
                        "player": player,
                        "event_type": "shot",
                        "commentary":
                            f"{player} 完成射门",
                        "score":
                            f"{home_score}-{away_score}"
                    })

                    goal_prob = 0.25

                    if random.random() < goal_prob:

                        if acting_agent == home_agent:
                            home_score += 1
                        else:
                            away_score += 1

                        timeline.append({
                            "minute": minute,
                            "team": team_name,
                            "player": player,
                            "event_type": "goal",
                            "commentary":
                                f"⚽ {player} 破门得分！",
                            "score":
                                f"{home_score}-{away_score}"
                        })

                    else:

                        timeline.append({
                            "minute": minute,
                            "team":
                                home_agent.team["name"]
                                if acting_agent == away_agent
                                else away_agent.team["name"],
                            "player": "Goalkeeper",
                            "event_type": "save",
                            "commentary":
                                "门将完成精彩扑救",
                            "score":
                                f"{home_score}-{away_score}"
                        })

            elif intent == "defend":

                timeline.append({
                    "minute": minute,
                    "team": team_name,
                    "player": player,
                    "event_type": "defense",
                    "commentary":
                        f"{player} 完成关键防守",
                    "score":
                        f"{home_score}-{away_score}"
                })

            elif intent == "tactical_change":

                timeline.append({
                    "minute": minute,
                    "team": team_name,
                    "event_type":
                        "formation_change",
                    "formation": formation,
                    "reason": reason,
                    "commentary":
                        f"主教练调整阵型为 {formation}",
                    "score":
                        f"{home_score}-{away_score}"
                })

            elif intent == "substitution":

                timeline.append({
                    "minute": minute,
                    "team": team_name,
                    "event_type": "substitution",
                    "commentary":
                        "球队进行换人调整",
                    "score":
                        f"{home_score}-{away_score}"
                })

        return {
            "score":
                f"{home_score}-{away_score}",
            "timeline": timeline
        }