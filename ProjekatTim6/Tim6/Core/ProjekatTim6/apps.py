import pkg_resources
from django.apps.config import AppConfig


class Projekattim6Config(AppConfig):
    name = 'ProjekatTim6'
    plugini_prikaz = []
    plugini_ucitavanje = []

    def ready(self):
        #self.plugini_ucitavanje=[]
        self.plugini_prikaz=load_plugins("graph.prikazati")
        self.plugini_ucitavanje= load_plugins("data_import.ucitati");
        #self.plugini_ucitavanje = load_plugins("dbschemaimport.ucitati");
        #self.plugini_ucitavanje.append(load_plugins("html_import.ucitati"))
        #self.plugini_ucitavanje.append(load_plugins("dbschemaimport.ucitati"))

def load_plugins(oznaka):
    plugins = []
    for ep in pkg_resources.iter_entry_points(group=oznaka):
        p = ep.load()
        print("{} {}".format(ep.name, p))
        plugin = p()
        plugins.append(plugin)
    return plugins
