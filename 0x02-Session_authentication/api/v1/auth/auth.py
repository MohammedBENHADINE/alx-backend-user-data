#!/usr/bin/env python3
""" Module of Authentication
"""
from flask import request
from typing import List, TypeVar
import os
from fnmatch import fnmatch


class Auth():
    """ Auth class for all authentication system
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ check if resource require auth or not
        """
        if not path or not excluded_paths:
            return True
        if path[-1] != '/':
            path += '/'
        return not [n for n in excluded_paths if fnmatch(path, n)]
    
    def authorization_header(self, request=None) -> str:
        """ get the Authorization header
        """
        if request is None:
            return None
        elif 'Authorization' in request.headers:
            return request.headers['Authorization']
        else:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Get the current user
        """
        return None

    def session_cookie(self, request=None):
        """get cookier value
        """
        if request is None:
            return None
        return request.cookies.get(os.environ.get('SESSION_NAME'))
