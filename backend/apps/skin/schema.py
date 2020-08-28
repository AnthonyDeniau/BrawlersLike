from graphene_django import DjangoObjectType
import graphene
from .models import Skin


class SkinType(DjangoObjectType):
    class Meta:
        model = Skin


class CreateSkin(graphene.Mutation):
    class Arguments:

        name = graphene.String()
        description = graphene.String()
        avatar = graphene.String()
        price = graphene.Decimal()
        ThreeDModelFile = graphene.String()
        TextureFile = graphene.String()
        VoiceLineFile = graphene.String()

    ok = graphene.Boolean()
    skin = graphene.Field(lambda: skin)

    def mutate(root, info, name, description, avatar, price, ThreeDModelFile, TextureFile, VoiceLineFile):
        projectilPattern = skin.objects.create(
            name=name,
            description=description,
            avatar=avatar,
            price=price,
            ThreeDModelFile = ThreeDModelFile,
            TextureFile = TextureFile,
            VoiceLineFile = VoiceLineFile)
        ok = True
        return CreateSkin(person=skin, ok=ok)


class UpdateSkin(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        description = graphene.String()
        avatar = graphene.String()
        price = graphene.Decimal()
        ThreeDModelFile = graphene.String()
        TextureFile = graphene.String()
        VoiceLineFile = graphene.String()

    ok = graphene.Boolean()
    skin = graphene.Field(lambda: skin)

    def mutate(root, info, **kwargs):
        skin = skin.objects.get(pk=kwargs['id'])
        for k, v in kwargs.items():
            skin.k = v
        skin.save()
        ok = True
        return skin(person=skin, ok=ok)

class DeleteSkin(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    ok = graphene.Boolean()

    def mutate(root, info, id):
        skin = Skin.objects.get(pk=id)
        skin.delete()
        ok = True
        return DeleteSkin(person=skin, ok=ok)


class Mutations(graphene.ObjectType):
    create_skin = CreateSkin.Field()
    update_skin = UpdateSkin.Field()
    delete_skin = DeleteSkin.Field()


class Query(graphene.ObjectType):
    skin = graphene.Field(SkinType, id=graphene.Int())
    skins = graphene.List(SkinType)

    def resolve_skin(self, context, id=None):
        if id is not None:
            return Skin.objects.get(pk=id)
        return None

    def resolve_skins(self, context):
        return Skin.objects.all()