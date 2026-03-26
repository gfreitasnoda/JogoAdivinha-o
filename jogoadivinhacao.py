import random
from abc import ABC, abstractmethod

class Jogo(ABC):

    @abstractmethod
    def iniciar (self):
        pass

    @abstractmethod
    def jogar(self):
        pass

class jogoAdivinhacao(Jogo):
    def __init__(self):
        self._numero_secreto = random.randint(1, 100)
        self._tentativas = 0
        self._limite = 10
        self._nome = None
        self._pontuacao = 10

    def iniciar(self):
      print("JOGO DA ADIVINHAÇÃO")
      print("Tente adivinhar o número secreto entre 1 e 100")
      print("Voce tem", self._limite, "tentativas")
      self._nome = input("Qual seu nome? ")


    def jogar(self):
      while self._tentativas < self._limite:
        try:
          palpite = int(input("Digite seu palpite: "))
        except:
          print("Digite um número válido")
          continue
        self._tentativas += 1
        self._pontuacao -= 1

        if palpite == self._numero_secreto:
          print("Parabéns!", self._nome, "Você acertouuuu !!!")
          print("Tentativas usadas:", self._tentativas)
          print("Pontução é: ", self._pontuacao)
          return

        elif palpite < self._numero_secreto:
          print("O número secreto é maior")

        else:
          print("O número secreto é menor")

      print("Suas tentativas acabaram!", self._nome)
      print("O numero secreto era:", self._numero_secreto)
      print("Pontuação é: ", self._pontuacao)
def executar_jogo(jogo: Jogo):
    jogo.iniciar()
    jogo.jogar()

jogo = jogoAdivinhacao()
executar_jogo(jogo)