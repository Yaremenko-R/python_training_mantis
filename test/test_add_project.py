from model.project import Project


def test_add_project(app):
    app.session.login("administrator", "root")
    project = Project(name="Pr22", status="development", view_state="public", description="Some Project")
    old_projects = app.soap.get_project_list()
    app.project.create(project)
    new_projects = app.soap.get_project_list()
    old_projects.append(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
