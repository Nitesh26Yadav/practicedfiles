from flask import Flask
from flask_restful import Api,Resource,reqparse,abort

app = Flask(__name__)
api = Api(app)


todos = {
    1:{"task":"ABC","summary":"data1"},
    2:{"task":"DEF","summary":"data2"}
}

task_post_args = reqparse.RequestParser()
task_post_args.add_argument("task", type=str, help = "Task is required", required = True)
task_post_args.add_argument("summary", type=str ,help ="summary is required",required = True)


task_put_args = reqparse.RequestParser()
task_put_args.add_argument("task",type = str)
task_put_args.add_argument("summary",type = str)

class Todolist(Resource):
    def get(self):
        return todos

class Todo(Resource):
    def get(self,todo_id):
        return todos[todo_id]

    def post(self,todo_id):
        args = task_post_args.parse_args()

        if todo_id in todos:
            abort(404, "Task already exists!")
        todos[todo_id] = {"task":args["task"],"summary":args["summary"]}

        return todos[todo_id]

    def put(self,todo_id):
        args = task_put_args.parse_args()

        if todo_id not in todos:
            abort(404, message ="todo_id not in list cannot update")
        if args["task"]:
            todos[todo_id]["task"] = args["task"]
        if args["summary"]:
            todos[todo_id]["summary"] = args["summary"]

        return todos[todo_id]



    def delete(self,todo_id):
        del todos[todo_id]
        return todos

api.add_resource(Todolist,'/todos')
api.add_resource(Todo,'/todos/<int:todo_id>')

if __name__ == '__main__':
    app.run(debug = True)