"""This module focuses on session manage
"""

import time
import uuid
import hashlib
from collections import namedtuple
from readerwriterlock import rwlock


class SessionManager:
    """Record logged-in user data, the session timeout will be 3600 seconds.
    Calling add() can extend session expire time.
    """

    def __init__(self):
        self._rwlock = rwlock.RWLockFairD()
        self._sessions = {}

    def add(self, user):
        """Add user to the cache and get an unique id as session.
        if user has been there, it will extend the session expire time.
        """

        with self._rwlock.gen_wlock():  # write lock
            for session, user_info in self._sessions.items():
                if user.name == user_info.name:
                    # just extend the session live time
                    user_info.login_time = int(time.time())
                    return session

            # new user case
            login_time = int(time.time())
            name_with_salt = uuid.uuid4().hex + user.name + r":" + str(login_time)
            session = hashlib.sha384(name_with_salt.encode()).hexdigest()
            new_user_info = namedtuple("UserInfo", ["name", "is_admin", "login_time"],
                                       defaults=[user.name, user.is_admin, login_time])()
            self._sessions[session] = new_user_info
            return session

    def get(self, session):
        """Query user data from session, return user info or None if session has no record
        """

        with self._rwlock.gen_rlock():  # read lock
            if user_info := self._sessions.get(session) \
                    and (int(time.time()) - user_info.login_time) < 3600:
                # session timeout is 3600 seconds
                return user_info
            return None


session_manager_singleton = SessionManager()
