import random
from model.project import Project


def test_delete_project_by_name(app):
    app.session.login("administrator", "root")
    project = Project(name="Pr0", status="development", view_state="public", description="Some Project")
    if app.soap.get_project_list() == 0:
        app.project.create(project)
    old_projects = app.soap.get_project_list()
    project = random.choice(old_projects)
    app.project.delete_project_by_name(project.name)
    new_projects = app.soap.get_project_list()
    old_projects.remove(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)