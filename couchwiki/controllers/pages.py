import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from couchwiki.lib.base import BaseController, render

log = logging.getLogger(__name__)

class PagesController(BaseController):

    def render_page(self, page_id):
        db = self._get_db()
        page = Page.load(db, "page_%s" % (page_id,))
        
        if not page:
            c.desired_page_name = page_id
            return render("new_page")

        c.page = page
        c.page.page_id = page_id
        return render("page")

    def edit(self, **kwargs):
        db = self._get_db()
        page_id = kwargs.get("page_id")
        doc_name = "page_%s" % (page_id,)
        page = Page.load(db, doc_name)

        c.page = page

        return render("edit_page")
        
    def create(self, **kwargs):
        c.desired_page_name = kwargs.get("page_id")
        return render("new_page")

    def index(self):
        db = self._get_db()
        pages = [ p.value for p in db.view('_design/wiki/_view/pages') ]
        c.pages = pages
        c.pagey = h.url_for(controller='pages', page_id="boner", action='create_update')
        return render("pages")

    def create_update(self, **kwargs):
        db = self._get_db()

        page_id = request.POST['page_name']
        doc_name = "page_%s" % (page_id,)
        page = Page.load(db, doc_name)

        if page:
            page.name = request.POST['page_name']
            page.body = request.POST['body']
            page.store(db)
        else:
            page = Page(doc_name, name=page_id, body=request.POST['body'])
            page.store(db)

        redirect_to(str('/pages/%s' % (page_id,)))
        return

    def view(self, **kwargs):
        return self.render_page(kwargs['page_id'])
