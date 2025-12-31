from abc import ABC, abstractmethod
from typing import Tuple, Union


from entities.task import Task
from entities.task_status import TaskStatus


class TaskDAO(ABC):

    """
    'Data Access Object' da entidade tarefa, que realiza interface com o banco de dados
    """

    @abstractmethod
    def insert(self, task: Task) -> None:
        
        """Cria uma nova tarefa no banco de dados, a partir dos dados de 'task'

        Parameters
        ----------
        task: entities.task.Task
            Objeto Task com os dados a serem armazenados no banco de dados
        """

        pass

    @abstractmethod
    def list_all(self) -> Union[Tuple[Task], None]:

        """Lista todas as tarefas do banco de dados

        Returns
        -------
        Union[Tuple[entities.task.Task], None] 
            Objetos Task com os dados armazenados no banco de dados
        """

        pass

    @abstractmethod
    def delete(self, task_id: int) -> None:

        """Remove uma tarefa do banco de dados, a partir do seu identificador

        Parameters
        ----------
        task_id: int
            Identificador da tarefa a ser removida do banco de dados
        """

        pass

    @abstractmethod
    def update_status(self, task_id: int, status: TaskStatus) -> None:

        """Altera o status de uma tarefa do banco de dados, a partir do seu identificador

        Parameters
        ----------
        task_id: int
            Identificador da tarefa cujo status será alterado no banco de dados
        status: entities.task_status.TaskStatus
            Status a ser alterado 
        """

        pass