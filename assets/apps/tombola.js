const liste_noms = [
  'Aymen', 'Amir', 'Ahmed', 'Adem', 'Ayoub', 'Amine', 'Achref', 'Ali', 'Aziz',
  'Béchir', 'Bayrem', 'Bassem', 'Bilel',
  'Chadi', 'Chokri', 'Chahid', 'Chaouki',
  'Hafedh', 'Habib',
  'Omar', 'Oussema',
  'Rayan', 'Raslène', 'Rami', 'Ramzi',
  'Salem', 'Salim', 'Sajed', 'Salsabil', 'Sinane', 'Saber', 'Sami',
  'Mohamed', 'Mahmoud', 'Mehdi', 'Majed', 'Malik', 'Mejdi', 'Marouane', 'Mourad',
  'Nadhmi', 'Naceur', 'Noureddine',
  'Walid', 'Wajdi', 'Wahbi'
];
const liste_prix = [
  'Tablette Lenovo 7"', 'Tablette MediaTab 8"',
  'Smartphone Huawei', 'Smartphone A01',
  "Bon d'achat 100 DT", "Bon d'achat 200 DT", "Bon d'achat 500 DT",
  'TV 32" Sony', 'TV 48" Samsung', 'TV 48" Panasonic',
  'Bicyclette enfant', 'Bicyclette Decathlon',
  'iPhone 12', 'iPad Pro'
];

function choix_elements(arr, n) {
  const items = [];
  for (let i = 0; i < n; i++) {
    let item = '';
    while ((item.length == 0 || items.includes(item)) && items.length < arr.length) {
      item = arr[randint(0, arr.length - 1)];
    }
    items.push(item);
  }
  return items;
}

function randint(d, f) {
  return Math.floor(Math.random() * (f - d + 1)) + d;
}

const app = new Vue({
  el: '#ex1',
  data: {
    etape: 0,
    n: 0,
    noms: [],
    np: 0,
    prix: [],
    cadeaux: []
  },
  mounted: function () {
    this.n = randint(5, 8);
    this.initHasardNoms(this.n);
    this.np = randint(2, Math.min(this.n, 3));
    this.initHasardPrix(this.np);
    this.tirageAuSort();
    this.etape = 4;
  },
  methods: {
    initNbreNoms: function () {
      this.n = randint(5, 20)
    },
    initHasardNoms: function (n) {
      this.noms = choix_elements(liste_noms, n);
    },
    initNbrePrix: function () {
      this.np = randint(1, Math.min(this.n, 10));
    },
    initHasardPrix: function (n) {
      this.prix = choix_elements(liste_prix, n);
    },
    tirageAuSort: function () {
      this.cadeaux = choix_elements(this.noms, this.np);
    },
    onValiderEtape: function (etape) {
      switch (etape) {
        case -1: this.initNbreNoms(); break;
        case 0: this.initHasardNoms(this.n); break;
        case 1: this.initNbrePrix(); break;
        case 2: this.initHasardPrix(this.np); break;
        case 3: this.tirageAuSort();
      }
      this.etape = etape + 1;
    }
  }
});

const app2 = new Vue({
  el: '#ex2',
  data: {
    np: 0,
    n: 0,
    noms: [],
    noms2: []
  },
  mounted: function () {
    this.n = 5;
    this.initHasardNoms(this.n);
    this.np = 2;
    this.initHasardPrix(this.np);
    this.tirageAuSort();
  },
  methods: {
    initNbreNoms: function () {
      this.n = randint(5, 20)
    },
    initHasardNoms: function (n) {
      this.noms = choix_elements(liste_noms, n);
    },
    initNbrePrix: function () {
      this.np = randint(1, Math.min(this.n, 10));
    },
    initHasardPrix: function (n) {
      this.prix = choix_elements(liste_prix, n);
    },
    tirageAuSort: function () {
      this.noms2 = this.noms.slice();
      for (let i = 0; i < this.np; i++) {
        let j = randint(0, this.noms2.length - 1);
        const t = this.noms2[i];
        this.noms2[i] = this.noms2[j];
        this.noms2[j] = t;
      }
    }
  }
});

const app3 = new Vue({
  el: '#ex3',
  data: {
    np: 0,
    n: 0,
    noms: [],
    prix: []
  },
  mounted: function () {
    this.n = 5;
    this.initHasardNoms(this.n);
    this.np = 2;
    this.initHasardPrix(this.np);
    this.tirageAuSort();
  },
  methods: {
    initNbreNoms: function () {
      this.n = randint(5, 20)
    },
    initHasardNoms: function (n) {
      this.noms = choix_elements(liste_noms, n);
    },
    initNbrePrix: function () {
      this.np = randint(1, Math.min(this.n, 10));
    },
    initHasardPrix: function (n) {
      this.prix = choix_elements(liste_prix, n);
    },
    tirageAuSort: function () {
      for (let i = 0; i < this.n; i++) {
        let j = randint(0, this.noms.length - 1);
        const t = this.noms[i];
        this.noms[i] = this.noms[j];
        this.noms[j] = t;
      }
    }
  }
});

const app4 = new Vue({
  el: '#ex4',
  data: {
    etape: 0,
    n: 0,
    notes: [],
    moy: 0.0,
    notemin: 0.0,
    notemax: 0.0,
    nbr_el: 0,
    nbr_moy: 0,
    nbi: [],
    notes_sd: []
  },
  mounted: function () {
    this.n = randint(3, 10);
    this.notes = Array(this.n).fill(0.0).map(note => randint(0, 80) / 4);
    this.moy = this.notes.reduce((pv, cv) => pv + cv, 0.0) / this.notes.length;
    this.notemin = Math.min(...this.notes);
    this.notemax = Math.max(...this.notes);
    this.nbr_moy = this.notes.reduce((pv, cv) => pv + +(cv >= 10.0), 0);
    this.nbr_el = this.notes.reduce((pv, cv) => pv + +(cv >= this.moy), 0);
    this.nbi = Array(5).fill(0).map((v, i) => this.notes.reduce((pv, cv) => pv + +(cv >= 5 * i && cv < 5 * (i + 1)), 0));
    this.notes_sd = this.notes.filter((note, idx) => this.notes.indexOf(note) === idx);
    this.notes_sd.sort((a, b) => a - b);
    this.etape = 6;
  },
  methods: {
    onValiderEtape: function (etape) {
      switch (etape) {
        case -1: this.n = randint(3, 10); break;
        case 0: this.notes = Array(this.n).fill(0.0).map(note => randint(0, 80) / 4); break;
        case 1: 
          this.moy = this.notes.reduce((pv, cv) => pv + cv, 0.0) / this.notes.length; break;
        case 2:
          this.notemin = Math.min(...this.notes);
          this.notemax = Math.max(...this.notes); break;
        case 3: 
          this.nbr_el = this.notes.reduce((pv, cv) => pv + +(cv >= this.moy), 0);
          this.nbr_moy = this.notes.reduce((pv, cv) => pv + +(cv >= 10.0), 0); break;
        case 4: this.nbi = Array(5).fill(0).map((v, i) => this.notes.reduce((pv, cv) => pv + +(cv >= 5 * i && cv < 5 * (i + 1)), 0)); break;
        case 5:
          this.notes_sd = this.notes.filter((note, idx) => this.notes.indexOf(note) === idx);
          this.notes_sd.sort((a, b) => a - b);
      }
      this.etape = etape + 1;
    }
  }
});

const app5 = new Vue({
  el : '#app-5',
  data: {
    nb_sieges: 20,
    reserves: [],
    libres: []
  },
  mounted: function() {
    this.libres = Array(20).fill(0).map((v, i) => i + 1);
    Array(randint(10, 15)).fill(0).forEach(() => {
      const p = randint(0, this.libres.length - 1);
      this.reserves.push(this.libres[p]);
      this.libres.splice(p, 1);
    });
  }
});
