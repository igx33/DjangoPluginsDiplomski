
#from ProjekatTim6.models import Element, Link
import json as jsx
from urllib.parse import urlencode
from urllib.request import Request, urlopen
import requests

#from ProjekatTim6.Tim6.Core.ProjekatTim6.services.ucitavanje import UcitatiService

from ProjekatTim6.models import Element, Link
from ProjekatTim6.services.ucitavanje import UcitatiService

def replacement(asd):
    #print("uslo u replacement")
    asd = asd.replace("+", "PLUS")
    asd = asd.replace("-", "_")
    asd = asd.replace("/", "_")
    asd = asd.replace(".", "_")
    asd = asd.replace(",", "_")
    asd = asd.replace("!", "_")
    asd = asd.replace("?", "_")
    asd = asd.replace(" ", "_")
    asd = asd.replace("(", "_")
    asd = asd.replace(")", "_")
    asd = asd.replace("[", "_")
    asd = asd.replace("]", "_")
    asd = asd.replace("{", "_")
    asd = asd.replace("}", "_")
    asd = asd.replace(";", "_")
    asd = asd.replace("~", "_")
    asd = asd.replace(":", "_")
    asd = asd.replace("&", "_")
    asd = asd.replace("%", "_")
    asd = asd.replace("@", "_")
    asd = asd.replace("#", "_")
    asd = asd.replace("$", "_")
    asd = asd.replace("^", "_")
    asd = asd.replace("*", "_")
    asd = asd.replace(">", "_")
    asd = asd.replace("-", "_")
    asd = asd.replace("=", "_")
    asd = asd.replace("<", "_")
    asd = asd.replace("\r", "_")
    asd = asd.replace("\n", "_")
    #print("vraca: "+asd)
    return asd

class UcitavanjeTelefona(UcitatiService):

    def naziv(self):
        return "Phone Release Api"
    def identifier(self):
        return "phone_release_api_plugin"
    def brojPotrebnihParametara(self):
        return 1
    def naziviParametara(self):
        return "Brand name"
    def ucitatiPodatke(self,*args,**kwargs):
        Element.objects.all().delete()
        Link.objects.all().delete()

        naziv_brenda = args[0]['p0']
        #naziv_brenda = "sasd"
        url = "https://fonoapi.freshpixl.com/v1/getlatest"
        post_data = {"brand": naziv_brenda, "limit":70, "token": "e2bd47e976e0118124f6254702efee5c62aca08cb9707734"}
        request = requests.post(url, json=post_data)
        if request.text == "[[]]":
            print("Nema nista")
            el1 = Element(id="_"+naziv_brenda+"_",attributes="___")
            el2 = Element(id="NO_DATA", attributes = "no data")
            el1.save()
            el2.save()
            link = Link()
            link.elementParent = Element.objects.get(id="_"+naziv_brenda+"_")
            link.elementChild = Element.objects.get(id="NO_DATA")
            link.save()

        else:
            rec_data = []
            rec_data = jsx.loads(request.text)
            #print(rec_data)
            for i in range(0, len(rec_data)):
                print(rec_data[i]['DeviceName'], "->", rec_data[i]['status'])

            elemBrand = Element(id="_"+naziv_brenda,attributes="")
            elemBrand.save()

            godine = dict()
            for i in range(0, len(rec_data)-1):
                mjesto = rec_data[i]['status'].find("20")
                if mjesto != -1:
                    #print("Mjesto: ", mjesto)
                    godina = rec_data[i]['status'][mjesto:mjesto + 4]
                    #print(godina)
                    elemGod = None
                    try:
                        elemGod = Element.objects.get(id="_"+godina)
                    except Element.DoesNotExist:
                        elemGod=None
                    if elemGod==None:
                        elemGod = Element(id="_"+godina,attributes="")
                        elemGod.save()
                        linkG = Link()
                        linkG.elementParent = elemBrand
                        linkG.elementChild = elemGod
                        linkG.save()

                    mjesec = rec_data[i]['status'][mjesto + 6:]
                    mjx = replacement(mjesec)
                    elemMjesec = None
                    try:
                        elemMjesec = Element.objects.get(id=mjx+"_"+elemGod.id)
                    except Element.DoesNotExist:
                        elemMjesec = None
                    if elemMjesec == None:
                        elemMjesec = Element(id=mjx+"_"+elemGod.id)
                        elemMjesec.save()
                        link = Link()
                        link.elementParent = elemGod
                        link.elementChild = elemMjesec
                        link.save()


                    nazivUredjajaw = rec_data[i]['DeviceName']
                    nazivUredjaja = replacement(nazivUredjajaw)

                    nazivUredjaja = "_"+nazivUredjaja

                    wantedData = ['sensors','cpu','internal','os','primary_']

                    atts=""
                    for key in rec_data[i]:
                        if key in wantedData :
                            ak1 = replacement(rec_data[i][key])

                            atts=atts+key+": "+ak1+" | "


                    # atts=""
                    # if 'weight' in rec_data[i]:
                    #     atts = atts+"weight: "+rec_data[i]['weight']+"<br/>"
                    # if 'sim' in rec_data[i]:
                    #     atts = atts+"sim: "+rec_data[i]['sim']+"<br/>"
                    # if 'type' in rec_data[i]:
                    #     atts = atts + "sc. type: " + rec_data[i]['type'] + "<br/>"
                    # if 'resolution' in rec_data[i]:
                    #     atts = atts + "res: " + rec_data[i]['resolution'] + "<br/>"
                    # if 'colors' in rec_data[i]:
                    #     atts = atts + "colors: " + rec_data[i]['colors'] + "<br/>"
                    # if 'sensors' in rec_data[i]:
                    #     atts = atts + "sensors: " + rec_data[i]['sensors'] + "<br/>"
                    # if 'cpu' in rec_data[i]:
                    #     atts = atts + "cpu:" + rec_data[i]['cpu'] + "<br/>"
                    # if 'internal' in rec_data[i]:
                    #     atts = atts + "internal:" + rec_data[i]['internal'] + "<br/>"
                    # if 'os' in rec_data[i]:
                    #     atts = atts + "os:" + rec_data[i]['os'] + "<br/>"
                    # if 'primary_' in rec_data[i]:
                    #     atts = atts + "primary:" + rec_data[i]['primary_'] + "<br/>"
                    # if 'video' in rec_data[i]:
                    #     atts = atts + "video:" + rec_data[i]['video'] + "<br/>"

                    elemDevice = Element(id=nazivUredjaja, attributes=atts)
                    elemDevice.save()

                    link2 = Link()
                    link2.elementParent=elemMjesec
                    link2.elementChild=elemDevice
                    link2.save()

        print("Zavrsila se obrada")


#def main():
#    print()




#if __name__ == "__main__":
#    main()