from graphene_django import DjangoObjectType
import graphene
from .models import Skin

class SkinType(DjangoObjectType):
    #determination de l'objet
    class Meta:
        model = Skin

#Fonction de création de skin
# class CreateSkin(graphene.Mutation)
# #Champs utilisé
#     class Arguments:
#         name = graphene.String(required=True)
#         Description = graphene.String(required=True)
#         Avatar = graphene.String(required=True)
#         Price = graphene.Decimal(required=True)
#         Model3DFile = graphene.String(required=True)
#         TextureFile = graphene.String(required=True)
#         VoiceLineFile = graphene.String(required=True)
#         #Ajout d'un boolean en plus pour renvoyer quand la requête est bonne
#     ok = graphene.Boolean()
#     skin = graphene.Field(SkinType)

# #constructeur
#     def mutate(root, info, name, Description, Avatar, Price, Model3DFile, TextureFile, VoiceLineFile):
#         skin = Skin.objects.create(
#             name=name, 
#             Description=Description,
#             Avatar=Avatar,
#             Price=Price,
#             Model3DFile=Model3DFile,
#             TextureFile=TextureFile,
#             VoiceLineFile= VoiceLineFile)
#         ok = True
#         return CreateSkin(skinCreate=skin, ok=ok)

#creation d'une requête de récupération des données
class Query(graphene.ObjectType):
   
    skin = graphene.Field(SkinType,
                        id=graphene.Int())
    skins = graphene.List(SkinType)

    def resolve_skin(self, context, id=None):
        if id is not None:
            return skin.objects.get(pk=id)
        return None

    def resolve_skins(self, context):
        return skin.objects.all()

# class ModifySkin(graphene.mutation)
#     Arguments:
#         id = graphene.Int()

#         def ModifySkin(id):
#             if(skins.get(pk=id)
#                 skins.objects.mutation({
#                 name=name, 
#                 Description=Description,
#                 Avatar=Avatar,
#                 Price=Price,
#                 Model3DFile=Model3DFile,
#                 TextureFile=TextureFile,
#                 VoiceLineFile= VoiceLineFile)
#                 })
#                 ok= true
#             else 
#                 ok = false
#     return ok

# class DeleteSkin(graphene.mutation)
#     Arguments:
#         id = graphene.Int()

#         def DeleteSkin(id):
#             if(skins.get(pk=id)
#                 skins.objects.delete()
#                 ok= true
#             else 
#                 'Veuillez selectionner un skin à supprimer'
#                 ok = false
#         return ok




                