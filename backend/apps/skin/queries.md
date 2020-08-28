# Get

```
query get_all_skins {
  skins{
    name,
    description,
    avatar,
    price,
    modelFile,
    textureFile,
    voiceLineFile
  }
}
```

# Create

```
mutation create_skin {
    createSkin(
        name:"Skin de Michel", 
        description:"Ce Skin est super", 
        avatar:"Lien de l'avatar", 
        price:3, 
        modelFile:"Lien du model", 
        textureFile:"Lien de la texture",
        voiceLineFile:"Lien de la voice line")
        {
            ok,
          	skin {
              id
            }
        }
}
```

# Update

```
mutation update_skin {
    updateSkin(
      	id:1,
        name:"Mon super skin", 
        description:"Ce Skin est super", 
        avatar:"Lien de l'avatar", 
        price:3, 
        modelFile:"Lien du model", 
        textureFile:"Lien de la texture",
        voiceLineFile:"Lien de la voice line")
        {
            ok,
          	skin {
              id,
              name
            }
        }
}
```

# Delete

```
mutation delete_skin {
    deleteSkin(id:2)
    {
        ok
    }
}
```