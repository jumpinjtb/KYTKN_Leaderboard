import csv

def dump_to_csv(result):
    tournaments = result["tournaments"]["nodes"]

    with open("KYTKN_Leaderboard.csv", 'w', newline='') as csv_file:
        result_writer = csv.writer(csv_file)
        for tournament in tournaments:
            #We are only requesting Tekken events for now so I'm assuming there will only be 1 event per Tournament
            players = tournament["events"][0]["entrants"]["nodes"]
            for player in players:
                if player["name"] is not None and player["standing"] is not None:
                    print(player["name"])
                    print(player["standing"]["placement"])
                    result_writer.writerow([player["name"], player["standing"]["placement"]])