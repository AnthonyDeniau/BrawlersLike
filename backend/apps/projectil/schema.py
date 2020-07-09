from graphene_django import DjangoObjectType
import graphene
from .models import Projectil


class ProjectilType(DjangoObjectType):
    class Meta:
        model = Projectil


class Query(graphene.ObjectType):
    brawler = graphene.Field(ProjectilType,
                             id=graphene.Int(),
                             name=graphene.String(),
                             description=graphene.String(),
                             cost=graphene.Float())
    brawlers = graphene.List(ProjectilType)

    def resolve_brawler(self, context, id=None, name=None):
        if id is not None:
            return Projectil.objects.get(pk=id)

        if name is not None:
            return Projectil.objects.get(name=name)

        return None

    def resolve_brawlers(self, context):
        return Projectil.objects.all()