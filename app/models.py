from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base

# Representa a tabela de tarefas no banco de dados
class Task(Base):
    __tablename__ = "tasks"

    # ID único da tarefa
    id = Column(Integer, primary_key=True, index=True)

    # Título da tarefa (descrição curta)
    title = Column(String)

    # Indica se a tarefa foi concluída ou não
    completed = Column(Boolean, default=False)