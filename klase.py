class Racun:
    def __init__(self,broj_racuna,ime_prezime,stanje):
        self.broj_racuna=broj_racuna
        self.ime_prezime=ime_prezime
        self.stanje=stanje
        self.blok=False
        
    def __str__(self):
        return '{} {} {} {}'.format(self.broj_racuna,
        self.sifra,self.ime_prezime,self.stanje)

    def podigni_novac(self,iznos):
        if self.blok:
            print('Racun je blokiran')
            return
        if iznos>self.stanje:
            print( "Nedovoljno sredstava na racunu")
        else:
            self.stanje-=iznos
            print ('Novac uspesno podignut, novo stanje:{}'.format(self.stanje))
            refresh()

    def uplati_novac(self,iznos):
        if self.blok:
            print('Racun je blokiran')
            return
        self.stanje+=iznos
        print('Novac uspesno uplacen, novo stanje:{}'.format(self.stanje))
        refresh()

    def blokiraj_racun(self):
        if self.blok:
            self.blok=False
            print('Racun odblokiran')
        else:
            self.blok=True
            print('Racun blokiran')

    def upit_stanja(self):
        if self.blok:
            print('Racun je blokiran')
            return
        print(self.stanje)

    def izvestaj(self):
        if self.blok:
            print('Racun je blokiran')
            return
        print('Broj racuna:{}\nIme i prezime:{}\nStanje:{}'.format(self.broj_racuna,self.ime_prezime,self.stanje))


def refresh():
    f=open('racuni.txt','w')
    print('{} {} {}'.format(r.broj_racuna,r.ime_prezime,r.stanje),file=f)
    f.close()
    

    


lista_racuna=[]

tekst=open('racuni.txt').read()
racun=tekst.split()
r=Racun(racun[0],racun[1]+' '+racun[2],int(racun[3]))

