from graphene_django import DjangoObjectType
import graphene
from .models import ProjectilPattern


class ProjectilPatternType(DjangoObjectType):
    class Meta:
        model = ProjectilPattern


class Query(graphene.ObjectType):
    projectilPattern = graphene.Field(ProjectilPatternType,
                             id=graphene.Int(),
                             number=graphene.Int(),
                             interval=graphene.Int(),
                             spreadAngle=graphene.Decimal()
                             range=graphene.Decimal())
    projectilPatterns = graphene.List(ProjectilPattern)

    def resolve_projectilPattern(self, context, id=None, name=None):
        if id is not None:
            return ProjectilPattern.objects.get(pk=id)

        if number is not None:
            return ProjectilPattern.objects.get(number=number)
        
        if interval is not None:
            return ProjectilPattern.objects.get(interval=interval)
        
        if spreadAngle is not None:
            return ProjectilPattern.objects.get(spreadAngle=spreadAngle)
        
        if range is not None:
            return ProjectilPattern.objects.get(range=range)

        return None

    def resolve_projectilPatterns(self, context):
        return ProjectilPattern.objects.all()
