import csv
from tokenize import String
from typing import List
import pandas as pd
import random;
import os;
from sklearn.utils import murmurhash3_32;
# import mmh3;
import numpy as np;
from bitarray import bitarray
import math;
import string;
import matplotlib.pyplot as plt;
import sys
import statistics
from sympy import Min;
import heapq;
import time;

Seed=random.seed(2315); 
path=os.path.abspath(os.getcwd())+"/user-ct-test-collection-01.txt";
data = pd.read_csv(path, sep="\t");
urllist = data.ClickURL.dropna().unique()

def threeGram(x):
    Set=set();
    for i in range(len(x)-2):
        Set.add(x[i:i+3]);

    return Set;


querySet=['http://www.virtualbubblewrap.com', 'http://ww1.bbgetaways.com', 'http://majordomo.valenciacc.edu', 'http://indystar.gannettonline.com', 'http://www.century21bradley.com', 'http://www.southcentercosmetic.com', 'http://meems.imeem.com', 'http://www.sunrvresorts.com', 'http://www.glsc.org', 'http://www.myopenhouse.com', 'http://www.corridorcareers.com', 'http://www.vcfww.com', 'http://www.financialfederal.com', 'http://www.tulsamastergardeners.org', 'http://ccc.atmos.colostate.edu', 'http://www.faeco.telerama.com', 'http://www.africans-art.com', 'http://www.austlii.org', 'http://fudge.org', 'http://www.homeviewermagazine.com', 'http://www.maximumscented.com', 'http://www.sgim.org', 'http://www.largeandlovely.com', 'http://www.beckydorner.com', 'http://www.webelfin.com', 'http://www.me-go.net', 'http://www.windsorgardensnj.com', 'http://www.tejasthumpcycles.com', 'http://www.ask4greg.com', 'http://www.uat.edu', 'http://www.sunynassau.edu', 'http://www.caravanmusic.com', 'http://www.southernbushmotorsports.com', 'http://www.ustrust.com', 'http://www.wasv.com', 'http://www.avemariasingles.co.uk', 'http://www.bodkin.org', 'http://www.wildernesschurch.com', 'http://www.bugmagic.com', 'http://www.latinboys.com', 'http://www.signed-books.co.uk', 'http://www.autoinfozone.com', 'http://www.thejustusleague.com', 'http://www.elevator-world.com', 'http://www.elfa.com.au', 'http://www.hypnotism.org', 'http://www.ucc.vt.edu', 'http://www.woodallkids.org', 'http://helenacvb.visitmt.com', 'http://www.planetfemdom.com', 'http://www.djramsey.com', 'http://foros.chueca.com', 'http://kvasrulit.h.fc2.com', 'http://www.mumsnet.com', 'http://www.197typhoon.org.uk', 'http://www.blackburn.ac.uk', 'http://www.edc.org', 'http://www.cancerdecisions.com', 'http://www.successacres.com', 'http://www.mayraldole.com', 'http://www.jordanbaris.com', 'http://jaycost.blogspot.com', 'http://www.alpinerebuildablecars.com', 'http://livonia.lib.mi.us', 'http://articleonline.net', 'http://www.sweetleaftea.com', 'http://www.expertune.com', 'http://www.dimensionshealth.org', 'http://investors.outback.com', 'http://www.sunandgames.com', 'http://www.axiomrecords.com', 'http://gasparian.blogspot.com', 'http://www.sugarglider63.com', 'http://www.looksmartfood.com', 'http://www.exploris.org', 'http://www.westheimer.com', 'http://makepotlegal555.org', 'http://www.crwi.org', 'http://www.fanstory.com', 'http://directory.serasaskatchewan.com', 'http://www.unionoflove.com', 'http://www.mysilkweddingflowers.com', 'http://www.chricken.de', 'http://www.northgeorgiaguide.com', 'http://ru3.org', 'http://www.ricegourmet.com', 'http://www.mainsteel.com', 'http://www.davewilson.com', 'http://www.berryessa.k12.ca.us', 'http://www.newenglandtours.com', 'http://www.shoplikeanegyptian.com', 'http://store.securehosting.com', 'http://www.swedishinstitute.org', 'http://www.goenglish.com', 'http://www.belnyc.com', 'http://www.getyourrideon.com', 'http://www.houseofruthdothan.org', 'http://www.cotton.org', 'http://www.boson.com', 'http://www.milliondollarwebsite.com.au', 'http://www.reticles.com', 'http://www.deloff.com', 'http://www.meridianford.com', 'http://afvsolutions.com', 'http://thefifthdistrict.com', 'http://www.purelyrics.com', 'http://www.netelco.com', 'http://www.netwalk.com', 'http://www.serialdevil.com', 'http://1471.b9rsbh.info', 'http://sgage.cocc.edu', 'http://www.collectorsinfo.com', 'http://eqiiforums.station.sony.com', 'http://german-shepard-rescue.phoneteleconference.com', 'http://www.dalehollow.com', 'http://www.spraakservice.net', 'http://www.realjournalism.net', 'http://luminous-landscape.com', 'http://www.accessfares.com', 'http://shop.eskimojoes.com', 'http://www.bodybuilding.com', 'http://www.tshirtoutlet.com', 'http://www.yorkshireterrierrescue.net', 'http://wilkinsoncounty.georgia.gov', 'http://www.edfund.org', 'http://www.smithengines.com', 'http://www.thefillmore.com', 'http://bizrate.lycos.com', 'http://www.anddance.com', 'http://www.electric-bikes.com', 'http://products.bluemoonind.com', 'http://www.uww.edu', 'http://search.wral.com', 'http://www.saybrook.com', 'http://www.davidhalluk.com', 'http://www2.sd38.bc.ca:8004', 'http://www.hypoglycemia.asn.au', 'http://www.donegal.k12.pa.us', 'http://www.acibaobab.org', 'http://www.nutrias.org', 'http://www.suntan-bed.com', 'http://www.nrilinks.com', 'http://www.classicpostandbeam.com', 'http://www.balicompany.com', 'http://www.dogonvillage.com', 'http://www.celebritybeauties.net', 'http://www.giovannisroom.com', 'http://www.condolux.net', 'http://www.rctc.org', 'http://www.ecumenism.net', 'http://www.summitactivities.com', 'http://www.pro2.net', 'http://blog.batanga.com', 'http://www.anorexicweb.com', 'http://www.classictaxiservice.com', 'http://www.takeninhand.com', 'http://dbpubs.stanford.edu:8091', 'http://www.al-islam.org', 'http://www.alumni.rutgers.edu', 'http://www.uniformsplusonline.com', 'http://www.aquariumcouncil.org', 'http://wargames.spyz.org', 'http://bealscowboybuckles.com', 'http://www.carolinabeachlive.com', 'http://test-www.opr.ca.gov', 'http://www.thesanhedrin.org', 'http://buyit.twincities.com', 'http://www.troutmusic.com', 'http://www.horizondrugs.com', 'http://zenithstentgraft.com', 'http://www.spenceengineering.com', 'http://www.businessformsstore.com', 'http://www.npl.com', 'http://www.livethelegends.org', 'http://www.hirojo-u.ac.jp', 'http://www.greencar.com', 'http://chicagouncommon.com', 'http://www.cigarnexus.com', 'http://www.kimberlyfisher.com', 'http://www.rosehill.com', 'http://www.countryclipper.com', 'http://www.visitscotland.com', 'http://www.cellgroup.com', 'http://www.klddzdy.com', 'http://www.goextreme.com', 'http://www.williamleegolden.com', 'http://www.garmentaa.com', 'http://www.10w40.com', 'http://www.fireworksdepot.com', 'http://www.ipce.info', 'https://home.comcast.net/~wlbpd/', 'http://www.rdgtrust.com', 'http://www.monkees.net', 'http://www.jameswedgeworth.com', 'http://www.wbra.org', 'http://www.jetwebb.com', 'http://www.emporiumnaturals.com', 'http://www.adt-audio.com', 'http://www.childsaving.org', 'http://www.4myback.co.uk'];

print(len(urllist))
urllist=list(urllist);
for s in querySet:
    urllist.remove(s);

print(len(urllist))
start=time.time();
for s1 in querySet:
    set_s1=threeGram(s1);
    for s2 in urllist:
        set_s2=threeGram(s2);
        Jac=len(set_s1.intersection(set_s2))/len(set_s1.union(set_s2));


end= time.time();
print(end-start)