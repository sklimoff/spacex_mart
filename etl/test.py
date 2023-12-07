import requests
from graphql_query import Query, Operation, Argument
from spacex_dataset.rockets import RocketsRequest
from spacex_dataset.launches import LaunchesRequest

def main() -> None:
    request = LaunchesRequest()
    data = request.get_data()
    print(request._model.model_fields)
    for item in data:
        print(item)

if __name__ == '__main__':
    main()