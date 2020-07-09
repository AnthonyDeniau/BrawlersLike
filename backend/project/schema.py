import graphene
from apps.brawler import schema as brawler_schema


class Query(brawler_schema.Query, graphene.ObjectType):
    pass


class Mutation(brawler_schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)