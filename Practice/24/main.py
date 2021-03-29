import json


class UserTask:
    userId = 0
    task_completed = 0

    def __init__(self, user_id, task_complete):
        self.userId = user_id
        self.task_completed = task_complete

    def tojson(self):
        return {
            "userId": self.userId,
            "task_completed": self.task_completed
        }


if __name__ == '__main__':

    output = {}

    with open('in.json', 'r') as file:
        data = json.loads(file.read())

        for i in data:
            if i['userId'] in output:
                output[i['userId']].task_completed += (0, 1)[i['completed']]
            else:
                output[i['userId']] = UserTask(i['userId'], (0, 1)[i['completed']])

    class CustomEncoder(json.JSONEncoder):
        def default(self, o):
            if "tojson" in dir(o):
                return o.tojson()
            return json.JSONEncoder.default(self, o)

    with open('out.json', 'w') as file:
        json.dump(output, file, cls=CustomEncoder)