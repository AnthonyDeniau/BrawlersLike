from graphene_django import DjangoObjectType
import graphene
from .models import Equipment


class EquipmentType(DjangoObjectType):
    class Meta:
        model = Equipment


class Query(graphene.ObjectType):

    equipment = graphene.Field(
        EquipmentType,
        id=graphene.Int(),
        name=graphene.String(),
    )
    equipments = graphene.List(EquipmentType)

    def resolve_equipment(self, context, id=None, name=None):
        if id is not None:
            return Equipment.objects.get(pk=id)
        if name is not None:
            return Equipment.objects.get(name=name)
        return None

    def resolve_equipments(self, context):
        return Equipment.objects.all()


class CreateEuipmentMutation(graphene.Mutation):
    class Arguments:
        # The input arguments for this mutation
        name = graphene.String(required=True)
        cost = graphene.Int(required=True)
        description = graphene.String(required=True)

    # The class attributes define the response of the mutation
    equipment = graphene.Field(EquipmentType)
    ok = graphene.Boolean()

    def mutate(self, info, name, cost, description,):
        equipment = Equipment.objects.create(name=name,
                                             cost=cost,
                                             description=description,
                                             )
        # Notice we return an instance of this mutation
        return CreateEuipmentMutation(equipment=equipment, ok=True)


class Mutation(graphene.ObjectType):
    create_equipment = CreateEuipmentMutation.Field()
