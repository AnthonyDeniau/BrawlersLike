from graphene_django import DjangoObjectType
import graphene
from .models import Ability


class AbilityType(DjangoObjectType):
    class Meta:
        model = Ability


class Query(graphene.ObjectType):
    ability = graphene.Field(AbilityType,
                             id=graphene.Int(),
                             name=graphene.String(),
                             description=graphene.String(),
                             cost=graphene.Float())
    abilitys = graphene.List(AbilityType)

    def resolve_ability(self, context, id=None):
        if id is not None:
            return Ability.objects.get(pk=id)

        return None

    def resolve_abilitys(self, context):
        return Ability.objects.all()
