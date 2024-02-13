#!/usr/bin/env python3
""" Module of Basic Authentication
"""
from api.v1.auth.auth import Auth
from typing import List, TypeVar


class BasicAuth(Auth):
    """ BasicAuth class for basic auth system
    """

    def extract_base64_authorization_header(
            self, authorization_header: str
            ) -> str:
        """ get the authorization tocken
        """
        if (authorization_header is None):
            return None
        elif type(authorization_header) is not str:
            return None
        elif authorization_header[0:6] != "Basic ":
            return None
        else:
            return authorization_header[6:]
