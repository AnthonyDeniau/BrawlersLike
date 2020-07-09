import graphene
from apps.brawler import schema as brawler_schema
from apps.userprofile import schema as userprofile_schema


class Query(brawler_schema.Query, graphene.ObjectType):
    pass

class Query(userprofile_schema.Query, graphene.ObjectType):
    pass

class Mutation(graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)