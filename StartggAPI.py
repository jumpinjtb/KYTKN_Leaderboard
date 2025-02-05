import os
from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport
from dotenv import load_dotenv

load_dotenv()

class StartggAPI:

    def __init__(self):
        self.url = os.getenv("STARTGG_URL")
        self.headers = {"Authorization": f"Bearer {os.getenv("STARTGG_API_KEY")}"}

    def call_api(self, request, variables):
        transport = AIOHTTPTransport(url=self.url, headers=self.headers)
        client = Client(transport=transport, fetch_schema_from_transport=True)
        result = client.execute(request, variable_values=variables)
        print(result)

    def build_tournament_request(self):
        with open("GraphQLConfig/GetTournamentResults.graphql", "r") as file:
            query = gql(file.read())
        return query

    def build_tournament_variables(self, before_timestamp, after_timestamp, state_code):
        return {
            "tournamentQuery": {
                "filter": {
                  "addrState": f"{state_code}",
                  "videogameIds": "49783",
                  "beforeDate": before_timestamp,
                  "afterDate": after_timestamp
                }
              },
              "eventFilter": {
                "videogameId": "49783"
              }
        }
