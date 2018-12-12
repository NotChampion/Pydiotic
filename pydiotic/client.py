import asyncio

import aiohttp
from http.routes import Endpoints
from http.errors import InvalidArgument

class Client:
    def __init__(self, token, dev=False):
        self.token = token
        self.dev = dev
        self.headers = {"Authorization" if self.dev else "token": self.token}
        self.base_url = "https://dev.anidiots.guide" if self.dev else "https://api.anidiots.guide"
        self.session = aiohttp.ClientSession(loop=asyncio.get_event_loop())

    def __repr__(self):
        return "<Pydiotic.Client>"

    async def request(self, endpoint, params):

        async with self.session.get(f"{self.base_url}{endpoint}{params.replace('.webp', '.png')}", headers=self.headers) as resp:
            if resp.status != 200:
                status_codes = {
                    "403": "Either your API key is missing or an improper one was passed.",
                    "400": "You are missing some required fields."
                }
                raise InvalidArgument(status_codes[str(resp.status)])
            response = await resp.json()
        return bytes(response["data"])

    async def brightness(self, avatar, brightness):
        if brightness > 255:
            raise InvalidArgument("Brightness must be a range of 0 to 255.")
        return await self.request(Endpoints.BRIGHTNESS, f"?avatar={avatar}&brightness={brightness}")

    async def darkness(self, avatar, darkness):
        if darkness > 255:
            raise InvalidArgument("Darkness must be a range of 0 to 255.")
        return await self.request(Endpoints.DARKNESS, f"?avatar={avatar}&darkness={darkness}")

    async def greyscale(self, avatar):
        return await self.request(Endpoints.DARKNESS, f"?avatar={avatar}")

    async def invert(self, avatar):
        return await self.request(Endpoints.INVERT, f"?avatar={avatar}")

    async def invertgreyscale(self, avatar):
        return await self.request(Endpoints.INVERTGREYSCALE, f"?avatar={avatar}")

    async def invertthreshold(self, avatar):
        return await self.request(Endpoints.INVERTTHRESHOLD, f"?avatar={avatar}")


    async def blame(self, text):
        return await self.request(Endpoints.BLAME, f"?name={text}")

    async def bob_ross(self, avatar):
        return await self.request(Endpoints.BOB_ROSS, f"?avatar={avatar}")

    async def crush(self, crush, crusher):
        return await self.request(Endpoints.CRUSH, f"?crush={crush}&crusher={crusher}")

    async def facepalm(self, avatar):
        return await self.request(Endpoints.FACEPALM, f"?avatar={avatar}")

    async def fan_slap(self, slapper, slapped):
        return await self.request(Endpoints.FAN_SLAP, f"?slapper{slapper}&slapped{slapped}")

    async def garbage(self, avatar):
        return await self.request(Endpoints.GARBAGE, f"?avatar={avatar}")

    async def colour(self, colour):
        return await self.request(Endpoints.COLOUR, f"?colour={colour}")

    async def change_my_mind(self, avatar, *):
        if len(text) > 20:
            raise InvalidArgument("Characters cannot be more than 22 characters.")
        return await self.request(Endpoints.CHANGE_MY_MIND, f"?avatar={avatar}&text={text}")

    async def coffee(self, *, text1, text2):
        return await self.request(Endpoints.COFFEE, f"?text1={text1}&text2={text2}")

