import graphene
from apps.brawler import schema as brawler_schema
from apps.userprofile import schema as userprofile_schema
from apps.userprofilebrawler import schema as userprofilebrawler_schema
from apps.projectilPattern import schema as projectilpattern_schema
from apps.skin import schema as skin_schema


class Query(
        brawler_schema.Query, 
        userprofile_schema.Query,
        userprofilebrawler_schema.Query, 
        projectilpattern_schema.Query,
        skin_schema.Query,
        graphene.ObjectType
    ):
    pass


class Mutation(
        brawler_schema.Mutation, 
        skin_schema.Mutation, 
        graphene.ObjectType
    ):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)