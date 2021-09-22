from marshmallow import Schema, fields


class UserSchema(Schema):
    user_id = fields.String(required=True)
    user_name =fields.String(required=True)

class NamedSearchSchema(Schema):
    id = fields.Int(dump_only=True)
    accont_id = fields.String(required=True)
    name = fields.String(required=True)
    criteria = fields.String(required=True)
    Last_executed = fields.DateTime(dump_only=True)
    created_date = fields.DateTime(dump_only=True)


class RecentSearchSchema(Schema):
    pass