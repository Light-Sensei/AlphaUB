# ALPHA - UserBot
# Copyright (C) 2021-2022 Cultured_Heaven
#
# This file is a part of < https://github.com/Light-Sensei/AlphaUB/ >
# PLease read the GNU Affero General Public License in
# <https://github.com/Light-Sensei/AlphaUBOP/blob/main/LICENSE>.

import os
import sys

from .version import __version__

run_as_module = False

class ULTConfig:
    lang = "en"
    thumb = "resources/extras/ALPHA.jpg"

if sys.argv[0] == "-m":
    run_as_module = True

    import time

    from .configs import Var
    from .startup import *
    from .startup._database import ALPHADB
    from .startup.BaseClient import ALPHAClient
    from .startup.connections import validate_session, vc_connection
    from .startup.funcs import _version_changes, autobot, enable_inline, update_envs
    from .version import ALPHA_version

    if not os.path.exists("./plugins"):
        LOGS.error(
            "'plugins' folder not found!\nMake sure that, you are on correct path."
        )
        exit()

    start_time = time.time()
    _ult_cache = {}
    _ignore_eval = []

    udB = ALPHADB()
    update_envs()

    LOGS.info(f"Connecting to {udB.name}...")
    if udB.ping():
        LOGS.info(f"Connected to {udB.name} Successfully!")

    BOT_MODE = udB.get_key("BOTMODE")
    DUAL_MODE = udB.get_key("DUAL_MODE")

    if BOT_MODE:
        if DUAL_MODE:
            udB.del_key("DUAL_MODE")
            DUAL_MODE = False
        ALPHA_bot = None

        if not udB.get_key("BOT_TOKEN"):
            LOGS.critical(
                '"BOT_TOKEN" not Found! Please add it, in order to use "BOTMODE"'
            )

            sys.exit()
    else:
        ALPHA_bot = ALPHAClient(
            validate_session(Var.SESSION, LOGS),
            udB=udB,
            app_version=ALPHA_version,
            device_model="ALPHA",
        )
        ALPHA_bot.run_in_loop(autobot())

    asst = ALPHAClient(None, bot_token=udB.get_key("BOT_TOKEN"), udB=udB)

    if BOT_MODE:
        ALPHA_bot = asst
        if udB.get_key("OWNER_ID"):
            try:
                ALPHA_bot.me = ALPHA_bot.run_in_loop(
                    ALPHA_bot.get_entity(udB.get_key("OWNER_ID"))
                )
            except Exception as er:
                LOGS.exception(er)
    elif not asst.me.bot_inline_placeholder:
        ALPHA_bot.run_in_loop(enable_inline(ALPHA_bot, asst.me.username))

    vcClient = vc_connection(udB, ALPHA_bot)

    _version_changes(udB)

    HNDLR = udB.get_key("HNDLR") or "."
    DUAL_HNDLR = udB.get_key("DUAL_HNDLR") or "/"
    SUDO_HNDLR = udB.get_key("SUDO_HNDLR") or HNDLR
else:
    print("AlphaOP 2022 © Cultured_Heaven")

    from logging import getLogger

    LOGS = getLogger("AlphaOP")

    ALPHA_bot = asst = udB = vcClient = None
