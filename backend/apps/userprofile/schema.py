from graphene_django import DjangoObjectType
import graphene
from .models import UserProfile
from .models import Brawler
from apps.brawler.schema import BrawlerType


class UserProfileType(DjangoObjectType):
    class Meta:
        model = UserProfile


class Query(graphene.ObjectType):
    user_profile = graphene.Field(UserProfileType,
                             id=graphene.Int(), 
                             level=graphene.Int(),
                             )
    user_profiles = graphene.List(UserProfileType)

    def resolve_user_profile(self, context, id=None, level=None):
        if id is not None:
            return UserProfile.objects.get(pk=id)
        return None
        if level is not None:
            return UserProfile.objects.get(level=level)
        return None

    def resolve_user_profiles(self, context):
        return UserProfile.objects.all()


class CreateUserProfileMutation(graphene.Mutation):
    class Arguments:
        # The input arguments for this mutation
        selected_brawler = graphene.Int(required=True)
        coins = graphene.Int(required=True)
        trophy = graphene.Int(required=True)
        gems = graphene.Int(required=True)
        xp = graphene.Int(required=True)

    # The class attributes define the response of the mutation
    user_profile_type = graphene.Field(UserProfileType)
    ok = graphene.Boolean()

    def mutate(self, selected_brawler, coins, trophy, gems, xp):
        # Check id object.get on id = selected_brawler
        if(Brawler.objects.get(selected_brawler)):
            user_profile = UserProfile.objects.create(
                selected_brawler, 
                coins, 
                trophy, 
                gems, 
                xp
            )
            return CreateUserProfileMutation(user_profile=user_profile, ok=True)
        else:
            return {"error" : "nope"}


class Mutation(graphene.ObjectType):
    create_user_profile = CreateUserProfileMutation.Field()


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


