#!/usr/bin/env python3
""" Module of Session Authentication Mechanism
"""
from api.v1.auth.auth import Auth
from typing import List, TypeVar


class SessionAuth(Auth):
    """ BasicAuth class for basic auth system
    """
