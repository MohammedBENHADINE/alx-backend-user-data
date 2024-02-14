#!/usr/bin/env python3
""" Module of Session Authentication Mechanism
"""
from api.v1.auth.auth import Auth
from typing import List, TypeVar
import uuid


class SessionAuth(Auth):
    """ BasicAuth class for basic auth system
    """

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """create a new session
        """
        if user_id is None or type(user_id) is not str:
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id
