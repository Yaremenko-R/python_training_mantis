from selenium.webdriver.support.select import Select


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_manage_project_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/manage_proj_page.php")):
            wd.find_element_by_link_text("Manage").click()
            wd.find_element_by_link_text("Manage Projects").click()

    def return_to_manage_project_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/manage_proj_page.php")):
            wd.find_element_by_link_text("Manage").click()
            wd.find_element_by_link_text("Manage Projects").click()

    def create(self, project):
        wd = self.app.wd
        self.open_manage_project_page()
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()
        self.fill_project_form(project)
        self.fill_project_info(project)
        wd.find_element_by_xpath("//input[@value='Add Project']").click()
        self.return_to_manage_project_page()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_project_form(self, project):
        wd = self.app.wd
        self.change_field_value("name", project.name)
        self.change_field_value("description", project.description)

    def fill_select_info(self, field_name, text):
        wd = self.app.wd
        wd.find_element_by_name(field_name).click()
        Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)

    def fill_project_info(self, project):
        wd = self.app.wd
        self.fill_select_info("status", project.status)
        self.fill_select_info("view_state", project.view_state)

    def select_project_by_index(self, index):
        wd = self.app.wd

    def delete_project_by_index(self, index):
        wd = self.app.wd
        self.open_manage_project_page()
        self.select_project_by_index(index)
        wd.find_element_by_name("delete").click()
        self.return_to_manage_project_page()
