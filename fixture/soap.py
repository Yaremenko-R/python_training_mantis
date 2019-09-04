from suds.client import Client
from suds import WebFault
from model.project import Project


class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        soap_config = self.app.config['mantisConnect']
        client = Client(soap_config['soap_api'])
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_project_list(self):
        username = "administrator"
        password = "root"
        list = []
        soap_config = self.app.config['mantisConnect']
        client = Client(soap_config['soap_api'])
        try:
            projects = client.service.mc_projects_get_user_accessible(username, password)
            for p in projects:
                id = p[0]
                name = p[1]
                list.append(Project(id=id, name=name))
            return list
        except WebFault:
            return "Ups..."