import StartggAPI
import WriteCSV

def main():
    api = StartggAPI.StartggAPI()
    request = api.build_tournament_request()
    variables = api.build_tournament_variables(1735711200, 1704088800, "KY")
    result = api.call_api(request, variables)
    print(result)

    WriteCSV.dump_to_csv(result)

main()