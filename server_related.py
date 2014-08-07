import os


class ServerRelated():
    
    def get_project_directory_path(self):
        path = os.path.abspath(__file__)
        fold_index = path.index("Needle\\")
        return path[:fold_index]+"Needle\\"
    
    def get_path_in_project(self, location):
        return self.get_project_directory_path() + location