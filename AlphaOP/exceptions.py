# Ultroid - UserBot
# Copyright (C) 2021-2022 Cultured_Heaven
#
# This file is a part of < https://github.com/Cultured_Heaven/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://github.com/Cultured_Heaven/AlphaOP/blob/main/LICENSE>.

"""
Exceptions which can be raised by py-Ultroid Itself.
"""


class AlphaOPError(Exception):
    ...


class TelethonMissingError(ImportError):
    ...


class DependencyMissingError(ImportError):
    ...


class RunningAsFunctionLibError(AlphaOPError):
    ...
