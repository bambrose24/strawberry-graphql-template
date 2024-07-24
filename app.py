from flask import Flask
from strawberry.flask.views import GraphQLView

from schema import schema

app = Flask(__name__)

# Disable introspection for the real production server
app.add_url_rule(
    "/graphql",
    view_func=GraphQLView.as_view("graphql_view", schema=schema, graphiql=False),
)

app.get("/", lambda: "ok")

if __name__ == "__main__":
    app.run()
