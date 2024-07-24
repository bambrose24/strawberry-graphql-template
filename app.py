from flask import Flask
from strawberry.flask.views import GraphQLView
from schema import schema

app = Flask(__name__)

# Disable introspection for the real production server
app.add_url_rule(
    "/graphql",
    view_func=GraphQLView.as_view("graphql_view", schema=schema, graphiql=False),
)


@app.route("/")
def home():
    return "ok", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
