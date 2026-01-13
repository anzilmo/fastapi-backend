from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.schemas import ItemCreate, ItemUpdate, ItemResponse
from app.crud import crud
from app.core.dependencies import get_current_active_user
from app.models.models import User

router = APIRouter(prefix="/items", tags=["Items"])


@router.post("/", response_model=ItemResponse, status_code=status.HTTP_201_CREATED)
def create_item(
    item: ItemCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Create a new item."""
    return crud.create_item(db=db, item=item, user_id=current_user.id)


@router.get("/{item_id}", response_model=ItemResponse)
def read_item(item_id: int, db: Session = Depends(get_db)):
    """Get a specific item by ID."""
    db_item = crud.get_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item


@router.get("/", response_model=List[ItemResponse])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Get all items with pagination."""
    items = crud.get_items(db, skip=skip, limit=limit)
    return items


@router.get("/user/me", response_model=List[ItemResponse])
def read_my_items(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Get all items owned by the current user."""
    items = crud.get_user_items(db, user_id=current_user.id, skip=skip, limit=limit)
    return items


@router.put("/{item_id}", response_model=ItemResponse)
def update_item(
    item_id: int,
    item: ItemUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Update an item."""
    db_item = crud.get_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    
    # Only allow owner to update their item
    if db_item.owner_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to update this item"
        )
    
    return crud.update_item(db, item_id=item_id, item=item)


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(
    item_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Delete an item."""
    db_item = crud.get_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    
    # Only allow owner to delete their item
    if db_item.owner_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to delete this item"
        )
    
    crud.delete_item(db, item_id=item_id)
