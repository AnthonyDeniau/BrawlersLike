from graphene_django import DjangoObjectType
import graphene
from .models import Brawler


class BrawlerType(DjangoObjectType):
    class Meta:
        model = Brawler


class Query(graphene.ObjectType):
    brawler = graphene.Field(BrawlerType,
                             id=graphene.Int(),
                             name=graphene.String(),
                             description=graphene.String(),
                             cost=graphene.Float())
    brawlers = graphene.List(BrawlerType)

    def resolve_brawler(self, context, id=None, name=None):
        if id is not None:
            return Brawler.objects.get(pk=id)

        if name is not None:
            return Brawler.objects.get(name=name)

        return None

    def resolve_brawlers(self, context):
        return Brawler.objects.all()
