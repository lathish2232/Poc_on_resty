from flask_resty import Api

from . import app, views

api = Api(app, prefix='/app/v1')

api.add_resource("/users/", views.UserListView)
api.add_resource("/search/updatenamed/<id>", views.NamedSearchView)
api.add_resource("/search/addnamed/", views.NamedSearchListView)

