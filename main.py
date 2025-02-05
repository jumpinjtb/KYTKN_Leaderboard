import StartggAPI
import WriteCSV

def main():
    api = StartggAPI.StartggAPI()
    result = api.get_tournament_results(1735711200, 1704088800, "KY")
    print(result)

    WriteCSV.dump_to_csv(result)

main()