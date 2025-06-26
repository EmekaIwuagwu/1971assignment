from ariadne import QueryType, MutationType, convert_kwargs_to_snake_case
from sqlalchemy.exc import IntegrityError
from models import Person
from database import SessionLocal

query = QueryType()
mutation = MutationType()

# Query Resolvers
@query.field("persons")
def resolve_persons(_, info):
    db = SessionLocal()
    persons = db.query(Person).all()
    db.close()
    return persons

@query.field("person")
def resolve_person(_, info, id):
    db = SessionLocal()
    person = db.query(Person).get(id)
    db.close()
    return person

# Mutation Resolvers
@mutation.field("createPerson")
@convert_kwargs_to_snake_case
def resolve_create_person(_, info, input):
    db = SessionLocal()
    new_person = Person(**input)
    try:
        db.add(new_person)
        db.commit()
        db.refresh(new_person)
        return new_person
    except IntegrityError:
        db.rollback()
        raise Exception("Email must be unique.")
    finally:
        db.close()

@mutation.field("updatePerson")
@convert_kwargs_to_snake_case
def resolve_update_person(_, info, id, input):
    db = SessionLocal()
    person = db.query(Person).get(id)
    if not person:
        raise Exception(f"Person with id {id} not found.")
    for key, value in input.items():
        setattr(person, key, value)
    db.commit()
    db.refresh(person)
    db.close()
    return person

@mutation.field("deletePerson")
def resolve_delete_person(_, info, id):
    db = SessionLocal()
    person = db.query(Person).get(id)
    if not person:
        raise Exception(f"Person with id {id} not found.")
    db.delete(person)
    db.commit()
    db.close()
    return True
