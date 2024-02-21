import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from SamyuktX import LOGGER, app, userbot
from SamyuktX.core.call import SamyuktX
from SamyuktX.misc import sudo
from SamyuktX.plugins import ALL_MODULES
from SamyuktX.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("Assistant client variables not defined, exiting...")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("SamyuktX.plugins" + all_module)
    LOGGER("SamyuktX.plugins").info("Successfully Imported Modules...")
    await userbot.start()
    await SamyuktX.start()
    try:
        await SamyuktX.stream_call("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
    except NoActiveGroupCall:
        LOGGER("SamyuktX").error(
            "Please turn on the videochat of your log group\channel.\n\nStopping Bot..."
        )
        exit()
    except:
        pass
    await SamyuktX.decorators()
    LOGGER("SamyuktX").info(
        "Don't forget to visit @SamyuktXYT"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("SamyuktX").info("Stopping SamyuktX Music Bot...")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
