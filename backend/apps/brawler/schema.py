from graphene_django import DjangoObjectType
import graphene
from .models import Brawler, Rarity


class BrawlerType(DjangoObjectType):
    rarity_text = graphene.String()

    class Meta:
        model = Brawler

    def resolve_rarity_text(self, id):
        return str(self.rarity)


class Query(graphene.ObjectType):
    brawler = graphene.Field(
        BrawlerType,
        id=graphene.Int(),
        name=graphene.String(),
    )
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


class UpdateBrawlerMutation(graphene.Mutation):
    class Arguments:
        # The input arguments for this mutation
        id = graphene.ID(required=True)
        name = graphene.String(required=False)
        cost = graphene.Int(required=False)
        description = graphene.String(required=False)
        avatar = graphene.String(required=False)
        rarity = graphene.String(required=False)
        health = graphene.Int(required=False)
        speed = graphene.Int(required=False)

    # The class attributes define the response of the mutation
    brawler = graphene.Field(BrawlerType)

    def mutate(self,
               info,
               id,
               name=None,
               cost=None,
               description=None,
               avatar=None,
               rarity=None,
               health=None,
               speed=None):
        brawler = Brawler.objects.get(pk=id)
        if name:
            brawler.name = name
        if cost:
            brawler.cost = cost
        if description:
            brawler.description = description
        if avatar:
            brawler.avatar = avatar
        if health:
            brawler.health = health
        if speed:
            brawler.speed = speed
        if rarity:
            brawler.rarity = rarity

        brawler.save()
        # Notice we return an instance of this mutation
        return UpdateBrawlerMutation(brawler=brawler)


class Mutation(graphene.ObjectType):
    create_brawler = CreateBrawlerMutation.Field()
    update_brawler = UpdateBrawlerMutation.Field()
