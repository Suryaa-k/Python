from abc import ABC, abstractmethod
class Experiment(ABC):
    precision=0.1
    def __init__(self,para):
        self.__para=para

    @abstractmethod
    def setup():
        pass

    @abstractmethod
    def execute():
        pass

    @classmethod
    def change_p(cls,np):
        cls.precision=np

    def logging(self,mode="test"):
        print(f"Running in {mode} model")

TE=10 #This must be a class
CE=20 #This must be a class

batch=[TE(),CE()]
batch1=batch.copy()
batch1[0].setpara(100)

