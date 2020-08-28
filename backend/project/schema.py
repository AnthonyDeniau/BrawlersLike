import graphene
from apps.brawler import schema as brawler_schema
from apps.userprofile import schema as userprofile_schema
from apps.userprofilebrawler import schema as userprofilebrawler_schema
from apps.equipment import schema as equipment_schema


class Query(brawler_schema.Query, equipment_schema.Query, userprofile_schema.Query,
            userprofilebrawler_schema.Query, graphene.ObjectType):
    pass


class Mutation(brawler_schema.Mutation, equipment_schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
