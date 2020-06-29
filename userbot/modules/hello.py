# (c) @Unknown
# Original written by @Unknown edit by @RoyalBoyPriyanshu

from telethon import events
import asyncio
from collections import deque
from userbot.events import register

@register(outgoing=True, pattern="^.hello$")
async def hello(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`\n╔┓┏╦━╦┓╔┓╔━━╗ `"
                     "`\n║┗┛║┗╣┃║┃║X X║ `"
                     "`\n║┏┓║┏╣┗╣┗╣╰╯║ `" 
                     "`\n╚┛┗╩━╩━╩━╩━━╝﻿ `")