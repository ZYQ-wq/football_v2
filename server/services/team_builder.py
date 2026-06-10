from services.data_loader import DataLoader


class TeamBuilder:

    @staticmethod
    def build(team_id):

        team = DataLoader.load_team(team_id)

        players = DataLoader.load_players(team_id)

        coach = DataLoader.load_coach(
            team["coach_id"]
        )

        formation = DataLoader.load_formation(
            team["preferred_formation"]
        )

        formations = (
            DataLoader.load_all_formations()
        )

        tactical_profiles = (
            DataLoader.load_all_tactical_profiles()
        )

        return {
            "team": team,
            "players": players,
            "coach": coach,
            "formation": formation,

            # 足球知识库
            "formations": formations,
            "tactical_profiles": tactical_profiles
        }