import pymysql


# Simple routine to run a query on a database and print the results:
from ProjekatTim6.models import Element, Link
from ProjekatTim6.services.ucitavanje import UcitatiService


class UcitavanjeIzBaze(UcitatiService):
    """
        U ovoj klasi nalaze se metode koje nam 
        omogucavaju rad sa bazom.
        implementirane su tri metode:
            1)citanjeeTabela
            2)citanjeTabelaSaKolonama
            3)citanjeTabelaSaVezama (linkovi)

        1)citanjeeTabela: 
            ovu metodu koristimo da 
            bi smo saznali koje sve tabele se nalaze 
            u semi baze. Vraca vrednost liste tabela.

        2)citanjeTabelaSaKolonama:
            ova metoda koristi vrednosti koje vraca prva metoda
            i na taj nacin prolazi kroz sve tabele u semi baze
            gde se nad svakom tabelom izvrsava query upit.
            Sve to smestamo u listu gde ce prvi element  biti 
            ime tabele nad kojom vrsimo kverii upit, a ostali 
            elementi su kolone koje se nalaze u toj tabeli

        3)citanjeTabelaSaVezama:
            ova metoda takodje koristi vrednosti koje vraca prva metoda
            gde ce se opet prolaziti kroz sve tabele i nad svakom tabelom 
            ce se vrsiti query upit na osnovu kojeg cemo saznati veze
            izmedju tabela. Drugi element ce biti parent, a prvi element ce biti child
    """

    def naziv(self):
        return "Database Import"
    def identifier(self):
        return "database_import_plugin"

    def _citanjeeTabela(self,conn):
        cur = conn.cursor()
        listaTabela = []
        cur.execute("SHOW TABLES")
        response = cur.fetchall()
        for row in response:
            listaTabela.append(row[0])
            elem = Element(id=row[0], attributes="")
            elem.save()
        return listaTabela

    def _citanjeTabelaSaKolonama(self,conn, tabele,naziv):

        tabeleSaKolonama = []

        for t in tabele:
            cur = conn.cursor()
            cur.execute(
                "select * from information_schema.columns where table_schema = '"+naziv+"'  and table_name = " + "'" + t + "'")
            response = cur.fetchall()
            tab = []
            tab.append(t)



            attr_string = "Columns: "

            for row in response:
                tab.append(row[3])  # uzimam ime kolone
                attr_string=attr_string+" "+row[3]+";"
            tabeleSaKolonama.append(tab)

            elem = None
            try:
                elem = Element.objects.get(id=t)
                elem.attributes=attr_string
                elem.save()
            except Element.DoesNotExist:
                elem = None

        return tabeleSaKolonama



    def _citanjeTabelaSaVezama(self,conn, tabele,naziv):

        tabeleVeze = []

        for t in tabele:
            tab = []
            cur = conn.cursor()
            cur.execute(
                "select table_name from information_schema.KEY_COLUMN_USAGE where table_schema = '"+naziv+"' and referenced_table_name = " + "'" + t + "'")
            response = cur.fetchall()
            response = list(set(response))

            if response:
                for x in response:
                    tt = []
                    tt.append(x[0])
                    tt.append(t)
                    tab.append(tt)

                    try:
                        link = Link()
                        link.elementParent = Element.objects.get(id=t)
                        link.elementChild = Element.objects.get(id=x[0])
                        link.save()
                    except Element.DoesNotExist:
                        print("Ne postoji elem")

                tabeleVeze.append(tab)

        return tabeleVeze

    def _citanjeIzBaze(self,host,port, db, user, passw):

        myConnection = pymysql.connect(host=host,port=(int(port)), user=user, passwd=passw, db=db)

        tabele = self._citanjeeTabela(myConnection)
        print("ovo su tabele :")
        print(tabele)

        print()

        tabeleSaKolonama = self._citanjeTabelaSaKolonama(myConnection, tabele,db)
        print("ovo su tabele sa kolonama")
        print(tabeleSaKolonama)

        tabeleSaVezama = []
        tabeleSaVezama = self._citanjeTabelaSaVezama(myConnection, tabele,db)
        print()
        print("ovo su tabele sa vezama")
        print(tabeleSaVezama)



    def brojPotrebnihParametara(self):
        return 5

    def naziviParametara(self):
        return "Lokacija baze, Port, Naziv sheme, username, password"

    def ucitatiPodatke(self,*args,**kwargs):
        Element.objects.all().delete()
        Link.objects.all().delete()
        host = args[0]['p0']
        port = args[0]['p1']
        db = args[0]['p2']
        user = args[0]['p3']
        passw = args[0]['p4']

        print("host: "+host+", port: "+port+", db: "+ db +", user: "+user+", passw: "+passw)
        self._citanjeIzBaze(host,port,db,user,passw)



