from graphene_django import DjangoObjectType
import graphene
from .models import ProjectilPattern


class ProjectilPatternType(DjangoObjectType):
    def resolve_interval(self, info):
        return self.interval.total_seconds()

    class Meta:
        model = ProjectilPattern


class CreateProjectilPattern(graphene.Mutation):
    class Arguments:

        number = graphene.Int()
        interval = graphene.Int()
        spreadAngle = graphene.Decimal()
        range = graphene.Decimal()

    ok = graphene.Boolean()
    projectilPattern = graphene.Field(lambda: ProjectilPattern)

    def mutate(root, info, number, interval, spreadAngle, range):
        projectilPattern = ProjectilPattern.objects.create(
            number=number,
            interval=interval,
            spreadAngle=spreadAngle,
            range=range)
        ok = True
        return CreateProjectilPattern(person=projectilPattern, ok=ok)


class UpdateProjectilPattern(graphene.Mutation):
    class Arguments:
        number = graphene.Int()
        interval = graphene.Int()
        spreadAngle = graphene.Decimal()
        range = graphene.Decimal()

    ok = graphene.Boolean()
    projectilPattern = graphene.Field(lambda: ProjectilPattern)

    def mutate(root, info, **kwargs):
        projectilPattern = ProjectilPattern.objects.get(pk=kwargs['id'])
        for k, v in kwargs.items():
            projectilPattern.k = v
        projectil.save()
        ok = True
        return UpdateProjectilPattern(person=projectilPattern, ok=ok)


class DeleteProjectilPattern(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    ok = graphene.Boolean()

    def mutate(root, info, id):
        projectilPattern = ProjectilPattern.objects.get(pk=id)
        projectilPattern.delete()
        ok = True
        return DeleteProjectilPattern(person=projectilPattern, ok=ok)


class Mutations(graphene.ObjectType):
    create_projectilPattern = CreateProjectilPattern.Field()
    update_projectilPattern = UpdateProjectilPattern.Field()
    delete_projectilPattern = DeleteProjectilPattern.Field()


class Query(graphene.ObjectType):
    projectilPattern = graphene.Field(ProjectilPatternType, id=graphene.Int())
    projectilPatterns = graphene.List(ProjectilPatternType)

    def resolve_projectilPattern(self, context, id=None):
        if id is not None:
            return ProjectilPattern.objects.get(pk=id)
        return None

    def resolve_projectilPatterns(self, context):
        return ProjectilPattern.objects.all()