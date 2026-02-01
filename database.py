from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./secure_home.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String, unique=True, index=True)
    phone = Column(String)
    role = Column(String)
    balance = Column(Float, default=0.0)

Base.metadata.create_all(bind=engine)

def save_user_local(username, email, phone, role):
    db = SessionLocal()
    try:
        user = User(username=username, email=email, phone=phone, role=role)
        db.add(user)
        db.commit()
        return user
    except Exception as e:
        print(f"SQL Error: {e}")
        return None
    finally:
        db.close()