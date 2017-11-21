
#from ProjekatTim6.models import Element, Link
import json as jsx
from urllib.parse import urlencode
from urllib.request import Request, urlopen
import requests

#from ProjekatTim6.Tim6.Core.ProjekatTim6.services.ucitavanje import UcitatiService

from Core.ProjekatTim6.services.ucitavanje import UcitatiService


class UcitavanjeTelefona(UcitatiService):

    def naziv(self):
        return "Phone Import"
    def identifier(self):
        return "phone_release_api_plugin"
    def brojPotrebnihParametara(self):
        return 1
    def naziviParametara(self):
        return "Naziv brenda"
    def ucitatiPodatke(self,*args,**kwargs):
        print()

def main():

    url = "https://fonoapi.freshpixl.com/v1/getlatest"
    post_data = {"brand":"samsung", "token":"40431b4a3ee010cb9a655a999123054b356fc8777ae56c70"}
    json_send_data = jsx.dumps(post_data)
    request = Request(url,json_send_data)
    #json = urlopen(request).read().decode()


    print(urlopen(request).read())

if __name__ == "__main__":
    main()