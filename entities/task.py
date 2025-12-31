from entities.task_status import TaskStatus

class Task:

    """
    Representação da entidade tarefa no domínio da aplicação
    """

    def __init__(self, id: int, name: str, description: str, status: TaskStatus):

        """Inicializa um objeto Task
        
        Parameters
        ----------
        id: int
            Identificador da tarefa
        name: str
            Nome da tarefa
        description: str
            Descrição da tarefa
        status: entities.task_status.TaskStatus
            Status da tarefa
        """

        self.set_id(id)
        self.set_name(name)
        self.set_description(description)
        self.set_status(status)
    
    def set_id(self, id: int) -> None:

        """Modifica o valor do atributo privado 'id'
        
        Parameters
        ----------
        id: int
            Identificador da tarefa
        """

        if not isinstance(id, int) or id < 0:

            raise ValueError("O identificador deve ser um inteiro positivo!")
        
        self._id = id
    
    def set_name(self, name: str) -> None:

        """Modifica o valor do atributo privado 'name'
        
        Parameters
        ----------
        name: str
            Nome da tarefa
        """

        if not isinstance(name, str) or name == "":

            raise ValueError("O nome deve ser uma sequência de caracteres não vazia!")

        self._name = name
    
    def set_description(self, description: str) -> None:

        """Modifica o valor do atributo privado 'description'
        
        Parameters
        ----------
        description: str
            Descrição da tarefa
        """

        if not isinstance(description, str):

            raise ValueError("O identificador deve ser uma sequência de caracteres!")

        self._description = description
    
    def set_status(self, status: TaskStatus) -> None:

        """Modifica o valor do atributo privado 'status'
        
        Parameters
        ----------
        status: entities.task_status.TaskStatus
            Status da tarefa
        """

        if not isinstance(status, TaskStatus):

            raise ValueError("O status deve ser uma instância da classe TaskStatus!")

        self._status = status
    
    @property
    def id(self) -> int:

        """Acessa o valor do atributo privado 'id'

        Returns
        -------
        int
            Identificador da tarefa
        """

        return self._id

    @property
    def name(self) -> str:

        """Acessa o valor do atributo privado 'name'

        Returns
        -------
        str
            Nome da tarefa
        """

        return self._name

    @property
    def description(self) -> str:

        """Acessa o valor do atributo privado 'description'

        Returns
        -------
        str
            Descrição da tarefa
        """

        return self._description
    
    @property
    def status(self) -> TaskStatus:

        """Acessa o valor do atributo privado 'status'

        Returns
        -------
        entities.task_status.TaskStatus
            Status da tarefa
        """

        return self._status