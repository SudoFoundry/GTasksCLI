# tasks.py - A script capable of parsing JSON containing a tasklist to list all items in the tasklist.
# Usage: echo -n "<insert task json here"> | python3 tasks.py
# Usage [1]: echo -n "<insert task json here"> | python3 tasks.py [relative id]
# Usage [2]: echo -n "<insert task json here"> | python3 tasks.py -[relative id]
# Output: A list of tasks within the task list.
# Output [1]: The Google API self link of the relative id. Relative id is the id that is printed in order.
# Output [2]: The Google API ID of the relative ID.
# Returns 1 if there are no items in the task list (including an error json), returns 2 if relative id is out of bound
import json
import sys

# A foresight that an object might be a better idea than directly returning list of dictionaries
class task:
	def __init__(self):
		self.kind = self.id = self.etag = self.title = self.updated = self.selfLink = self.parent = self.position = self.notes = self.status = self.due = ""
		# Ridiculous ^

	def getKind(self):
		return self.kind

	def getId(self):
		return self.id

	def getEtag(self):
		return self.etag

	def getTitle(self):
		return self.title

	def getUpdated(self):
		return self.updated

	def getSelfLink(self):
		return self.selfLink

	def getParent(self):
		return self.parent

	def getPosition(self):
		return self.position

	def getNotes(self):
		return self.notes

	def getStatus(self):
		return self.status

	def getDue(self):
		return self.due

def createListOfTasks(fd): # create list of tasks from a file object
	data = json.load(fd)

	if "items" not in data:
		sys.exit(1)

	itemList = list()
	for item in data["items"]:
		t = task()
		if "kind" in item:
			t.kind = item["kind"]

		if "id" in item:
			t.id = item["id"]

		if "etag" in item:
			t.etag = item["etag"]

		if "title" in item:
			t.title = item["title"]

		if "updated" in item:
			t.updated = item["updated"]

		if "selfLink" in item:
			t.selfLink = item["selfLink"]

		if "parent" in item:
			t.parent = item["parent"]

		if "position" in item:
			t.position = item["position"]

		if "notes" in item:
			t.notes = item["notes"]

		if "status" in item:
			t.status = item["status"]

		if "due" in item:
			t.due = item["due"]
		
		itemList.append(t)

	return itemList

if __name__ == "__main__":
	tasks = createListOfTasks(sys.stdin)

	if len(sys.argv) < 2:
		i = 0
		print("{:s}\t{:s}".format("ID ", "Task"))

		for task in tasks:
			if task.getParent() == "":
				print("{:d}\t{:s}".format(i, task.getTitle()))
			else:
				print("{:d}\t'--> {:s}".format(i, task.getTitle())) # all child items always come arranged after their parents		
			i += 1
	else:
		try:
			if sys.argv[1][0] != '-':
				print(tasks[int(sys.argv[1])].getSelfLink())
			else: print(tasks[int(sys.argv[1][1:])].getId())
		except:
			sys.exit(2)

	sys.exit(0)
