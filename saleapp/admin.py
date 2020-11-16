from flask_login import logout_user, current_user
from flask import redirect
from saleapp import admin, db
from flask_admin.contrib.sqla import ModelView
from flask_admin import BaseView, expose
from saleapp.models import Category, Product


class ContactView(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin/contact.html')


class AboutUsView(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin/about-us.html')
    def is_accessible(self):
        return current_user.is_authenticated


class CategoryModelView(ModelView):
    column_display_pk = True;
    can_export = True

    def is_accessible(self):
        return current_user.is_authenticated



class LogoutView(BaseView):
    @expose('/')
    def logout(self):
        logout_user()

        return redirect('/admin')

    def is_accessible(self):
        return current_user.is_authenticated


admin.add_view(CategoryModelView(Category, db.session))
admin.add_view(ModelView(Product, db.session))
admin.add_view(ContactView(name='Liên hệ'))
admin.add_view(AboutUsView(name='About Us'))
admin.add_view(LogoutView(name='Logout'))
