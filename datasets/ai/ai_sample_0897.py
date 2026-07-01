import graphene

class Query(graphene.ObjectType):
    # An endpoint to fetch all books
    books = graphene.List(BookType)

    def resolve_books(self, info):
        return books


class Mutation(graphene.ObjectType):
    # An endpoint to add a book
    add_book = graphene.Field(BookType, title=graphene.String(), author=graphene.String(), )

    def mutate(self, info, title, author):
        book = Book(title=title, author=author)
        book.save()

        return book

schema = graphene.Schema(query=Query, mutation=Mutation)