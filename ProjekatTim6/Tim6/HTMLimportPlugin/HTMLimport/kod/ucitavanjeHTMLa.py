from ProjekatTim6.models import Element, Link
#from Tim6.Core.ProjekatTim6.services.ucitavanje import UcitatiService
import urllib

from ProjekatTim6.services.ucitavanje import UcitatiService
from bs4 import BeautifulSoup
from lxml import html
import lxml.html
import string
import random
import urllib.request
import requests
from django.db import models


class HTMLImport(UcitatiService):
    def naziv(self):
        return "HTML Import"
    def identifier(self):
        return "html_import_plugin"



    def brojPotrebnihParametara(self):
        return 1

    def naziviParametara(self):
        return "Site address"

    def _pretraga_u_dubinu(self,element, prethodniID):
        string.letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        parent_id = ""
        if prethodniID == "":

            parent_attrs = element[0].attrs
            naslo_za_parenta = False
            for key, value in parent_attrs.items():
                # print("KEY: "+key + ", VALUE: "+value)
                if (key == 'id'):
                    naslo_za_parenta = True
                    break
            if (naslo_za_parenta == True):
                parent_id = element[0].name + '_' + element[0]['id']
            else:
                parent_id = parent_id + element[0].name + '_'
                for ix in (0, 3):
                    parent_id = parent_id + random.choice(string.letters)

        else:
            parent_id = prethodniID

        eparent =None
        try:
            eparent = Element.objects.get(id=prethodniID)
        except Element.DoesNotExist:
            eparent=None

        if (eparent == None):
            attributi_parenta =""
            for key, value in parent_attrs.items():
                if isinstance(value,list):
                    for va in value:
                        attributi_parenta=attributi_parenta+ " "+key+" : "+va + "; "
                else:
                    attributi_parenta=attributi_parenta+" "+key+":"+value+";"
                #attributi_parenta=attributi_parenta+ " "+key+ " : "+"nesto"+ ";"
            eparent = Element(id=parent_id,attributes=attributi_parenta)
            eparent.save()

        children = element[0].find_all(recursive=False)

        # for key, value in parent_attrs.items():
        #    if (key == 'id'):
        #        parent_id = value
        #    else:
        #        for ix in (0, 3):
        #            parent_id = parent_id + random.choice(string.letters)
        for i in range(0, len(children)):

            child_id = ""
            naslo_za_child = False
            child_attrs = children[i].attrs
            for key, value in child_attrs.items():
                if (key == 'id'):
                    naslo_za_child = True
                    break
            if (naslo_za_child == True):
                child_id = children[i].name + '_' + children[i]['id']
            else:
                child_id = children[i].name + '_'
                for ix in (0, 3):
                    child_id = child_id + random.choice(string.letters)
            # child_id = ""
            # child_attrs = children[i].attrs
            # for key, value in child_attrs.items():
            #    if(key=="id"):
            #        child_id=value
            #    else:
            #        for ix in (0,3):
            #            child_id=child_id+random.choice(string.letters)
            #        #parent_id=
            attr_string =""
            for key, value in child_attrs.items():
                if isinstance(value,list):
                    for va in value:
                        attr_string=attr_string+ " "+key+" : "+va + "; "
                else:
                    attr_string=attr_string+" "+key+":"+value+";"

            e = Element(id=child_id, attributes=attr_string)
            e.save()

            link = Link()
            #link.elementParent = Element.objects.get(id=eparent.id)
            link.elementParent = Element.objects.get(id=parent_id)
            #link.elementChild = Element.objects.get(id=e.id)
            link.elementChild = Element.objects.get(id=child_id)
            link.save()
            # link = Link(children[i]['id'],element[0]['id'])
            #link = Link(child_id, parent_id)
            #lista_linkova.append(link)
            # print("-==-=-=-=-=-=-=-=-=-=-=-=-=")
            # print(children[i])
            self._pretraga_u_dubinu([children[i]], child_id)
            # print(len(children))
            # print(children)

        #for l in Link.objects.all():
        #    print("PARENT: "+ l.elementParent.id +" , CHILD: "+l.elementChild.id)


    def ucitatiPodatke(self,*args,**kwargs):
        Element.objects.all().delete()
        Link.objects.all().delete()
        #
        #print(kwargs['p0'])
        #for a in args:
        #    print(a)

        some_url=args[0]['p0']
        print("asdasdasdasdasdasdasdqweqweqw")

        #for key, value in kwargs.items():
        #    print(key + " " + value)
        #with urllib.request.urlopen("http://www.python.org") as url:
           # s = url.read()
        # I'm guessing this would output the html source code?
        #print(s)

        # url = "https://www.cafe.ba/"
        # print("*****************************")
        # print(url)
        # print("*****************************")
        # page=None
        # with urllib.request.urlopen(url) as url:
        #     page = html.fromstring(url.read())
        # page = html.fromstring(urllib.urlopen(url).read())
        #url = raw_input(urlx)
        #r = requests.get("http://" + url)

        #page = lxml.html.parse(url)
        #page = requests.get("http://www.rdrop.com/")
        page = requests.get(some_url)
        #page = urllib.urlopen("http://www.python.org")
        #s = page.read()
        #f.close()

        soup = BeautifulSoup(page.content, "html.parser")
        string.letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        lista_linkova = []
        prethodniID = ""
        body = soup("body", {})
        #print(body)
        #print("=====================================================")
        #print(w)

        self._pretraga_u_dubinu(body, "")

