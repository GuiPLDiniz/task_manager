from unittest.mock import Mock


from data_access_layer.dao.task_dao_impl import TaskDAOImpl
from entities.task import Task
from entities.task_status import TaskStatus


class TestTaskDAOImpl:

    def test_insert(self):

        fake_db_api_adapter = Mock()

        task_dao = TaskDAOImpl(fake_db_api_adapter)

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

        task_dao.insert(task)
        
        # Verifica se o método execute do adaptador de api foi chamado uma vez
        fake_db_api_adapter.execute.assert_called_once()

        # Verifica os argumentos do método execute do adaptador de api
        args, _ = fake_db_api_adapter.execute.call_args

        query_passed = args[0]
        parameters_passed = args[1]

        expected_query = """
        INSERT INTO task(name, description, status_id) 
        VALUES (?, ?, ?)
        """

        assert query_passed == expected_query
        
        assert parameters_passed[0] == task.name
        assert parameters_passed[1] == task.description
        assert parameters_passed[2] == task.status.id
    
    def test_list_all(self):

        fake_db_api_adapter = Mock()

        task_dao = TaskDAOImpl(fake_db_api_adapter)

        expected_values = [
            Task(1, "abc", "desc1", TaskStatus(1, "Disponível")),
            Task(2, "def", "desc2", TaskStatus(1, "Disponível")),
            Task(3, "ghi", "desc3", TaskStatus(2, "Fazendo")),
        ]

        fake_db_api_adapter.fetch_all.return_value = [
            {
                "task_id": 1, 
                "task_name": "abc", 
                "task_description": "desc1", 
                "status_id": 1, 
                "status_name": "Disponível"
            },
            {
                "task_id": 2, 
                "task_name": "def", 
                "task_description": "desc2", 
                "status_id": 1, 
                "status_name": "Disponível"
            },
            {
                "task_id": 3, 
                "task_name": "ghi", 
                "task_description": "desc3", 
                "status_id": 2, 
                "status_name": "Fazendo"
            },
        ]

        tasks = task_dao.list_all()

        fake_db_api_adapter.fetch_all.assert_called_once()

        args, _ = fake_db_api_adapter.fetch_all.call_args

        query_passed = args[0]

        expected_query = """
        SELECT
            t.id as task_id,
            t.name as task_name,
            t.description as task_description,
            s.id as status_id,
            s.name as status_name
        FROM task as t
        JOIN task_status as s ON t.status_id = s.id
        """

        assert query_passed == expected_query

        for task, expected_value in zip(tasks, expected_values):

            assert task.id == expected_value.id
            assert task.name == expected_value.name
            assert task.description == expected_value.description
            assert task.status.id == expected_value.status.id
            assert task.status.name == expected_value.status.name
    
    def test_list_all_empty(self):

        fake_db_api_adapter = Mock()

        task_dao = TaskDAOImpl(fake_db_api_adapter)

        expected_value = None

        fake_db_api_adapter.fetch_all.return_value = None

        tasks = task_dao.list_all()

        fake_db_api_adapter.fetch_all.assert_called_once()

        args, _ = fake_db_api_adapter.fetch_all.call_args

        query_passed = args[0]

        expected_query = """
        SELECT
            t.id as task_id,
            t.name as task_name,
            t.description as task_description,
            s.id as status_id,
            s.name as status_name
        FROM task as t
        JOIN task_status as s ON t.status_id = s.id
        """

        assert query_passed == expected_query

        assert tasks == expected_value
    
    def test_delete(self):

        fake_db_api_adapter = Mock()

        task_dao = TaskDAOImpl(fake_db_api_adapter)

        expected_task_id = 1
        task_dao.delete(expected_task_id)

        fake_db_api_adapter.execute.assert_called_once()

        args, _ = fake_db_api_adapter.execute.call_args

        query_passed = args[0]
        parameters_passed = args[1]

        expected_query = """
        DELETE FROM task
        WHERE id = ?
        """

        assert query_passed.strip() == expected_query.strip()

        assert parameters_passed[0] == expected_task_id
    
    def test_update_status(self):

        fake_db_api_adapter = Mock()

        task_dao = TaskDAOImpl(fake_db_api_adapter)

        task_id = 1
        status = TaskStatus(2, "Fazendo")

        task_dao.update_status(task_id, status)

        fake_db_api_adapter.execute.assert_called_once()

        args, _ = fake_db_api_adapter.execute.call_args

        query_passed = args[0]
        parameters_passed = args[1]

        expected_query = """
        UPDATE task SET status_id = ?
        WHERE id = ?
        """

        assert query_passed == expected_query

        assert parameters_passed[0] == status.id
        assert parameters_passed[1] == task_id








