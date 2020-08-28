from graphene_django import DjangoObjectType
import graphene
from .models import Skin


class SkinType(DjangoObjectType):
    class Meta:
        model = Skin


class Query(graphene.ObjectType):
    skin = graphene.Field(SkinType,
                             id=graphene.Int(), 
                             name=graphene.String(), 
                             description=graphene.String(),
                             avatar=graphene.String(),
                             price=graphene.Int(),
                             modelFile=graphene.String(),
                             textureFile=graphene.String(),
                             voiceLineFile=graphene.String()
                             )
    skins = graphene.List(SkinType)

    def resolve_skin(self, context, id=None):
        if id is not None:
            return Skin.objects.get(pk=id)
        return None

    def resolve_skins(self, context):
        return Skin.objects.all()

class CreateSkin(graphene.Mutation):
    class Arguments:
        name=graphene.String()
        description=graphene.String()
        avatar = graphene.String()
        price = graphene.Int()
        modelFile = graphene.String()
        textureFile = graphene.String()
        voiceLineFile = graphene.String()

    ok = graphene.Boolean()
    skin = graphene.Field(SkinType)

    def mutate(self,info, name, description, avatar, price, modelFile, textureFile, voiceLineFile):
        skin = Skin.objects.create(
            name=name,
            description=description,
            avatar=avatar,
            price=price,
            modelFile=modelFile,
            textureFile=textureFile,
            voiceLineFile=voiceLineFile)
        return CreateSkin(skin=skin, ok=True)

class DeleteSkin(graphene.Mutation):
    class Arguments:
        id=graphene.ID()

    ok = graphene.Boolean()

    def mutate(root, info, id):
        skin = Skin.objects.get(pk=id)
        skin.delete()
        return DeleteSkin(ok=True)

class UpdateSkin(graphene.Mutation):
    class Arguments:
        id=graphene.ID()
        name=graphene.String()
        description=graphene.String()
        avatar = graphene.String()
        price = graphene.Int()
        modelFile = graphene.String()
        textureFile = graphene.String()
        voiceLineFile = graphene.String()
        
    ok = graphene.Boolean()
    skin = graphene.Field(SkinType)

    def mutate(root, info, **kwargs):
        skin = Skin.objects.get(pk=kwargs['id'])
        for k, v in kwargs.items():
            if k!='id':
                setattr(skin, k, v)
        skin.save()
        return UpdateSkin(skin=skin, ok=True)


class Mutation(graphene.ObjectType):
    create_skin = CreateSkin.Field()
    delete_skin = DeleteSkin.Field()
    update_skin = UpdateSkin.Field()

####### requete a executer sur graphql #######

## pour recuperer l'ensemble des skins
'''
query allSkins{
  skins{
    id,
    name
  }
}
'''

## pour recuperer un unique skin via son id - Ici on recuperer le skin avec l'id 2
'''
query skin {
  skin(id:2) {
    name
  }
}
'''

## pour creer un skin 

'''
mutation createSkin {
  createSkin(name: "skin Feu", description: "magnifique", 
    avatar: "https://www.google.com/image.png",
    price: 10,  modelFile: "https://www.google.com/image.png", 
    textureFile: "https://www.google.com/image.png",
    voiceLineFile: "https://www.google.com/image.png"  ){
    ok
    skin {
      id
    }
  }
}
'''

## pour supprimer un skin 

'''
mutation deleteSkin {
  deleteSkin(id: 3) {
    ok
  }
}
'''

## pour update un skin 

'''
mutation updateSkin {
  updateSkin(
    id:6,
    name:"skin Glace"
  )
  {
    ok
    skin {
      id
    }
  }
}
'''