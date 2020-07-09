from graphene_django import DjangoObjectType
import graphene
from .models import UserProfileBrawler
from apps.brawler.schema import BrawlerType


class UserProfileBrawlerType(DjangoObjectType):
    class Meta:
        model = UserProfileBrawler


class Query(graphene.ObjectType):
    user_profile_brawler = graphene.Field(UserProfileBrawlerType,
                             id=graphene.Int())
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


