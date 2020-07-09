from graphene_django import DjangoObjectType
import graphene
from .models import Projectil


class ProjectilType(DjangoObjectType):
    class Meta:
        model = Projectil

class CreateProjectil(graphene.Mutation):
    class Arguments:
        name=graphene.String()
        sprite=graphene.String()
        speed=graphene.Decimal()
        hitboxSize=graphene.Decimal()
        damage=graphene.Int()
        range=graphene.Decimal()

    ok = graphene.Boolean()
    projectil = graphene.Field(lambda: Projectil)

    def mutate(root, info, name, sprite, hitboxSize, damage, range):
        projectil = Projectil(
            name=name, 
            sprite=graphene.String(),
            speed=graphene.Decimal(),
            hitboxSize=graphene.Decimal(),
            damage=graphene.Int(),
            range=graphene.Decimal())
        ok = True
        return CreateProjectil(person=projectil, ok=ok)

class ProjectilMutations(graphene.ObjectType):
    create_projectil = CreateProjectil.Field()

class Query(graphene.ObjectType):
    projectil = graphene.Field(ProjectilType,
                             id=graphene.Int(),
                             sprite=graphene.String(),
                             speed=graphene.Decimal(),
                             hitboxSize=graphene.Decimal(),
                             damage=graphene.Int(),
                             range=graphene.Decimal())
    projectils = graphene.List(ProjectilType)




    def resolve_projectil(self, context, id=None, name=None):
        if id is not None:
            return Projectil.objects.get(pk=id)

        if name is not None:
            return Projectil.objects.get(name=name)

        return None

    def resolve_projectils(self, context):
        return Projectil.objects.all()

schema = graphene.Schema(query=Query, mutation=ProjectilMutations)