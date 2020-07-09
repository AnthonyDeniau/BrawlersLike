from graphene_django import DjangoObjectType
import graphene
from .models import UserProfile
from apps.brawler.schema import BrawlerType


class UserProfileType(DjangoObjectType):
    class Meta:
        model = UserProfile


class Query(graphene.ObjectType):
    user_profile = graphene.Field(UserProfileType,
                             id=graphene.Int())
    user_profiles = graphene.List(UserProfileType)

    def resolve_user_profile(self, context, id=None):
        if id is not None:
            return UserProfile.objects.get(pk=id)
        return None

    def resolve_user_profiles(self, context):
        return UserProfile.objects.all()


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


