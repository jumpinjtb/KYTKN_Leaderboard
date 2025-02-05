import os
from idlelib import query

from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport
from dotenv import load_dotenv

load_dotenv()

class StartggAPI:

    def __init__(self):
        self.url = os.getenv("STARTGG_URL")
        self.headers = {"Authorization": f"Bearer {os.getenv("STARTGG_API_KEY")}"}
        self.query = self.build_tournament_request()

    def get_tournament_results(self, before_timestamp, after_timestamp, state_code):
        page = 1
        variables = self.build_tournament_variables(before_timestamp, after_timestamp, state_code, page)
        result = [self.call_api(self.query, variables)]

        while result[page - 1]["tournaments"]["pageInfo"]["page"] < result[page - 1]["tournaments"]["pageInfo"]["totalPages"]:
            page += 1
            variables = self.build_tournament_variables(before_timestamp, after_timestamp, state_code, page)
            result.append(self.call_api(self.query, variables))
        return result

    def get_tournament_results_page(self, before_timestamp, after_timestamp, state_code, page):
        variables = self.build_tournament_variables(before_timestamp, after_timestamp, state_code, page)
        return self.call_api(query, variables)

    def call_api(self, request, variables):
        transport = AIOHTTPTransport(url=self.url, headers=self.headers)
        client = Client(transport=transport, fetch_schema_from_transport=True)
        result = client.execute(request, variable_values=variables)
        return result

    def build_tournament_request(self):
        with open("GraphQLConfig/GetTournamentResults.graphql", "r") as file:
            query = gql(file.read())
        return query

    def build_tournament_variables(self, before_timestamp, after_timestamp, state_code, page):
        return {
            "tournamentQuery": {
                "page": page,
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
