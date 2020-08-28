from graphene_django import DjangoObjectType
import graphene
from .models import Skin


class SkinType(DjangoObjectType):
    class Meta:
        model = Skin


class Query(graphene.ObjectType):
    skin = graphene.Field(
        SkinType, 
        id=graphene.Int(), 
        name=graphene.String()
    )
    skins = graphene.List(SkinType)

    def resolve_skin(self, context, id=None):
        if id is not None:
            return Skin.objects.get(pk=id)
        return None

    def resolve_skins(self, context):
        return Skin.objects.all()


class CreateSkinMutation(graphene.Mutation):
    class Arguments:
        name =          graphene.String(required=True)
        description =   graphene.String(required=True)
        avatar =        graphene.String(required=True)
        price =         graphene.Int()
        model_file =    graphene.String(required=True)
        texture_file =  graphene.String(required=True)
        voice_line_file = graphene.String(required=True)

    skin = graphene.Field(SkinType)
    ok = graphene.Boolean()

    def mutate(self, info, name, description, avatar, price, model_file, texture_file, voice_line_file):
        skin = Skin.objects.create(
            name = name,
            description = description,
            avatar = avatar,
            price = price,
            model_file = model_file,
            texture_file = texture_file,
            voice_line_file = voice_line_file
        )
        return CreateSkinMutation(skin=skin, ok=True)


class UpdateSkin(graphene.Mutation):
    class Arguments:
        name =          graphene.String(required=True)
        description =   graphene.String(required=True)
        avatar =        graphene.String(required=True)
        price =         graphene.Int()
        model_file =    graphene.String(required=True)
        texture_file =  graphene.String(required=True)
        voice_line_file = graphene.String(required=True)

    ok = graphene.Boolean()
    skin = graphene.Field(lambda: Skin)

    def mutate(root, info, **kwargs):
        pass


class DeleteSkin(graphene.Mutation):
    class Arguments:
        id=graphene.ID()

    ok = graphene.Boolean()

    def mutate(root, info, id):
        ability = Ability.objects.get(pk=id)
        ability.delete()
        ok = True
        return DeleteAbility(person=ability, ok=ok)


class Mutation(graphene.ObjectType):
    create_skin = CreateSkinMutation.Field()
    #update_skin = UpdateSkinMutation.Field()
    #delete_skin = DeleteSkinMutation.Field()

