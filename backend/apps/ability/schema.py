from graphene_django import DjangoObjectType
import graphene
from .models import Ability


class AbilityType(DjangoObjectType):
    class Meta:
        model = Ability

class CreateAbility(graphene.Mutation):
    class Arguments:
        name=graphene.String()
        sprite=graphene.String()
        speed=graphene.Decimal()
        hitboxSize=graphene.Decimal()
        damage=graphene.Int()
        range=graphene.Decimal()

    ok = graphene.Boolean()
    ability = graphene.Field(lambda: Ability)

    def mutate(root, info, name, sprite, hitboxSize, damage, range):
        ability = Ability(
            name=name, 
            sprite=graphene.String(),
            speed=graphene.Decimal(),
            hitboxSize=graphene.Decimal(),
            damage=graphene.Int(),
            range=graphene.Decimal())
        ok = True
        return CreateAbility(person=ability, ok=ok)

class UpdateAbility(graphene.Mutation):
    class Arguments:
        name=graphene.String()
        sprite=graphene.String()
        speed=graphene.Decimal()
        hitboxSize=graphene.Decimal()
        damage=graphene.Int()
        range=graphene.Decimal()

    ok = graphene.Boolean()
    ability = graphene.Field(lambda: Ability)

    def mutate(root, info, **kwargs):
        ability = Ability.objects.get(pk=kwargs['id'])
        for k, v in kwargs.items():
            ability.k = v
        ability.save()
        ok = True
        return UpdateAbility(person=ability, ok=ok)

class DeleteAbility(graphene.Mutation):
    class Arguments:
        id=graphene.ID()

    ok = graphene.Boolean()

    def mutate(root, info, id):
        ability = Ability.objects.get(pk=id)
        ability.delete()
        ok = True
        return DeleteAbility(person=ability, ok=ok)

class AbilityMutations(graphene.ObjectType):
    create_ability = CreateAbility.Field()
    update_ability = UpdateAbility.Field()  
    delete_ability = DeleteAbility.Field()

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
