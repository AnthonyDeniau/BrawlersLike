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


class UpdateSkinMutation(graphene.Mutation):
    class Arguments:
        id =            graphene.Int(required=True)
        name =          graphene.String(required=True)
        description =   graphene.String(required=True)
        avatar =        graphene.String(required=True)
        price =         graphene.Int(required=True)
        model_file =    graphene.String(required=True)
        texture_file =  graphene.String(required=True)
        voice_line_file = graphene.String(required=True)

    ok = graphene.Boolean()
    skin = graphene.Field(SkinType)

    def mutate(root, info, **kwargs):
        skin = Skin.objects.get(pk=kwargs['id'])
        for k, v in kwargs.items():
            if(k != "id"): 
                setattr(skin, k, v)
        skin.save()

        ok = True
        return UpdateSkinMutation(skin=skin, ok=ok)


class DeleteSkinMutation(graphene.Mutation):
    class Arguments:
        id=graphene.ID()

    ok = graphene.Boolean()
    skin = graphene.Field(SkinType)

    def mutate(root, info, id):
        skin = Skin.objects.get(pk=id)
        skin.delete()
        ok = True
        return DeleteSkinMutation(skin=skin, ok=ok)


class Mutation(graphene.ObjectType):
    create_skin = CreateSkinMutation.Field()
    update_skin = UpdateSkinMutation.Field()
    delete_skin = DeleteSkinMutation.Field()


"""

query oneSkin {
  skin(id:1){
    id,
    name,
		description,
		avatar,
		price,
		modelFile,
		textureFile,
		voiceLineFile
  }
}

query allskins{
  skins {
    id,
    name,
		description,
		avatar,
		price,
		modelFile,
		textureFile,
		voiceLineFile
  }
}

mutation createSkin {
  createSkin(
    name:"BlueJack", 
    description:"Un skin tout bleu comme Jack LeBleu", 
    avatar:"http://bleuavatar.fr",            
    price:800, 
    modelFile:"http://bleumodel.fr",  
    textureFile:"http://bleutexture.fr",
    voiceLineFile:"http://bleuvoiceline.fr"
  )
  {
    ok
    skin {
      id
    }
  }
}

mutation updateSkin {
  updateSkin(
    id:9,
    name:"Blue_Jack", 
    description:"Un skin tout bleu comme Jack Blue", 
    avatar:"http://bleuavatar.com",            
    price:900, 
    modelFile:"http://bleumodel.com",  
    textureFile:"http://bleutexture.com",
    voiceLineFile:"http://bleuvoiceline.com"
  )
  {
    ok
    skin {
      id
    }
  }
}

mutation deleteSkin {
  deleteSkin(id:9) {
    ok
  }
}

"""
