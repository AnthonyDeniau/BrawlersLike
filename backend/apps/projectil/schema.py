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

class UpdateProjectil(graphene.Mutation):
    class Arguments:
        name=graphene.String()
        sprite=graphene.String()
        speed=graphene.Decimal()
        hitboxSize=graphene.Decimal()
        damage=graphene.Int()
        range=graphene.Decimal()

    ok = graphene.Boolean()
    projectil = graphene.Field(lambda: Projectil)

    def mutate(root, info, **kwargs):
        projectil = Projectil.objects.get(pk=kwargs['id'])
        for k, v in kwargs.items():
            projectil.k = v
        projectil.save()
        ok = True
        return UpdateProjectil(person=projectil, ok=ok)

class DeleteProjectil(graphene.Mutation):
    class Arguments:
        id=graphene.ID()

    ok = graphene.Boolean()

    def mutate(root, info, id):
        projectil = Projectil.objects.get(pk=id)
        projectil.delete()
        ok = True
        return DeleteProjectil(person=projectil, ok=ok)

class Mutations(graphene.ObjectType):
    create_projectil = CreateProjectil.Field()
    update_projectil = UpdateProjectil.Field()  
    delete_projectil = DeleteProjectil.Field()


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