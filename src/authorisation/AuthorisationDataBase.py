from threading import Lock
import copy

# class AuthorisationData:

#     def __init__(self):
#         self.reading = set()
#         self.writing = set()
#         self.deleting = set()
#         self.uploading = set()
#         self.downloading = set()


class AuthorisationDataBase:

    def __init__(self, records):
        self._records = records
        self._lock = Lock()

    def _common_updating(self, file, user_list: list, column_name, adding: bool):
        with self._lock:
            if not self._records.get(file):
                return
            
            columns = {
                "reading": self._records.get(file).get("reading"),
                "writing": self._records.get(file).get("writing"),
                "deleting": self._records.get(file).get("deleting"),
                "uploading": self._records.get(file).get("uploading"),
                "downloading": self._records.get(file).get("downloading")
            }
            for user in user_list:
                if adding and user not in columns.get(column_name):
                    columns.get(column_name).append(user)
                elif not adding and user in columns.get(column_name):
                    columns.get(column_name).remove(user)

    def update_reading(self, file, user_list: list, adding=True):
        self._common_updating(file, user_list, "reading", adding)
    
    def update_writing(self, file, user_list: list, adding=True):
        self._common_updating(file, user_list, "writing", adding)
    
    def update_deleting(self, file, user_list: list, adding=True):
        self._common_updating(file, user_list, "deleting", adding)
    
    def update_uploading(self, file, user_list: list, adding=True):
        self._common_updating(file, user_list, "uploading", adding)
    
    def update_downloading(self, file, user_list: list, adding=True):
        self._common_updating(file, user_list, "downloading", adding)

    def _common_get(self, file, column):
        with self._lock:
            if self._records.get(file):
                columns = {
                    "reading": self._records.get(file).get("reading"),
                    "writing": self._records.get(file).get("writing"),
                    "deleting": self._records.get(file).get("deleting"),
                    "uploading": self._records.get(file).get("uploading"),
                    "downloading": self._records.get(file).get("downloading")
                }
                return copy.deepcopy(columns.get(column))
        return None

    def get_reading(self, file):
        return self._common_get(file, "reading")
    
    def get_writing(self, file):
        return self._common_get(file, "writing")
    
    def get_deleting(self, file):
        return self._common_get(file, "deleting")
    
    def get_uploading(self, file):
        return self._common_get(file, "uploading")
    
    def get_downloading(self, file):
        return self._common_get(file, "downloading")
    
    

        
    
