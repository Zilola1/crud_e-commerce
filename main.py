from database import Base, engine, SessionLocal
from models import Author, Category, Tag, Post

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

session = SessionLocal()

try:
    author = Author(name="John")
    category = Category(name="Technology")

    tag1 = Tag(name="Python")
    tag2 = Tag(name="SQLAlchemy")

    post = Post(
        title="First Post",
        content="This is my first blog post",
        author=author,
        category=category,
        tags=[tag1, tag2]
    )

    session.add(post)
    session.commit()

    print("SUCCESS")

except Exception as error:
    session.rollback()
    print(error)

finally:
    session.close()