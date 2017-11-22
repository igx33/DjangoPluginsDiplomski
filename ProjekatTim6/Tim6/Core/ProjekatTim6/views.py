from django.core import serializers
from django.shortcuts import render, redirect

# Create your views here.
#from ProjekatTim6 import apps
from django.apps.registry import apps
from ProjekatTim6.models import Element, Link, TreeElement
from django.core.serializers.json import DjangoJSONEncoder


def index(request):

    elementi = Element.objects.all()
    linkovi = Link.objects.all()



    broj_param = 0

    #plugini = apps.get_app_config('d3_primeri').plugini_ucitavanje
    plugini = apps.get_app_config('ProjekatTim6').plugini_prikaz
    ucitavanje_plugini = apps.get_app_config('ProjekatTim6').plugini_ucitavanje

    print("OPE OVO..")
    return render(request,"index.html",{"title":"Index","linkovi":linkovi,"elementi":elementi,"plugini":plugini,"ucitavanje_plugini":ucitavanje_plugini, "broj_param":broj_param})

def daj_djecu(parent):
    linkovi = Link.objects.all()
    lista_djece = list()
    lista_te_djece = list()
    for l in linkovi:
        if parent.id == l.elementParent.id:
            lista_djece.append(l.elementChild)


    for ld in lista_djece:
        te = TreeElement()
        te._name=ld.id
        te._naziv=ld.id
        te._children=daj_djecu(ld)
        lista_te_djece.append(te)


    return lista_te_djece


def tree_view():
    elementi = Element.objects.all()
    linkovi = Link.objects.all()
    lista_pp = list()
    lista_pp_te = list()
    for e in elementi:
        naslo = False
        for l in linkovi:
            if e.id == l.elementChild.id:
                naslo = True
                break
        if naslo == False:
            lista_pp.append(e)

    #root = TreeElement('Root', lista_pp)

    for pp in lista_pp:
        te = TreeElement()
        te.naziv=pp.id
        te.name = pp.id
        te.children=daj_djecu(pp)
        #daj_djecu(pp)
        lista_pp_te.append(te)


    rootElementForTree = TreeElement()
    rootElementForTree._naziv='Root'
    rootElementForTree._name='Root'
    rootElementForTree._children=lista_pp_te
    #json_data = serializers.serialize("json",rootElementForTree)
    #context = {
    #    "json":json_data,
    #}
    return rootElementForTree.toJSON() #context

    #for x in lista_pp:
    #    print(x.id)

def primer1(request):
    return render(request, "primer1.html")

def primer2(request):
    return render(request, "primer2.html")



def prikazi_plugin(request,id):
    request.session['izabran_plugin_prikaz']=id
    plugini=apps.get_app_config('ProjekatTim6').plugini_prikaz
    elementi = Element.objects.all()
    linkovi = Link.objects.all()
    izabrani_id = id



    ucitavanje_plugini = apps.get_app_config('ProjekatTim6').plugini_ucitavanje
    for i in plugini:
        if i.identifier() == id:
            print("TYPE:")
            return render(request,"index.html",
                  {"title":"Index2",
                    "prikazFunkcija":i.srediPrikaz,
                    "staticPrikaz":i.staticPrikaz,
                   "elementi":elementi, "linkovi":linkovi,"plugini":plugini,"ucitavanje_plugini":ucitavanje_plugini}
                   )
    #return redirect('index')

def ucitavanje_plugin_broj_param(request,id):
    request.session['izabran_plugin_ucitavanje']=id
    izabrani_id = id
    plugini = apps.get_app_config('ProjekatTim6').plugini_prikaz
    elementi = Element.objects.all()
    linkovi = Link.objects.all()
    ucitavanje_plugini = apps.get_app_config('ProjekatTim6').plugini_ucitavanje
    broj_potrebnih_podataka = 0
    naziviParametara = ""
    for i in ucitavanje_plugini:
        if i.identifier() == id:
           #i.ucitatiPodatke()
            broj_potrebnih_podataka=i.brojPotrebnihParametara()
            naziviParametara = i.naziviParametara()

    #<h3>'+id+':</h3>
    neophodni_parametri = '<form action="/ucitavanje/plugin/">'
    for i in range(0,broj_potrebnih_podataka):
        neophodni_parametri=neophodni_parametri+'<input type="text" name="p'+str(i)+'" > '
    neophodni_parametri=neophodni_parametri+'<input type="hidden" name="id" id="id" value="'+id+'">'
    neophodni_parametri=neophodni_parametri+'<input type="submit" value="Submit">'
    return render(request, "index.html",
                      {"title": "Index2",
                       "elementi": elementi, "linkovi": linkovi, "plugini": plugini,
                       "ucitavanje_plugini": ucitavanje_plugini,"naziviParametara":naziviParametara,"neophodni_parametri":neophodni_parametri, "treeElement":tree_view()})

        #return redirect('index')
    #return redirect('index')

def ucitavanje_plugin(request,id):
    #p0= request.GET['p0']
    #try:
    #    p1=request.GET['p1']
    #except None:
    #    p1 = ""
    #if request.get['p1']:
    #    p1 = request.GET['p1']
    #p2 = request.GET['p2']
    #idx =  request.GET['id']
    some_dict = {}
    for key,value in request.GET.items():
        print(key + " " + value)
        some_dict[key]=value
    id = request.GET['id']
    print("USLO U OVO UOPSTE")
    request.session['izabran_plugin_ucitavanje']=id
    ucitavanje_plugini=apps.get_app_config('ProjekatTim6').plugini_ucitavanje
    broj_potrebnih_podataka = None
    for i in ucitavanje_plugini:
        if i.identifier() == id:
            i.ucitatiPodatke(some_dict)
            #broj_potrebnih_podataka=i.brojPotrebnihParametara()
            #return render(request, "index.html",
            #      {"title": "Index2",
            #       "graf_prikaz": i.prikazatiPodatke(elementi, linkovi),
            #       "elementi": elementi, "linkovi": linkovi, "plugini": plugini,
            #       "ucitavanje_plugini": ucitavanje_plugini, "neophodni_parametri": neophodni_parametri})

    return redirect('index')
    #return redirect('index')


def complex_graph_prikaz(request):
    print("asdasdasdasd:")
    plugini = apps.get_app_config('ProjekatTim6').plugini_prikaz
    ucitavanje_plugini = apps.get_app_config('ProjekatTim6').plugini_ucitavanje
    xm = None
    for i in plugini:
        #if i.identifier() == id:
        #    i.ucitati()
        #i.prikazatiPodatke()
        xm=i
    elementi=Element.objects.all()
    linkovi=Link.objects.all()

    return render(request,"index.html",
                  {"title":"Index2",
                   "graf_prikaz": xm.prikazatiPodatke(elementi,linkovi)[0],"graf_prikaz": xm.prikazatiPodatke(elementi,linkovi),
                   "elementi":elementi, "linkovi":linkovi,"ucitavanje_plugini":ucitavanje_plugini,"plugini":plugini, "treeElement":tree_view()})