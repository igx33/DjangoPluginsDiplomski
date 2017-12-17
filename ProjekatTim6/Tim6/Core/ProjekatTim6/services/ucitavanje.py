import abc


class UcitatiService(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def naziv(self):
        pass

    @abc.abstractmethod
    def identifier(self):
        pass

    @abc.abstractmethod
    def ucitatiPodatke(self,*args,**kwargs):
        pass

    @abc.abstractmethod
    def brojPotrebnihParametara(self):
        pass

    @abc.abstractmethod
    def naziviParametara(self):
        pass