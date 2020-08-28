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

    def Mutations(root, info, brawler,isSuper,name, description, reloadSpeed, attackSpeed, projectilPattern):
        ability = Ability(
            brawler=brawler,
            isSuper=isSuper,
            name=name, 
            description=graphene.String(),
            image=graphene.String(),
            reloadSpeed=graphene.Decimal(),
            attackSpeed=graphene.Decimal(),
            projectilPattern=projectilPattern())
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
                             name=graphene.String())
    abilitys = graphene.List(AbilityType)

    def resolve_ability(self, context, id=None, name=None):
        if id is not None:
            return Ability.objects.get(pk=id)

        if name is not None:
            return Ability.objects.get(name=name)

        return None

    def resolve_abilitys(self, context):
        return Ability.objects.all()
