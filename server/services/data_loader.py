import json
from pathlib import Path


class DataLoader:

    # football_v2 根目录
    BASE_DIR = Path(__file__).resolve().parent.parent.parent

    # football_v2/data
    DATA_DIR = BASE_DIR / "data"

    @staticmethod
    def load_json(folder: str, filename: str):
        path = DataLoader.DATA_DIR / folder / f"{filename}.json"

        if not path.exists():
            raise FileNotFoundError(
                f"文件不存在: {path}"
            )

        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    @staticmethod
    def load_team(team_id: str):
        return DataLoader.load_json(
            "teams",
            team_id
        )

    @staticmethod
    def load_players(team_id: str):
        return DataLoader.load_json(
            "players",
            team_id
        )

    @staticmethod
    def load_coach(coach_id: str):
        return DataLoader.load_json(
            "coaches",
            coach_id
        )

    @staticmethod
    def load_formation(formation_id: str):
        return DataLoader.load_json(
            "formations",
            formation_id
        )

    @staticmethod
    def load_head_to_head(team1: str, team2: str):

        filename = "_".join(
            sorted([team1, team2])
        )

        return DataLoader.load_json(
            "head_to_head",
            filename
        )
    
    @staticmethod
    def load_all_tactical_profiles():
        tactical_dir = DataLoader.DATA_DIR / "tactical_profiles"
        result = []
        for file in tactical_dir.glob("*.json"):
            with open(file, "r", encoding="utf-8") as f:
                result.append(json.load(f))
        return result
    
    @staticmethod
    def load_all_formations():

        formations_dir = (
            DataLoader.DATA_DIR
            / "formations"
        )

        result = []

        for file in formations_dir.glob("*.json"):

            with open(
                file,
                "r",
                encoding="utf-8"
            ) as f:

                result.append(
                    json.load(f)
                )

        return result


    @staticmethod
    def load_all_tactical_profiles():

        tactical_dir = (
            DataLoader.DATA_DIR
            / "tactical_profiles"
        )

        result = []

        for file in tactical_dir.glob("*.json"):

            with open(
                file,
                "r",
                encoding="utf-8"
            ) as f:

                result.append(
                    json.load(f)
                )

        return result

    @staticmethod
    def get_all_teams():

        teams_dir = (
            DataLoader.DATA_DIR
            / "teams"
        )

        result = []

        for file in teams_dir.glob("*.json"):

            with open(
                file,
                "r",
                encoding="utf-8"
            ) as f:

                team = json.load(f)

                result.append({
                    "id": team["id"],
                    "name": team["name"],
                    "flag": team.get("flag", "")
                })

        return result