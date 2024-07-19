import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '4fbb780c93fff7f1663b3131d38bc799'
HEADER = {'Content-Type': 'application/json', 'trainer_token':TOKEN}
TRAINER_ID = '6554'


def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_part_response():
    response_get = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()["data"][0]["name"]== 'Бульбазавр'

@pytest.mark.parametrize('key, value', [('name', 'Бульбазавр'),('trainer_id', TRAINER_ID),('id', '44229')])
def test_parametrize(key, value):
    response_parametrize = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response_parametrize.json()["data"][0][key] == value 