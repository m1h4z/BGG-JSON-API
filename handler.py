import json
import requests
import xmltodict

def boardgames(event, context):
    game_ids = event['pathParameters']['id']
    body = get_raw_data(game_ids, type='boardgame')

    response = {
        "statusCode": 200,
        "body": json.dumps(body, ensure_ascii=False)
    }

    return response


def boardgameexpansions(event, context):
    game_ids = event['pathParameters']['id']
    body = get_raw_data(game_ids, type='boardgameexpansion')

    response = {
        "statusCode": 200,
        "body": json.dumps(body, ensure_ascii=False)
    }

    return response


def get_raw_data(game_ids, type):
    url = f'https://www.boardgamegeek.com/xmlapi2/thing?id={game_ids}&type={type}'
    response = requests.get(url)
    raw = xmltodict.parse(response.text)
    return json.loads(json.dumps(raw, ensure_ascii=False).encode('utf8'))