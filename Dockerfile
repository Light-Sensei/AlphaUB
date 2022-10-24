# ALPHA - UserBot
# Copyright (C) 2021-2022 Cultured_Heaven
# This file is a part of < https://github.com/Light-Sensei/AlphaUB/ >
# PLease read the GNU Affero General Public License in <https://www.github.com/Light-Sensei/AlphaUB/blob/main/LICENSE/>.

FROM theLight-Sensei/AlphaUB:main

# set timezone
ENV TZ=Asia/Kolkata
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

COPY installer.sh .

RUN bash installer.sh

# changing workdir
WORKDIR "/root/Cultured_Heaven"

# start the bot.
CMD ["bash", "startup"]
