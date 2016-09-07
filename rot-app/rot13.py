import os
import jinja2
import webapp2

template_dir = os.path.join(os.path.dirname(__file__), 'template')
jinja_env = \
    jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),
                       autoescape=True)

class Handler(webapp2.RequestHandler):

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

class MainPage(Handler):
    def get(self):
        self.render("rot13.html")

    def post(self):
        rot13 = ''
        text = self.request.get("text")
        if text:
            rot13 = text.encode("rot13")

        self.render("rot13.html", text = rot13)


app = webapp2.WSGIApplication([('/', MainPage)], debug=True)
