from enum import Enum, auto
from os.path import exists, isfile, isdir

class AuthorisationType(Enum):
    READING = auto()
    WRITING = auto()
    UPLOADING = auto()
    DOWNLOADING = auto()
    DELETING = auto()

class Authorisation:
    
    def __init__(self, userManager, AuthorisationDataBase):
        self._permissions = { 
            AuthorisationType.READING: self._reading_permission,
            AuthorisationType.WRITING: self._writing_permission,
            AuthorisationType.UPLOADING: self._uploading_permission,
            AuthorisationType.DOWNLOADING: self._downloading_permission,
            AuthorisationType.DELETING: self._deleting_permission
        }
        self._userManager = userManager
        self._authorisationDataBase = AuthorisationDataBase

    def has_premission(self, user_name, permission_type: AuthorisationType, **kwargs) -> bool:
        # query user login status
        if user_info := self._userManager(user_name):
            if f := self._permissions.get(permission_type):
                return f(user_info, kwargs)

        return False

    def _common_checking(self, f, user_info, **kwargs):
        file = kwargs.get(file)
        if not file or not exists(file) or isfile(file):
            # no file parameters or file not exists or not a file
            return False
        
        user_list = f(file)
        if user_info.name in user_list:
            return True
        
        return False
    
    def _reading_permission(self, user_info, **kwargs):
        return self._common_file_checking(self._authorisationDataBase.get_reading, user_info, kwargs)

    def _writing_permission(self, user_info, **kwargs):
        return self._common_file_checking(self._authorisationDataBase.get_writing, user_info, kwargs)

    def _downloading_permission(self, user_info, **kwargs):
        return self._common_file_checking(self._authorisationDataBase.get_downloading, user_info, kwargs)
    
    def _deleting_permission(self, user_info, **kwargs):
        return self._common_file_checking(self._authorisationDataBase.get_deleting, user_info, kwargs)

    def _uploading_permission(self, user_info, **kwargs):
        folder = kwargs.get(file)
        if not folder or not exists(folder) or isdir(folder):
            # no file parameters or file not exists
            return False
        
        user_list = _authorisationDataBase.get_uploading(folder)
        if user_info.name in user_list:
            return True
        
        return False
