class BaseViewTemplate():

    def get_template(self):
        if self.request.user.is_authenticated:
            template = "core/base.html"
        else:
            template = "core/base-nav.html"
        return template
