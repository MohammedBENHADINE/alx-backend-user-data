#!/usr/bin/env python3
""" Module of Authentication
"""
from flask import request
from typing import List, TypeVar
import os


class Auth():
    """ Auth class for all authentication system
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ check if resource require auth or not
        """
        if path is None:
            return True
        elif excluded_paths is None:
            return True
        elif len(excluded_paths) == 0:
            return True
        if path[-1] != '/':
            normalizedPath = path + '/'
        else:
            normalizedPath = path
        for item in excluded_paths:
            i = 0
            for char in item:
                if char == normalizedPath[i]:
                    i = i + 1
                    continue
                elif len(item) == i + 1 and char == '*':
                    return False
                else:
                    return True
        if normalizedPath in excluded_paths:
            return False
        else:
            return True

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
        if request is None:
            return None
        return request.cookies.get(os.environ.get('SESSION_NAME'))
