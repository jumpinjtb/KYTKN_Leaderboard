import StartggAPI

def main():
    api = StartggAPI.StartggAPI()
    request = api.build_tournament_request()
    variables = api.build_tournament_variables(1735711200, 1704088800, "KY")
    api.call_api(request, variables)

main()