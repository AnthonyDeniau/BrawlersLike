import graphene
from apps.brawler import schema as brawler_schema
from apps.ability import schema as ability_schema
from apps.projectil import schema as projectil_schema


class Query(brawler_schema.Query, userprofile_schema.Query,
            userprofilebrawler_schema.Query, graphene.ObjectType):
    pass


class Mutation(projectil_schema.Mutations, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
