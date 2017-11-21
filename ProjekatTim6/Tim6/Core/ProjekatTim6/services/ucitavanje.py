import abc


class UcitatiService(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def naziv(self):
        """
        Funjkcija koja vraca naziv plugina
        """

        pass

    @abc.abstractmethod
    def identifier(self):
        """
        Funjkcija koja vraca identifikator za plugin
        da bi se mogli povezati
        """

        pass

    @abc.abstractmethod
    def ucitatiPodatke(self,*args,**kwargs):
        """
         Prima potrebne parametre koje koristi plugin i vrsi ucitavanje podataka, te kreira modele i smjesta ih u bazu
         
        """

        pass

    @abc.abstractmethod
    def brojPotrebnihParametara(self):
        pass

    @abc.abstractmethod
    def naziviParametara(self):
        pass