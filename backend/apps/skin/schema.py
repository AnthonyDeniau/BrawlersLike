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
        price = graphene.Int()
        model_file = graphene.String()
        texture_file = graphene.String()
        voice_line_file = graphene.String()

    ok = graphene.Boolean()
    skin = graphene.Field(SkinType)

    @staticmethod
    def mutate(root, info, name, description, avatar, price, model_file,
               texture_file, voice_line_file):
        skin = Skin.objects.create(name=name,
                                   description=description,
                                   avatar=avatar,
                                   price=price,
                                   model_file=model_file,
                                   texture_file=texture_file,
                                   voice_line_file=voice_line_file)
        ok = True
        return CreateSkin(skin=skin, ok=ok)


class UpdateSkin(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        name = graphene.String()
        description = graphene.String()
        avatar = graphene.String()
        price = graphene.Int()
        model_file = graphene.String()
        texture_file = graphene.String()
        voice_line_file = graphene.String()

    ok = graphene.Boolean()
    skin = graphene.Field(SkinType)

    @staticmethod
    def mutate(root, info, **kwargs):
        skin = Skin.objects.get(pk=kwargs['id'])
        for _, v in kwargs.items():
            skin.k = v
        skin.save()
        ok = True
        return UpdateSkin(skin=skin, ok=ok)


class DeleteSkin(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    ok = graphene.Boolean()
    skin = graphene.Field(SkinType)

    @staticmethod
    def mutate(root, info, id):
        skin = Skin.objects.get(pk=id)
        skin.delete()
        ok = True
        return DeleteSkin(skin=skin, ok=ok)


class Mutation(graphene.ObjectType):
    create_skin = CreateSkin.Field()
    update_skin = UpdateSkin.Field()
    delete_skin = DeleteSkin.Field()


class Query(graphene.ObjectType):
    skin = graphene.Field(
        SkinType,
        id=graphene.Int(),
        name=graphene.String(),
        description=graphene.String(),
        avatar=graphene.String(),
        price=graphene.Int(),
        model_file=graphene.String(),
        texture_file=graphene.String(),
        voice_line_file=graphene.String(),
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
