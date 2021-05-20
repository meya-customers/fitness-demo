from dataclasses import dataclass
from meya.component.element import Component
from meya.component.element import ComponentResponse
from meya.element.field import element_field
from meya.element.field import response_field
from meya.entry import Entry
from meya.text.event.say import SayEvent
from typing import List

USER_DB = [
    dict(user_id="1", name="Roger", email="roger@example.com", is_paid=True),
    dict(user_id="2", name="Susan", email="susan@example.com", is_paid=False),
]


@dataclass
class AuthenticateUserComponent(Component):
    url: str = element_field()
    api_token: str = element_field()
    user_id: str = element_field()

    @dataclass
    class UserData:
        name: str = response_field()
        email: str = response_field()
        is_paid: bool = response_field()
        result: bool = response_field()

    async def start(self) -> List[Entry]:
        # Option 1: Use test DB.
        user = [x for x in USER_DB if x["user_id"] == self.user_id]
        user = user[0] if len(user) else None
        if user:
            user_data = self.UserData(
                name=user["name"],
                email=user["email"],
                is_paid=user["is_paid"],
                result=True,
            )
            return self.respond(data=user_data)
        else:
            return self.respond(data=ComponentResponse(result=False))

        # Option 2: Uncomment this section to make real API calls.
        # response = await self.http.get(f"{self.url}/users/{self.user_id}")
        # if response.status == 200:
        #     data = response.data
        #     user_data = self.UserData(
        #         name=data["name"],
        #         email=data["email"],
        #         is_paid=data["is_paid"],
        #         result=True,
        #     )
        #     return self.respond(data=user_data)
        # else:
        #     return self.respond(data=ComponentResponse(result=False))
