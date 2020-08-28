from graphene_django import DjangoObjectType
import graphene
from .models import UserProfile
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
        return skin.objects.all()


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


