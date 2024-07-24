import typing
import strawberry
import os


@strawberry.type
class Book:
    title: str
    author: str


def get_books():
    return [
        Book(title="The Great Gatsby", author="F. Scott Fitzgerald"),
    ]


@strawberry.type
class Query:
    books: typing.List[Book] = strawberry.field(resolver=get_books)


schema = strawberry.Schema(query=Query)

if __name__ == "__main__":
    port = os.getenv("PORT", "8080")
    strawberry.server(schema, port=int(port))
