# ALPHA - UserBot
# Copyright (C) 2021-2022 Cultured_Heaven
#
# This file is a part of < https://github.com/Light-Sensei/AlphaUB/ >
# PLease read the GNU Affero General Public License in
# <https://github.com/Light-Sensei/AlphaUBOP/blob/main/LICENSE>.

"""
Exceptions which can be raised by py-ALPHA Itself.
"""


class AlphaOPError(Exception):
    ...


class TelethonMissingError(ImportError):
    ...


class DependencyMissingError(ImportError):
    ...


class RunningAsFunctionLibError(AlphaOPError):
    ...
