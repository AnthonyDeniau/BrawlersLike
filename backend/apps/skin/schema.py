from graphene_django import DjangoObjectType
import graphene
from .models import Skin


class SkinType(DjangoObjectType):

    class Meta:
        model = Skin

class CreateSkin(graphene.Mutation):
    class Arguments:
        # The input arguments for this mutation
        name=graphene.String(required=True)
        description=graphene.String(required=True)
        avatar=graphene.String(required=False)
        price=graphene.Int(required=True)
        modelfile=graphene.String(required=False)
        texturefile=graphene.String(required=False)
        voicelinefile=graphene.String(required=False)

    # The class attributes define the response of the mutation
    skin = graphene.Field(SkinType)
    ok = graphene.Boolean()

    def mutate(self, info, name, description, avatar, price, modelfile,
               texturefile,voicelinefile):
        skin = Skin.objects.create(name=name,
                                         description=description,
                                         avatar=avatar,
                                         price=price,
                                         modelfile=modelfile,
                                         texturefile=texturefile,
                                         voicelinefile=voicelinefile)
        # Notice we return an instance of this mutation
        return CreateSkin(skin=skin, ok=True)

class UpdateSkin(graphene.Mutation):
    class Arguments:
        name=graphene.String(required=True)
        description=graphene.String(required=True)
        avatar=graphene.String(required=False)
        price=graphene.Int(required=True)
        modelfile=graphene.String(required=False)
        texturefile=graphene.String(required=False)
        voicelinefile=graphene.String(required=False)

    ok = graphene.Boolean()
    Skin = graphene.Field(SkinType)

    def mutate(root, info, **kwargs):
        skin = Skin.objects.get(pk=kwargs['id'])
        for k, v in kwargs.items():
            skin.k = v
        skin.save()
        ok = True
        return UpdateSkin(person=skin, ok=ok)


class DeleteSkin(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    ok = graphene.Boolean()

    def mutate(root, info, id):
        skin = Skin.objects.get(pk=id)
        skin.delete()
        ok = True
        return DeleteSkin(person=skin, ok=ok)


class Mutation(graphene.ObjectType):
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
