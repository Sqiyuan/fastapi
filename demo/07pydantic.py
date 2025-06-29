from pydantic import BaseModel, PositiveInt, ValidationError
from datetime import datetime
from typing import Dict

class User(BaseModel):
    id: int
    name: str = 'John Doe'
    date_time: datetime = datetime.now()
    test: Dict[str, PositiveInt]

if __name__ == '__main__':
    try:
        user = User(id=1, test={ 'a': 1, 'b': 41})
        print(user)
    except ValidationError as e:
        print(e.errors())