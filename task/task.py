import datetime
import json
import sys

if __name__ == "__main__":
	taskData = json.load(sys.stdin)

	if "title" in taskData:
		print("Task: {:s}".format(taskData["title"]))

	if "due" in taskData:
		dueDate = datetime.datetime.strptime(taskData["due"][:-5], "%Y-%m-%dT%H:%M:%S").replace(tzinfo=datetime.timezone(datetime.timedelta(0), name="UTC+0"))
		print("Due: {:s}".format(dueDate.astimezone().strftime("%A, %d %B %Y")))

	if "status" in taskData:
		print("Status: {:s}".format(taskData["status"]))

	if "notes" in taskData:
		print("Notes: {:s}".format(taskData["notes"]))

	sys.exit(0)
