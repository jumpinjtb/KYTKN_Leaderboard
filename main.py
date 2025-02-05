import StartggAPI
import WriteCSV

def api_test():
    api = StartggAPI.StartggAPI()
    request = api.build_tournament_request()
    variables = api.build_tournament_variables(1735711200, 1704088800, "KY")
    result = api.call_api(request, variables)
    print(result)

def main():
    api = StartggAPI.StartggAPI()
    request = api.build_tournament_request()
    variables = api.build_tournament_variables(1735711200, 1704088800, "KY")
    result = api.call_api(request, variables)
    print(result)

    ParseJSON.parse_json(result)

main()