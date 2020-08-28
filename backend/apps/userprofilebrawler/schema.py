from graphene_django import DjangoObjectType
import graphene
from .models import UserProfileBrawler
from apps.brawler.schema import BrawlerType


class UserProfileBrawlerType(DjangoObjectType):
    class Meta:
        model = UserProfileBrawler


class CreateUserProfileBrawlerMutation(graphene.Mutation):
    class Arguments:
        brawler = graphene.Int()
        level = graphene.Int()
        power_points = graphene.Int()
        equipments = graphene.Int()
        abilities = graphene.Int()

    ok = graphene.Boolean()
    userProfileBrawler = graphene.Field(lambda: UserProfileBrawler)

    def mutate(root, info, brawler, level, power_points, equipments, abilities):
        userProfileBrawler = UserProfileBrawler.objects.create(
            brawler_id=brawler,
            level=level,
            power_points=power_points, 
            equipments=equipments,
            abilities=abilities
            )
        ok = True
        return CreateUserProfileBrawlerMutation(userProfileBrawler=userProfileBrawler, ok=ok)


class UpdateUserProfileBrawlerMutation(graphene.Mutation):
    class Arguments:
        brawler = graphene.String()
        level = graphene.Int()
        power_points = graphene.String()
        equipments = graphene.Int()
        abilities = graphene.Int()

    ok = graphene.Boolean()
    userProfileBrawler = graphene.Field(lambda: UserProfileBrawler)

    def mutate(root, info, id, **kwargs):
        userProfileBrawler = UserProfileBrawler.objects.get(pk=id)
        for k, v in kwargs.items():
            userProfileBrawler.k = v
        userProfileBrawler.save()
        ok = True
        return UpdateUserProfileBrawlerMutation(UserProfileBrawler=userProfileBrawler, ok=ok)


class DeleteUserProfileBrawlerMutation(graphene.Mutation):
    class Arguments:
        id=graphene.ID()

    ok = graphene.Boolean()

    def mutate(root, info, id):
        userProfileBrawler = UserProfileBrawler.objects.get(pk=id)
        userProfileBrawler.delete()
        ok = True
        return DeleteUserProfileBrawlerMutation(UserProfileBrawler=userProfileBrawler, ok=ok)


class Mutation(graphene.ObjectType):
    create_user_profile_brawler = CreateUserProfileBrawlerMutation.Field()
    update_user_profile_brawler = UpdateUserProfileBrawlerMutation.Field()  
    delete_user_profile_brawler = DeleteUserProfileBrawlerMutation.Field()


class Query(graphene.ObjectType):
    user_profile_brawler = graphene.Field(UserProfileBrawlerType, id=graphene.Int())
    user_profile_brawlers = graphene.List(UserProfileBrawlerType)

    def resolve_user_profile_brawler(self, context, id=None):
        if id is not None:
            return UserProfileBrawler.objects.get(pk=id)
        return None

    def resolve_user_profile_brawlers(self, context):
        return UserProfileBrawler.objects.all()


## query allprofile{
##   userProfiles {
##     id,
##     coins,
##     selectedBrawler{
##       id,
##       name
##     }
##   }
## }
## 
## query profile {
##   userProfile(id:1) {
##     id,
##     coins
##   }
## }


