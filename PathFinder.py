import requests
from StrToCoords import get_coordinates


def get_path(startPoint: str, endPoint: str):
    startPoint, endPoint = get_coordinates(startPoint), get_coordinates(endPoint)
    if not startPoint:
        print(f'I couldn\'t get coords for the {startPoint}, sorry')
    elif not endPoint:
        print(f'I couldn\'t get coords for the {endPoint}, sorry')

    url = "https://graphhopper.com/api/1/route"
    # API IS FREE, check - https://graphhopper.com/dashboard/#/apikeys
    query = {
        "key": "YOUR API KEY"
    }

    payload = {
        "points": [
            [
                startPoint[0],
                startPoint[1]
            ],
            [
                endPoint[0],
                endPoint[1]
            ]
        ],
        "vehicle": "car",
        "locale": "en",
        "instructions": True,
        "calc_points": True,
        "points_encoded": False
    }

    headers = {"Content-Type": "application/json"}

    response = requests.post(url, json=payload, headers=headers, params=query)

    data = response.json()
    # data = data["paths"][0]
    path_coords = data["paths"][0]["points"]["coordinates"]
    return path_coords