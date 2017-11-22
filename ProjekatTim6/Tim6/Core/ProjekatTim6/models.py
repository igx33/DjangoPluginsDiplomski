from django.db import models
import json

class TreeElement(object):
    def __init__(self,*args,**kwargs):
        self._name = ''
        self._naziv = ''
        self._children = list()

    def toJSON(self):
        return json.dumps(self,default=lambda o: o.__dict__,sort_keys=True,indent=4)
    #def __iter__(self):
        #return iter(self.naziv,self.name)
        #return iter(self._children)
        #for item in self._children:
        #    yield item
            #yield self._name
            #yield self._naziv
        #return [ self.name, self.naziv, self.children]
        #return iter(self.name, self.naziv, self.children)



# Create your models here.

#class Element(object):
#    def __init__(self,*args,**kwargs):
#        self.__name = kwargs.pop('name',None)
#        self.__id = kwargs.pop('id',None)
#        self.__attributes = kwargs.pop('attributes',None)
#
#    @property
#    def name(self):
#        return self.__name
#
#    @property
#    def id(self):
#        return self.__id
#
#    @property
#    def attributes(self):
#        return self.__attributes
#
#    @name.setter
#    def name(self, vrednost):
#        if isinstance(vrednost, str):
#            self.__name = vrednost
#        else:
#            raise TypeError('Mora biti tipa string')
#
#    @id.setter
#    def id(self, vrednost):
#        if isinstance(vrednost, str):
#            self.__id = vrednost
#        else:
#            raise TypeError('Mora biti tipa string')
#
#    @attributes.setter
#    def attributes(self, vrednost):
#        self.attributes = vrednost
#
#class Link(object):
#    def __init__(self,*args,**kwargs):
#        self.__idRoditelja = kwargs.pop('idRoditelja',None)
#        self.__idDjeteta = kwargs.pop('idDjeteta',None)
#        #self.__attributes = kwargs.pop('attributes',None)
#
#    @property
#    def idRoditelja(self):
#        return self.idRoditelja
#
#    @property
#    def idDjeteta(self):
#        return self.__idDjeteta
#
#    @idRoditelja.setter
#    def idRoditelja(self, vrednost):
#        if isinstance(vrednost, str):
#            self.__idRoditelja = vrednost
#        else:
#            raise TypeError('Mora biti tipa string')
#
#    @idDjeteta.setter
#    def idDjeteta(self, vrednost):
#        if isinstance(vrednost, str):
#            self.__idDjeteta = vrednost
#        else:
#            raise TypeError('Mora biti tipa string')



class Element(models.Model):
    id = models.CharField(max_length=240, primary_key=True)
    #attributes = models.CharField(max_length=240)
    attributes = models.CharField(max_length=240)

    def __str__(self):
        return self.id

class Link(models.Model):
    elementParent = models.ForeignKey(Element, related_name='parentElementi')
    elementChild = models.ForeignKey(Element, related_name='childElementi')

    def __str__(self):
        return self.elementParent




