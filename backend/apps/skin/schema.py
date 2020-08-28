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
        name=graphene.String(),
    )
    skins = graphene.List(SkinType)

    def resolve_skin(self, context, id=None, name=None):
        if id is not None:
            return Skin.objects.get(pk=id)

        if name is not None:
            return Skin.objects.get(name=name)

        return None

    def resolve_skins(self, context):
        return Skin.objects.all()


class CreateSkinMutation(graphene.Mutation):
    class Arguments:
        # The input arguments for this mutation
        name = graphene.String(required=True)
        description = graphene.String(required=True)
        avatar = graphene.String(required=True)
        price = graphene.Int(required=True)
        modelFile = graphene.String(required=True)
        textureFile = graphene.String(required=True)
        voiceLineFile = graphene.String(required=True)

    # The class attributes define the response of the mutation
    skin = graphene.Field(SkinType)
    ok = graphene.Boolean()

    def mutate(self, info, name, description, avatar, price, modelFile, textureFile, voiceLineFile):
        skin = Skin.objects.create(name=name,
                                   description=description,
                                   avatar=avatar,
                                   price=price,
                                   modelFile=modelFile,
                                   textureFile=textureFile,
                                   voiceLineFile=voiceLineFile)
        # Notice we return an instance of this mutation
        return CreateSkinMutation(skin=skin, ok=True)


class UpdateSkinMutation(graphene.Mutation):
    class Arguments:
        # The input arguments for this mutation
        id = graphene.ID(required=True)
        name = graphene.String(required=False)
        description = graphene.String(required=False)
        avatar = graphene.String(required=False)
        price = graphene.Int(required=False)
        modelFile = graphene.String(required=False)
        textureFile = graphene.String(required=False)
        voiceLineFile = graphene.String(required=False)

    # The class attributes define the response of the mutation
    skin = graphene.Field(SkinType)

    def mutate(self,
               info,
               id,
               name=None,
               description=None,
               avatar=None,
               price=None,
               modelFile=None,
               textureFile=None,
               voiceLineFile=None):
        skin = Skin.objects.get(pk=id)
        if name:
            skin.name = name
        if description:
            skin.description = description
        if avatar:
            skin.avatar = avatar
        if price:
            skin.price = price
        if modelFile:
            skin.modelFile = modelFile
        if textureFile:
            skin.textureFile = textureFile
        if voiceLineFile:
            skin.voiceLineFile = voiceLineFile

        skin.save()
        # Notice we return an instance of this mutation
        return UpdateSkinMutation(skin=skin)


class DeleteSkinMutation(graphene.Mutation):
    class Arguments:
        # The input arguments for this mutation
        id = graphene.ID(required=True)
        name = graphene.String(required=False)

    # The class attributes define the response of the mutation
    is_deleted = graphene.Boolean()

    def mutate(self, info, id, name=None):
        skin = Skin.objects.get(pk=id)
        skin.delete()
        # Notice we return an instance of this mutation
        return DeleteSkinMutation(is_deleted=True)


class Mutation(graphene.ObjectType):
    create_skin = CreateSkinMutation.Field()
    update_skin = UpdateSkinMutation.Field()
    delete_skin = DeleteSkinMutation.Field()
