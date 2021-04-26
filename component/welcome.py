from dataclasses import dataclass
from meya.component.element import Component
from meya.element.field import element_field
from meya.entry import Entry
from meya.text.event.say import SayEvent
from typing import List


@dataclass
class WelcomeComponentElement(Component):
    language: str = element_field()

    async def start(self) -> List[Entry]:
        if self.language == "en":
            text = "Welcome! Let's get started!"
        elif self.language == "fr":
            text = "Bienvenue! Commençons!"
        else:
            text = "🤔"
        text_event = SayEvent(text=text)
        return self.respond(text_event)
