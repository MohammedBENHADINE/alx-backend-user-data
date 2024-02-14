#!/usr/bin/env python3
""" Module of Basic Authentication
"""
from api.v1.auth.auth import Auth
from typing import List, TypeVar
import binascii
import base64
from api.v1.views.users import User


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

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str
            ) -> TypeVar('User'):
        """get user from credentials
        """
        if user_email is None or type(user_email) is not str:
            return None
        if user_pwd is None or type(user_pwd) is not str:
            return None
        found_users = User.search({'email': user_email})
        for found_user in found_users:
            if found_user.is_valid_password(user_pwd) is True:
                return found_user
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """retrieve user
        """
        hdr = self.authorization_header(request)
        if hdr is None:
            return None
        else:
            tocken = self.extract_base64_authorization_header(hdr)
            if tocken is None:
                return None
            else:
                decoded = self.decode_base64_authorization_header(tocken)
                if decoded is None:
                    return None
                else:
                    email, pwd = self.extract_user_credentials(decoded)
                    return self.user_object_from_credentials(email, pwd)
