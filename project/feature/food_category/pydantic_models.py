from pydantic import BaseModel, validator
from typing import Optional


class FoodPydantic(BaseModel):
    
    category: str
    id: Optional[int] =None
    title: str
    description: str
    picture: str
    ingredients: str
    

    