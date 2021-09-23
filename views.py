from flask_resty import GenericModelView

from . import models, schemas

import json



class UserViewBase(GenericModelView):
    model = models.MobiUsers
    schema = schemas.UserSchema()
class UserListView(UserViewBase):
    def get(self):
        return self.list()

    def post(self):
        return self.create()



class NamedSearch(GenericModelView):
    model = models.NamedSearch
    schema = schemas.NamedSearchSchema()

class NamedSearchListView(NamedSearch):
    def get(self):
        return self.list()

    def post(self):
        return self.create()
    

class NamedSearchView(NamedSearch):
    def get(self, id):
        return self.retrieve(id)

    def patch(self, id):
        return self.update(id, partial=True)

    def delete(self, id):
        return self.destroy(id)



        
