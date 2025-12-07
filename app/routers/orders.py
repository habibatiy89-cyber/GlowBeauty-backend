from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas, database

router = APIRouter(
    prefix="/orders",
    tags=["orders"],
)

@router.post("/", response_model=schemas.Order)
def create_order(order: schemas.OrderCreate, db: Session = Depends(database.get_db)):
    # Create the order object
    db_order = models.Order(user_id=order.user_id, status="pending", total_amount=0.0)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    
    total = 0.0
    for item in order.items:
        # Fetch product price from DB to avoid client-side price manipulation
        product = db.query(models.Product).filter(models.Product.id == item.product_id).first()
        if not product:
             continue 
        
        price = product.price
        total += price * item.quantity
        
        db_item = models.OrderItem(
            order_id=db_order.id,
            product_id=product.id,
            quantity=item.quantity,
            price_at_purchase=price
        )
        db.add(db_item)
    
    db_order.total_amount = total
    db.commit()
    db.refresh(db_order) # Refresh to get updated fields and items
    return db_order

@router.get("/{user_id}", response_model=List[schemas.Order])
def read_orders(user_id: int, db: Session = Depends(database.get_db)):
    orders = db.query(models.Order).filter(models.Order.user_id == user_id).all()
    return orders
