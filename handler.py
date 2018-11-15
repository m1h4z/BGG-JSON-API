import json
import requests
import xmltodict

def boardgames(event, context):
    game_ids = event['pathParameters']['id']
    body = get_thing_raw_data(game_ids, type='boardgame')
    return create_response(body)

def boardgameexpansions(event, context):
    game_ids = event['pathParameters']['id']
    body = get_thing_raw_data(game_ids, type='boardgameexpansion')
    return create_response(body)


def hot(event, context):
    type = event['pathParameters']['type']
    body = get_hot_raw_data(type)
    return create_response(body)


def collection(event, context):
    username = event['pathParameters']['username']
    body = get_collection_raw_data(username)
    return create_response(body)


def create_response(body, status_code=200):
    response = {
        "statusCode": 200,
        "body": json.dumps(body, ensure_ascii=False)
    }
    return response


def get_thing_raw_data(game_ids, type):
    url = f'https://www.boardgamegeek.com/xmlapi2/thing?id={game_ids}&type={type}'
    response = requests.get(url)
    raw = xmltodict.parse(response.text)
    return json.loads(json.dumps(raw, ensure_ascii=False).encode('utf8'))


def get_hot_raw_data(type):
    url = f'https://boardgamegeek.com/xmlapi2/hot?type={type}'
    response = requests.get(url)
    raw = xmltodict.parse(response.text)
    return json.loads(json.dumps(raw, ensure_ascii=False).encode('utf8'))


def get_collection_raw_data(username):
    url = f'https://boardgamegeek.com/xmlapi2/collection?username={username}&own=1'
    response = requests.get(url)
    if response.status_code == 202:
        return {}
    raw = xmltodict.parse(response.text)
    return json.loads(json.dumps(raw, ensure_ascii=False).encode('utf8'))

