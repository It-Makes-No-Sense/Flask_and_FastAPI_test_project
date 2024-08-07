from sqlalchemy.orm import Session
from models import User, Item, Order, UserCreate, ItemCreate, OrderCreate, OrderUpdate
import bcrypt


def create_user(db: Session, user: UserCreate):
    user.password = bcrypt.hashpw(user.password.encode(), bcrypt.gensalt())
    db_user = User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_users(db: Session):
    return db.query(User).all()


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def delete_user(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
        return {"message": "User deleted successfully"}
    else:
        return {"error": "User not found"}


def create_item(db: Session, item: ItemCreate):
    db_item = Item(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def get_item(db: Session, item_id: int):
    return db.query(Item).filter(Item.id == item_id).first()


def get_items(db: Session):
    return db.query(Item).all()


def delete_item(db: Session, item_id: int):
    item = db.query(Item).filter(Item.id == item_id).first()
    if item:
        db.delete(item)
        db.commit()
        return {"message": "Item deleted successfully"}
    else:
        return {"error": "Item not found"}


def create_order(db: Session, order: OrderCreate):
    db_order = Order(**order.model_dump())
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order


def get_order(db: Session, order_id: int):
    return db.query(Order).filter(Order.id == order_id).first()


def get_orders(db: Session):
    return db.query(Order).all()


def delete_order(db: Session, order_id: int):
    order = db.query(Order).filter(Order.id == order_id).first()
    if order:
        db.delete(order)
        db.commit()
        return {"message": "Order deleted successfully"}
    else:
        return {"error": "Order not found"}


def update_order(db: Session, order: OrderUpdate):
    res = db.query(Order).filter(Order.id == order.order_id).first()
    if res:
        query = db.query(Order).filter(Order.id == order.order_id).update({Order.status: order.status})
        print(query)
        db.commit()
        return {"message": "Order Updated successfully"}
    else:
        return {"error": "Order not found"}
