from graphene_django import DjangoObjectType
import graphene
from .models import Ability


class AbilityType(DjangoObjectType):
    class Meta:
        model = Ability


class Query(graphene.ObjectType):
    ability = graphene.Field(Ability,
                             id=graphene.Int(),
                             name=graphene.String(),
                             description=graphene.String(),
                             cost=graphene.Float())
    ability = graphene.List(Ability)

    def resolve_brawler(self, context, id=None, name=None):
        if id is not None:
            return Ability.objects.get(pk=id)

        if name is not None:
            return Ability.objects.get(name=name)

        return None

    def resolve_abilitys(self, context):
        return Ability.objects.all()
