import graphene
from apps.brawler import schema as brawler_schema
from apps.userprofile import schema as userprofile_schema
from apps.userprofilebrawler import schema as userprofilebrawler_schema
from apps.projectilPattern import schema as projectilpattern_schema


class Query(brawler_schema.Query, userprofile_schema.Query,
            userprofilebrawler_schema.Query, projectilpattern_schema.Query,
            graphene.ObjectType):
    pass


class Mutation(projectil_schema.Mutations, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
