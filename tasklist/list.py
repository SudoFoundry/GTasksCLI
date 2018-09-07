# Usage: echo -n "<text here>" | python3 line.py
# Usage [2]: echo -n "<text here>" | python3 line.py [item list name]
# Error codes: 0 if ok, 1 if JSON deserialization error, 2 if Google API error, 3 if item not found, 4 for every other error
from datetime import datetime
from datetime import timezone
from datetime import timedelta
import json
import sys

class taskList:
    def __init__(self, kind, id, title, updated, selfLink):
        # Initialize class with variables of a task list
        self.kind = kind
        self.id = id
        self.title = title
        self.updated = updated
        self.selfLink = selfLink
        pass

    def getKind(self):
        return self.kind

    def getId(self):
        return self.id

    def getTitle(self):
        return self.title

    def getUpdated(self):
        return self.updated

    def getSelfLink(self):
        return self.selfLink

def getList():
    returnList = list()

    # Load stdin as JSON object
    obj = json.load(sys.stdin)
    
    # Check if JSON is a Google API error response
    if "error" in obj:
        raise RuntimeError

    assert(obj["kind"] == "tasks#taskLists")
    for i in obj["items"]:
        kind = i["kind"]
        id = i["id"]
        title = i["title"]
        updated = i["updated"]
        selfLink = i["selfLink"]
        returnList.append(taskList(kind, id, title, updated, selfLink))

    return returnList

if __name__ == "__main__":
    try:
        if len(sys.argv) < 2:
            parsedList = getList()
            print("{:<16s}\t{:s}".format("Item", "Last Modified"))
            for i in parsedList:
                # The line after this parses the time in as UTC+0. The print line then prints it out in system time.
                dt = datetime.strptime(i.getUpdated()[:-5], "%Y-%m-%dT%H:%M:%S").replace(tzinfo=timezone(timedelta(0), name="UTC Default (+0)"))
                print("{:<16s}\t{:s}".format(i.getTitle(), dt.astimezone().strftime("%A, %d %B %Y, %H:%M:%S")))
        else:
            parsedList = getList()
            listname = str()
            for args in sys.argv[1:]:
	            listname += args + " "

            listname = listname[:-1]
            for i in parsedList:
                if i.getTitle() == listname:
                    print(i.getId())
                    break
            else:
                sys.exit(3) # didn't find item

    except json.JSONDecodeError:
        sys.exit(1)
    except RuntimeError:
        sys.exit(2)
    except:
        sys.exit(3) # every other error

    sys.exit(0)
