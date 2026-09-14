from tools.tavily_tool import tavily_search
from tools.flight_tool import search_flights
from backend import run_travel_agent

""" res1 = tavily_search("Best hotels in India")
print(res1)


res2 = search_flights("Plan a 7 days India trip from DE")
print(res2) """

user_input = input("Enter travel request: ")

response = run_travel_agent(
    user_input=user_input,
    thread_id="test_user"
)

print("\nFINAL RESPONSE:\n")
print(response["answer"]) 