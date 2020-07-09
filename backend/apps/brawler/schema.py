from graphene_django import DjangoObjectType
import graphene
from .models import Brawler, Rarity


class BrawlerType(DjangoObjectType):
    rarity_text = graphene.String()

    class Meta:
        model = Brawler

    def resolve_rarity_text(self, context):
        return str(self.rarity)


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


class CreateBrawlerMutation(graphene.Mutation):
    class Arguments:
        # The input arguments for this mutation
        name = graphene.String(required=True)
        cost = graphene.Int(required=True)
        description = graphene.String(required=True)
        avatar = graphene.String(required=True)
        rarity = graphene.String()
        health = graphene.Int(required=True)
        speed = graphene.Int(required=True)

    # The class attributes define the response of the mutation
    brawler = graphene.Field(BrawlerType)
    ok = graphene.Boolean()

    def mutate(self, info, name, cost, description, avatar, rarity, health,
               speed):
        brawler = Brawler.objects.create(name=name,
                                         cost=cost,
                                         description=description,
                                         avatar=avatar,
                                         rarity=Rarity.CLASSIC,
                                         health=health,
                                         speed=speed)
        # Notice we return an instance of this mutation
        return CreateBrawlerMutation(brawler=brawler, ok=True)


class Mutation(graphene.ObjectType):
    create_brawler = CreateBrawlerMutation.Field()
