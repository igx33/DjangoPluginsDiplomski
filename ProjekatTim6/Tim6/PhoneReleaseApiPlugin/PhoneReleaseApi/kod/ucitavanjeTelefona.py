
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
    post_data = {"brand":"samsung", "token":"e2bd47e976e0118124f6254702efee5c62aca08cb9707734"}
    json_send_data = jsx.dumps(post_data)
    request = requests.post(url,json=post_data)
    #json = urlopen(request).read().decode()
    rec_data= []
    rec_data = jsx.loads(request.text)


    print(rec_data)
    for i in range(0,len(rec_data)):
        print(rec_data[i]['DeviceName'], "->", rec_data[i]['status'])

if __name__ == "__main__":
    main()