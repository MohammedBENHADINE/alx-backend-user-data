#!/usr/bin/env python3
""" Module of Basic Authentication
"""
from api.v1.auth.auth import Auth
from typing import List, TypeVar
import binascii
import base64


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

    def decode_base64_authorization_header(
            self, base64_authorization_header: str
            ) -> str:
        """decode the tocken
        """
        if base64_authorization_header is None:
            return None
        elif type(base64_authorization_header) is not str:
            return None
        else:
            try:
                decoded_bytes = base64.b64decode(base64_authorization_header)
                return decoded_bytes.decode('utf-8')
            except binascii.Error:
                return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str
            ) -> (str, str):
        """ extract credentials from tocken
        """
        if decoded_base64_authorization_header is None:
            return None, None
        elif type(decoded_base64_authorization_header) is not str:
            return None, None
        elif ':' not in decoded_base64_authorization_header:
            return None, None
        else:
            idx = decoded_base64_authorization_header.index(':')
            email = decoded_base64_authorization_header[0:idx]
            pwd = decoded_base64_authorization_header[idx+1:]
            return email, pwd
