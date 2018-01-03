from django.db import models
import json

class TreeElement(object):
    def __init__(self,*args,**kwargs):
        self._name = ''
        self._naziv = ''
        self._children = list()

    def toJSON(self):
        return json.dumps(self,default=lambda o: o.__dict__,sort_keys=True,indent=4)



class Element(models.Model):
    id = models.CharField(max_length=240, primary_key=True)
    attributes = models.CharField(max_length=240)

    def __str__(self):
        return self.id

class Link(models.Model):
    elementParent = models.ForeignKey(Element, related_name='parentElementi')
    elementChild = models.ForeignKey(Element, related_name='childElementi')

    def __str__(self):
        return self.elementParent




