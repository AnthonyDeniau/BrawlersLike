import json
from graphene_django.utils.testing import GraphQLTestCase
from . import schema
from .models import Brawler

query_all = '''
query {
  brawlers {
    name
    id
    description
    cost
    avatar
    rarity
    health
    speed 
  }
}
'''
query_all_results = {
    "brawlers": [{
        'name': 'Shelly',
        'id': '1',
        'description':
        "Shelly's spread-fire shotgun blasts the other team with buckshot. Her Super destroys cover and keeps her opponents at a distance!",
        'cost': 0,
        'avatar': 'https://cdn.starlist.pro/brawler/Shelly.png?v=1',
        'rarity': 'A_0',
        'health': 5320,
        'speed': 1
    }]
}

query_one = '''
query getBrawler($id: Int!) {
  brawler (id: $id) {
    name
    id
  }
}
'''
query_one_results = {'brawler': {'id': '1', 'name': 'Shelly'}}

mutation_create = '''
mutation createBrawler($name: String!,
 $cost: Int!,
 $speed: Int!,
 $description: String!,
 $avatar: String!,
 $health: Int!,
 $rarity: String) {
  createBrawler (
    name: $name,
    cost: $cost,
    speed: $speed,
    description: $description,
    avatar: $avatar,
    health: $health,
    rarity: $rarity
  ) {
    ok
  }
}
'''
mutation_create_results = {"createBrawler": {"ok": True}}

mutation_delete_brawler = """
mutation deleteBrawler($id: ID!) {
  deleteBrawler (id: $id) {
    isDeleted
  }
}
"""
mutation_delete_results = {"deleteBrawler": {"isDeleted": True}}


class BrawlerCRUDTestCase(GraphQLTestCase):
    GRAPHQL_SCHEMA = schema

    fixtures = ['apps/brawler/fixtures/brawlers.json']

    def test_query_all(self):
        response = self.query(query_all)

        content = json.loads(response.content)

        # This validates the status code and if you get errors
        self.assertResponseNoErrors(response)
        assert content.get("data") == query_all_results

    def test_query_one(self):
        response = self.query(query_one,
                              variables={'id': 1},
                              op_name="getBrawler")

        content = json.loads(response.content)

        # This validates the status code and if you get errors
        self.assertResponseNoErrors(response)
        assert content.get("data") == query_one_results

    def test_delete(self):
        response = self.query(mutation_delete_brawler,
                              variables={"id": 1},
                              op_name="deleteBrawler")
        content = json.loads(response.content)
        self.assertResponseNoErrors(response)
        assert content.get("data") == mutation_delete_results
        assert Brawler.objects.filter(id=1).count() == 0

    def test_create_mutation(self):
        response = self.query(
            mutation_create,
            variables={
                "name": "Nita",
                "cost": 10,
                "speed": 1,
                "description":
                "Nita strikes her enemies with a thunderous shockwave. Her Super summons a massive bear to fight by her side!",
                "avatar": "https://cdn.starlist.pro/brawler/Nita.png?v=1",
                "health": 5600,
                "rarity": "Trophy Road"
            },
            op_name="createBrawler")
        content = json.loads(response.content)
        self.assertResponseNoErrors(response)
        assert content.get("data") == mutation_create_results
        Brawler.objects.get(name="Nita")