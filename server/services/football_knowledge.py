from pathlib import Path
import json

from services.data_loader import DataLoader


class FootballKnowledge:

    def __init__(self):

        self.formations = self.load_formations()

        self.tactics = self.load_tactics()

    def load_formations(self):

        result = {}

        folder = (
            DataLoader.DATA_DIR
            / "formations"
        )

        for file in folder.glob("*.json"):

            with open(
                file,
                "r",
                encoding="utf-8"
            ) as f:

                data = json.load(f)

                result[data["id"]] = data

        return result

    def load_tactics(self):

        result = {}

        folder = (
            DataLoader.DATA_DIR
            / "tactical_profiles"
        )

        for file in folder.glob("*.json"):

            with open(
                file,
                "r",
                encoding="utf-8"
            ) as f:

                data = json.load(f)

                result[data["id"]] = data

        return result