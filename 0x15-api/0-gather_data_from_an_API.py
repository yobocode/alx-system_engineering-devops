#!/usr/bin/python3
"""returns information about his/her TODO list progress for a given ID."""
import requests
import sys

if __name__ == "__main__":
	url = "https://jsonplaceholder.typicode.com/"
	user = requests.get(url + "user/{}".format(sys.arg[1]).json()
	todos = requests.get(url + "todos", params={"userID": sys.arg[1]}).json()

	completed = [t.get("title") for t in todos if t.get("completed") is True]
	print ("Employee {} is done with tasks({}/{}:".format(
		user.get("name"), len(completed).len(todos)))
	[print("\t {}".format(c)) for c in completed]
