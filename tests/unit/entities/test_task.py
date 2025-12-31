import pytest


from entities.task import Task
from entities.task_status import TaskStatus


class TestTask:

    def test_set_id(self):

        name = "Atividade de Engenharia de Software"
        description = "Realizar projeto de gerenciamento de tarefas usando dois padrões de projetos."

        status = TaskStatus(1, "Disponível")

        data = {
            "id": 1,
            "name": name,
            "description": description,
            "status": status,
        }

        task = Task(**data)

        # Inteiro
        task.set_id(3)

        # Inteiro negativo
        with pytest.raises(ValueError):

            task.set_id(-1)

        # String
        with pytest.raises(ValueError):

            task.set_id("3")

        # Float
        with pytest.raises(ValueError):
            
            task.set_id(3.4)

        # Sequência
        with pytest.raises(ValueError):
            
            task.set_id([1, 2, 3])
    
    def test_set_name(self):

        name = "Atividade de Engenharia de Software"
        description = "Realizar projeto de gerenciamento de tarefas usando dois padrões de projetos."

        status = TaskStatus(1, "Disponível")

        data = {
            "id": 1,
            "name": name,
            "description": description,
            "status": status,
        }

        task = Task(**data)

        # String
        task.set_name("abc")

        # String vazia
        with pytest.raises(ValueError):

            task.set_name("")

        # Inteiro
        with pytest.raises(ValueError):

            
            task.set_name(1)

        # Float
        with pytest.raises(ValueError):
            
            task.set_name(3.4)

        # Sequência
        with pytest.raises(ValueError):
            
            task.set_name([1, 2, 3])
    
    def test_set_description(self):

        name = "Atividade de Engenharia de Software"
        description = "Realizar projeto de gerenciamento de tarefas usando dois padrões de projetos."

        status = TaskStatus(1, "Disponível")

        data = {
            "id": 1,
            "name": name,
            "description": description,
            "status": status,
        }

        task = Task(**data)

        # String
        task.set_description("desc")

        # String vazia
        task.set_description("")

        # Inteiro
        with pytest.raises(ValueError):

            
            task.set_description(1)

        # Float
        with pytest.raises(ValueError):
            
            task.set_description(3.4)

        # Sequência
        with pytest.raises(ValueError):
            
            task.set_description([1, 2, 3])
    
    def test_set_status(self):

        name = "Atividade de Engenharia de Software"
        description = "Realizar projeto de gerenciamento de tarefas usando dois padrões de projetos."

        status = TaskStatus(1, "Disponível")

        data = {
            "id": 1,
            "name": name,
            "description": description,
            "status": status,
        }

        task = Task(**data)

        # String
        task.set_status(TaskStatus(2, "Fazendo"))

        # String
        with pytest.raises(ValueError):

            task.set_status("Fazendo")

        # Inteiro
        with pytest.raises(ValueError):

            
            task.set_status(1)

        # Float
        with pytest.raises(ValueError):
            
            task.set_status(3.4)

        # Sequência
        with pytest.raises(ValueError):
            
            task.set_status([1, 2, 3])
    
    def test_get_id(self):

        name = "Atividade de Engenharia de Software"
        description = "Realizar projeto de gerenciamento de tarefas usando dois padrões de projetos."

        status = TaskStatus(1, "Disponível")

        data = {
            "id": 1,
            "name": name,
            "description": description,
            "status": status,
        }

        task = Task(**data)
        assert task.id == 1
    
    def test_get_name(self):

        name = "Atividade de Engenharia de Software"
        description = "Realizar projeto de gerenciamento de tarefas usando dois padrões de projetos."

        status = TaskStatus(1, "Disponível")

        data = {
            "id": 1,
            "name": name,
            "description": description,
            "status": status,
        }

        task = Task(**data)
        assert task.name == name
    
    def test_get_description(self):

        name = "Atividade de Engenharia de Software"
        description = "Realizar projeto de gerenciamento de tarefas usando dois padrões de projetos."

        status = TaskStatus(1, "Disponível")

        data = {
            "id": 1,
            "name": name,
            "description": description,
            "status": status,
        }

        task = Task(**data)
        assert task.description == description
    
    def test_get_status(self):

        name = "Atividade de Engenharia de Software"
        description = "Realizar projeto de gerenciamento de tarefas usando dois padrões de projetos."

        status = TaskStatus(1, "Disponível")

        data = {
            "id": 1,
            "name": name,
            "description": description,
            "status": status,
        }

        task = Task(**data)
        assert task.status == status