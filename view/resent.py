# import operator
# from flask_resty import (
#     ColumnFilter,
#     Filtering,
#     GenericModelView,
#     NoOpAuthentication,
#     NoOpAuthorization,
#     PagePagination,
#     Sorting,
# )
# #from flask_resty import Api


# from app import app
# from model.recent import MobiUsers,NamedSearch
# from schema.recent import UserSchema, NamedSearchSchema

# from flask_restx import reqparse, Api, Resource, fields

# api = Api(app)  #rest plus

# @api.route('/users')
# @api.response(200, 'Successful')
# class UserViewBase(GenericModelView):
#     model = MobiUsers
#     schema = UserSchema()

#     authentication = NoOpAuthentication()
#     authorization = NoOpAuthorization()

#     pagination = PagePagination(page_size=10)


# class UserListView(UserViewBase):
#     def get(self):
#         return self.list()

#     def post(self):
#         return self.create()

# api.add_resource(UserListView,'/users', methods=['GET'])

# @api.route('/test')
# @api.response(200, 'Successful')

# class Atms(Resource):
#     def get(self):
#         print('---------------i am in')
#         resp={"code":200,"message":"This is a test url"}
#         return resp

# api.add_resource(Atms, '/test', methods=['GET'])