class TaskStatus:

    """
    Representação da entidade status da tarefa no domínio da aplicação
    """

    def __init__(self, id: int, name: str):

        """Inicializa um objeto TaskStatus
        
        Parameters
        ----------
        id: int
            Identificador do status da tarefa
        name: str
            Nome do status da tarefa
        """

        self.set_id(id)
        self.set_name(name)
    
    def set_id(self, id: int):

        """Modifica o valor do atributo privado 'id'
        
        Parameters
        ----------
        id: int
            Identificador do status da tarefa
        """

        if not isinstance(id, int) or id < 0:

            raise ValueError("O identificador deve ser um inteiro positivo!")

        self._id = id
    
    def set_name(self, name: str):

        """Modifica o valor do atributo privado 'name'
        
        Parameters
        ----------
        name: str
            Nome do status da tarefa
        """

        if not isinstance(name, str) or name == "":

            raise ValueError("O nome deve ser uma sequência de caracteres não vazia!")

        self._name = name
    
    @property
    def id(self) -> int:

        """Acessa o valor do atributo privado 'id'

        Returns
        -------
        int
            Identificador do status da tarefa
        """

        return self._id

    @property
    def name(self) -> str:

        """Acessa o valor do atributo privado 'name'

        Returns
        -------
        str
            Nome do status da tarefa
        """

        return self._name