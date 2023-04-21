from sqlalchemy import String, Integer, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column

DATABASE_URL = "sqlite:///" + "db.sqlite3"
engine = create_engine(DATABASE_URL, echo=True)

class Base(DeclarativeBase):
    pass

class Users(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(10))
    password: Mapped[str] = mapped_column(String(12))
    name:  Mapped[str] = mapped_column(String(40))
    category: Mapped[int] = mapped_column(Integer)
    create_at: Mapped[str] = mapped_column(String(30))

    def __repr__(self) -> str:        
        return f"Users(id={self.id!r}, username={self.username!r}, password={self.password!r}, name={self.name!r}, category={self.category!r}, create_at={self.create_at!r})"

class Persons(Base):
    __tablename__ = "persons"
    id: Mapped[int] = mapped_column(primary_key=True)
    dni: Mapped[str] = mapped_column(String(8))
    paterno: Mapped[str] = mapped_column(String(20))
    materno: Mapped[str] = mapped_column(String(20))
    nombre: Mapped[str] = mapped_column(String(30))
    nacimiento: Mapped[str] = mapped_column(String(10))
    ingreso: Mapped[str] = mapped_column(String(10))
    planilla: Mapped[str] = mapped_column(String(8))
    movilidad: Mapped[str] = mapped_column(String(7))
    asignacion: Mapped[str] = mapped_column(String(2))
    aportacion: Mapped[str] = mapped_column(String(9))
    comision: Mapped[str] = mapped_column(String(5))
    cuenta: Mapped[str] = mapped_column(String(20))
    cargo: Mapped[str] = mapped_column(String(30))
    distrito: Mapped[str] = mapped_column(String(30))
    domicilio: Mapped[str] = mapped_column(String(50))
    area: Mapped[str] = mapped_column(String(10))
    cuspp: Mapped[str] = mapped_column(String(12))
    celular: Mapped[str] = mapped_column(String(9))
    licencia: Mapped[str] = mapped_column(String(9))
    categoria: Mapped[str] = mapped_column(String(3))
    revalidacion: Mapped[str] = mapped_column(String(10))
    foto: Mapped[str] = mapped_column(String(25))
    fotodni: Mapped[str] = mapped_column(String(25))
    fotolicencia: Mapped[str] = mapped_column(String(25))
    fotopolicial: Mapped[str] = mapped_column(String(25))
    create_at: Mapped[str] = mapped_column(String(30))

    def __repr__(self) -> str:                
        return f"""Persons(id={self.id!r}, dni={self.dni!r}, paterno={self.paterno!r}, materno={self.materno!r}, nombre={self.nombre!r}, nacimiento={self.nacimiento!r}, ingreso={self.ingreso!r}, planilla={self.planilla!r}, movilidad={self.movilidad!r}, asignacion={self.asignacion!r}, aportacion={self.aportacion!r}, comision={self.comision!r}, cuenta={self.cuenta!r}, cargo={self.cargo!r}, distrito={self.distrito!r}, domicilio={self.domicilio!r}, area={self.area!r}, cuspp={self.cuspp!r}, celular={self.celular!r}, licencia={self.licencia!r}, categoria={self.categoria!r}, revalidacion={self.revalidacion!r}, create_at={self.create_at!r})"""

Base.metadata.create_all(engine)
session = Session(engine)