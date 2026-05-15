from abc import ABC, abstractmethod
#mediador aqui
class ChatMediator(ABC):

    @abstractmethod
    def enviar_mensagem(self, msg: str, usuario: 'usuario'):
        pass
        
    @abstractmethod
    def add_usuario(self, usuario: 'usuario'):
        pass

class TelegramGroup(ChatMediator):
    
    def __init__(self, group_nome: str):
        self.group_nome = group_nome
        self.usuarios = []

    def add_usuario(self, usuario: 'usuario'):
        self.usuarios.append(usuario)
        usuario.mediator = self
        print(f"{usuario.nome} entrou no grupo '{self.group_nome}'")

    def enviar_mensagem(self, msg: str, enviar: 'usuario'):
        for usuario in self.usuarios:
            if usuario != enviar:
                usuario.receive(msg, enviar.nome)

class usuario(ABC):
    
    def __init__(self, nome: str):
        self.nome = nome
        self.mediator: ChatMediator = None

    @abstractmethod
    def enviar(self, msg: str):
        pass

    @abstractmethod
    def receive(self, msg: str, enviar_nome: str):
        pass

class Chatusuario(usuario):
    
    def enviar(self, msg: str):
        print(f"\n[{self.nome} enviando]: {msg}")
        if self.mediator:
            self.mediator.enviar_mensagem(msg, self)
        else:
            print("usuario não esta em nenhuma sala de chat.")

    def receive(self, msg: str, enviar_nome: str):
        print(f"{self.nome} recebeu de {enviar_nome}: {msg}")

# fabrica

class usuarioFactory:
    @staticmethod
    def create_usuario(nome: str) -> usuario:
        return Chatusuario(nome)
# teste na main

if __name__ == "__main__":
    dev_group = TelegramGroup("Devs poo2")

    nick = usuarioFactory.create_usuario("nick")
    fabio = usuarioFactory.create_usuario("fabio")
    Joao = usuarioFactory.create_usuario("Joao")
    
    print("Iniciando o chat!")
    dev_group.add_usuario(nick)
    dev_group.add_usuario(fabio)
    dev_group.add_usuario(Joao)


    nick.enviar("ola mundo! tudo certo?")
    fabio.enviar("Oi nick! Tudo ótimo por aqui. Alguém sabe o que vai cair na prova de poo2?")
    Joao.enviar("acho que mediador cai")
