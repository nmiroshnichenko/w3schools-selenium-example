import json
from dataclasses import dataclass

from selenium.webdriver.common.by import By


@dataclass
class Locator:
    def __init__(self, by: By, value: str, frame: "Locator" = None):
        self.by = by
        self.value = value
        self.frame = frame

    def to_dict(self) -> dict:
        return {"by": self.by, "value": self.value}

    def toJSON(self) -> str:
        return json.dumps(self, default=self.to_dict, sort_keys=True, indent=4)
