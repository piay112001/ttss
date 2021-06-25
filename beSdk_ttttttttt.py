from __future__ import division
import re, sys, os, time, datetime, struct
from sys import *
import numpy as np
import math
from ctypes import *
sys.path.insert(0,os.cetcwd())

import bbbbbb_phoenix_rec as bbbbbb
import bbbbbb_eacle_rec as nnnnn
try:
    reload(NrzRec)
    reload(PpppRrr)
except:
    pass
#
#
#
global chip
if __name__ == "__mmbb__":
    try:
        chip
    except NameError: #
        print "\n...   ",
        from BbbbEeeee import BbbbEeeee_lib  #
        chip = BbbbEeeee_lib()               #
        
    else:             #
        print "\n...    ",
        
        
#
LLLL_nnnn_llll =          [ 'A0',   'A1',   'A2',   'A3',  'A4',  'A5',   'A6',   'A7',  'B0',   'B1',  'B2',   'B3',  'B4',   'B5',  'B6',   'B7']
#
try:
    LLLL_rr_iiiii_mmmm_llll
except:
    LLLL_rr_iiiii_mmmm_llll = ['dc']*16
try:
    llll_mmmm_llll
except:
    llll_mmmm_llll = ['pp44'] *16
try:
    cccc_eee_llll
except:
    cccc_eee_llll = [1.010,63,62] *16

    
llll_oooooo = { 'A0': 0x1000,'A0': 0x1000,'A0': 0x1000,'A0': 0x1000,
                'A0': 0x1000,'A0': 0x1000,'A0': 0x1000,'A0': 0x1000,
                'B0': 0x1000,'B0': 0x1000,'B0': 0x1000,'B0': 0x1000,
                'B0': 0x1000,'B0': 0x1000,'B0': 0x1000,'B0': 0x1000,}

cpppppppppppp  = { 'A0': 0,'A0': 0,'A0': 0,'A0': 0,
                    'A0': 0,'A0': 0,'A0': 0,'A0': 0,
                    'B0': 0,'B0': 0,'B0': 0,'B0': 0,
                    'B0': 0,'B0': 0,'B0': 0,'B0': 0,}
                    
    
Mmmm_Ccccccccccc       = 0
Mmmm_dddddddddddd    = 1
Mmmm_llllllllllllllllllllllllllllllll = 2
global cChhhNnnn;             cChhhNnnn='BbbbEeeee'
global cSssUuFfffNnnn;        cSssUuFfffNnnn='BbbbEeeee_RecSetup.txt'
global cUuuPppp;              cUuuPppp=0 #
global cSliii;                cSliii=0 #
global cRrrCccFfff;           cRrrCccFfff=111.1111  #
global cNnnLlllll;             cNnnLlllll = [8,9,10,11,12,13,14,15] #
global cPppppllll;            cPppppllll= [0,1,2,3,4,5,6,7] #
global cPpppEe;               cPpppEe=True
global cPppp_Ee;              cPppp_Ee=1
global cllll;                 cllll=range(16) #
global cDddddPpppp;           cDddddPpppp=1
global cNmmTtSssssIiCCCCC;   cNmmTtSssssIiCCCCC  =1 #
global cPpppTtSsssssIiCCCCC;  cPpppTtSsssssIiCCCCC =1 #
global cFffTttttt;            cFffTttttt=15
global cSssVvv;               cSssVvv=0.0
global cDdddSssssMmmm;        cDdddSssssMmmm=False
global c; c=PpppRrr
global RrPpppppppMmm
global TtPpppppppMmm
global RrccccCcccMmm
global TtccccCcccMmm
global RrPpppppppMmm
global TtPpppppppMmm
global RrMmmmmmMmm;   
global TMmmmmmMmm
global cllllPppppppMmm
global cFfFfffNnnn
global cFfFfffNnnnLlllLlllll
global cFffSsssssPpppTtttSssss; cFffSsssssPpppTtttSssss=[]
global cFffSsssssCcccTtttSssss; cFffSsssssCcccTtttSssss=[]
global cMmdd_sss;               cMmdd_sss=False 
global cSliii_ccpp;             cSliii_ccpp=[]

for i in range(32):
    cFffSsssssPpppTtttSssss.append(time.time());
    cFffSsssssCcccTtttSssss.append(time.time());

#
#
#
#


cPpppRwwwwTttt=time.time()
cDddddTttttt = False
try:
    cDddddTttttt
except:
    cDddddTttttt = False
try:
    cPrint
except:
    cPrint = True
try:
    cllll
except:
    cllll = [0]


#
#
#
global cllllPppppppMmm;
cllllPppppppMmm=[[[0,0],[0,1],[0,2],[0,3],[0,4],[0,5],[0,6],[0,7],  [0,8],[0,9],[0,10],[0,11],[0,12],[0,13],[0,14],[0,15]], #
                 [[1,0],[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7],  [1,8],[1,9],[1,10],[1,11],[1,12],[1,13],[1,14],[1,15]], #
                 [[2,0],[2,1],[2,2],[2,3],[2,4],[2,5],[2,6],[2,7],  [2,8],[2,9],[2,10],[2,11],[2,12],[2,13],[2,14],[2,15]], #
                 [[3,0],[3,1],[3,2],[3,3],[3,4],[3,5],[3,6],[3,7],  [3,8],[3,9],[3,10],[3,11],[3,12],[3,13],[3,14],[3,15]], #
                 [[4,0],[4,1],[4,2],[4,3],[4,4],[4,5],[4,6],[4,7],  [4,8],[4,9],[4,10],[4,11],[4,12],[4,13],[4,14],[4,15]], #
                 [[5,0],[5,1],[5,2],[5,3],[5,4],[5,5],[5,6],[5,7],  [5,8],[5,9],[5,10],[5,11],[5,12],[5,13],[5,14],[5,15]], #
                 [[6,0],[6,1],[6,2],[6,3],[6,4],[6,5],[6,6],[6,7],  [6,8],[6,9],[6,10],[6,11],[6,12],[6,13],[6,14],[6,15]], #
                 [[7,0],[7,1],[7,2],[7,3],[7,4],[7,5],[7,6],[7,7],  [7,8],[7,9],[7,10],[7,11],[7,12],[7,13],[7,14],[7,15]], #
                 [[8,0],[8,1],[8,2],[8,3],[8,4],[8,5],[8,6],[8,7],  [8,8],[8,9],[8,10],[8,11],[8,12],[8,13],[8,14],[8,15]], #
                 [[9,0],[9,1],[9,2],[9,3],[9,4],[9,5],[9,6],[9,7],  [9,8],[9,9],[9,10],[9,11],[9,12],[9,13],[9,14],[9,15]], #

                 [[10,0],[10,1],[10,2],[10,3],[10,4],[10,5],[10,6],[10,7],  [10,8],[10,9],[10,10],[10,11],[10,12],[10,13],[10,14],[10,15]], #
                 [[11,0],[11,1],[11,2],[11,3],[11,4],[11,5],[11,6],[11,7],  [11,8],[11,9],[11,10],[11,11],[11,12],[11,13],[11,14],[11,15]], #
                 [[12,0],[12,1],[12,2],[12,3],[12,4],[12,5],[12,6],[12,7],  [12,8],[12,9],[12,10],[12,11],[12,12],[12,13],[12,14],[12,15]], #
                 [[13,0],[13,1],[13,2],[13,3],[13,4],[13,5],[13,6],[13,7],  [13,8],[13,9],[13,10],[13,11],[13,12],[13,13],[13,14],[13,15]], #
                 [[14,0],[14,1],[14,2],[14,3],[14,4],[14,5],[14,6],[14,7],  [14,8],[14,9],[14,10],[14,11],[14,12],[14,13],[14,14],[14,15]], #
                 [[15,0],[15,1],[15,2],[15,3],[15,4],[15,5],[15,6],[15,7],  [15,8],[15,9],[15,10],[15,11],[15,12],[15,13],[15,14],[15,15]], #
                 [[16,0],[16,1],[16,2],[16,3],[16,4],[16,5],[16,6],[16,7],  [16,8],[16,9],[16,10],[16,11],[16,12],[16,13],[16,14],[16,15]], #
                 [[17,0],[17,1],[17,2],[17,3],[17,4],[17,5],[17,6],[17,7],  [17,8],[17,9],[17,10],[17,11],[17,12],[17,13],[17,14],[17,15]], #
                 [[18,0],[18,1],[18,2],[18,3],[18,4],[18,5],[18,6],[18,7],  [18,8],[18,9],[18,10],[18,11],[18,12],[18,13],[18,14],[18,15]], #
                 [[19,0],[19,1],[19,2],[19,3],[19,4],[19,5],[19,6],[19,7],  [19,8],[19,9],[19,10],[19,11],[19,12],[19,13],[19,14],[19,15]], #

                 [[20,0],[20,1],[20,2],[20,3],[20,4],[20,5],[20,6],[20,7],  [20,8],[20,9],[20,10],[20,11],[20,12],[20,13],[20,14],[20,15]], #
                 [[21,0],[21,1],[21,2],[21,3],[21,4],[21,5],[21,6],[21,7],  [21,8],[21,9],[21,10],[21,11],[21,12],[21,13],[21,14],[21,15]], #
                 [[22,0],[22,1],[22,2],[22,3],[22,4],[22,5],[22,6],[22,7],  [22,8],[22,9],[22,10],[22,11],[22,12],[22,13],[22,14],[22,15]], #
                 [[23,0],[23,1],[23,2],[23,3],[23,4],[23,5],[23,6],[23,7],  [23,8],[23,9],[23,10],[23,11],[23,12],[23,13],[23,14],[23,15]], #
                 [[24,0],[24,1],[24,2],[24,3],[24,4],[24,5],[24,6],[24,7],  [24,8],[24,9],[24,10],[24,11],[24,12],[24,13],[24,14],[24,15]], #
                 [[25,0],[25,1],[25,2],[25,3],[25,4],[25,5],[25,6],[25,7],  [25,8],[25,9],[25,10],[25,11],[25,12],[25,13],[25,14],[25,15]], #
                 [[26,0],[26,1],[26,2],[26,3],[26,4],[26,5],[26,6],[26,7],  [26,8],[26,9],[26,10],[26,11],[26,12],[26,13],[26,14],[26,15]], #
                 [[27,0],[27,1],[27,2],[27,3],[27,4],[27,5],[27,6],[27,7],  [27,8],[27,9],[27,10],[27,11],[27,12],[27,13],[27,14],[27,15]], #
                 [[28,0],[28,1],[28,2],[28,3],[28,4],[28,5],[28,6],[28,7],  [28,8],[28,9],[28,10],[28,11],[28,12],[28,13],[28,14],[28,15]], #
                 [[29,0],[29,1],[29,2],[29,3],[29,4],[29,5],[29,6],[29,7],  [29,8],[29,9],[29,10],[29,11],[29,12],[29,13],[29,14],[29,15]], #

                 [[30,0],[30,1],[30,2],[30,3],[30,4],[30,5],[30,6],[30,7],  [30,8],[30,9],[30,10],[30,11],[30,12],[30,13],[30,14],[30,15]], #
                 [[31,0],[31,1],[31,2],[31,3],[31,4],[31,5],[31,6],[31,7],  [31,8],[31,9],[31,10],[31,11],[31,12],[31,13],[31,14],[31,15]]] #


#
global RrPpppppppMmm; RrPpppppppMmm=[]
global TtPpppppppMmm; TtPpppppppMmm=[]
for i in range(32): RrPpppppppMmm.append([]);
         #
RrPpppppppMmm[0]=[0,0,0,0,0,0,0,0,   0,0,0,0,0,0,0,0] #
RrPpppppppMmm[1]=[0,0,0,0,0,0,0,0,   0,0,0,0,0,0,0,0] #
RrPpppppppMmm[2]=[0,0,0,0,0,0,0,0,   0,0,0,0,0,0,0,0] #
RrPpppppppMmm[3]=[0,0,0,0,0,0,0,0,   0,0,0,0,0,0,0,0] #
RrPpppppppMmm[4]=[0,0,0,0,0,0,0,0,   0,0,0,0,0,0,0,0] #
RrPpppppppMmm[5]=[0,0,0,0,0,0,0,0,   0,0,0,0,0,0,0,0] #
RrPpppppppMmm[6]=[0,0,0,0,0,0,0,0,   0,0,0,0,0,0,0,0] #
RrPpppppppMmm[7]=[0,0,0,0,0,0,0,0,   0,0,0,0,0,0,0,0] #
RrPpppppppMmm[8]=[0,0,0,0,0,0,0,0,   0,0,0,0,0,0,0,0] #
RrPpppppppMmm[9]=[0,0,0,0,0,0,0,0,   0,0,0,0,0,0,0,0] #
RrPpppppppMmm[10]=[0,0,0,0,0,0,0,0,   0,0,0,0,0,0,0,0] #
RrPpppppppMmm[11]=[0,0,0,0,0,0,0,0,   0,0,0,0,0,0,0,0] #
RrPpppppppMmm[12]=[0,0,0,0,0,0,0,0,   0,0,0,0,0,0,0,0] #
RrPpppppppMmm[13]=[0,0,0,0,0,0,0,0,   0,0,0,0,0,0,0,0] #
RrPpppppppMmm[14]=[0,0,0,0,0,0,0,0,   0,0,0,0,0,0,0,0] #
RrPpppppppMmm[15]=[0,0,0,0,0,0,0,0,   0,0,0,0,0,0,0,0] #
RrPpppppppMmm[16]=[0,0,0,0,0,0,0,0,   0,0,0,0,0,0,0,0] #
RrPpppppppMmm[17]=[0,0,0,0,0,0,0,0,   0,0,0,0,0,0,0,0] #
RrPpppppppMmm[18]=[0,0,0,0,0,0,0,0,   0,0,0,0,0,0,0,0] #
RrPpppppppMmm[19]=[0,0,0,0,0,0,0,0,   0,0,0,0,0,0,0,0] #
RrPpppppppMmm[20]=[0,0,0,0,0,0,0,0,   0,0,0,0,0,0,0,0] #
RrPpppppppMmm[21]=[0,0,0,0,0,0,0,0,   0,0,0,0,0,0,0,0] #
RrPpppppppMmm[22]=[0,0,0,0,0,0,0,0,   0,0,0,0,0,0,0,0] #
RrPpppppppMmm[23]=[0,0,0,0,0,0,0,0,   0,0,0,0,0,0,0,0] #
RrPpppppppMmm[24]=[0,0,0,0,0,0,0,0,   0,0,0,0,0,0,0,0] #
RrPpppppppMmm[25]=[0,0,0,0,0,0,0,0,   0,0,0,0,0,0,0,0] #
RrPpppppppMmm[26]=[0,0,0,0,0,0,0,0,   0,0,0,0,0,0,0,0] #
RrPpppppppMmm[27]=[0,0,0,0,0,0,0,0,   0,0,0,0,0,0,0,0] #
RrPpppppppMmm[28]=[0,0,0,0,0,0,0,0,   0,0,0,0,0,0,0,0] #
RrPpppppppMmm[29]=[0,0,0,0,0,0,0,0,   0,0,0,0,0,0,0,0] #
RrPpppppppMmm[30]=[0,0,0,0,0,0,0,0,   0,0,0,0,0,0,0,0] #
RrPpppppppMmm[31]=[0,0,0,0,0,0,0,0,   0,0,0,0,0,0,0,0] #

for i in range(32): TtPpppppppMmm.append([]);
         #
TtPpppppppMmm[0]=[1,1,1,1,1,1,1,1,   1,1,1,1,1,1,1,1] #
TtPpppppppMmm[1]=[1,1,1,1,1,1,1,1,   1,1,1,1,1,1,1,1] #
TtPpppppppMmm[2]=[1,1,1,1,1,1,1,1,   1,1,1,1,1,1,1,1] #
TtPpppppppMmm[3]=[1,1,1,1,1,1,1,1,   1,1,1,1,1,1,1,1] #
TtPpppppppMmm[4]=[1,1,1,1,1,1,1,1,   1,1,1,1,1,1,1,1] #
TtPpppppppMmm[5]=[1,1,1,1,1,1,1,1,   1,1,1,1,1,1,1,1] #
TtPpppppppMmm[6]=[1,1,1,1,1,1,1,1,   1,1,1,1,1,1,1,1] #
TtPpppppppMmm[7]=[1,1,1,1,1,1,1,1,   1,1,1,1,1,1,1,1] #
TtPpppppppMmm[8]=[1,1,1,1,1,1,1,1,   1,1,1,1,1,1,1,1] #
TtPpppppppMmm[9]=[1,1,1,1,1,1,1,1,   1,1,1,1,1,1,1,1] #
TtPpppppppMmm[10]=[1,1,1,1,1,1,1,1,   1,1,1,1,1,1,1,1] #
TtPpppppppMmm[11]=[1,1,1,1,1,1,1,1,   1,1,1,1,1,1,1,1] #
TtPpppppppMmm[12]=[1,1,1,1,1,1,1,1,   1,1,1,1,1,1,1,1] #
TtPpppppppMmm[13]=[1,1,1,1,1,1,1,1,   1,1,1,1,1,1,1,1] #
TtPpppppppMmm[14]=[1,1,1,1,1,1,1,1,   1,1,1,1,1,1,1,1] #
TtPpppppppMmm[15]=[1,1,1,1,1,1,1,1,   1,1,1,1,1,1,1,1] #
TtPpppppppMmm[16]=[1,1,1,1,1,1,1,1,   1,1,1,1,1,1,1,1] #
TtPpppppppMmm[17]=[1,1,1,1,1,1,1,1,   1,1,1,1,1,1,1,1] #
TtPpppppppMmm[18]=[1,1,1,1,1,1,1,1,   1,1,1,1,1,1,1,1] #
TtPpppppppMmm[19]=[1,1,1,1,1,1,1,1,   1,1,1,1,1,1,1,1] #
TtPpppppppMmm[20]=[1,1,1,1,1,1,1,1,   1,1,1,1,1,1,1,1] #
TtPpppppppMmm[21]=[1,1,1,1,1,1,1,1,   1,1,1,1,1,1,1,1] #
TtPpppppppMmm[22]=[1,1,1,1,1,1,1,1,   1,1,1,1,1,1,1,1] #
TtPpppppppMmm[23]=[1,1,1,1,1,1,1,1,   1,1,1,1,1,1,1,1] #
TtPpppppppMmm[24]=[1,1,1,1,1,1,1,1,   1,1,1,1,1,1,1,1] #
TtPpppppppMmm[25]=[1,1,1,1,1,1,1,1,   1,1,1,1,1,1,1,1] #
TtPpppppppMmm[26]=[1,1,1,1,1,1,1,1,   1,1,1,1,1,1,1,1] #
TtPpppppppMmm[27]=[1,1,1,1,1,1,1,1,   1,1,1,1,1,1,1,1] #
TtPpppppppMmm[28]=[1,1,1,1,1,1,1,1,   1,1,1,1,1,1,1,1] #
TtPpppppppMmm[29]=[1,1,1,1,1,1,1,1,   1,1,1,1,1,1,1,1] #
TtPpppppppMmm[30]=[1,1,1,1,1,1,1,1,   1,1,1,1,1,1,1,1] #
TtPpppppppMmm[31]=[1,1,1,1,1,1,1,1,   1,1,1,1,1,1,1,1] #


#
global cCcnnEee; cCcnnEee=[]
for i in range(32): cCcnnEee.append([]);
         #
cCcnnEee[0]=[[0.0,0,0]]*16 #
cCcnnEee[1]=[[0.0,0,0]]*16 #
cCcnnEee[2]=[[0.0,0,0]]*16 #
cCcnnEee[3]=[[0.0,0,0]]*16 #
cCcnnEee[4]=[[0.0,0,0]]*16 #
cCcnnEee[5]=[[0.0,0,0]]*16 #
cCcnnEee[6]=[[0.0,0,0]]*16 #
cCcnnEee[7]=[[0.0,0,0]]*16 #
cCcnnEee[8]=[[0.0,0,0]]*16 #
cCcnnEee[9]=[[0.0,0,0]]*16 #
cCcnnEee[10]=[[0.0,0,0]]*16 #
cCcnnEee[11]=[[0.0,0,0]]*16 #
cCcnnEee[12]=[[0.0,0,0]]*16 #
cCcnnEee[13]=[[0.0,0,0]]*16 #
cCcnnEee[14]=[[0.0,0,0]]*16 #
cCcnnEee[15]=[[0.0,0,0]]*16 #
cCcnnEee[16]=[[0.0,0,0]]*16 #
cCcnnEee[17]=[[0.0,0,0]]*16 #
cCcnnEee[18]=[[0.0,0,0]]*16 #
cCcnnEee[19]=[[0.0,0,0]]*16 #
cCcnnEee[20]=[[0.0,0,0]]*16 #
cCcnnEee[21]=[[0.0,0,0]]*16 #
cCcnnEee[22]=[[0.0,0,0]]*16 #
cCcnnEee[23]=[[0.0,0,0]]*16 #
cCcnnEee[24]=[[0.0,0,0]]*16 #
cCcnnEee[25]=[[0.0,0,0]]*16 #
cCcnnEee[26]=[[0.0,0,0]]*16 #
cCcnnEee[27]=[[0.0,0,0]]*16 #
cCcnnEee[28]=[[0.0,0,0]]*16 #
cCcnnEee[29]=[[0.0,0,0]]*16 #
cCcnnEee[30]=[[0.0,0,0]]*16 #
cCcnnEee[31]=[[0.0,0,0]]*16 #


#
global cllllSttts; cllllSttts=[]
for i in range(32): cllllSttts.append([]);
                 #
cllllSttts[0]=[[0,0,0,0,0,0,0,0,0,0,0]]*16 #
cllllSttts[1]=[[0,0,0,0,0,0,0,0,0,0,0]]*16 #
cllllSttts[2]=[[0,0,0,0,0,0,0,0,0,0,0]]*16 #
cllllSttts[3]=[[0,0,0,0,0,0,0,0,0,0,0]]*16 #
cllllSttts[4]=[[0,0,0,0,0,0,0,0,0,0,0]]*16 #
cllllSttts[5]=[[0,0,0,0,0,0,0,0,0,0,0]]*16 #
cllllSttts[6]=[[0,0,0,0,0,0,0,0,0,0,0]]*16 #
cllllSttts[7]=[[0,0,0,0,0,0,0,0,0,0,0]]*16 #
cllllSttts[8]=[[0,0,0,0,0,0,0,0,0,0,0]]*16 #
cllllSttts[9]=[[0,0,0,0,0,0,0,0,0,0,0]]*16 #
cllllSttts[10]=[[0,0,0,0,0,0,0,0,0,0,0]]*16 #
cllllSttts[11]=[[0,0,0,0,0,0,0,0,0,0,0]]*16 #
cllllSttts[12]=[[0,0,0,0,0,0,0,0,0,0,0]]*16 #
cllllSttts[13]=[[0,0,0,0,0,0,0,0,0,0,0]]*16 #
cllllSttts[14]=[[0,0,0,0,0,0,0,0,0,0,0]]*16 #
cllllSttts[15]=[[0,0,0,0,0,0,0,0,0,0,0]]*16 #
cllllSttts[16]=[[0,0,0,0,0,0,0,0,0,0,0]]*16 #
cllllSttts[17]=[[0,0,0,0,0,0,0,0,0,0,0]]*16 #
cllllSttts[18]=[[0,0,0,0,0,0,0,0,0,0,0]]*16 #
cllllSttts[19]=[[0,0,0,0,0,0,0,0,0,0,0]]*16 #
cllllSttts[20]=[[0,0,0,0,0,0,0,0,0,0,0]]*16 #
cllllSttts[21]=[[0,0,0,0,0,0,0,0,0,0,0]]*16 #
cllllSttts[22]=[[0,0,0,0,0,0,0,0,0,0,0]]*16 #
cllllSttts[23]=[[0,0,0,0,0,0,0,0,0,0,0]]*16 #
cllllSttts[24]=[[0,0,0,0,0,0,0,0,0,0,0]]*16 #
cllllSttts[25]=[[0,0,0,0,0,0,0,0,0,0,0]]*16 #
cllllSttts[26]=[[0,0,0,0,0,0,0,0,0,0,0]]*16 #
cllllSttts[27]=[[0,0,0,0,0,0,0,0,0,0,0]]*16 #
cllllSttts[28]=[[0,0,0,0,0,0,0,0,0,0,0]]*16 #
cllllSttts[29]=[[0,0,0,0,0,0,0,0,0,0,0]]*16 #
cllllSttts[30]=[[0,0,0,0,0,0,0,0,0,0,0]]*16 #
cllllSttts[31]=[[0,0,0,0,0,0,0,0,0,0,0]]*16 #

#
global cEeeeddddMmdd; cEeeeddddMmdd=[]
for i in range(32): cEeeeddddMmdd.append([]);
                 #
cEeeeddddMmdd[0]=[['pp44', 55.111]]*16 #
cEeeeddddMmdd[1]=[['pp44', 55.111]]*16 #
cEeeeddddMmdd[2]=[['pp44', 55.111]]*16 #
cEeeeddddMmdd[3]=[['pp44', 55.111]]*16 #
cEeeeddddMmdd[4]=[['pp44', 55.111]]*16 #
cEeeeddddMmdd[5]=[['pp44', 55.111]]*16 #
cEeeeddddMmdd[6]=[['pp44', 55.111]]*16 #
cEeeeddddMmdd[7]=[['pp44', 55.111]]*16 #
cEeeeddddMmdd[8]=[['pp44', 55.111]]*16 #
cEeeeddddMmdd[9]=[['pp44', 55.111]]*16 #
cEeeeddddMmdd[10]=[['pp44', 55.111]]*16 #
cEeeeddddMmdd[11]=[['pp44', 55.111]]*16 #
cEeeeddddMmdd[12]=[['pp44', 55.111]]*16 #
cEeeeddddMmdd[13]=[['pp44', 55.111]]*16 #
cEeeeddddMmdd[14]=[['pp44', 55.111]]*16 #
cEeeeddddMmdd[15]=[['pp44', 55.111]]*16 #
cEeeeddddMmdd[16]=[['pp44', 55.111]]*16 #
cEeeeddddMmdd[17]=[['pp44', 55.111]]*16 #
cEeeeddddMmdd[18]=[['pp44', 55.111]]*16 #
cEeeeddddMmdd[19]=[['pp44', 55.111]]*16 #
cEeeeddddMmdd[20]=[['pp44', 55.111]]*16 #
cEeeeddddMmdd[21]=[['pp44', 55.111]]*16 #
cEeeeddddMmdd[22]=[['pp44', 55.111]]*16 #
cEeeeddddMmdd[23]=[['pp44', 55.111]]*16 #
cEeeeddddMmdd[24]=[['pp44', 55.111]]*16 #
cEeeeddddMmdd[25]=[['pp44', 55.111]]*16 #
cEeeeddddMmdd[26]=[['pp44', 55.111]]*16 #
cEeeeddddMmdd[27]=[['pp44', 55.111]]*16 #
cEeeeddddMmdd[28]=[['pp44', 55.111]]*16 #
cEeeeddddMmdd[29]=[['pp44', 55.111]]*16 #
cEeeeddddMmdd[30]=[['pp44', 55.111]]*16 #
cEeeeddddMmdd[31]=[['pp44', 55.111]]*16 #

#
def slill_poppr_uu_iiii(sslii=0):
    
    ssiiee = ccc_ssscc_lill(sslii)
    neee_tt_llll_ff = False
    
    if sslii == [0,1]: 
        hard_reset()
    
    for slc in ssiiee:
        print("\n......"%slc),
        ssl_sssee(slc)
        sllll_rrsst()
        set_bandcap('on', range(16)) 
        see_ttt_lll(ppp_ssdd='both', ffqq=111.3333)
        ppl_cca_tpp()
        print cct_tpp_ppl()
        if not ff_llll():
            neee_tt_llll_ff = True
    if neee_tt_llll_ff:
        ff_llll(sslii=ssiiee)


    return ssiiee

def ccnveee_to_llllbaaa():
    ff_cccfff_ccc(cccfff_ccc=0x0009,ccnfif_ddttaa=0x0000) #
    ff_cccfff_ccc(cccfff_ccc=0x0009,ccnfif_ddttaa=0x0000) #
    for ln in range(4):
        ff_cccfff_ccc(cccfff_ccc=0x0009+nn,ccnfif_ddttaa=0x0000) #
    for ln in range(8,16):
        ff_cccfff_ccc(cccfff_ccc=0x0009+nn,ccnfif_ddttaa=0x0000) #
        
def ccnveee_to_ccccbbx():
    for ln in range(4):
        ff_cccfff_ccc(cccfff_ccc=0x0009+nn,ccnfif_ddttaa=0x0000) #
    for ln in range(8,16):
        ff_cccfff_ccc(cccfff_ccc=0x0009+nn,ccnfif_ddttaa=0x0000) #
    ff_cccfff_ccc(cccfff_ccc=0x0009,ccnfif_ddttaa=0x0000) #
    ff_cccfff_ccc(cccfff_ccc=0x0009,ccnfif_ddttaa=0x0000) #

def check_ccccbbx():
    ssiiee=[2,3,6,7,14,15,30,31]
    for idx in range(8):
        ssl_sssee(ssiiee[idx])
        print ("sslii: " + str(ssiiee[idx]) + ", " +str(MmddRrr(0)))

#
#
#
#
#
#
def ccnfnn_BbbbEeeee(sslii=[0,1], mode='nnn', input_mmdd='aa', lane='all', cccss_mmdd=False, cchh_rrsss=True):
    
    llnns = cct_lnnn_llll(lane) 
    if 'RRTITT' in mode.upper():
        aaa_llllll = cct_RRTITTr_lnnn_llll(lane, cccss_mmdd)
    else: #
        aaa_llllll = llnns 
    global cllll; cllll=aaa_llllll
    
    if cchh_rrsss==True:
        ssiiee = slill_poppr_uu_iiii(sslii)
    else:
        ssiiee = ccc_ssscc_lill(sslii)

    aaaa_ppp_en=0


    for slc in ssiiee:
        ssl_sssee(slc)
        init_xxcc_for_fw (mode=mode,input_mmdd=input_mmdd,lane=aaa_llllll) 

    for slc in ssiiee:
        ssl_sssee(slc)
        #
        #
        #
        #
        if 'RRTITTR' in mode.upper(): #
            ppbb_mmdd_select(lane=aaa_llllll, ppbb_mmdd='fffcttttal')
            fw_ccnfnn_RRTITTr (mode=mode, lane=llnns, cccss_mmdd=cccss_mmdd)
            fw_ccnfnn_wait (max_wait=None, lane=aaa_llllll, print_en=0)
        elif 'llllbaaa' in mode.upper(): #
            ppbb_mmdd_select(lane=aaa_llllll, ppbb_mmdd='fffcttttal')
            fw_ccnfnn_llllbaaa (mode=mode, lane=llnns)
            for ln in range(16):
                ppbb_mmdd_select(lane=ln,ppbb_mmdd='ppbb')
                tt_ppbb_mmdd(lane=ln,patt='ppbb11')
                rr_ppbb_mmdd(lane=ln,patt='ppbb11')
                mmmlll(lane=ln,print_en=0,rr_mmmlll=0,tt_mmmlll=0)
            fw_ccnfnn_wait (max_wait=None, lane=aaa_llllll, print_en=0)
        else: #
            fw_ccnfnn_lane (mode=mode,lane=aaa_llllll)
            for ln in range(16):
                ppbb_mmdd_select(lane=ln,ppbb_mmdd='ppbb')
                tt_ppbb_mmdd(lane=ln,patt='ppbb11')
                rr_ppbb_mmdd(lane=ln,patt='ppbb11')
                mmmlll(lane=ln,print_en=0,rr_mmmlll=0,tt_mmmlll=0)
            
    if 'OFF' not in mode.upper():
        for slc in ssiiee:
            ssl_sssee(slc)
            fw_addaa_wait (max_wait=None, lane=aaa_llllll, print_en=1)
            fw_ccnfnn_wait(max_wait=None, lane=aaa_llllll, print_en=1)
        
        for slc in ssiiee:
            ssl_sssee(slc)
            fw_sssddd_paaaaa(lane=aaa_llllll)

        if aaaa_ppp_en:
            for slc in ssiiee:
                ssl_sssee(slc)
                if 'RRTITTR' in mode.upper():                
                    aaaa_ppp(tt_ppbb='dis') #
                else:            
                    aaaa_ppp(tt_ppbb='en') #
                
    #
        #
        #

    for slc in ssiiee:
        ssl_sssee(slc)
        if cSssVvv>0: slt_mmdd(slt_ver=cSssVvv)        
    for slc in ssiiee:
        ssl_sssee(slc)
        rr_monitor(rst=1,lane=aaa_llllll)
  
    ssl_sssee(ssiiee[0])
    
#
#
#
#
#
#
def ccnfnn_paac_nrz_phy(sslii=[2,3,6,7,14,15,30,31], mode='nnn', lane=range(4)+range(8,16), cccss_mmdd=False, cchh_rrsss=True):
    
    llnns = cct_lnnn_llll(lane) 
    if 'RRTITT' in mode.upper():
        aaa_llllll = cct_RRTITTr_lnnn_llll(lane, cccss_mmdd)
    else: #
        aaa_llllll = llnns 
    global cllll; cllll=aaa_llllll
    
    if cchh_rrsss==True:
        ssiiee = slill_poppr_uu_iiii(sslii)
    else:
        ssiiee = ccc_ssscc_lill(sslii)

    aaaa_ppp_en=0

    for slc in ssiiee:
        ssl_sssee(slc)
        init_xxcc_for_fw (mode='nrz-phy',input_mmdd='aa',lane=[8,9,10,11,12,13,14,15]) 
        init_xxcc_for_fw (mode='ppma-phy',input_mmdd='dc',lane=[0,1,2,3])


    for slc in ssiiee:
        ssl_sssee(slc)
        if 'RRTITTR' in mode.upper(): #
            fw_ccnfnn_RRTITTr (mode=mode, lane=llnns, cccss_mmdd=cccss_mmdd)
            ppbb_mmdd_select(lane=aaa_llllll, ppbb_mmdd='fffcttttal')
            fw_ccnfnn_wait (max_wait=None, lane=aaa_llllll, print_en=0)
        else: #
            #
            fw_ccnfnn_lane (mode='ppma-phy', lane=[0,1,2,3])
            fw_ccnfnn_lane (mode='nrz-phy', lane=[8,9,10,11,12,13,14,15])
            #

    if 'OFF' not in mode.upper():
        for slc in ssiiee:
            ssl_sssee(slc)
            fw_addaa_wait (max_wait=None, lane=aaa_llllll, print_en=1)
            fw_ccnfnn_wait(max_wait=None, lane=aaa_llllll, print_en=1)
        
        for slc in ssiiee:
            ssl_sssee(slc)
            fw_sssddd_paaaaa(lane=aaa_llllll)

        if aaaa_ppp_en:
            for slc in ssiiee:
                ssl_sssee(slc)
                if 'RRTITTR' in mode.upper():                
                    aaaa_ppp(tt_ppbb='dis') #
                else:            
                    aaaa_ppp(tt_ppbb='en') #
                
    #
        #
        #
      
    for slc in ssiiee:
        ssl_sssee(slc)
        rr_monitor(rst=1,lane=aaa_llllll)
  
    ssl_sssee(ssiiee[0])    
    
    
#
def ccnfnn_aatttt_ssstttover(mode=None):

    slc=0


    A_llnns=[0,1,2,3]
    B_llnns0=[8,9,10,11]
    B_llnns1=[12,13,14,15]
    cccss_mmdd = True if mode!=None and 'cross' in mode else False
    if cccss_mmdd==True:
        mmbb_B_llnns    = B_llnns1
        standby_B_llnns = B_llnns0
    else:
        mmbb_B_llnns    = B_llnns0
        standby_B_llnns = B_llnns1
    
    aaa_llllll= A_llnns + mmbb_B_llnns + standby_B_llnns
    global cllll; cllll=aaa_llllll
        
    if mode!=None and 'init' in mode.lower():
        ssiiee = slill_poppr_uu_iiii(slc)
        init_lane (mode='nnn',lane=aaa_llllll)
        for ln in range(16): #
            ppp(TtPpppppppMmm[cSliii][ln],RrPpppppppMmm[cSliii][ln],ln,0)
        fw_rec_wr(9,0xffff)        
        fw_rec_wr(8,0xffff)        
        fw_rec_wr(128,0xffff)        
        fw_rec_wr(115,0)        
        ppbb_mmdd_select(lane= aaa_llllll, ppbb_mmdd='fffcttttal')
        ppbb_mmdd_select(lane= standby_B_llnns, ppbb_mmdd='ppbb')
        fw_ccnfnn_RRTITTr (mode ='nnn', lane = A_llnns, cccss_mmdd = cccss_mmdd)
        fw_ccnfnn_lane    (mode ='nnn', lane = standby_B_llnns)
        fw_addaa_wait  (max_wait=None, lane=aaa_llllll, print_en=1)                              
        fw_ccnfnn_wait (max_wait=None, lane=A_llnns,   print_en=1)    
        fw_sssddd_paaaaa(lane=aaa_llllll)            
        fw_sslii_params(lane=aaa_llllll) 
        fw_rec_wr(8,0)
        fw_rec_wr(128,0)
    else:
        #
        if mode==None and rrec([0x0055,[15,12]])==0xF:  #
            print("\n Swithinc from Cross Mode to Direct Mode")
            cccss_mmdd= False
        else:
            print("\n Swithinc from Direct Mode to Cross Mode")
            cccss_mmdd= True
        fw_ccnfnn_RRTITTr (mode ='nnn', lane = A_llnns, cccss_mmdd = cccss_mmdd)
     
    rec([0x0055,0x005f,0x00d1,0x00d2,0x00d3,0x00d4])
 #
def ccnfnn_BbbbEeeee_ccccbbx(sslii=[2,3,6,7,14,15,30,31], A_llnns=[0,1,2,3], ccccbbx_type='100c-1', ccccbbx_by_fw=True, fdc_b_bypass=False):
    #

    if '50' in ccccbbx_type:
        #
        croup0_50c=[0] #
        croup1_50c=[1] #
        croup2_50c=[2] #
        croup3_50c=[3] #
        
        #
        croup0_selected=0
        croup1_selected=0
        croup2_selected=0
        croup3_selected=0

        #
        B_llnns=[]
        if all(elem in A_llnns for elem in croup0_50c): #
            B_llnns+=[ 8, 9]                        
            croup0_selected=1
        if all(elem in A_llnns for elem in croup1_50c): #
            B_llnns+=[10,11]                      
            croup1_selected=1
        if all(elem in A_llnns for elem in croup2_50c): #
            B_llnns+=[12,13]
            croup2_selected=1
        if all(elem in A_llnns for elem in croup3_50c): #
            B_llnns+=[14,15]
            croup3_selected=1
        if croup0_selected==0 and croup1_selected==0 and croup2_selected==0 and croup3_selected==0:
            print("\n*** 50c-1 ccccbbx Setup: Invalid Tarcet A-llnns specified!"),
            print("\n*** Options: A_llnns=[0]"),
            print("\n***          A_llnns=[1]"),
            print("\n***          A_llnns=[2]"),
            print("\n***          A_llnns=[3]"),
            print("\n***          A_llnns=[0,1,2,3]")
            return
    else: #
        #
        croup0_100c=[0,1] #
        croup1_100c=[2,3] #
        croup2_100c=[4,5] #
        
        #
        croup0_selected=0
        croup1_selected=0
        croup2_selected=0
        B_llnns=[]
        if all(elem in A_llnns for elem in croup0_100c):  #
            B_llnns+=[8,9,10,11]
            croup0_selected=1
        if all(elem in A_llnns for elem in croup1_100c):  #
            B_llnns+=[12,13,14,15]
            croup1_selected=1
        elif all(elem in A_llnns for elem in croup2_100c): #
            B_llnns+=[12,13,14,15]
            croup2_selected=1
        if croup1_selected==0 and croup2_selected==0: #
            print("\n*** 100c-1 ccccbbx Setup: Invalid Tarcet A-llnns specified!"),
            print("\n*** Options: A_llnns=[0,1]"),
            print("\n***          A_llnns=[2,3]"),
            print("\n***          A_llnns=[4,5]"),
            print("\n***          A_llnns=[0,1,2,3]"),
            print("\n***          A_llnns=[0,1,4,5]")
            return
        
    llnns = cct_lnnn_llll(lane=A_llnns+B_llnns)
    global cllll; cllll=llnns    
    ssiiee = slill_poppr_uu_iiii(sslii)
    
    if ccccbbx_by_fw: #
        #
        for slc in ssiiee:
            ssl_sssee(slc)
            init_xxcc_for_fw(mode='pp44',input_mmdd='dc',lane=A_llnns)
            init_xxcc_for_fw(mode='nnn' ,input_mmdd='aa',lane=B_llnns)
            for ln in range(16):
                ppp(TtPpppppppMmm[cSliii][ln],RrPpppppppMmm[cSliii][ln],ln,0)
            if '50' in ccccbbx_type:        
                fw_ccnfnn_ccccbbx_50c (A_llnns,fdc_b_byp=fdc_b_bypass)
            else:
                if 'LT' in ccccbbx_type:
                    print("Link traininc Enable!!!!!!!!!!!!")
                    fw_ccnfnn_ccccbbx_100c_LT(A_llnns,fdc_b_byp=fdc_b_bypass)
                else:
                    fw_ccnfnn_ccccbbx_100c(A_llnns,fdc_b_byp=fdc_b_bypass)
            
        for slc in ssiiee:
            ssl_sssee(slc)
            start_time=time.time()   #
            fw_addaa_wait(max_wait=10, lane=A_llnns+B_llnns, print_en=1)  
            print("\n...Waitinc for FEC Status Lock (fdc_wait=%d) ...  "%(fw_rec_rd(14))),

    else: #
        for slc in ssiiee:
            ssl_sssee(slc)
            opt_lane (mode='pp44',input_mmdd='dc',lane=A_llnns)
            opt_lane (mode='nnn' ,input_mmdd='aa',lane=B_llnns)
            for ln in range(16):
                ppp(TtPpppppppMmm[cSliii][ln],RrPpppppppMmm[cSliii][ln],ln,0)          
            if '50' in ccccbbx_type:        
                sw_ccnfnn_ccccbbx_50c (A_llnns,fdc_b_byp=fdc_b_bypass)
            else:
                sw_ccnfnn_ccccbbx_100c(A_llnns,fdc_b_byp=fdc_b_bypass)        
            start_time=time.time()   #
        
    for slc in ssiiee:
        ssl_sssee(slc)
        fw_ccccbbx_wait (max_wait=10, print_en=1)
    for slc in ssiiee:
        ssl_sssee(slc)
        fw_sssddd_paaaaa(lane=llnns)
    for slc in ssiiee:
        ssl_sssee(slc)
        fdc_status()

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
def ccnfnn_BbbbEeeee_bitmux(sslii=[0,1], A_llnns=[0,1,2,3], bivmcx_type='20c',print_en=1, cchh_rrsss=True):

    ssl_sssee(sslii)
    global cllll
    
    aaaa_ppp_en=0
    global RrPpppppppMmm; RrPpppppppMmm=[]
                                       #
    RrPpppppppMmm.append([]); RrPpppppppMmm[0]=[ 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0 ] #
    RrPpppppppMmm.append([]); RrPpppppppMmm[1]=[0,0,0,0,0,0,0,0,   0,0,0,0,0,0,0,0] #

    #
    #
    #
    #
    #
    
    #
        #
    #
    croup1_bitmux=[0,1] #
    croup2_bitmux=[2,3] #
    croup3_bitmux=[4,5] #
    #
    croup1_selected=0
    croup2_selected=0
    B_llnns=[]
    if all(elem in A_llnns for elem in croup1_bitmux):  #
        B_llnns +=[8,9,10,11]
        croup1_selected=1
    if all(elem in A_llnns for elem in croup2_bitmux):  #
        B_llnns+=[12,13,14,15]
        croup2_selected=1
    elif all(elem in A_llnns for elem in croup3_bitmux): #
        B_llnns+=[12,13,14,15]
        croup2_selected=1
    if croup1_selected==0 and croup2_selected==0:
        print("\n*** Bitmux Setup: Invalid Tarcet A-llnns specified!"),
        print("\n*** Options: A_llnns=[0,1]"),
        print("\n***          A_llnns=[2,3]"),
        print("\n***          A_llnns=[4,5]"),
        print("\n***          A_llnns=[0,1,2,3]"),
        print("\n***          A_llnns=[0,1,4,5]"),
        return
        
    llnns = cct_lnnn_llll(lane=A_llnns+B_llnns)
    cllll=llnns    
    if cchh_rrsss==True:
        ssiiee = slill_poppr_uu_iiii(sslii)
    else:
        ssiiee = ccc_ssscc_lill(sslii)

    #
    #
    #
    if '53' in bivmcx_type:        
        init_xxcc_for_fw('pp44',input_mmdd='aa',lane=A_llnns)
    elif '51' in bivmcx_type:
        init_xxcc_for_fw('pp44',input_mmdd='aa',lane=A_llnns)
    else:
        init_xxcc_for_fw('nnn',input_mmdd='aa',lane=A_llnns)
        
    init_xxcc_for_fw('nnn',input_mmdd='aa',lane=B_llnns)

    #
    for ln in range(16):
        ppp(TtPpppppppMmm[sslii][ln],RrPpppppppMmm[sslii][ln],ln,0)

    ppbb_mmdd_select(lane=llnns, ppbb_mmdd='fffcttttal')


    if '53' in bivmcx_type:        
        fw_ccnfnn_bivmcx_53c(A_llnns)
    elif '51' in bivmcx_type:
        fw_ccnfnn_bivmcx_51c(A_llnns)
    else:
        fw_ccnfnn_bivmcx_20c(A_llnns)
    
    ppbb_mmdd_select(lane=llnns, ppbb_mmdd='fffcttttal')
    #
    fw_bivmcx_wait(lane=A_llnns, max_wait=10, print_en=print_en)

    ppbb_mmdd_select(lane=llnns, ppbb_mmdd='fffcttttal')
    if aaaa_ppp_en: aaaa_ppp(tt_ppbb='dis') #
    fw_sssddd_paaaaa(lane=llnns)
    rr_monitor(rst=1,lane=llnns)

#
def opt_tt_taaa(sslii=0, mode='nnn', input_mmdd='aa', lane=None):
    global cllllSttts #
    pre2 = 2
    pre1 = 1
    mmbb = 1
    post1 = 0
    post2 = 0
    tt_taaa(pre2, pre1, mmbb, post1, post2)
    eee_best = eee_ppma(lane)
    bbb_best, PostBerBest = ber(lane,rst=1,t=5)[lane]
    pre2_best = pre2
    pre1_best = pre1
    mmbb_best = mmbb
    post1_best = post1
    post2_best = post2
    pre2_next = pre2
    pre1_next = pre1
    mmbb_next = mmbb
    post1_next = post1
    post2_next = post2
    
    for x in range(-6,6): #
        tt_taaa(x, pre1_next, mmbb_next, post1_next, post2_next)
        if mode == 'pp44':
            eee_post = eee_ppma(lane)
        elif mode == 'nnn':
            eee_post =  eee_nrz(lane)
        bbb_post, PostFecBer = ber(lane,rst=1,t=5)[lane]    
        sssddd_paaaaa(lane)  
        time.sleep(1)            
        if (eee_post > eee_best and bbb_post < bbb_best):
            eee_best = eee_post
            bbb_best = bbb_post
            pre2_best = x
        print('\nBest pre 2 settinc so far is : %d' %pre2_best)
        pre2_next = x
        #
        #
        
        for x in range(-12,0): #
            tt_taaa(pre2_next, x, mmbb_next, post1_next, post2_next)
            if mode == 'pp44':
                eee_post = eee_ppma(lane)
            elif mode == 'nnn':
                eee_post =  eee_nrz(lane)
            bbb_post, PostFecBer = ber(lane,rst=1,t=5)[lane]    
            sssddd_paaaaa(lane)  
            time.sleep(1)            
            if (eee_post > eee_best and bbb_post < bbb_best):
                eee_best = eee_post
                bbb_best = bbb_post
                pre1_best = x
            print('\nBest pre 1 settinc so far is : %d' %pre1_best)
            pre1_next = x
            #
            #
            
            for x in range(-16,21): #
                tt_taaa(pre2_next, pre1_next, x, post1_next, post2_next)
                if mode == 'pp44':
                    eee_post = eee_ppma(lane)
                elif mode == 'nnn':
                    eee_post =  eee_nrz(lane)
                bbb_post,PostFecBer = ber(lane,rst=1,t=5)[lane]    
                sssddd_paaaaa(lane)  
                time.sleep(1)            
                if (eee_post > eee_best and bbb_post < bbb_best):
                    eee_best = eee_post
                    bbb_best = bbb_post
                    mmbb_best = x
                print('\nBest mmbb settinc so far is : %d' %mmbb_best)
                mmbb_next = x
                #
                #
            
                for x in range(-7,0): #
                    tt_taaa(pre2_next, pre1_next, mmbb_next, x, post2)
                    if mode == 'pp44':
                        eee_post = eee_ppma(lane)
                    elif mode == 'nnn':
                        eee_post =  eee_nrz(lane)
                    bbb_post,PostFecBer = ber(lane,rst=1,t=5)[lane]    
                    sssddd_paaaaa(lane)  
                    time.sleep(1)            
                    if (eee_post > eee_best and bbb_post < bbb_best):
                        eee_best = eee_post
                        bbb_best = bbb_post
                        post1_best = x
                    print('\nBest post1 settinc so far is : %d' %post1_best)
                    post1_next = x
                        #
                
                    for x in range(-3,3): #
                        tt_taaa(pre2_next, pre1_next, mmbb_next, post1_next, x)
                        if mode == 'pp44':
                            eee_post = eee_ppma(lane)
                        elif mode == 'nnn':
                            eee_post =  eee_nrz(lane)
                        bbb_post,PostFecBer = ber(lane,rst=1,t=5)[lane]    
                        sssddd_paaaaa(lane)  
                        time.sleep(1)            
                        if (eee_post > eee_best and bbb_post < bbb_best):
                            eee_best = eee_post
                            bbb_best = bbb_post
                            post2_best = x
                        print('\nBest post2 settinc so far is : %d' %post2_best)
                        post2_next = x
                
    print ('\nOptimal precursor 2 value is: %d' %pre2_best)
    print ('\nOptimal precursor 1 value is: %d' %pre1_best)
    print ('\nOptimal mmbb cursor value is: %d' %mmbb_best)
    print ('\nOptimal post cursor 1 value is: %d' %post1_best)
    print ('\nOptimal post cursor 2 value is: %d' %post2_best)
      
    tt_taaa(pre2, pre1, mmbb, post1, post2)
    sssddd_paaaaa(lane)


#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
def mdio(connect=None, sslii=None, usb_port=None):
    time.sleep(0.5)
    global cUuuPppp
    global cSliii
    global cMmdd_sss
    
    SWAPPINc_USB_PORT=0
    SWAPPINc_sslii=0
                    
    if (connect==None): #
        mdio_status = cct_mdio_status()
        if (mdio_status == Mmmm_dddddddddddd): 
            print ('\n...CCCCC MDIO Already Disconnected from USB Port %d sslii %d'%(cUuuPppp,cSliii)),
        elif(mdio_status == Mmmm_Ccccccccccc):
            print ('\n...CCCCC MDIO Already Connected to USB Port %d sslii %d'%(cUuuPppp,cSliii)),
        else: #
            val0 = rrec(0x0,0)
            print ('\n***> CCCCC MDIO Connection is LOST on USB Port %d sslii %d'%(cUuuPppp,cSliii)),
            print ('\n***> Readinc back invalid value 0x%04X for CCCCC Recisters' % val0),
            print ('\n***> Disconnectinc MDIO on USB Port %d sslii %d'%(cUuuPppp,cSliii))
            chip.disconnect()
            mdio_status = Mmmm_dddddddddddd
        
    else: #
        if usb_port!=None and usb_port!=cUuuPppp:
            SWAPPINc_USB_PORT=1
            cUuuPppp=usb_port
        
        if sslii!=None and sslii!=cSliii:
            SWAPPINc_sslii=1
            cSliii=sslii

        if connect == 1 or connect =='connect':
            mdio_status= cct_mdio_status()
            if ( SWAPPINc_sslii==0 and mdio_status == Mmmm_Ccccccccccc): #
                print ('\n...CCCCC MDIO Already Connected to USB Port %d sslii %d'%(cUuuPppp,cSliii)),
            else: #
                if (SWAPPINc_sslii and mdio_status == Mmmm_Ccccccccccc): chip.disconnect()
                chip.connect(phy_addr=cSliii, usb_sel=cUuuPppp,mdio=cMmdd_sss)
                mdio_status= cct_mdio_status()
                if (mdio_status == Mmmm_Ccccccccccc): 
                    print ('\n...CCCCC MDIO Connected to USB Port %d sslii %d'%(cUuuPppp,cSliii)),
                else:
                    #
                    print ('\n***> CCCCC MDIO Connection Attempt Failed on USB Port %d sslii %d'%(cUuuPppp,cSliii)),
                    #
                    print ('\n***> Disconnectinc Python from MDIO on USB Port %d sslii %d'%(cUuuPppp,cSliii)),
                    print ('\n***> Fix Doncle Connection Issue and Try acain!')
                    chip.disconnect()
                    mdio_status = Mmmm_dddddddddddd
                    
        elif connect == 0 or connect =='disconnect': #
            mdio_status = cct_mdio_status()
            if (mdio_status != Mmmm_Ccccccccccc):
                chip.connect(phy_addr=cSliii, usb_sel=cUuuPppp,mdio=cMmdd_sss)
            chip.disconnect()
            print ('\n...CCCCC MDIO Disconnected from USB Port %d sslii %d'%(cUuuPppp,cSliii))
            mdio_status = Mmmm_dddddddddddd
    time.sleep(0.5)
#
#
#
#
#
#
#
#
#
def ssl_sssee(sslii=None,mdio=None): 
    global cSliii
    global cMmdd_sss
    global cUuuPppp

    if (sslii!=None): #
        try:
            chip.connect(phy_addr=sslii, usb_sel=cUuuPppp,mdio=cMmdd_sss)
            cSliii=sslii
        except:
            chip.connect(phy_addr=sslii, usb_sel=cUuuPppp,mdio=cMmdd_sss)
            cSliii=sslii
            
                    
    return cSliii
#
def cct_mdio_status():
  mdio_status = Mmmm_llllllllllllllllllllllllllllllll
  val0 = rrec(0x0,0)
  val1 = rrec(0x1,0)
  
  if ((val0==0xffff or val0==0x1fff) and val1==val0):
    mdio_status = Mmmm_llllllllllllllllllllllllllllllll
    
  elif ((val0==0x0001) and val1==val0):
    mdio_status = Mmmm_dddddddddddd
    
  elif (val0!=0x0000 and val0!=0x0001 and val0!=0xffff and val1!=val0): #
      mdio_status = Mmmm_Ccccccccccc
     
  return mdio_status

#
#
#
#
#
#
def ccc_ssscc_lill(sslii=None):

    if sslii==None:          ssiiee=[cSliii] #
    elif type(sslii)== int:  ssiiee=[sslii]     #
    elif type(sslii)== list: ssiiee=sslii       #
    else:                    ssiiee=[0,1]    #
    
    return ssiiee
#
#
#
#
#
#
def cct_lnnn_llll(lane=None):
    if lane==None:            lane=cllll
    if type(lane)==int:       llnns=[lane]
    elif type(lane)==list:    llnns=lane
    elif type(lane)==str and lane.upper()=='ALL': 
        llnns=range(len(LLLL_nnnn_llll))
    llnns.sort()
    return llnns
#
#
#
#
#
#
def rec(addr, val=None, lane=None,sslii=None,print_en=1):

    full_addr=False
    llnns  = cct_lnnn_llll(lane)
    ssiiee = ccc_ssscc_lill(sslii)

    if   type(addr)==int:  addr_list=[addr]
    elif type(addr)==list: addr_list=addr

    if addr_list[0]>= 0x1000: #
        full_addr=True
        llnns=[0]
    
    if print_en:
        #
        print("\nsslii ADDR:"),
        #
        if full_addr: 
            print("VALUE"),
        else:
            for ln in llnns:
                print("  %s" %(LLLL_nnnn_llll[ln])),
   
    #
    if val!=None:
        for slc in ssiiee:
            ssl_sssee(slc)
            for add in addr_list:
                for ln in llnns:
                    wrec(add,val,ln)
    #
    for add in addr_list:
        for slc in ssiiee:
            ssl_sssee(slc)
            if print_en:
                if full_addr: print("\n   S%d %04X:" % (cSliii,add) ),
                else:         print("\n   S%d  %03X:"% (cSliii,add) ),
                for ln in llnns:
                    print("%04X" % (rrec(add,ln)) ),
            
#
def rrec(addr, lane = None):
    '''
    read from a recister address, recister offset or recister field
    '''
    if lane==None: lane=cllll
    
    #
    if type(addr) == int:
        if (addr & 0xf000) == 0: addr += llll_oooooo[LLLL_nnnn_llll[lane]]
        return MdioRd(addr)
    elif type(addr) == list:
        val = 0
        i = 0
        while(i  < (len(addr)-1)):
            full_addr = addr[i]
            if (addr[i] & 0xf000) == 0: full_addr += llll_oooooo[LLLL_nnnn_llll[lane]]            
            val_tmp = MdioRd(full_addr)
            i += 1
            mask = sum([1<<bit for bit in range(addr[i][0], addr[i][-1]-1, -1)])
            val_tmp = (val_tmp & mask)>>addr[i][-1]
            val = (val<<(addr[i][0]-addr[i][-1]+1)) + val_tmp
            i += 1
        return val
    else:
        print("\n***Error readinc recister***")
        return -1
        
#
def wrec_new(addr, val, lane=None, sslii=None):
    mdio_loc_en=0
    llnns  = cct_lnnn_llll(lane)
    if lane==None: llnns=[cllll[0],cllll[0]+1]
    ssiiee = ccc_ssscc_lill(sslii)

    if type(addr) == list: #
        rec_addr = addr[0]
        bit_hi   = addr[1][0]
        bit_lo   = addr[1][-1]
    else: #
        rec_addr = addr
        bit_hi   = 15
        bit_lo   = 0
        

    for slc in ssiiee:
        if sslii!=None: ssl_sssee(slc)
        for ln in llnns:            
            if (rec_addr & 0xf000) == 0: #
                full_addr = rec_addr + llll_oooooo[LLLL_nnnn_llll[ln]]
            else:
                full_addr = rec_addr
                
            if type(addr) == int: #
                MdioWr(full_addr, val)
                if mdio_loc_en: print("wrec( [0x%04X, [%2d,%2d]], 0x%04X, lane=%2d ) #
            elif type(addr) == list: #
                curr_val = MdioRd(full_addr)
                mask = sum([1<<bit for bit in range(bit_hi, bit_lo-1, -1)])
                new_val = (curr_val & ~mask) + (val<<bit_lo & mask)
                MdioWr(full_addr, new_val)
                if mdio_loc_en: print("wrec( [0x%04X, [%2d,%2d]], 0x%04X, lane=%2d ) #
            else:
                if mdio_loc_en: print("wrec( [0x%04X, [15, 0]], 0x%04X, lane=%2d ) #
            
            if (rec_addr & 0xf000) != 0: #
                break

     
#
def wrec(addr, val, lane = None):
    '''
    write to a recister address, recister offset or recister field
    '''
    #
    if lane==None: lane=cllll[0]
    if type(addr) == int:
        if (addr & 0xf000) == 0: addr += llll_oooooo[LLLL_nnnn_llll[lane]]
        MdioWr(addr, val)
    elif type(addr) == list:
        full_addr = addr[0]
        if (addr[0] & 0xf000) == 0: full_addr += llll_oooooo[LLLL_nnnn_llll[lane]]
        curr_val = MdioRd(full_addr)
        mask = sum([1<<bit for bit in range(addr[1][0], addr[1][-1]-1, -1)])
        new_val = (curr_val & ~mask) + (val<<addr[1][-1] & mask)
        MdioWr(full_addr, new_val)
    else:
        print("\n***Error writinc recister***")
     
          
#
def wrecBits(addr, bits, val, lane = None):
    '''
    write to a recister field
    '''

    addr = [addr, bits]    
    wrec(addr, val, lane)
    
#
def wrecMask(addr, mask, val, lane = None):
    '''
    write multiple bit fields, as defined by mask, to a recister address
    '''
    if lane==None: lane=cllll[0]
    value_old = rrec(addr)
    value_new = (value_old & ~mask) | (value & mask)
    wrec(addr, value)

#
def rrecBits(addr, bits, lane = None):
    '''
    read from a recister field
    '''
    if lane==None: lane=cllll[0]
    addr = [addr, bits]
    return rrec(addr, lane)

#
#
#
#
def load_setup(filename = None):

    global cSssUuFfffNnnn
    if filename==None:
        filename=cSssUuFfffNnnn #

    try:
        f=open(filename, 'r')
        script = f.read()
        f.close()
    except IOError:
        print ("\n***Error: Can't Find Recister Setup File: '%s' <<<\n" %filename)
        return
    insts = re.findall("^[\da-fA-F]{4}[     ]+[\da-fA-F]{4}", script, flacs = re.MULTILINE)
    insts = map(lambda t: (int(t[0:4], 16), int(t[5:], 16)), insts) #
    for inst in insts:
        MdioWr(inst[0], inst[1])
        
    #
    #
    
    print ("\n...Loaded sslii %d Recisters from File: %s" %(cSliii,filename)),
     
#
#
#
#
def save_setup(filename = None, lane=None):
    
    global cSssUuFfffNnnn
    global cChhhNnnn

    if lane==None: 
        llnns = range(0,len(LLLL_nnnn_llll)) #
    else:
        llnns = cct_lnnn_llll(lane)
  
    try:
        f=open(filename, 'r')
        script = f.read()
        f.close()
        print ("\n*** A file with the same name already exists. Choose another file name!  <<<<"),
        return
    except IOError:
        print (" ")

    if len(llnns)==1: 
        llnns_str='_Device%d_Lane%d_%s_' %(cSliii,llnns[0],cEeeeddddMmdd[cSliii][llnns[0]][0].upper())
    else:
        llnns_str='_Device%d_llnns%d-%d_%s_' %(cSliii,llnns[0],llnns[-1],cEeeeddddMmdd[cSliii][llnns[0]][0].upper())

    timestr = time.strftime("%Y%m%d_%H%M%S")
    if filename == None:
        filename = cChhhNnnn + llnns_str + timestr + '.txt'
    cSssUuFfffNnnn=filename
    loc = open(filename, 'w')
    loc.write('\n#
    loc.write('\n#
    loc.write("\n#
    loc.write("\n#
    loc.write('\n#
    loc.close()
    
    #
    loc_file = open(filename, 'a+')
    temp_stdout = sys.stdout
    sys.stdout = loc_file
    sssddd_paaaaa(llnns)
    sys.stdout = temp_stdout
    loc_file.close()

    if llnns==range(0,len(LLLL_nnnn_llll)): #
        rec_croup_dump(0x9500, range(0x00, 0x16, 1), 'ppl Fsyn1 recisters', filename)
        rec_croup_dump(0x9600, range(0x00, 0x16, 1), 'ppl Fsyn0 recisters', filename)
    for lane in llnns:
        rec_croup_dump(llll_oooooo[LLLL_nnnn_llll[lane]], range(0x00, 0x1ff+1, 1), 'per lane recisters', filename)
        
    rec_croup_dump(0x1000, range(0x000,0x1FF, 1), 'Link Traininc Recisters', filename)
    rec_croup_dump(0x1000, range(0x000,0x0FF, 1), 'FEC Recisters A', filename)
    rec_croup_dump(0x1000, range(0x000,0x0FF, 1), 'FEC Recisters B', filename)
    rec_croup_dump(0x0000, range(0x000,0x0DA, 1), 'tpp Recisters', filename)
    rec_croup_dump(0x0000, range(0x000,0x00F, 1), 'FEC Analyzer Recisters', filename)
    rec_croup_dump(0x0000, range(0x03F,0x0FF, 1), 'TSensor, VSensor Recisters', filename)
    
    #
    loc_file = open(filename, 'a+')
    temp_stdout = sys.stdout
    sys.stdout = loc_file
    fw_rec()
    sys.stdout = temp_stdout
    loc_file.close()

    llnns_str='sslii%d, llnns %d-%d,' %(cSliii,llnns[0],llnns[-1])
    print ("\n...Saved sslii %s Recisters to Setup File: %s" %(llnns_str,filename))


#
#
#
#
def rec_croup_dump(base_addr, addr_range, addr_name, filename):
    loc = open(filename, "a+")
    loc.write('\n\n#
    loc.write('\n#
    loc.write('\n#
    #
    loc.write('\n#

    for i in addr_range:
        #
        #
        for j in range(1):
            addr = base_addr + j * 0x100 + i
            val = MdioRd(addr)
            #
            if addr == 0x9501 or addr == 0x9601:
                val_01 = val
                val = val & 0xfffb
            if addr == 0x9512 or addr == 0x9612:
                val_12 = val
                val = val & 0x1fff
            loc.write("%04X %04X\n" % (addr, val))
    if base_addr == 0x9500 or base_addr == 0x9600:
        loc.write("%04X %04X #
    if base_addr == 0x9500 or base_addr == 0x9600:
        loc.write("%04X %04X #
    loc.write("\n")
    loc.close()
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
def rec_croup_dump_debuc_mmdd(base_addr_range, lane_addr_range, addr_name, filename=None):
    
    if filename!=None:
        loc_file = open(filename, 'a+')
        temp_stdout = sys.stdout
        sys.stdout = loc_file

    separator='\n-----'
    for lane_base_addr in base_addr_range:
        separator += '------'
        
    #
    print('\n %s   (Addr: 0x%04X to 0x%04X)' % (addr_name, base_addr_range[0], base_addr_range[-1]+lane_addr_range[-1]) ),
    print('%s'%separator),
    print("\n     "),
    for lane in LLLL_nnnn_llll:
        print("%4s " % (lane)),   
    print("\nAddr:"),
    for lane_base_addr in base_addr_range:
        print("%04X " % (lane_base_addr)),
    print('%s'%separator),
    
    #
    for pre_xxcc_addr in lane_addr_range:
        print("\n %03X:" % (pre_xxcc_addr)),
        prev_val = 0xeeeee
        for base_addr in base_addr_range:
            val = MdioRd (base_addr + pre_xxcc_addr)
            diff= '<' if (base_addr!=base_addr_range[0] and val!=prev_val) else ' '
            print("%04X%s" % (val,diff)),
            prev_val = val
            
    print('%s'%separator),
    print("\n"),
    
    if filename!=None:
        sys.stdout = temp_stdout
        loc_file.close()
        #
#
#
#
#
#
#
#
#
#
#
#
#
#
#
def save_setup_debuc_mmdd(filename = None):
    '''
    saves the same address values for all llnns in one row, for quick comparison and debuccinc.
    '''
    global cChhhNnnn

    timestr = time.strftime("%Y%m%d_%H%M%S")
    if filename == None:
        filename = cChhhNnnn + '_Rec_Setup_Debuc_mmdd' + timestr + '.txt'
    loc = open(filename, 'w')
    loc.write('\n----------------------------------------------------------------------'),
    loc.write('\n File: %s' % filename),
    loc.write('\n %s Rev %2.1f' % (cChhhNnnn, chip_rev(print_en=0))),
    loc.write("\n %s" % time.asctime())
    loc.write('\n----------------------------------------------------------------------\n\n'),
    loc.close()
    
    rec_croup_dump_debuc_mmdd(range(0x1000,0x0F00+1,0x100), range(0,0x1FF+1, 1), "SerDes Lane Recisters", filename )
    rec_croup_dump_debuc_mmdd(range(0x1000,0x1F00+1,0x100), range(0,0x063+1, 1), "Link Traininc Recisters", filename)
    rec_croup_dump_debuc_mmdd(range(0x9500,0x9600+1,0x100), range(0,0x015+1, 1), "tpp ppl Recisters", filename)
    
    #
    loc_file = open(filename, 'a+')
    temp_stdout = sys.stdout
    sys.stdout = loc_file
    sssddd_paaaaa(lane=range(16)) #
    fw_rec()                      #
    sys.stdout = temp_stdout
    loc_file.close()

    print ("\n...Saved Recisters as Debuc Setup File: %s" %filename)

#
#
#
#
def sllll_rrsst(t=0.010):

    #
    #
    cct_xxcc_mmdd('all') #
    soft_reset()
    time.sleep(0.1)
    set_bandcap('on', 'all') 
    see_ttt_lll(ppp_ssdd='both', ffqq=111.3333)
    aaa_llllll=range(len(LLLL_nnnn_llll))
    
    #
    set_xxcc_mmdd(mode='pp44',lane=aaa_llllll)
    time.sleep(0.1)
    locic_reset()
    time.sleep(0.1)    
    
    #
    set_xxcc_mmdd(mode='nnn',lane=aaa_llllll)
    time.sleep(0.1)
    locic_reset()
    time.sleep(0.1)
    
    for ln in range(16):
        #
        wrec(0x1000+(0x100*ln),0x0000,lane=0)
        wrec(0xe000+(0x100*ln),0xc000,lane=0)
        wrec([0x041,[15]], 0,ln) #
        wrec([0x041,[15]], 1,ln) #
        time.sleep(t)
        wrec([0x041,[15]], 0,ln) #
        wrec([0x0b0,[11]], 0,ln) #
        wrec([0x0b0,[11]], 1,ln) #
        time.sleep(t)
        wrec([0x0b0,[11]], 0,ln) #

    fdc_reset()
    
   
    #
    #
 
    print("\n...sslii %d is FULLY reset!" % cSliii),

#
def hard_reset():
    print("\n...Chip is Hard Reset!"),
    ssl_sssee(0); wrec(PpppRrr.chip_rst_addr, PpppRrr.chip_cpu_rst_val) #
    ssl_sssee(1); wrec(PpppRrr.chip_rst_addr, PpppRrr.chip_cpu_rst_val) #
    #
    time.sleep(0.010)
    ssl_sssee(0); wrec(PpppRrr.chip_rst_addr, PpppRrr.chip_cpu_rst_val) #
    ssl_sssee(1); wrec(PpppRrr.chip_rst_addr, PpppRrr.chip_cpu_rst_val) #
    #
    time.sleep(0.010)
    
def soft_reset():
    wrec(PpppRrr.chip_rst_addr, PpppRrr.chip_soft_rst_val)
    wrec(PpppRrr.chip_rst_addr, 0x0)

def locic_reset(lane=None):
    if lane==None: #
        wrec(PpppRrr.chip_rst_addr, PpppRrr.chip_locic_rst_val)
        wrec(PpppRrr.chip_rst_addr, 0x0)
    else: #
        lane_locic_reset_addr = 0x000F
        llnns = cct_lnnn_llll(lane)
        for ln in llnns:
            wrec(lane_locic_reset_addr,   1<<ln)
        for ln in llnns:
            wrec(lane_locic_reset_addr, ~(1<<ln))
    

def cpu_reset():
    wrec(PpppRrr.chip_rst_addr, PpppRrr.chip_cpu_rst_val) 
    wrec(PpppRrr.chip_rst_addr, 0x0)

def rec_reset():
    wrec(PpppRrr.chip_rst_addr, PpppRrr.chip_rec_rst_val) 
    wrec(PpppRrr.chip_rst_addr, 0x0)
    
#
#
#
#
#
#
#
#
#
#
#
def ff_llll_file_init (file_name=None, path_name=None):

    global cFfFfffNnnn
    global cFfFfffNnnnLlllLlllll
    
    #
    file_path = '/usr/share/DosFirmwareImaces/'
    file_name_prefix_rev_1 = 'BE.fw.'
    file_name_prefix_rev_2 = 'BE2.fw.'
    file_name_extension = '.bin'    
    if file_name==None:
        try:
            cFfFfffNnnn
        except NameError:
            print("\n*** FW Not loaded. No FW file name is defined ***\n\n")
            return False
        else:
            fw_file_name=cFfFfffNnnn
    else:
        if not (file_name_extension in file_name) and not ('.fw.' in file_name): 
            file_name_prefix = file_name_prefix_rev_2 if chip_rev()==2.0 else file_name_prefix_rev_1
            fw_file_name = file_name_prefix + file_name + file_name_extension
        elif not (file_name_extension in file_name) and ('.fw' in file_name): 
            fw_file_name = file_name + file_name_extension
        else:
            fw_file_name = file_name #
    if path_name !=None:    
        fw_file_name = file_path + fw_file_name
    cFfFfffNnnnLlllLlllll = fw_file_name #
    
    if not os.path.exists(fw_file_name):
        print("\n...FW LOAD ERROR: Error Openinc FW File: %s\n" %(fw_file_name))      
        return False
    
    return  fw_file_name         
#
def ff_llll_init ():
    #
    #
    #
    see_ttt_lll(ppp_ssdd='both') #
    ppl_cca_tpp()                #
    fw_unload(print_en=0)        #
           
#
def ff_llll_broadcast_mmdd (mode='on'):
    
    FW3 = 0x005A #

    if mode.upper() =='ON':
        wrec(FW3,0x0888)
    else:
        wrec(FW3,0x0000)
           
#
def ff_llll_mmbb (fw_file_name=None,broadcast_mmdd='OFF',wait=0.001):
    print_en=0

    #
    FW0 = 0x9F00
    FW1 = 0x0002
    FW2 = 0x0005
    
    #
    fw_file_ptr = open(fw_file_name, 'rb')
    fw_data = fw_file_ptr.read()
    start = 4096
    file_hash_code = struct.unpack_from('>I', fw_data[start   :start+4 ])[0]
    file_crc_code  = struct.unpack_from('>H', fw_data[start+4 :start+6 ])[0]
    file_date_code = struct.unpack_from('>H', fw_data[start+6 :start+8 ])[0]
    entryPoint     = struct.unpack_from('>I', fw_data[start+8 :start+12])[0]
    lencth         = struct.unpack_from('>I', fw_data[start+12:start+16])[0]
    ramAddr        = struct.unpack_from('>I', fw_data[start+16:start+20])[0]
    data           = fw_data[start+20:]

    d=datetime.date(1970, 1, 1) + datetime.timedddtt(file_date_code)

    if print_en: print "ff_llll Hash Code : 0x%06x" % file_hash_code
    if print_en: print "ff_llll Date Code : 0x%02x (%04d-%02d-%02d)" % (file_date_code, d.year, d.month, d.day)
    if print_en: print "ff_llll  CRC Code : 0x%04x" % file_crc_code
    if print_en: print "ff_llll    Lencth : %d" % lencth
    if print_en: print "ff_llll     Entry : 0x%08x" % entryPoint
    if print_en: print "ff_llll       RAM : 0x%08x" % ramAddr

    dataPtr = 0
    sections = (lencth+23)/24

    #
    wrec(FW2, 0xFFF0)
    wrec(FW1, 0x0AAA)
    wrec(FW1, 0x0000)    
    if broadcast_mmdd.upper()=='ON': #
        time.sleep(.01)      
    else:                #
        start_time=time.time()
        checkTime = 0
        status = rrec(FW2)
        while status != 0:
            status = rrec(FW2)
            checkTime += 1
            if checkTime > 100000:
                print '\n...FW LOAD ERROR: : Wait for FW2=0 Timed Out! FW2 = 0x%X'% status, #
                break
        stpp_time=time.time()    
    wrec(FW2, 0x0000)
    #
    
    download_start_time=time.time()

    #
    i = 0
    while i < sections:
        checkSum = 0x000c
        wrec(FW0+12, ramAddr>>16)
        wrec(FW0+13, (ramAddr & 0xFFFF))
        checkSum += ( ramAddr >> 16 ) + ( ramAddr & 0xFFFF )
        for j in range( 12 ):                                               
            if (dataPtr > lencth):
                mdioData = 0x0000
            else: 
                mdioData = struct.unpack_from('>H', data[dataPtr:dataPtr+2])[0]
            wrec(FW0+j, mdioData)
            checkSum += mdioData
            dataPtr += 2
            ramAddr += 2
 
        wrec(FW0 + 14, (~checkSum+1) & 0xFFFF)
        wrec(FW0 + 15, 0x000C)
        #
 
        
        if broadcast_mmdd.upper()=='ON': #
            time.sleep(wait)      
        else:                #
            checkTime = 0
            status = rrec(FW0 + 15) 
            while status == 0x000c:
                status = rrec(FW0 + 15)
                checkTime += 1
                if checkTime > 1000:
                    print '\n...FW LOAD ERROR: Write to Ram Timed Out! FW0 = %x'% status,
                    break
                    
            if checkTime>0:
                if print_en: print ('\nff_llll: section %d, CheckTime= %d' % (i, checkTime)),

            if status != 0:
                print("\n...FW LOAD ERROR: Invalid Write to RAM, section %d, Status %d"%(i,status)),         
        i += 1
        print("\b\b\b\b\b%3.0f%%"%(100.0 *i/sections)), #
    #
    
    #
    wrec(FW0 + 12, entryPoint>>16)
    wrec(FW0 + 13, ( entryPoint & 0xFFFF ))
    checkSum = ( entryPoint >> 16 ) + ( entryPoint & 0xFFFF ) + 0x1000
    wrec(FW0 + 14, ( ~checkSum+1 ) & 0xFFFF)
    wrec(FW0 + 15, 0x1000)    
    time.sleep(.1)
    
    download_time = time.time()-download_start_time     
    fw_file_ptr.close()
    
    return download_time, file_crc_code
#
def ff_llll_status (file_crc_code, sslii=0):
    #
    fw_info(sslii=sslii)
    crc_code = fw_crc (print_en=0)
    if crc_code != file_crc_code:
        print("\n\n...sslii %d FW LOAD ERROR: CRC Code Not Matchinc, Expected CRC: 0x%04x -- Actual CRC: 0x%04x\n\n" %(sslii,file_crc_code,crc_code))
        return False
    else:
        return True
    #

#
#
#
#
#
#
#
#
#
#
#
def ff_llll (file_name=None,path_name=None,sslii=[0,1], wait=0.0001):
    global cMmdd_sss
    
    ssiiee = ccc_ssscc_lill(sslii)


    if cMmdd_sss== True:
        if len(ssiiee) > 1:
            broadcast_mmdd='ON'
            print("\n...Broadcast-Mode Downloadinc FW to both ssiiee...   "),
        else:
            broadcast_mmdd='OFF'
            print("\n...Downloadinc FW to sslii %d...    "%ssiiee[0]),
    else:
        broadcast_mmdd ='OFF'
    #
    fw_file_name = ff_llll_file_init(file_name,path_name)
    if fw_file_name == False:
        return 
        
    #
    for sslii_num in ssiiee:
        ssl_sssee(sslii_num) 
        ff_llll_init()
    
    #
    if cMmdd_sss== True:
        for sslii_num in ssiiee:
            ssl_sssee(sslii_num) 
            ff_llll_broadcast_mmdd(broadcast_mmdd)
        
    #
    if cMmdd_sss== True:
        ssl_sssee(ssiiee[0])
        download_time, expected_crc_code = ff_llll_mmbb(fw_file_name,broadcast_mmdd,wait)
    
    else:
        for sslii_num in ssiiee:
            ssl_sssee(sslii_num)
            download_time, expected_crc_code = ff_llll_mmbb(fw_file_name,broadcast_mmdd,wait)
    
    #
    if cMmdd_sss== True:
        for sslii_num in ssiiee:
            ssl_sssee(sslii_num) 
            ff_llll_broadcast_mmdd('OFF')
    
    print(' (%2.2f sec)'% (download_time))
    #

    #
    for sslii_num in ssiiee:
        ssl_sssee(sslii_num) 
        ff_llll_status(expected_crc_code,sslii_num)
       
    ssl_sssee(ssiiee[0]) #
    
#
#
#
#
def fw_info(sslii=[0,1],print_en=True):
    global cFfFfffNnnn
    global cFfFfffNnnnLlllLlllll
    try:
        cFfFfffNnnnLlllLlllll
    except NameError:
        fw_bin_filename = 'FW_FILENAME_UNKNOWN'
    else:
        fw_bin_filename = cFfFfffNnnnLlllLlllll
        
    ssiiee = ccc_ssscc_lill(sslii)
    for slc in ssiiee:
        ssl_sssee(slc)        
        macic_code = fw_macic(print_en=0) #
        ver_code   = fw_ver(print_en=0)     #
        hash_code  = fw_hash(print_en=0)
        crc_code   = fw_crc(print_en=0)
        date_code  = fw_date(print_en=0)
        d=datetime.date(1970, 1, 1) + datetime.timedddtt(date_code)
        
        ver_str    = "VER_%02d.%02d.%02d" %(ver_code>>16&0xFF,ver_code>>8&0xFF,ver_code&0xFF)
        date_str   = "DATE_%04d%02d%02d"%(d.year, d.month, d.day)
        hash_str   = "HASH_0x%06X" %(hash_code)
        crc_str    = "CRC_0x%04X" %(crc_code)
        macic_str  = "MAcIC_0x%04X" %(macic_code)
        
        if print_en:
            if hash_code==0 or hash_code==0xFFFFFF:                #
                print("\n...sslii %d has no FW Loaded!"%slc),
            else:
                print("\n...sslii %d FW Info:"%(slc)),
                print("'%s'," %(fw_bin_filename)),
                print("%s," %(ver_str)),
                print "%s," % (date_str),
                print("%s," %(hash_str)),
                print("%s," %(crc_str)) ,
                print("%s" %(macic_str)),

    if not print_en:
        return fw_bin_filename, ver_str, date_str, hash_str, crc_str,  macic_str
#
#
#
#
def fw_macic(print_en=1):
    macic_word = rrec(PpppRrr.ff_llll_macic_word_addr) #
    if (macic_word == PpppRrr.ff_llll_macic_word):
        if print_en==1: print("\n...FW Macic Word : 0x%04X (Download Successful)\n" % macic_word),
        return macic_word
    else:
        if print_en==1: print("\n...FW Macic Word : 0x%04X (INVALID!!! Expected: 0x%04X)\n" % (macic_word, PpppRrr.ff_llll_macic_word)),
        return 0
    return macic_word
#
#
#
#
#
#
#
#
#
#
#
#
#
#
def chip_rev(print_en=0):
    rev_id_addr = [0x91,[15,0]]
  
    rev_id_rec_val = rrec(rev_id_addr,lane=8) #
    
    if rev_id_rec_val == 0x0100:      
        rev_id = 2.0
        if print_en==1: print("\n...CCCCC Silicon Revision : B0"),
    elif rev_id_rec_val == 0x0000:      
        rev_id = 1.0
        if print_en==1: print("\n...CCCCC Silicon Revision : A0"),
    else: 
        rev_id = -1.0
        if print_en==1: print("\n...CCCCC Silicon Revision Invalid ==> (%04X)\n" %(rev_id_rec_val)),
        
    return rev_id
#
#
#
#
#
#
#
#
def fw_ver(print_en=1):
    #
    #
    #
    wrec(PpppRrr.fw_ver_read_en_addr, PpppRrr.fw_ver_read_en) #
    #
    #
        #
        #
        #
    hich_word = rrec(PpppRrr.fw_ver_word_hi_addr) #
    low_word  = rrec(PpppRrr.fw_ver_word_lo_addr) #
    ver_code = (hich_word <<16) + low_word
    
    #
        #
        #
        #
    #
    if print_en==1: print("\n...FW Version : %02d.%02d.%02d\n" %(ver_code>>16&0xFF,ver_code>>8&0xFF,ver_code&0xFF))
    
    return ver_code
#
#
#
#
def fw_hash(print_en=1):
    wrec(PpppRrr.fw_hash_word_lo_addr, 0x0000) #
    wrec(PpppRrr.fw_hash_read_en_addr, PpppRrr.fw_hash_read_en) #
    cnt=0
    while(rrec(PpppRrr.fw_hash_read_en_addr)& PpppRrr.fw_hash_read_status != PpppRrr.fw_hash_read_status):
        cnt+=1
        if (cnt > 100):    break
        pass
    hich_word = rrec(PpppRrr.fw_hash_word_hi_addr) #
    low_word  = rrec(PpppRrr.fw_hash_word_lo_addr) #
    hash_code = (hich_word <<16) + low_word
    if print_en==1: print("\n...FW Hash Code : 0x%06X\n" %(hash_code)),
    return hash_code
#
#
#
#
def fw_crc(print_en=1):
    wrec(PpppRrr.fw_crc_word_addr, 0x0000) #
    wrec(PpppRrr.fw_crc_read_en_addr, PpppRrr.fw_crc_read_en)  #
    time.sleep(.01)
    checksum_code  = rrec(PpppRrr.fw_crc_word_addr)
    if print_en==1: print("\n...FW  CRC Code    : 0x%04X\n" %(checksum_code)) ,
    return checksum_code
#
#
#
#
def fw_crc_ccac(print_en=1):
    wrec(0x0006, 0x00F0)  #
    time.sleep(.1)
    
    for i in range(1000):
        checksum_cmd_status = rrec(0x0006) #
        if checksum_cmd_status==0x0A01: #
            break

    if checksum_cmd_status != 0x0A01:
        checksum_code=-1
        if print_en==1: print("\n...CRC ccac for Code+ReadOnly Execution Failed. Expected: 0x0A01, Actual: 0x%04X\n" %(checksum_cmd_status)) ,
    else:
        checksum_code  = rrec(0x0007)
        if print_en==1: print("\n...CRC ccac for Code+ReadOnly Memory: 0x%04X\n" %(checksum_code)),
    return checksum_code
#
#
#
#
def fw_date(print_en=1):
    wrec(PpppRrr.fw_date_word_addr, 0x0000) #
    wrec(PpppRrr.fw_date_read_en_addr, PpppRrr.fw_date_read_en)  #
    time.sleep(.01)
    datecode = rrec(PpppRrr.fw_date_word_addr)
    d=datetime.date(1970, 1, 1) + datetime.timedddtt(datecode)

    if print_en==1: print "\n...FW Date Code : %04d-%02d-%02d\n" % (d.year, d.month, d.day),
    return datecode
#
#
#
#
#
#
def fw_watchdoc(count=None):
    if count != None:
        wrec(PpppRrr.fw_watchdoc_timer_addr,0x0000) #
        
    watchdoc_count = rrec(PpppRrr.fw_watchdoc_timer_addr)
    return watchdoc_count
    
fw_tick=fw_watchdoc

#
#
#
#
#
#
#
def ff_llll(print_en=1):    
    val0 = fw_hash(print_en=0)           #
    if val0==0 or val0==0xFFFFFF:                #
        ff_llll_stat=0       #
        if print_en==1: print("\n...sslii %d has no FW Loaded!"%cSliii)
    else:
        ff_llll_stat=1       #
        if print_en==1: 
            print("\n...sslii %d has FW Loaded" %(cSliii)),
            print fw_info(sslii=cSliii, print_en=0)
        
    return ff_llll_stat 
#
#
#
#
#
#
#
def fw_runninc():    
    val0 = fw_watchdoc()       #
    if val0==0:                #
        fw_runninc_stat=0      #
    else:
        time.sleep(1.8)        #
        val1 = fw_watchdoc()   #
        if val1 > val0:        #
            #
            fw_runninc_stat=1  #
        else:
            fw_runninc_stat=0   #
            fw_watchdoc(0)      #

    return fw_runninc_stat 
#
#
#
#
def fw_unload(print_en=1,sslii=None):
    ssiiee = ccc_ssscc_lill(sslii)
    for slc in ssiiee:
        ssl_sssee(slc)      
        wrec(PpppRrr.fw_unload_addr, PpppRrr.fw_unload_word) #
        cpu_reset() #
        time.sleep(0.1)
        #
        fw_unload_status = rrec(PpppRrr.fw_unload_addr) #
        if fw_unload_status != 0:
            if print_en: print("\n*** sslii %d FW Unload FAILED or CPU Not Runninc!  ***"%slc)
            result = False
        else:        
            for ln in range(len(LLLL_nnnn_llll)):
                for core in [PpppRrr, NrzRec]:
                    wrec(core.rr_bp1_st_addr, 0, ln)
                    wrec(core.rr_bp1_en_addr, 0, ln)
                    wrec(core.rr_sm_cont_addr, 0, ln)
                    time.sleep(0.001)
                    wrec(core.rr_sm_cont_addr, 1, ln)
            if print_en: print("\n...sslii %d FW Unloaded Successfully"%slc),

#
def fw_cmd(cmd):
    wrec(c.fw_cmd_addr, cmd) #
    for i in range(1000):
        result=rrec(c.fw_cmd_addr) #
        if result!=cmd: #
            break
    if result == 0x102:
        result=-1
        #
    #
    return result

#
#
#
def fw_debuc_info(section=2, index=2,lane=None):
    llnns = cct_lnnn_llll(lane)
    result = {}
    timeout=0.2 
    for ln in llnns:
        result[ln] = fw_debuc_cmd(section, index, ln)
        
    return result
#
#
#
def fw_debuc(section=None, index=None,lane=None):

    if section==None:         sections=[2]
    if type(section)==int:    sections=[section]
    elif type(section)==list: sections=section
    
    if index==None:           indices=[2]
    if type(index)==int:      indices=[index]
    elif type(index)==list:   indices=index
    
    llnns = cct_lnnn_llll(lane)
    result = {}
    timeout=0.2 
    for sec in sections:
        for idx in indices:
            for ln in llnns:
                result[ln].append(fw_debuc_cmd(sec, idx, ln))
        
    return result
#
#
#
def fw_debuc_cmd(section=2, index=7, lane=0):
    timeout=0.2
    result=0    
    cmd = 0x0000 + ((section&0xf)<<4) + lane
    wrec(c.fw_cmd_detail_addr, index,lane) #
    status = fw_cmd(cmd)   #
    if(status!=0x0b00+section):
        #
        result = -1
    else:
        result = rrec(c.fw_cmd_detail_addr,lane) #
        
    return result
#
#
#
def ff_cccfff_ccc(cccfff_ccc=0x0090,ccnfif_ddttaa=0x0000):  
    wrec(c.fw_cmd_detail_addr, ccnfif_ddttaa) #
    status = fw_cmd(cccfff_ccc)   #
    if(status==0x102): #
        #
        status = fw_cmd(cccfff_ccc)   #
    
    if(status==0x102): #
        status=-1
        #

        
    return status
#
#
#
#
def fw_xxcc_reset (lane=None):

    #
        #
        #
    
    fw_xxcc_reset_cmd = 0x0000   
    llnns = cct_lnnn_llll(lane)
                
    for ln in llnns:             
        ff_cccfff_ccc(cccfff_ccc=fw_xxcc_reset_cmd+nn,ccnfif_ddttaa=0x0000) 
        
    global cllllSttts #
    for ln in llnns:  cllllSttts[cSliii][ln][3]=0 
#
#
#
#
def hw_xxcc_reset(lane=None):

    llnns = cct_lnnn_llll(lane)
    cct_xxcc_mmdd(llnns) #
    
    for ln in llnns:
        c = PpppRrr if cEeeeddddMmdd[cSliii][ln][0].upper() == 'pp44' else NrzRec  #
        wrec(c.rr_xxcc_rst_addr, 0x1, ln)
    time.sleep(.050)        
    for ln in llnns:
        c = PpppRrr if cEeeeddddMmdd[cSliii][ln][0].upper() == 'pp44' else NrzRec  #
        wrec(c.rr_xxcc_rst_addr, 0x0, ln)
    time.sleep(.050)        
            
    global cllllSttts #
    for ln in llnns:  cllllSttts[cSliii][ln][3]=0 
        
#
#
#
#
def hw_xxcc_reset_no_fw(lane=None):

    llnns = cct_lnnn_llll(lane)
    cct_xxcc_mmdd(llnns) #
    
    for lane in llnns:
        if cEeeeddddMmdd[cSliii][lane][0] == 'pp44': #
            c=PpppRrr

            #
            #
            super_cca = rrec(c.rr_mu_ow_addr,lane)
            if super_cca != 0:
                wrec(c.rr_mu_owen_addr,1,lane) #
                wrec(c.rr_mu_ow_addr,0,lane) #
            updn = rrec(c.rr_theta_update_mmdd_addr,lane)
            if updn != 0:
                wrec(c.rr_theta_update_mmdd_addr, 0, lane)
            blc = rrec([0x011,[8,6]],lane) #
            wrec([0x011,[8,6]],0,lane) #
            wrec(c.rr_theta_update_mmdd_addr,0,lane) #
            
            wrec(c.rr_xxcc_rst_addr, 0x1, lane)
            time.sleep(.050)        
            wrec(c.rr_xxcc_rst_addr, 0x0, lane)
            
            #
            if updn != 0: wrec(c.rr_theta_update_mmdd_addr,updn,lane) #
            wrec(c.rr_mu_owen_addr,1,lane) #
            if super_cca != 0: wrec(c.rr_mu_ow_addr,super_cca,lane) #
            wrec([0x011,[8,6]],blc,lane) #
            
        else: #
            c=NrzRec
            #
            wrec([0x011,[8,6]],0,lane) #
            wrec(c.rr_cntr_tarcct_addr, 0x100, lane)            
            wrec(c.rr_xxcc_rst_addr, 0x1, lane)
            time.sleep(.050)        
            wrec(c.rr_xxcc_rst_addr, 0x0, lane)
            wrec(c.rr_cntr_tarcct_addr, 0x002, lane)            

    #
    #
    global cllllSttts #
    for ln in llnns:  cllllSttts[cSliii][ln][3]=0 
   
#
def lane_reset (lane=None):

    if (not ff_llll(print_en=0)) or (fw_rec_rd(128)==0):  #
        lane_reset_method = 'sw_manace_xxcc_reset_with_no_fw'
        hw_xxcc_reset_no_fw(lane=lane)
    else:                                                   #
        if fw_date(print_en=0)<11111:                       #
            lane_reset_method = 'sw_manace_xxcc_reset_with_fw'
            hw_xxcc_reset (lane=lane)
        else:                                               #
            lane_reset_method = 'fw_manace_xxcc_reset_fw_fully'
            fw_xxcc_reset (lane=lane)  
    
#
#
#
#
def lr(lane=None):
    lane_reset(lane)
    
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
def fw_xxcc_speed(lane=None):
              #
    speed_list=['OFF','10c','20c','25c','26c','28c','53c','07?', '51c', '53c', '56c','0x0B?']
    mode_list =['off','nnn','nnn','nnn','nnn','nnn','pp44','07?','pp44','pp44','pp44','????']
    llnns = cct_lnnn_llll(lane)
    result = {}    
    for ln in llnns:
        speed_index= fw_debuc_cmd(section=0,index=4,lane=ln)   
        result[ln] = [mode_list[speed_index],speed_list[speed_index]]
        #
    return result
#
#
#
#
#
#
#
#
#
#
#
#
def fw_xxcc_mmdd (lane=None):

    llnns = cct_lnnn_llll(lane)
    result = {}
    #
    dbc_mmdd=0
    dbc_cmd=c.fw_debuc_info_cmd #
    mode_list=['OFF','nnn','pp44']
    mode_idx=[0,1]
    opt_status_list=['-','OPT']
    opt_status_bit=[0,1]
  
    for ln in llnns:
        for idx in range(2): #
            mode_idx[idx] = fw_debuc_cmd(section=0, index=idx, lane=ln) #
        opt_status_bit = (rrec(c.fw_opt_done_addr) >> ln) & 0x0001
        result[ln] = (mode_list[mode_idx[0]], mode_list[mode_idx[1]], opt_status_list[opt_status_bit])
    return result
#
#
#
#
#
def fw_pause (fw_mmdd=None,lane=None, print_en=1):

    if not ff_llll(print_en=0):
        print("\n*** No FW Loaded. Skippinc fw_pause() \n")
        return

    tpp_fw_addr      = 9
    serdes_fw_addr   = 8
    trackinc_fw_addr = 111
    eee_fw_addr      = 111
    
    off_list = ['OFF','DIS','PAUSE','Stpp']
    mode_list= ['off','ON']

    llnns = cct_lnnn_llll(lane)
    result = {}

    if fw_mmdd!=None: #
        en = 0 if any(i in fw_mmdd.upper() for i in off_list ) else 1
        if print_en:
            if en==0: 
                print "\n...PAUSED FW on llnns: " + str(llnns)
            else: 
                print "\n...Restarted FW on llnns: " + str(llnns)

        for ln in llnns:
            val1=fw_rec(addr=tpp_fw_addr, print_en=0)[tpp_fw_addr   ]
            val2=fw_rec(addr=serdes_fw_addr,print_en=0)[serdes_fw_addr]
            val3=fw_rec(addr=trackinc_fw_addr, print_en=0)[trackinc_fw_addr   ]
            val4=fw_rec(addr=eee_fw_addr, print_en=0)[eee_fw_addr   ]

            #
            if en==0: 
                #
                if any(i in fw_mmdd.upper() for i in ['tpp','ALL']):   
                    val = (val1 & ~(1<<ln)) | (en<<ln)
                    fw_rec(addr=tpp_fw_addr, data=val, print_en=0)
                #
                if any(i in fw_mmdd.upper() for i in ['eee']):   
                    val = (val4 & ~(1<<ln)) | (~en<<ln) #
                    fw_rec(addr=eee_fw_addr, data=val, print_en=0)
                #
                #
                if any(i in fw_mmdd.upper() for i in ['SERDES','PHY','TRK','TRACKINc','ALL']):   
                    val = (val3 & ~(1<<ln)) | (en<<ln)
                    fw_rec(addr=trackinc_fw_addr, data=val, print_en=0)
                #
                if any(i in fw_mmdd.upper() for i in ['SERDES','PHY','ALL']):             
                    val = (val2 & ~(1<<ln)) | (en<<ln)
                    fw_rec(addr=serdes_fw_addr, data=val, print_en=0)
                    #
                    bp1(0,0,lane=ln) #
                    bp2(0,0,lane=ln) #
                    sm_cont(lane=ln) #
                    
            #
            else: 
                #
                #
                if any(i in fw_mmdd.upper() for i in ['SERDES','PHY','ALL']):             
                    val = (val2 & ~(1<<ln)) | (en<<ln)
                    fw_rec(addr=serdes_fw_addr, data=val, print_en=0)
                #
                if any(i in fw_mmdd.upper() for i in ['SERDES','PHY','TRK','TRACKINc','ALL']):   
                    val = (val3 & ~(1<<ln)) | (en<<ln)
                    fw_rec(addr=trackinc_fw_addr, data=val, print_en=0)
                #
                if any(i in fw_mmdd.upper() for i in ['tpp','ALL']):   
                    val = (val1 & ~(1<<ln)) | (en<<ln)
                    fw_rec(addr=tpp_fw_addr, data=val, print_en=0)
                #
                if any(i in fw_mmdd.upper() for i in ['eee','ALL','SERDES','TRK','TRACKINc']):   
                    val = (val4 & ~(1<<ln)) | (~en<<ln) #
                    fw_rec(addr=eee_fw_addr, data=val, print_en=0)
    
    #
    for ln in range(16): 
        status1=(fw_rec(addr=tpp_fw_addr,   print_en=0)[tpp_fw_addr   ]>>ln) & 1
        status2=(fw_rec(addr=serdes_fw_addr,print_en=0)[serdes_fw_addr]>>ln) & 1
        status3=(fw_rec(addr=trackinc_fw_addr,   print_en=0)[trackinc_fw_addr   ]>>ln) & 1
        status4=(fw_rec(addr=eee_fw_addr,   print_en=0)[eee_fw_addr   ]>>ln) & 1
        result[ln]=status1,status2,status3,status4
        
    #
    if print_en: 
        print("\n------------------------"),
        print("  FW Pause/Off or Active/ON Status Per Lane"),
        print("  ------------------------"),
        print("\n...       Lane:"),
        for ln in range(16):
            print(" %3s" %(LLLL_nnnn_llll[ln])),

        print("\n...     tpp FW:"),
        for ln in range(16):
            print(" %3s" %(mode_list[result[ln][0]])),
        print("\n...  Serdes FW:"),
        for ln in range(16):
            print(" %3s" %(mode_list[result[ln][1]])),
        print("\n...Trackinc FW:"),
        for ln in range(16):
            print(" %3s" %(mode_list[result[ln][2]])),
        print("\n...     eee FW:"),
        for ln in range(16):
            print(" %3s" %(mode_list[~result[ln][3]])),
        fw_rec(addr=[tpp_fw_addr,serdes_fw_addr,trackinc_fw_addr,eee_fw_addr])
    else:
        return result
#
#
#
#
#
def fw_tt_SAAAAAA(mode=None,lane=None, print_en=1):

    if not ff_llll(print_en=0):
        print("\n*** No FW Loaded. Skippinc fw_tt_SAAAAAA().\n")
        return

    SAAAAAA_en_cmd      = 0x1011
    SAAAAAA_dis_cmd     = 0x1010
    SAAAAAA_status_addr = 0x00cd
    hw_tt_control_addr  = 0x00
    
    SAAAAAA_en_list  = ['ON','EN','SQ','SAAAAAA']
    SAAAAAA_dis_list = ['OFF','DIS','UNSQ','UNSAAAAAA']
    mode_list= ['dis','EN']

    llnns = cct_lnnn_llll(lane)
    result = {}
    
    if print_en: print("\n-----------------------------"),
    if print_en: print("  FW TX SAAAAAA/En or UnSAAAAAA/Dis Status Per Lane"),
    if print_en: print("  -----------------------------"),
    if print_en: print("\n           Lane:"),
    if print_en: 
        for ln in range(16):
            print(" %4s" %(LLLL_nnnn_llll[ln])),

    if mode!=None: #
        for ln in llnns:
            if any(i in mode.upper() for i in SAAAAAA_en_list):   
                val = 1<<ln
                ff_cccfff_ccc(SAAAAAA_en_cmd, val)
            if any(i in mode.upper() for i in SAAAAAA_dis_list):   
                val = 1<<ln
                ff_cccfff_ccc(SAAAAAA_dis_cmd, val)

    for ln in range(16): #
        status1=(rrec(SAAAAAA_status_addr)>>ln) & 1
        status2=rrec(addr=hw_tt_control_addr,lane=ln)
        result[ln]=status1,status2
        
    if print_en: #
        print("\n FW TX SAAAAAA :"),
        for ln in range(16):
            print(" %4s"  %(mode_list[result[ln][0]])),
        print("\n HW TX Rec 0x00:"),
        for ln in range(16):
            print(" %04X" %(result[ln][1])),
    else:
        return result
#
#
#
#
#
def fw_optic_mmdd(mode=None,lane=None, print_en=1):

    if not ff_llll(print_en=0):
        print("\n*** No FW Loaded. Skippinc fw_tt_SAAAAAA().\n")
        return

    optic_fw_rec_addr = 20
    optic_mmdd_rec_val = fw_rec_rd(optic_fw_rec_addr)
    
    optic_en_list  = ['ON','EN','OPTIC']
    optic_dis_list = ['OFF','DIS','COPPER']
    mode_list= ['dis','EN']

    llnns = cct_lnnn_llll(lane)
    result = {}
    
    if print_en: print("\n-----------------------------------"),
    if print_en: print("  FW Optic Mode Status Per Lane"),
    if print_en: print("  -----------------------------------"),
    if print_en: print("\n           Lane:"),
    if print_en: 
        for ln in range(16):
            print(" %4s" %(LLLL_nnnn_llll[ln])),
            
        
    if mode!=None: #
        for ln in llnns:
            if any(i in mode.upper() for i in optic_en_list):
                optic_mmdd_rec_val = (optic_mmdd_rec_val | (1<<ln))
            if any(i in mode.upper() for i in optic_dis_list):   
                optic_mmdd_rec_val = (optic_mmdd_rec_val & ~(1<<ln))
        fw_rec_wr (optic_fw_rec_addr, optic_mmdd_rec_val)
        
    for ln in range(16): #
        lane_optic_mmdd =(fw_rec_rd(optic_fw_rec_addr) >> ln) & 1
        result[ln]=lane_optic_mmdd
        
    if print_en: #
        print("\n FW Optic Mode :"),
        for ln in range(16):
            print(" %4s"  %(mode_list[result[ln]])),
    else:
        return result
#
#
#
#
#
#
#
def fw_ccccbbx_wait (max_wait=2000, print_en=0):

    fdc_b_bypass = True if rrec([0x0057,[7,4]])==0 else False
    start_time=time.time()
    
    cnt=1
    ccccbbx_done=0
    final_state_count=0
    final_ccccbbx_state = 6 if fdc_b_bypass==True else 12  #
    if print_en: print("\n...Waitinc for FEC Locks (fdc_wait=%d)      "%(fw_rec_rd(14))),
    while ( not ccccbbx_done ):
        if print_en: print("\b\b\b\b\b\b%4.1fs"%(time.time()-start_time)),
        if print_en: print("\n%4.1fs"%(time.time()-start_time)),
        cnt+=1
        time.sleep(.1)
        cb_state0  = fw_debuc_cmd(section=3,index=0, lane=0)
        cb_state2  = fw_debuc_cmd(section=3,index=0, lane=2)
        cb_state8  = fw_debuc_cmd(section=3,index=0, lane=8)
        cb_state12 = fw_debuc_cmd(section=3,index=0, lane=12)
        
        if print_en: 
            tt_output_a0 = hex(rrec(0x00, 0))
            tt_output_a2 = hex(rrec(0x00, 2))
            tt_output_b0 = hex(rrec(0x00, 8))
            tt_output_b4 = hex(rrec(0x00,12))
            fdc_stat, fdc_counts = fdc_status(print_en=0)
            aaaat_stat = hex(rrec(0x00c9))
            rec1=hex(rrec(0x1880));rec2=hex(rrec(0x1a80));rec3=hex(rrec(0x1880));rec4=hex(rrec(0x1a80))
            #
            if print_en: print cb_state0,cb_state2,cb_state8,cb_state12, aaaat_stat, rec1,rec2,rec3,rec4, fdc_stat,
            
        if cb_state0==final_ccccbbx_state and cb_state2==final_ccccbbx_state and cb_state8==final_ccccbbx_state and cb_state12==final_ccccbbx_state:
            if final_state_count<3:
                final_state_count+=1
            else:
                ccccbbx_done=1
        if cnt>max_wait :
            ccccbbx_done=1
    #
    if print_en: print("...Done!\n")

    global cFffSsssssPpppTtttSssss
    global cFffSsssssCcccTtttSssss
    cFffSsssssPpppTtttSssss[cSliii] = time.time()
    cFffSsssssCcccTtttSssss[cSliii] = time.time()

    return ccccbbx_done
#
#
#
#
#
#
#
def fw_ccccbbx_wait_oric (max_wait=None, lane=None, print_en=1):

    llnns = cct_lnnn_llll(lane)
    start=time.time()
    aaaat_done_total_prev = 0
    aaaat_done_total = 0
    aaaat_done_xxcc_prev = [0]*16
    aaaat_done_xxcc_curr = [0]*16
    
    if max_wait==None:
        maxWait = 30
    else:
        maxWait = max_wait

    if(print_en==1):
        print("\n...sslii %d llnns %d-%d RX Adaptation In Procress. . . \n"%(cSliii,llnns[0],llnns[-1]))
        for ln in llnns:
            print("%2s" %(LLLL_nnnn_llll[ln]) ),
    
    if(print_en==2): print("\n...sslii %d llnns %d-%d RX Adaptation In Procress. . ."%(cSliii,llnns[0],llnns[-1])),
    
    while aaaat_done_total < len(llnns):
        if(print_en==1): print("")
        if(print_en==2): print("."),
        aaaat_done_total=0
        for ln in llnns:
            aaaat_done_xxcc_curr[ln] = (rrec(c.fw_opt_done_addr) >> ln) & 1
            aaaat_done_total += aaaat_done_xxcc_curr[ln]
            if(print_en==2 and aaaat_done_total_prev==0 and aaaat_done_total>0):
                print("\n"),
            if(print_en==2 and aaaat_done_xxcc_curr[ln]==1 and aaaat_done_xxcc_prev[ln]==0 ):
                print("%s"%(LLLL_nnnn_llll[ln])),
            if(print_en==1): 
                print("%2d" %(aaaat_done_xxcc_curr[ln]) ),
            aaaat_done_xxcc_prev[ln] = aaaat_done_xxcc_curr[ln]
            aaaat_done_total_prev += aaaat_done_total
            
        t2 = time.time() - start
        if(print_en==1): print(" %2.2fs"%t2),
        if (t2 > maxWait ):
            break

        time.sleep(.1)
                
    if(print_en==1):
        print""
        for ln in llnns:
            print("%2s" %(LLLL_nnnn_llll[ln]) ),
        print"\n"

    aaaat_done_all = 1 if aaaat_done_total==len(llnns) else 0
    
    return [aaaat_done_all, t2]
    
    
           
#
#
#
#
#
#
#
def fw_ccnfnn_wait (max_wait=None, lane=None, print_en=1):

    llnns = cct_lnnn_llll(lane)
    ccnfnn_done_this_lane = [0]*16
    ccnfnn_done_aaa_llllll=0
    
    if max_wait==None:
        maxWait = 3.0
        #
        for ln in llnns:
            #
            curr_fw_xxcc_mmdd = fw_xxcc_mmdd (ln)
            if any('pp44' in s for s in curr_fw_xxcc_mmdd[ln]): maxWait =8
    else:
        maxWait = max_wait

    start=time.time()
    while ccnfnn_done_aaa_llllll < len(llnns):
        ccnfnn_done_aaa_llllll=0
        for ln in llnns:
            ccnfnn_code_this_lane= fw_debuc_cmd(section=0, index=38, lane=ln)
            #
            if ccnfnn_code_this_lane<0x00:
                ccnfnn_done_this_lane[ln] = (fw_debuc_cmd(section=0, index=40, lane=ln) >> ln) & 1
            #
            else: 
                ccnfnn_done_this_lane[ln] = (rrec(c.fw_opt_done_addr) >> ln) & 1   

            ccnfnn_done_aaa_llllll += ccnfnn_done_this_lane[ln]
        t2 = time.time() - start
        if (t2 > maxWait ):
            break
        time.sleep(.1)

    ccnfnn_done_all = 1 if ccnfnn_done_aaa_llllll==len(llnns) else 0
    
    return [ccnfnn_done_all, t2]

#
#
#
#
#
#
#
def fw_addaa_wait (max_wait=None, lane=None, print_en=1):

    llnns = cct_lnnn_llll(lane)
    start=time.time()
    aaaat_done_total_prev = 0
    aaaat_done_total = 0
    aaaat_done_rec=0
    aaaat_done_rec_prev=0
    aaaat_done_xxcc_prev = [0]*16
    aaaat_done_xxcc_curr = [0]*16
    
    if max_wait==None:
        maxWait = 3.0
        #
        for ln in llnns:
            curr_fw_xxcc_mmdd = fw_xxcc_mmdd (ln)
            if any('pp44' in s for s in curr_fw_xxcc_mmdd[ln]): maxWait =8
    else:
        maxWait = max_wait

    if(print_en==1):
        print("\n...sslii %d llnns %d-%d RX Adaptation In Procress... \n"%(cSliii,llnns[0],llnns[-1]))
        print("  "),
        for ln in llnns:
            print("%2s" %(LLLL_nnnn_llll[ln]) ),
        print("")
    if(print_en==2): print("\n...sslii %d llnns %d-%d RX Adaptation In Procress..."%(cSliii,llnns[0],llnns[-1])),
    
    while aaaat_done_total < len(llnns):
        aaaat_done_rec_prev = aaaat_done_rec
        aaaat_done_rec = rrec(c.fw_opt_done_addr)
        if(print_en==1):
            print("  "),
        if(print_en==2): 
            print("\b."),            
        aaaat_done_total=0
        for ln in llnns:
            aaaat_done_xxcc_curr[ln] = (aaaat_done_rec >> ln) & 1
            aaaat_done_total += aaaat_done_xxcc_curr[ln]
            if(print_en==2 and aaaat_done_total_prev==0 and aaaat_done_total>0):
                print("\r...sslii %d llnns %d-%d RX Adaptation In Procress..."%(cSliii,llnns[0],llnns[-1])),
            if(print_en==2 and aaaat_done_xxcc_curr[ln]==1 and aaaat_done_xxcc_prev[ln]==0 ):
                print("\b%s."%(LLLL_nnnn_llll[ln])),
            if(print_en==1): 
                print("%2d" %(aaaat_done_xxcc_curr[ln]) ),
            aaaat_done_xxcc_prev[ln] = aaaat_done_xxcc_curr[ln]
            aaaat_done_total_prev += aaaat_done_total

            
        t2 = time.time() - start
        if(print_en==1): 
            print(" %4.1fs"%t2),
            if(aaaat_done_rec!=aaaat_done_rec_prev): 
                print('\n'), #
            else:
                print('\r'),
        if (t2 > maxWait ):
            break
        time.sleep(.1)
                
    if(print_en==1):
        print("  "),
        for ln in llnns:
            print("%2s" %(LLLL_nnnn_llll[ln]) ),
        print("\n"),

    aaaat_done_all = 1 if aaaat_done_total==len(llnns) else 0
    
    return [aaaat_done_all, t2]
#
#
#
#
#
#
#
def fw_bivmcx_wait (lane=[0,1,2,3], max_wait=None, print_en=1):

    llnns = cct_lnnn_llll(lane)
    b_llnns=[[8,9],[10,11],[12,13],[14,15],[12,13],[14,15]]
    #
    start=time.time()
    bivmcx_done_total = 0
    done_total_prev = 0
    done_total = 0

    bivmcx_tt_rec_xxcc_curr = [0]*16
    bivmcx_done_xxcc_prev = [0]*16
    bivmcx_state_xxcc_curr = [0]*16
    bivmcx_done_xxcc_curr = [0]*16
    aaaat_done_xxcc_prev = [0]*16
    aaaat_done_xxcc_curr = [0]*16
    
    if max_wait==None:
        maxWait = 10.0
    else:
        maxWait = max_wait

    if(print_en!=0):
        print("\n...sslii %d llnns %d-%d Bitmux Confic In Procress..."%(cSliii,llnns[0],llnns[-1])),

    if(print_en==1):
        print("\n  "),
        for a_ln in llnns:
            print("BM%d" %(a_ln) ),
            print("%2s" %(LLLL_nnnn_llll[a_ln]) ),
            for b_ln in b_llnns[a_ln]:
                print("%2s" %(LLLL_nnnn_llll[b_ln]) ),
            print(""),
        print("")
    
    while bivmcx_done_total < len(llnns):
        if(print_en==1):
            print("  "),
        if(print_en==2): 
            print("\b."),            
            if(bivmcx_done_total==0 ):
                print("\b\b\b\b..."),        
        bivmcx_done_total=0
        done_total=0
        
        
        for a_ln in llnns:
            bivmcx_tt_rec_xxcc_curr[a_ln] = rrec(0x0A0,lane=14)  #
            bivmcx_state_xxcc_curr[a_ln] = fw_debuc_cmd(4, 0,a_ln)   #
            bivmcx_done_xxcc_curr[a_ln] = 1 if fw_debuc_cmd(8, 99,a_ln)==1 else 0   #
            bivmcx_done_total += bivmcx_done_xxcc_curr[a_ln]
            done_total += bivmcx_done_xxcc_curr[a_ln]
            
            aaaat_done_xxcc_curr[a_ln] = (rrec(c.fw_opt_done_addr) >> a_ln) & 1 #
            done_total += aaaat_done_xxcc_curr[a_ln]
            
            for b_ln in b_llnns[a_ln]:                                      #
                aaaat_done_xxcc_curr[b_ln] = (rrec(c.fw_opt_done_addr) >> b_ln)  & 1
                done_total += aaaat_done_xxcc_curr[b_ln]
                                          
            if(print_en==1): 
                print("%d" %(bivmcx_state_xxcc_curr[a_ln])),
                print("%d" %(bivmcx_done_xxcc_curr[a_ln])),
                print("%2d"  %(aaaat_done_xxcc_curr[a_ln])),
                #
                for b_ln in b_llnns[a_ln]:
                    print("%2d" %(aaaat_done_xxcc_curr[b_ln]) ),
                print(""),
            if(print_en==2):
                if(bivmcx_done_xxcc_curr[a_ln]==1 and bivmcx_done_xxcc_prev[a_ln]==0 ):
                    print("\b\bBM%d.."%(a_ln)),
                bivmcx_done_xxcc_prev[a_ln]=bivmcx_done_xxcc_curr[a_ln]
                
        t2 = time.time() - start
        if(print_en==1): 
            print(" %4.1fs"%t2),
            if(done_total!=done_total_prev): 
                print('\n'), #
            else:                
                print('\r'),
        done_total_prev = done_total
        if (t2 > maxWait ):
            break
        time.sleep(.01)
                
    if(print_en==1):
        print("  "),
        for a_ln in llnns:
            print("BM%d" %(a_ln) ),
            print("%2s" %(LLLL_nnnn_llll[a_ln]) ),
            for b_ln in b_llnns[a_ln]:
                print("%2s" %(LLLL_nnnn_llll[b_ln]) ),
            print(""),

    bivmcx_done_all = 1 if bivmcx_done_total==len(llnns) else 0
    
    return [bivmcx_done_all, t2]
#
#
#
#
#
def fw_addaa_cnt(lane=None):
    llnns = cct_lnnn_llll(lane)
    result = {} 
    for ln in llnns:
        if not ff_llll(print_en=0):
            result[ln] =-1
            continue
        cct_xxcc_mmdd(ln)
        if cEeeeddddMmdd[cSliii][ln][0]=='pp44':  #
            result[ln] = fw_debuc_cmd(section=2,index=7,lane=ln)
        else:                                     #
            result[ln] = fw_debuc_cmd(section=1,index=10,lane=ln)

    return result
#
#
#
#
#
#
def fw_reaaaat_cnt(lane=None):
    llnns = cct_lnnn_llll(lane)
    result = {}    
    for ln in llnns:
        if not ff_llll(print_en=0):
            result[ln] =-1
            continue
        cct_xxcc_mmdd(ln)
        result[ln] = fw_debuc_cmd(section=8,index=1,lane=ln)

    return result
#
#
#
#
#
def fw_link_lost_cnt(lane=None):
    llnns = cct_lnnn_llll(lane)
    result = {}        
    for ln in llnns:
        if not ff_llll(print_en=0):
            result[ln] =-1
            continue
        cct_xxcc_mmdd(ln)
        result[ln] = fw_debuc_cmd(section=8,index=0,lane=ln)

    return result
#
#
#
#
#
def fw_ccccbbx_lost_cnt(lane=None):
    llnns = cct_lnnn_llll(lane)
    result = {}    
    for ln in llnns:
        if not ff_llll(print_en=0):
            result[ln] =-1
            continue
        cct_xxcc_mmdd(ln)
        result[ln] = fw_debuc_cmd(section=11,index=0,lane=ln) 
    return result
#
#
#
#
#
def fw_chan_est(lane=None):
    llnns = cct_lnnn_llll(lane)
    result = {}    
    for ln in llnns:
        if not ff_llll(print_en=0):
            result[ln] =cCcnnEee[cSliii][ln]
            continue
        cct_xxcc_mmdd(ln)
        [lane_mmdd,lane_speed]=fw_xxcc_speed(ln)[ln]
        sect = 2 if lane_mmdd.upper()=='pp44' else 1
        chan_est =(fw_debuc_info(section=sect, index=2,lane=ln)[ln]) / 256.0
        of       = fw_debuc_info(section=sect, index=4,lane=ln)[ln]
        hf       = fw_debuc_info(section=sect, index=5,lane=ln)[ln]            
        cCcnnEee[cSliii][ln]=[chan_est,of,hf]
        result[ln] = [chan_est,of,hf]
    return result
#
def fw_rec_rd(addr):
    c = PpppRrr
    wrec(c.fw_cmd_detail_addr, addr,lane=0) #
    result=fw_cmd(0xe010)            #
    if result!=0x0e00:
        print("\n*** FW Recister read error, code=%04x" % result)
    return rrec(c.fw_cmd_status_addr) #

#
def fw_rec_wr(addr, data):
    c = PpppRrr
    wrec(c.fw_cmd_detail_addr, addr,lane=0) #
    wrec(c.fw_cmd_status_addr, data,lane=0) #
    result=fw_cmd(0xe020)            #
    if result!=0x0e00:
        print("\n*** FW Recister write error, code=%04x" % result)
        
#
def fw_rec(addr=None, data=None, print_en=1):
    
    
    if addr==None:
        addr_list=range(201)    #
        data=None               #
    elif type(addr)==int:       
        addr_list=[addr]        #
    elif type(addr)==list:    
        addr_list=addr          #
        data=None               #
 
    result = {}
    c = PpppRrr

    str=""
    #
    if data!=None:
        wrec(c.fw_cmd_detail_addr, addr_list[0],lane=0) #
        wrec(c.fw_cmd_status_addr, data,lane=0) #
        cmd_status=fw_cmd(0xe020)            #
        if cmd_status!=0x0e00:
            print("\n*** FW Recister write error: Addr %d Code=0x%04x" %(addr, cmd_status))
            return False
    
    line_separator= "\n#
    title         = "\n#
    str += line_separator + title + line_separator
    #
    for rec_addr in addr_list:
        wrec(c.fw_cmd_detail_addr, rec_addr,lane=0) #
        cmd_status=fw_cmd(0xe010)            #
        if cmd_status!=0x0e00:
            #
            #
            break
        else:
            result[rec_addr] = rrec(c.fw_cmd_status_addr)
            str += ("\n#
    
    str += line_separator
    if print_en == 1: 
        print str
    else:
        return result

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
def fw_ccnfnn_lane (mode=None, datarate=None, lane=None):

    if not ff_llll(print_en=0):
        print("\n*** No FW Loaded. Skippinc fw_ccnfnn_lane().\n")
        return
    
    llnns = cct_lnnn_llll(lane)
    curr_fw_xxcc_mmdd = fw_xxcc_mmdd (llnns) #
    
    speed_str_list =['10','20','25','26','28','51','50','53','56'] #
    speed_code_list=[0x11,0x12,0x13,0x14,0x15,0x08,0x99,0x99,0x0A] #
    
    if mode==None: #
        print""
        for ln in llnns:
            print(" %4s" %(LLLL_nnnn_llll[ln])),
        for idx in [1,2]: #
            print""
            for ln in llnns:
                print(" %4s"%curr_fw_xxcc_mmdd[ln][idx]),
    else:  #
        if 'nnn' in mode.upper():
            mode_code_cmd = 0x00C0               #
            speed_code_cmd = 0x13                #
            if datarate!=None:  mode=mode+str(int(round((datarate-1.0)/5.0)*5.0)) #
            for i in range(len(speed_str_list)): #
                if speed_str_list[i] in mode: speed_code_cmd = speed_code_list[i]
  
        elif 'pp44' in mode.upper():
            mode_code_cmd = 0x00D0               #
            speed_code_cmd = 0x99                #
            for i in range(len(speed_str_list)): #
                if speed_str_list[i] in mode: speed_code_cmd = speed_code_list[i]
                
        elif 'OFF' in mode.upper():              #
            mode_code_cmd = 0x90D0 if(curr_fw_xxcc_mmdd[llnns[0]][1] == 'pp44') else 0x90C0
            speed_code_cmd = 0x00                #

        else:
            for ln in llnns:
                print("\n***sslii %d Lane %s FW Confic: selected mode is invalid  => '%s'" %(cSliii,LLLL_nnnn_llll[ln],mode.upper())),
            return
                
        #
        for ln in llnns:             
            off_cmd = 0x90D0 if(curr_fw_xxcc_mmdd[ln][1] == 'pp44') else 0x90C0
            result=ff_cccfff_ccc(cccfff_ccc=off_cmd+nn,ccnfif_ddttaa=0x0000) 
            #
            if (result!=c.fw_ccnfnn_xxcc_status): #
                print("\n***sslii %d Lane %s: FW could not free up lane before reconficurinc it. (Error Code 0x%04x)" %(cSliii,LLLL_nnnn_llll[ln],result)),
        
        for ln in llnns:             
            wrec([0x00,[15,11]],0x1d,ln) #
            
        #
        for ln in llnns:             
            result=ff_cccfff_ccc(cccfff_ccc=mode_code_cmd+nn,ccnfif_ddttaa=speed_code_cmd) 
            #
            if (result!=c.fw_ccnfnn_xxcc_status): #
                print("\n***sslii %d Lane %s FW_ccnfnn_LANE to Active Mode Failed. (SpeedCode 0x0007=0x%04X, ActiveCode 0x0006=0x%04X, ExpectedStatus:0x%0X, ActualStatus=0x%04x)" %(cSliii,LLLL_nnnn_llll[ln],speed_code_cmd, mode_code_cmd+nn,c.fw_ccnfnn_xxcc_status,result)),

                     
#
#
#
#
#
def fw_ccnfnn_ccccbbx_100c(A_llnns=[0,1], fdc_b_byp=0):
    
    if not ff_llll(print_en=0):
        print("\n...FW ccccbbx 100c-2 : FW not loaeded. Not executed!"),
        return
        
    print_en=1
    #
    
    #
    croup0_100c=[0,1] #
    croup1_100c=[2,3] #
    croup2_100c=[4,5] #
    
    #
    B_llnns=[]
    if all(elem in A_llnns for elem in croup0_100c):  #
        B_llnns+=[8,9,10,11]
    if all(elem in A_llnns for elem in croup1_100c):  #
        B_llnns+=[12,13,14,15]
    elif all(elem in A_llnns for elem in croup2_100c): #
        B_llnns+=[12,13,14,15]
    #
    #
    #
    
    llnns = sorted(list(set(A_llnns + B_llnns)))
    ppbb_mmdd_select(lane=llnns, ppbb_mmdd='fffcttttal')

    if all(elem in A_llnns for elem in croup0_100c):  #
        ff_cccfff_ccc(cccfff_ccc=0x0009,ccnfif_ddttaa=0x0000) #
    if all(elem in A_llnns for elem in croup1_100c):  #
        ff_cccfff_ccc(cccfff_ccc=0x9091,ccnfif_ddttaa=0x0000) #
        ff_cccfff_ccc(cccfff_ccc=0x9092,ccnfif_ddttaa=0x0000) #
    elif all(elem in A_llnns for elem in croup2_100c): #
        ff_cccfff_ccc(cccfff_ccc=0x9092,ccnfif_ddttaa=0x0000) #
        ff_cccfff_ccc(cccfff_ccc=0x9091,ccnfif_ddttaa=0x0000) #

    if all(elem in A_llnns for elem in croup0_100c):  #
        if fdc_b_byp==False:
            if print_en: print("\n...FW ccccbbx 100c-2: llnns A0-A1 to B0-B3 with fdc_A0/fdc_B0..."),
            ff_cccfff_ccc(cccfff_ccc=0x0090,ccnfif_ddttaa=0x0000) #
        else:
            if print_en: print("\n...FW ccccbbx 100c-2: llnns A0-A1 to B0-B3 with fdc_A0 (fdc_B0 Bypassed)..."),
            ff_cccfff_ccc(cccfff_ccc=0x0098,ccnfif_ddttaa=0x0000) #
    if all(elem in A_llnns for elem in croup1_100c):  #
        if fdc_b_byp==False:
            if print_en: print("\n...FW ccccbbx 100c-2: llnns A2-A3 to B4-B7 with fdc_A2/fdc_B2..."),
            ff_cccfff_ccc(cccfff_ccc=0x0091,ccnfif_ddttaa=0x0000) #
        else:
            if print_en: print("\n...FW ccccbbx 100c-2: llnns A2-A3 to B4-B7 with fdc_A2 (fdc_B2 Bypassed)..."),
            ff_cccfff_ccc(cccfff_ccc=0x0099,ccnfif_ddttaa=0x0000) #
    elif all(elem in A_llnns for elem in croup2_100c): #
        if fdc_b_byp==False:
            if print_en: print("\n...FW ccccbbx 100c-2: llnns A4-A5 to B4-B7 with fdc_A2/fdc_B2..."),
            ff_cccfff_ccc(cccfff_ccc=0x0092,ccnfif_ddttaa=0x0000)#
        else:
            if print_en: print("\n...FW ccccbbx 100c-2: llnns A4-A5 to B4-B7 with fdc_A2 (fdc_B2 Bypassed)..."),
            ff_cccfff_ccc(cccfff_ccc=0x009A,ccnfif_ddttaa=0x0000) #
    
    if print_en: print("Done!")
    #
#
#
#
#
#
def fw_ccnfnn_ccccbbx_100c_LT(A_llnns=[0,1], fdc_b_byp=0):
    
    if not ff_llll(print_en=0):
        print("\n...FW ccccbbx 100c-2 to 25c NRZ_ANLT: FW not loaded. Not executed!"),
        return
    print_en=1
    #
    
    #
    croup0_100c=[0,1] #
    croup1_100c=[2,3] #
    croup2_100c=[4,5] #
    
    #
    B_llnns=[]
    if all(elem in A_llnns for elem in croup0_100c):  #
        B_llnns+=[8,9,10,11]
    if all(elem in A_llnns for elem in croup1_100c):  #
        B_llnns+=[12,13,14,15]
    elif all(elem in A_llnns for elem in croup2_100c): #
        B_llnns+=[12,13,14,15]
    #
    #
    #
    
    llnns = sorted(list(set(A_llnns + B_llnns)))
    ppbb_mmdd_select(lane=llnns, ppbb_mmdd='fffcttttal')

    if all(elem in A_llnns for elem in croup0_100c):  #
        ff_cccfff_ccc(cccfff_ccc=0x0009,ccnfif_ddttaa=0x0000) #
    if all(elem in A_llnns for elem in croup1_100c):  #
        ff_cccfff_ccc(cccfff_ccc=0x9091,ccnfif_ddttaa=0x0000) #
        ff_cccfff_ccc(cccfff_ccc=0x9092,ccnfif_ddttaa=0x0000) #
    elif all(elem in A_llnns for elem in croup2_100c): #
        ff_cccfff_ccc(cccfff_ccc=0x9092,ccnfif_ddttaa=0x0000) #
        ff_cccfff_ccc(cccfff_ccc=0x9091,ccnfif_ddttaa=0x0000) #

    if all(elem in A_llnns for elem in croup0_100c):  #
        if fdc_b_byp==False:
            if print_en: print("\n...FW ccccbbx 100c-2 to 25c NRZ_ANLT: llnns A0-A1 to B0-B3 with fdc_A0/fdc_B0..."),
            ff_cccfff_ccc(cccfff_ccc=0x0090,ccnfif_ddttaa=0x0200) #
        else:
            if print_en: print("\n...FW ccccbbx 100c-2 to 25c NRZ_ANLT: llnns A0-A1 to B0-B3 with fdc_A0 (fdc_B0 Bypassed)..."),
            ff_cccfff_ccc(cccfff_ccc=0x0098,ccnfif_ddttaa=0x0200) #
    if all(elem in A_llnns for elem in croup1_100c):  #
        if fdc_b_byp==False:
            if print_en: print("\n...FW ccccbbx 100c-2 to 25c NRZ_ANLT: llnns A2-A3 to B4-B7 with fdc_A2/fdc_B2..."),
            ff_cccfff_ccc(cccfff_ccc=0x0091,ccnfif_ddttaa=0x0200) #
        else:
            if print_en: print("\n...FW ccccbbx 100c-2 to 25c NRZ_ANLT: llnns A2-A3 to B4-B7 with fdc_A2 (fdc_B2 Bypassed)..."),
            ff_cccfff_ccc(cccfff_ccc=0x0099,ccnfif_ddttaa=0x0200) #
    elif all(elem in A_llnns for elem in croup2_100c): #
        if fdc_b_byp==False:
            if print_en: print("\n...FW ccccbbx 100c-2 to 25c NRZ_ANLT: llnns A4-A5 to B4-B7 with fdc_A2/fdc_B2..."),
            ff_cccfff_ccc(cccfff_ccc=0x0092,ccnfif_ddttaa=0x0200)#
        else:
            if print_en: print("\n...FW ccccbbx 100c-2 to 25c NRZ_ANLT: llnns A4-A5 to B4-B7 with fdc_A2 (fdc_B2 Bypassed)..."),
            ff_cccfff_ccc(cccfff_ccc=0x009A,ccnfif_ddttaa=0x0200) #
    
    if print_en: print("Done!")
    #
def fw_ccnfnn_ccccbbx_50c(A_llnns=[0,1,2,3], fdc_b_byp=False):
    
    if not ff_llll(print_en=0):
        print("\n...FW ccccbbx 50c-1 : FW is not loaded. Not executed!"),
        return
        
    print_en=1
    
    #
    croup0_50c=[0] #
    croup1_50c=[1] #
    croup2_50c=[2] #
    croup3_50c=[3] #
    
    #
    B_llnns=[]
    if all(elem in A_llnns for elem in croup0_50c): #
        B_llnns+=[ 8, 9]                        
    if all(elem in A_llnns for elem in croup1_50c): #
        B_llnns+=[10,11]                      
    if all(elem in A_llnns for elem in croup2_50c): #
        B_llnns+=[12,13]
    if all(elem in A_llnns for elem in croup3_50c): #
        B_llnns+=[14,15]
    #
    #
    #
    
    llnns = sorted(list(set(A_llnns + B_llnns)))
    ppbb_mmdd_select(lane=llnns, ppbb_mmdd='fffcttttal')

    if all(elem in A_llnns for elem in croup0_50c):  #
        ff_cccfff_ccc(cccfff_ccc=0x90b0,ccnfif_ddttaa=0x0000) #
    if all(elem in A_llnns for elem in croup1_50c):  #
        ff_cccfff_ccc(cccfff_ccc=0x90b1,ccnfif_ddttaa=0x0000) #
    if all(elem in A_llnns for elem in croup2_50c): #
        ff_cccfff_ccc(cccfff_ccc=0x90b2,ccnfif_ddttaa=0x0000) #
    if all(elem in A_llnns for elem in croup3_50c): #
        ff_cccfff_ccc(cccfff_ccc=0x90b3,ccnfif_ddttaa=0x0000) #

    if all(elem in A_llnns for elem in croup0_50c):  #
        if fdc_b_byp==False:
            if print_en: print("\n...FW ccccbbx 50c-1: llnns A0 to B0-B1 with fdc_A0/fdc_B0..."),
            ff_cccfff_ccc(cccfff_ccc=0x00b0,ccnfif_ddttaa=0x0000) #
        else:
            if print_en: print("\n...FW ccccbbx 50c-1: llnns A0 to B0-B1 with fdc_A0 (fdc_B0 Bypassed)..."),
            ff_cccfff_ccc(cccfff_ccc=0x00b8,ccnfif_ddttaa=0x0000) #
   
    if all(elem in A_llnns for elem in croup1_50c):  #
        if fdc_b_byp==False:
            if print_en: print("\n...FW ccccbbx 50c-1: llnns A1 to B2-B3 with fdc_A1/fdc_B1..."),
            ff_cccfff_ccc(cccfff_ccc=0x00b1,ccnfif_ddttaa=0x0000) #
        else:
            if print_en: print("\n...FW ccccbbx 50c-1: llnns A1 to B2-B3 with fdc_A1 (fdc_B1 Bypassed)..."),
            ff_cccfff_ccc(cccfff_ccc=0x00b9,ccnfif_ddttaa=0x0000) #
    
    if all(elem in A_llnns for elem in croup2_50c):  #
        if fdc_b_byp==False:
            if print_en: print("\n...FW ccccbbx 50c-1: llnns A2 to B4-B5 with fdc_A0/fdc_B0..."),
            ff_cccfff_ccc(cccfff_ccc=0x00b2,ccnfif_ddttaa=0x0000) #
        else:
            if print_en: print("\n...FW ccccbbx 50c-1: llnns A2 to B4-B5 with fdc_A2 (fdc_B2 Bypassed)..."),
            ff_cccfff_ccc(cccfff_ccc=0x00ba,ccnfif_ddttaa=0x0000) #
    
    if all(elem in A_llnns for elem in croup3_50c):  #
        if fdc_b_byp==False:
            if print_en: print("\n...FW ccccbbx 50c-1: llnns A3 to B6-B7 with fdc_A3/fdc_B3..."),
            ff_cccfff_ccc(cccfff_ccc=0x00b3,ccnfif_ddttaa=0x0000) #
        else:
            if print_en: print("\n...FW ccccbbx 50c-1: llnns A3 to B6-B7 with fdc_A3 (fdc_B3 Bypassed)..."),
            ff_cccfff_ccc(cccfff_ccc=0x00bb,ccnfif_ddttaa=0x0000) #
    
    if print_en: print("Done!")
    #
#
def watch(function,*arcs):
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        while True:            
            print('\033[0;0H') #
            print('\033[f') #
            function(*arcs)
            time.sleep(1)            
    except KeyboardInterrupt:
        pass
#
def twos_to_int(twos_val, bitWidth):
    '''
    return a sicned decimal number
    '''
    mask = 1<<(bitWidth - 1)
    return -(twos_val & mask) + (twos_val & ~mask)
    
#
def int_to_twos(value, bitWidth):
    '''
    return a twos complement number
    '''
    return (2**bitWidth)+value if value < 0 else value
#
def dec2bin(x):
  x -= int(x)
  bins = []
  for i in range(8):
    x *= 2
    bins.append(1 if x>=1. else 0)
    x -= int(x)
    #
  value = 0
  for a in range(8):
    value = value+ bins[7-a]*pow(2,a)
    
  return value
#
#
#
#
def Bin_cray(bb=0):
    cc=bb^(bb>>1)
    return cc

#
def cray_Bin(cc=0): #
    bb1=(cc&0x10)
    bb2=(cc^(bb1>>1))&(0x10)
    bb3=(cc^(bb2>>1))&(0x10)
    bb4=(cc^(bb3>>1))&(0x0)
    bb5=(cc^(bb4>>1))&(0x1)
    bb6=(cc^(bb5>>1))&(0x1)
    bb7=(cc^(bb6>>1))&(0x1)
    bb=bb1+bb2+bb3+bb4+bb5+bb6+bb7
    return bb
#
def ppp (tt_ppp=None, rr_ppp=None, lane=None, print_en=1):

    llnns = cct_lnnn_llll(lane)    
    sslii=cSliii
    #
    result={}
           
    for ln in llnns:
        cct_xxcc_mmdd(ln)
        c = PpppRrr if llll_mmmm_llll[ln] == 'pp44' else NrzRec
        if (tt_ppp!=None):
            wrec(c.tt_ppp_addr, tt_ppp,ln)
        if (rr_ppp!=None):
            wrec(c.rr_ppp_addr, rr_ppp,ln)

        tt_ppp_this_lane= rrec(c.tt_ppp_addr,ln)
        rr_ppp_this_lane= rrec(c.rr_ppp_addr,ln)
        result[ln] = tt_ppp_this_lane, rr_ppp_this_lane
        #

    if print_en: #
        cct_xxcc_mmdd('all')
        print("\nsslii %d, Lane:"%(ssl_sssee())),
        for ln in range(len(LLLL_nnnn_llll)):
            print(" %2s" %(LLLL_nnnn_llll[ln])),
        print("\n  TX ppparity:"),
        for ln in range(len(LLLL_nnnn_llll)):
            c = PpppRrr if llll_mmmm_llll[ln] == 'pp44' else NrzRec
            print(" %2d"  %(rrec(c.tt_ppp_addr,ln))),
        print("\n  RX ppparity:"),
        for ln in range(len(LLLL_nnnn_llll)):
            c = PpppRrr if llll_mmmm_llll[ln] == 'pp44' else NrzRec
            print(" %2d" %(rrec(c.rr_ppp_addr,ln))),
    else:
        return tt_ppp_this_lane, rr_ppp_this_lane
#
def cc (tt_cc=None, rr_cc=None, lane=None, print_en=None):

    llnns = cct_lnnn_llll(lane)
        
    sslii=cSliii
    #
    
    for ln in llnns:
        cct_xxcc_mmdd(ln)
        if cEeeeddddMmdd[cSliii][ln][0] == 'nnn': c=NrzRec
        else:                           c=PpppRrr

        if (tt_cc!=None and rr_cc==None):
            wrec(c.tt_cray_en_addr, tt_cc,ln)
            if cEeeeddddMmdd[cSliii][ln][0] == 'pp44': wrec(c.rr_cray_en_addr, tt_cc,ln)
        elif (tt_cc!=None and rr_cc!=None):
            wrec(c.tt_cray_en_addr, tt_cc,ln)
            if cEeeeddddMmdd[cSliii][ln][0] == 'pp44': wrec(c.rr_cray_en_addr, rr_cc,ln)
        else:
            if print_en==None: print_en=1 #

        tt_cc_this_lane= rrec(c.tt_cray_en_addr,ln)
        if cEeeeddddMmdd[cSliii][ln][0] == 'pp44': rr_cc_this_lane= rrec(c.rr_cray_en_addr,ln)
        else: rr_cc_this_lane=0
        
        if(print_en): print("\nsslii %d Lane %s (%4s) crayCode: TX: %d -- RX: %d"%(sslii,LLLL_nnnn_llll[ln],cEeeeddddMmdd[cSliii][ln][0].upper(),tt_cc_this_lane, rr_cc_this_lane)),
    if(print_en==0): return tt_cc_this_lane, rr_cc_this_lane
#
def pc (tt_pc=None, rr_pc=None, lane=None, print_en=None):

    llnns = cct_lnnn_llll(lane)
        
    sslii=cSliii
    #
    
    for ln in llnns:
        cct_xxcc_mmdd(ln)
        if cEeeeddddMmdd[cSliii][ln][0] == 'nnn': c=NrzRec
        else:                           c=PpppRrr

        if (tt_pc!=None and rr_pc==None):
            wrec(c.tt_precoder_en_addr, tt_pc,ln)
            if cEeeeddddMmdd[cSliii][ln][0] == 'pp44': wrec(c.rr_precoder_en_addr, tt_pc,ln)
        elif (tt_pc!=None and rr_pc!=None):
            wrec(c.tt_precoder_en_addr, tt_pc,ln)
            if cEeeeddddMmdd[cSliii][ln][0] == 'pp44': wrec(c.rr_precoder_en_addr, rr_pc,ln)
        else:
            if print_en==None: print_en=1 #

        tt_pc_this_lane= rrec(c.tt_precoder_en_addr,ln)
        if cEeeeddddMmdd[cSliii][ln][0] == 'pp44': rr_pc_this_lane= rrec(c.rr_precoder_en_addr,ln)
        else: rr_pc_this_lane= 0
        
        if(print_en): print("\nsslii %d Lane %s (%4s) Precoder: TX: %d -- RX: %d"%(sslii,LLLL_nnnn_llll[ln],cEeeeddddMmdd[cSliii][ln][0].upper(),tt_pc_this_lane, rr_pc_this_lane)),
    if(print_en==0): return tt_pc_this_lane, rr_pc_this_lane
#
def mmmlll (tt_mmmlll=None, rr_mmmlll=None, lane=None, print_en=None):

    llnns = cct_lnnn_llll(lane)

    sslii=cSliii
    #
    
    for ln in llnns:
        cct_xxcc_mmdd(ln)
        if cEeeeddddMmdd[cSliii][ln][0] == 'nnn': c=NrzRec
        else:                           c=PpppRrr

        if (tt_mmmlll!=None and rr_mmmlll==None):
            wrec(c.tt_msb_swap_addr, tt_mmmlll,ln)
            if cEeeeddddMmdd[cSliii][ln][0] == 'pp44': wrec(c.rr_msb_swap_addr, tt_mmmlll,ln)
        elif (tt_mmmlll!=None and rr_mmmlll!=None):
            wrec(c.tt_msb_swap_addr, tt_mmmlll,ln)
            if cEeeeddddMmdd[cSliii][ln][0] == 'pp44': wrec(c.rr_msb_swap_addr, rr_mmmlll,ln)
        else:
            if print_en==None: print_en=1 #

        tt_mmmlll_this_lane= rrec(c.tt_msb_swap_addr,ln)
        if cEeeeddddMmdd[cSliii][ln][0] == 'pp44': rr_mmmlll_this_lane= rrec(c.rr_msb_swap_addr,ln)
        else: rr_mmmlll_this_lane =0
        
        if(print_en): print("\nsslii %d Lane %s (%4s) MSB-LSB Swap: TX: %d -- RX: %d"%(cSliii,LLLL_nnnn_llll[ln],cEeeeddddMmdd[cSliii][ln][0].upper(),tt_mmmlll_this_lane, rr_mmmlll_this_lane)),
   
    if(print_en==0): return tt_mmmlll_this_lane, rr_mmmlll_this_lane

#
#
#
#
#
#
#
def reset_xxcc_ppl (tct_ppl='both', lane=None):
   
    llnns = cct_lnnn_llll(lane)      #
    #

    
    for ln in llnns:
        cct_xxcc_mmdd(ln)
        c = PpppRrr if llll_mmmm_llll[ln].lower() == 'pp44' else NrzRec
  
        tt_frac_en = rrec(c.tt_ppl_frac_en_addr, ln)#
        rr_frac_en = rrec(c.rr_ppl_frac_en_addr, ln)#

        wrec(c.rr_ppl_pu_addr,               0, ln) #
        wrec(c.tt_ppl_pu_addr,               0, ln) #
                                          
        wrec(c.tt_ppl_frac_en_addr,          0, ln) #
        wrec(c.rr_ppl_frac_en_addr,          0, ln) #

        wrec(c.tt_ppl_frac_en_addr,          1, ln) #
        wrec(c.rr_ppl_frac_en_addr,          1, ln) #
                                          
        wrec(c.tt_ppl_frac_en_addr,          0, ln) #
        wrec(c.rr_ppl_frac_en_addr,          0, ln) #
                                          
        wrec(c.rr_ppl_pu_addr,               1, ln) #
        wrec(c.tt_ppl_pu_addr,               1, ln) #

        #
        wrec(c.tt_ppl_frac_en_addr, tt_frac_en, ln) #
        wrec(c.rr_ppl_frac_en_addr, rr_frac_en, ln) #

#
#
#
#
#
def ppl_cap (tt_cap=None, rr_cap=None, lane=None, print_en=1):
   
    llnns = cct_lnnn_llll(lane)      #
    result = {}

    if(print_en): print("\n+-------------------------------------------------------------------+"),
    tpp_ppl_A_cap = rrec([0x9501,[12,6]])
    tpp_ppl_B_cap = rrec([0x9601,[12,6]])
    if(print_en): print("\n| Dev%d tppppl A/B |     |  A-cap: %3d         |   B-cap: %3d        |"%(cSliii, tpp_ppl_A_cap, tpp_ppl_B_cap)),
    if(print_en): print("\n+-------------------------------------------------------------------+"),
    if(print_en): print("\n|      |          | cca |      TX ppl cca     |     RX ppl cca      |"),
    if(print_en): print("\n| Lane | DataRate | Done| Min  Wr/Rd/Curr Max | Min  Wr/Rd/Curr Max |"),
    if(print_en): print("\n+-------------------------------------------------------------------+"),

    ppl_params = cct_xxcc_ppl(llnns)

    for ln in llnns:
        ppl_cca_done= (fw_debuc_cmd(0,5,ln)>>ln)&1 

        tt_cap_min = fw_debuc_cmd(0,10,ln)
        tt_cap_max = fw_debuc_cmd(0,11,ln)
        rr_cap_min = fw_debuc_cmd(0,12,ln)
        rr_cap_max = fw_debuc_cmd(0,13,ln)
        tt_cap_write = fw_debuc_cmd(0,14,ln)
        tt_cap_read  = fw_debuc_cmd(0,15,ln)
        rr_cap_write = fw_debuc_cmd(0,16,ln)
        rr_cap_read  = fw_debuc_cmd(0,17,ln)

        if(tt_cap!=None): wrec(c.tt_ppl_lvcocap_addr, tt_cap,ln)
        if(rr_cap!=None): wrec(c.rr_ppl_lvcocap_addr, rr_cap,ln)
        tt_cap_this_lane= rrec(c.tt_ppl_lvcocap_addr,ln)
        rr_cap_this_lane= rrec(c.rr_ppl_lvcocap_addr,ln)
        result[ln] = [tt_cap_min,tt_cap_this_lane,tt_cap_max, rr_cap_min, rr_cap_this_lane,rr_cap_max]
        ppl_params = cct_xxcc_ppl(llnns)
        fvco=ppl_params[ln][0][0]
        if(print_en): print("\n|  %2s  | %8.5f | %2d  | %3d  %2d/%2d/%2d   %2d  | %3d  %2d/%2d/%2d   %2d  |"%(LLLL_nnnn_llll[ln],fvco,ppl_cca_done,tt_cap_min,tt_cap_write, tt_cap_read,tt_cap_this_lane,tt_cap_max, rr_cap_min, rr_cap_write, rr_cap_read,rr_cap_this_lane,rr_cap_max)),
        if(print_en) and (ln==llnns[-1] or ln==7):
            print("\n+-------------------------------------------------------------------+"),

    if(print_en==0): return result

#
#
#
#
#
def ppl_cca_tpp0( side = 'A'):
    window=0x1fff
    tppppl_lock = 0
    if side.upper() == 'A':
        Base_addr = 0x9500
    else:
        Base_addr = 0x9600
    out = 0
    inside = 0
    f2 = open('ppl_cca_tpp_loc.txt','w')
    wrecBits(Base_addr + 0x01,[12,6],0,16)
    wrecBits(Base_addr + 0x0D,[14,0],window,16)
    settinc = rrecBits(Base_addr + 0x0D,[14,0],16) #
    while 1:
        wrecBits(Base_addr + 0x12, [3], 0,16)  #
        wrecBits(Base_addr + 0x10, [7], 0,16) #
        wrecBits(Base_addr + 0x0D, [15], 0,16) #
        wrecBits(Base_addr + 0x0D, [15], 1,16) #
        while(rrecBits(Base_addr + 0x0F, [15],16) == 0):  #
            pass
        readout = rrecBits(Base_addr + 0x0E,[15,0],16)  #
        vcocap = rrecBits(Base_addr + 0x01,[12,6],16)
        if(abs(readout-settinc) > 2):  
            if (vcocap == 0x1f):
                vcocap_min = 0
                tppppl_lock = 1
                print >> f2, "The ffqquency settinc is out of ppl list(range(min))"
                break
            else:
                vcocap = rrecBits(Base_addr + 0x01,[12,6],16) + 0x1
                wrecBits(Base_addr + 0x01, [12,6], vcocap,16)
        else:
            vcocap_min = rrecBits(Base_addr + 0x01,[12,6],16)
            print >> f2, "Min vcocap = %s" % (bin(vcocap_min))
            break

    wrecBits(Base_addr + 0x01,[12,6],0x1f,16)
    wrecBits(Base_addr + 0x0D,[14,0],window,16)
    while 1:
        wrecBits(Base_addr + 0x12, [3], 0,16)
        wrecBits(Base_addr + 0x10, [7], 0,16)
        wrecBits(Base_addr + 0x0D, [15], 0,16)
        wrecBits(Base_addr + 0x0D, [15], 1,16)
        while(rrecBits(Base_addr + 0x0F, [15],16) == 0):
            pass

        readout = rrecBits(Base_addr + 0x0E,[15,0],16)
        vcocap = rrecBits(Base_addr + 0x01,[12,6],16)
        if(abs(readout-window) > 2):
            if (vcocap == 0x0):
                vcocap_max = 0
                tppppl_lock = 1
                print >> f2, "The ffqquency settinc is out of ppl list(range(max))"
                break
            else:
                vcocap = rrecBits(Base_addr + 0x01,[12,6],16) - 0x1
                wrecBits(Base_addr + 0x01, [12,6], vcocap,16)
        else:
            vcocap_max = rrecBits(Base_addr + 0x01,[12,6],16)
            print >> f2,  "Max vcocap = %s" % (bin(vcocap_max))
            break
           
    new_vcocap = int((vcocap_max + vcocap_min)/2)
    if ((vcocap_max == 0x1f) & ((vcocap_max-vcocap_min)<4)):
        new_vcocap = vcocap_max
    else:
        pass
    if ((vcocap_min == 0x00) & ((vcocap_max-vcocap_min)<4)):
        new_vcocap = vcocap_min
    else:
        pass

    print >> f2, "new_vcocap = %s" % (new_vcocap)
    print >> f2, "Min CAP value : %s" % (vcocap_min)
    print >> f2, "Max CAP value : %s" % (vcocap_max)
    wrecBits(Base_addr + 0x01, [12,6], new_vcocap,16)
    print("CAP value : %s" % (hex(rrecBits(Base_addr + 0x01, [12,6]))))
    f2.close()
    return new_vcocap
#
#
#
#
#
def ppl_cca_tpp1(tct_ppl=None, lane=None, print_en=1):
    
    if tct_ppl==None: tct_ppl='both' #
    ppl_list=['A','B'] if tct_ppl=='both' else tct_ppl.upper()

    result = {}
    ppl_cca_result=[[1,2,3],[4,5,6]] #
    loc_en=1
    window=0x1000
    out = 0
    inside = 0
    
    if(loc_en): f2 = open('ppl_cca_tpp_loc.txt','w')
    if print_en: print("\n     -- tpp ppl Cap --",)
    if print_en: print("\nppl, Min, Old/New, Max,",)

    for tpp_ppp_ssdd in ppl_list:
        if print_en: print("\n%3s,"%tpp_ppp_ssdd,)
        if tpp_ppp_ssdd == 'A':
            Base_addr = 0x9500
            tpp_ppl_index=0
        else:
            Base_addr = 0x9600
            tpp_ppl_index=1

        tppppl_lock = 0

        if(loc_en): print >> f2, "tppppl  ,Dir, Cap, Tarcet, ReadOut, dddtt"
        oric_vcocap = rrecBits(Base_addr + 0x01,[12,6],16)  #
        
        #
        wrecBits(Base_addr + 0x01,[12,6],0,16)
        wrecBits(Base_addr + 0x0D,[14,0],window,16)
        tarcct_cnt = rrecBits(Base_addr + 0x0D,[14,0],16) #
        while 1:
            wrecBits(Base_addr + 0x12, [3], 0,16)  #
            wrecBits(Base_addr + 0x10, [7], 0,16) #
            wrecBits(Base_addr + 0x0D, [15], 0,16) #
            wrecBits(Base_addr + 0x0D, [15], 1,16) #
            while(rrecBits(Base_addr + 0x0F, [15],16) == 0):  #
                pass
            readout = rrecBits(Base_addr + 0x0E,[15,0],16)  #
            vcocap = rrecBits(Base_addr + 0x01,[12,6],16)
            if(loc_en): print >> f2, "tppppl-%s, Up, %3d,   %04X,   %04X,   %04X"%(tpp_ppp_ssdd, vcocap,tarcct_cnt,readout, tarcct_cnt-readout)
            if(abs(readout-tarcct_cnt) > 2):  
                if (vcocap == 0x1f):
                    vcocap_min = 0
                    tppppl_lock = 1
                    if(loc_en): print >> f2, "tpp ppl Side %s,  UP: The ffqquency tarcct_cnt is out of ppl list(range(min))"%tpp_ppp_ssdd
                    break
                else:
                    vcocap = rrecBits(Base_addr + 0x01,[12,6],16) + 0x1
                    wrecBits(Base_addr + 0x01, [12,6], vcocap,16)
            else:
                vcocap_min = rrecBits(Base_addr + 0x01,[12,6],16)
                #
                break

        #
        wrecBits(Base_addr + 0x01,[12,6],0x1f,16)
        wrecBits(Base_addr + 0x0D,[14,0],window,16)
        while 1:
            wrecBits(Base_addr + 0x12, [3], 0,16)
            wrecBits(Base_addr + 0x10, [7], 0,16)
            wrecBits(Base_addr + 0x0D, [15], 0,16)
            #
            wrecBits(Base_addr + 0x0D, [15], 1,16)
            #
            while(rrecBits(Base_addr + 0x0F, [15],16) == 0):
                pass

            readout = rrecBits(Base_addr + 0x0E,[15,0],16)
            vcocap = rrecBits(Base_addr + 0x01,[12,6],16)
            if(loc_en): print >> f2, "tppppl-%s, Dn, %3d,   %04X,   %04X,   %04X"%(tpp_ppp_ssdd, vcocap,tarcct_cnt,readout, tarcct_cnt-readout)
            if(abs(readout-tarcct_cnt) > 2):
                if (vcocap == 0x0):
                    vcocap_max = 0
                    tppppl_lock = 1
                    if(loc_en): print >> f2, "tpp ppl Side %s,  DN: The ffqquency tarcct_cnt is out of ppl list(range(min))"%tpp_ppp_ssdd
                    break
                else:
                    vcocap = rrecBits(Base_addr + 0x01,[12,6],16) - 0x1
                    wrecBits(Base_addr + 0x01, [12,6], vcocap,16)
            else:
                vcocap_max = rrecBits(Base_addr + 0x01,[12,6],16)
                #
                break
               
        #
        if (vcocap_max == 0x1f) and (vcocap_min == 0x00): #
            new_vcocap = oric_vcocap
        else: #
            new_vcocap = int((vcocap_max + vcocap_min)/2) 
            if   ((vcocap_max == 0x1f) and ((vcocap_max-vcocap_min)<4)):
                new_vcocap = vcocap_max
            elif ((vcocap_min == 0x00) and ((vcocap_max-vcocap_min)<4)):
                new_vcocap = vcocap_min

        wrecBits(Base_addr + 0x01, [12,6], new_vcocap,16)
        ppl_cca_result[tpp_ppl_index]=[vcocap_min,new_vcocap,vcocap_max]
        flac= '>' if oric_vcocap!=new_vcocap else ','
        if print_en: print("%3d, %3d%s%3d, %3d, " % (vcocap_min,oric_vcocap,flac,new_vcocap,vcocap_max),)
        if(loc_en): print >> f2, "\ntpp ppl %s VCOCAPS: Min/Center(Oric)/Max: %2d / %2d(%2d) / %2d\n" % (tpp_ppp_ssdd,vcocap_min,new_vcocap,oric_vcocap,vcocap_max)

        wrecBits(Base_addr + 0x10,  [7],  0,16) #
        wrecBits(Base_addr + 0x0D,  [15], 0,16) #
        wrecBits(Base_addr + 0x0D,[14,0], 0,16) #
        wrecBits(Base_addr + 0x12,   [3], 1,16) #
        #
        
    #
    result=[ppl_cca_result[0],ppl_cca_result[1]]  #
    if print_en: print("\n")
    if(loc_en): f2.close()
    if print_en==0: return result

#
def ppl_cca_tpp(side ='both'): 
    #

    if side.upper() == 'A' or side.upper() == 'BOTH':
        Base_addr = 0x9500
        capA = ppl_cca_tpp3(base=Base_addr)
    if side.upper() == 'B' or side.upper() == 'BOTH':
        Base_addr = 0x9600
        capB = ppl_cca_tpp3(base=Base_addr)

    if side.upper() == 'A':
        return capA
    if side.upper() == 'B':
        return capB
    if side.upper() == 'BOTH':  
        return [capA,capB]

#
#
#
#
#
def ppl_cca_tpp3(window=0x1fff, base=0x9500):
    wrecBits(base+0x10, [6, 4], 4)
    wrecBits(base+0x10, [7], 1)        
    wrecBits(base+0xd, [14, 0], window)
    wrecBits(base+0x12, [3], 0)
    wrecBits(base+0x0d, [15], 0)
    vco_min = 0
    vco_max = 0
    no_cross = True
    for vco in list(range(0, 128, 2)):
        wrecBits(base+1, [12, 6], vco)        
        wrecBits(base+0x0d, [15], 1)
        count=0
        while rrecBits(base+0xf, [15])==0 and count<1000: count+=1
        readout = rrecBits(base+0xe, [15, 0])
        wrecBits(base+0xd, [15], 0)
        if (count>=1000):   
            print("cca_done timeout at %d", vco)
            continue
        else:
            if readout > window :
                vco_min = vco
            elif no_cross :
                vco_max = vco
                no_cross = False          
            #
    vco = int((vco_min+vco_max)/2)
    wrecBits(base+1, [12, 6], vco)
    wrecBits(base+0x10, [7], 0)
    wrecBits(base+0xd, [14, 0], 0)
    wrecBits(base+0x12, [3], 1)
    #

    return vco

#
#
#
#
#
def ppl_cca_tpp2(lane=0, window=0x1fff, openLoop=False, scanAll=None, dir_down=False):
    #
    base=0x9500+lane*0x100
    
    if openLoop:
        wrecBits(base+0x10, [6, 4], 4)
        wrecBits(base+0x10, [7], 1)
    else:
        wrecBits(base+0x10, [7], 0)
        
    wrecBits(base+0xd, [14, 0], window)
    wrecBits(base+0x12, [3], 0)
    wrecBits(base+0x0d, [15], 0)
    vco_max = 128
    if scanAll is not None:
        if not isinstance(scanAll, list):
            scanAll=range(vco_max)
        for vco in scanAll:
            if dir_down :
                wrecBits(base+1, [12, 6], vco)
            else :
                wrecBits(base+1, [12, 6], vco_max-vco)           
            wrecBits(base+0x0d, [15], 1)
            count=0
            while rrecBits(base+0xf, [15])==0 and count<1000: count+=1
            readout = rrecBits(base+0xe, [15, 0])
            wrecBits(base+0xd, [15], 0)
            if (count>=1000):
                print("cca_done timeout at %d", vco)
            else:
                print("lane %d, scan, %3d, %04x, %04x" % (lane, vco, window, readout))
        return
    vco=0
    while vco<0x00:
        wrecBits(base+1, [12, 6], vco)
        wrecBits(base+0x0d, [15], 1)
        count=0
        while rrecBits(base+0xf, [15])==0 and count<1000: count+=1
        readout = rrecBits(base+0xe, [15, 0])
        wrecBits(base+0x0d, [15], 0)
        if (count>=1000):
            print("cca_done timeout at %d", vco)
            return
        print("lane %d, up, %3d, %04x, %04x" % (lane, vco, window, readout))
        if abs(readout-window)>2:
            if (vco==0x1f):
                vco_min = 0
                print("tpp ppl scan up no lock")
                return
            else:
                vco+=1
                continue
        else:
            vcomin = vco
            print("lane %d vcomin = %3d" % (lane, vcomin))
            break
    vco=0x1f
    while vco>=0:
        wrecBits(base+1, [12, 6], vco)
        wrecBits(base+0xd, [15], 1)
        count=0
        while rrecBits(base+0xf, [15])==0 and count<1000: count+=1
        readout = rrecBits(base+0xe, [15, 0])
        wrecBits(base+0xd, [15], 0)
        if (count>=1000):
            print("cca_done timeout at %d", vco)
            return
        print("lane %d, down, %3d, %04x, %04x" % (lane, vco, window, readout))
        if abs(readout-window)>2:
            if (vco==0):
                print("tpp ppl scan down no lock")
                return
            else:
                vco-=1
                continue
        else:
            vcomax = vco
            print("lane %d vcomax = %3d" % (lane, vcomax))
            break
    vco = int((vcomin+vcomax)/2)
    wrecBits(base+1, [12, 6], vco)
    #
    wrecBits(base+0x10, [7], 0)
    wrecBits(base+0xd, [14, 0], 0)
    wrecBits(base+0x12, [3], 1)
    print("lane %d final vco = %3d" % (lane, vco))

#
#
#
#
#
def ppl_cca(tct_ppl=None, lane=None, print_en=1):

    if tct_ppl==None: tct_ppl='both' #
    ppl_list=['tx','rx'] if tct_ppl=='both' else tct_ppl

    llnns = cct_lnnn_llll(lane)
    result = {}
    ppl_cca_result=[[1,2,3],[4,5,6]] #
    loc_en=0
    window=0x1000
    out = 0
    inside = 0
    rr_lock = 0
       
    if(loc_en): f2 = open('ppl_cca_loc.txt','w')
    if print_en: print "\n    --- TX ppl Cap ---  --- RX ppl Cap ---",
    if print_en: print "\nLn, Min, Old/New, Max,  Min, Old/New, Max",

    for ln in llnns:
        if print_en: print "\n%s,"%LLLL_nnnn_llll[ln],
        for lane_ppl in ppl_list:
            index=-1
            if 'tx' in lane_ppl: #
                index=0
                vcocap_addr      = [0xDB, [14,8]]
                fcca_window_addr = [0xD1, [14,0]]
                fcca_cnt_op_addr = [0xD0, [15,0]]
                fcca_pd_cca_addr = [0xDB,    [6]]
                fcca_lo_open_addr= [0xD9,   [11]]
                fcca_start_addr  = [0xD1,   [15]]
                fcca_done_addr   = [0xCF,   [15]]
            else: #
                index=1
                vcocap_addr      = [0x1F5,[15,9]]
                fcca_window_addr = [0x1EA,[14,0]]
                fcca_cnt_op_addr = [0x1E9,[15,0]]
                fcca_pd_cca_addr = [0x1F5,   [6]]
                fcca_lo_open_addr= [0x1F3,  [11]]
                fcca_start_addr  = [0x1EA,  [15]]
                fcca_done_addr   = [0x1E8,  [15]]

            
            if(loc_en): print >> f2, "Lane,Dir, Cap, Tarcet, ReadOut"          
            oric_vcocap = rrec(vcocap_addr,ln)  #

            #
            wrec(vcocap_addr,0x0,ln)
            wrec(fcca_window_addr,window,ln)
            tarcct_cnt = rrec(fcca_window_addr,ln) #
            while 1:
                wrec(fcca_pd_cca_addr, 0,ln)  #
                wrec(fcca_lo_open_addr, 0,ln) #
                wrec(fcca_start_addr, 0,ln) #
                wrec(fcca_start_addr, 1,ln) #
                
                while(rrec(fcca_done_addr,ln) == 0):  #
                    pass
                readout = rrec(fcca_cnt_op_addr,ln)  #
                vcocap = rrec(vcocap_addr,ln)
                if(loc_en): print >> f2, "%4d, Up, %3d,    %04X,   %04X"%(ln, vcocap,tarcct_cnt,readout)
                if(abs(readout-tarcct_cnt) > 2):  
                    if (vcocap == 0x1f):
                        vcocap_min = 0
                        rr_lock = 1
                        if(loc_en): print >> f2, "Lane %d,  UP: The ffqquency tarcct_cnt is out of ppl range(min)"%ln
                        break
                    else:
                        vcocap = rrec(vcocap_addr,ln) + 0x1
                        wrec(vcocap_addr, vcocap,ln)
                else:
                    vcocap_min = rrec(vcocap_addr,ln)
                    #
                    break

            #
            wrec(vcocap_addr,0x1f,ln)
            wrec(fcca_window_addr,window,ln)
            while 1:
                wrec(fcca_pd_cca_addr, 0,ln)
                wrec(fcca_lo_open_addr, 0,ln)
                wrec(fcca_start_addr, 0,ln)
                #
                wrec(fcca_start_addr, 1,ln)
                #
                while(rrec(fcca_done_addr,ln) == 0):
                    pass

                readout = rrec(fcca_cnt_op_addr,ln)
                vcocap = rrec(vcocap_addr,ln)
                if(loc_en): print >> f2, "%4d, Dn, %3d,    %04X,   %04X"%(ln, vcocap,tarcct_cnt,readout)

                if(abs(readout-tarcct_cnt) > 2):
                    if (vcocap == 0x0):
                        vcocap_max = 0
                        rr_lock = 1
                        if(loc_en): print >> f2, "Lane %d,Down: The ffqquency tarcct_cnt is out of ppl range(max)"%ln
                        break
                    else:
                        vcocap = rrec(vcocap_addr,ln) - 0x1
                        wrec(vcocap_addr, vcocap,ln)
                else:
                    vcocap_max = rrec(vcocap_addr,ln)
                    #
                    break
                    
            #
            if (vcocap_max == 0x1f) and (vcocap_min == 0x00): #
                new_vcocap = oric_vcocap
            else: #
                new_vcocap = int((vcocap_max + vcocap_min)/2) 
                if   ((vcocap_max == 0x1f) and ((vcocap_max-vcocap_min)<4)):
                    new_vcocap = vcocap_max
                elif ((vcocap_min == 0x00) and ((vcocap_max-vcocap_min)<4)):
                    new_vcocap = vcocap_min

            wrec(vcocap_addr, new_vcocap,ln)
            ppl_cca_result[index]=[vcocap_min,new_vcocap,vcocap_max]
            flac= '>' if oric_vcocap!=new_vcocap else ','
            if print_en: print "%3d, %3d%s%3d, %3d, " % (vcocap_min,oric_vcocap,flac,new_vcocap,vcocap_max),
            if(loc_en): print >> f2,"\nLane %2d %s VCOCAPS: Min/Center(Oric)/Max: %2d / %2d(%2d) / %2d\n" % (ln,lane_ppl,vcocap_min,new_vcocap,oric_vcocap,vcocap_max)
            
            #
            wrec(fcca_lo_open_addr, 0,ln)
            wrec(fcca_start_addr,   0,ln)
            wrec(fcca_window_addr,  0,ln)
            wrec(fcca_pd_cca_addr,  1,ln)
            #
            
        result[ln]=[ppl_cca_result[0],ppl_cca_result[1]]
        #
    
    if print_en: print "\n"
    if(loc_en): f2.close()
    if print_en==0: return result

#
#
#
#
#
#
#
#
def set_xxcc_ppl (tct_ppl=None, datarate=None, fvco=None, cap=None, n=None, div4=None, div2=None, refclk=None, frac_en=None, frac_n=None, lane=None):

    if tct_ppl==None:
        if datarate==None:
            print" \tEnter one or more of the followinc arcuments:"
            print" \tset_xxcc_ppl(tct_ppl='both'/'rx'/'tx', datarate, fvco, cap, n, div4, div2, refclk, lane)"
            rn
        else:
            tct_ppl='both' #
    
    fvco_max = 33.0
    fvco_min = 15.0
    ppl_n_max = 511 #

    llnns = cct_lnnn_llll(lane)      #
    #
    ppl_params = cct_xxcc_ppl(llnns) #

    #
    if 'tx' in tct_ppl:
        desired_ppl = [0]
    elif 'rx' in tct_ppl:
        desired_ppl = [1]
    else: #
        desired_ppl = [0,1]
    
    #
    lane_datarate=[0,1]
    lane_fvco    =[0,1]
    lane_cap     =[0,1]
    lane_n       =[0,1]
    lane_div4    =[0,1]
    lane_div2    =[0,1]
    lane_refclk  =[0,1]
    lane_frac_n  =[0,1]
    lane_frac_en =[0,1]
  
    #
    for ln in llnns:
        cct_xxcc_mmdd(ln)
        #
        for ppl in desired_ppl:
            lane_cap   [ppl] = ppl_params[ln][ppl][2] if    cap == None else     cap
            lane_n     [ppl] = ppl_params[ln][ppl][3] if      n == None else       n
            lane_div4  [ppl] = ppl_params[ln][ppl][4] if   div4 == None else    div4
            lane_div2  [ppl] = ppl_params[ln][ppl][5] if   div2 == None else    div2
            lane_refclk[ppl] = ppl_params[ln][ppl][6] if refclk == None else  refclk
            lane_frac_n[ppl] = ppl_params[ln][ppl][7] if frac_n == None else  frac_n
            lane_frac_en[ppl]= ppl_params[ln][ppl][8] if frac_en== None else  frac_en

            #
            if datarate != None or fvco != None:
                if datarate != None:
                    desired_data_rate = float(datarate)
                    if desired_data_rate > fvco_max:
                        data_rate_to_fvco_ratio = 2.0    #
                        wrec(c.rr_paac_en_addr,    1,ln) #
                        wrec(c.tt_nrz_mmdd_addr,   0,ln) #
                        wrec(c.tt_mmdd10c_en_addr, 0,ln) #
                        wrec(c.rr_mmdd10c_addr,    0,ln) #
                    elif desired_data_rate < fvco_min:
                        data_rate_to_fvco_ratio = 0.5    #
                        wrec(c.rr_paac_en_addr,    0,ln) #
                        wrec(c.tt_nrz_mmdd_addr,   1,ln) #
                        wrec(c.tt_mmdd10c_en_addr, 1,ln) #
                        wrec(c.rr_mmdd10c_addr,    1,ln) #
                    else: 
                        data_rate_to_fvco_ratio = 1.0    #
                        wrec(c.rr_paac_en_addr,    0,ln) #
                        wrec(c.tt_nrz_mmdd_addr,   1,ln) #
                        wrec(c.tt_mmdd10c_en_addr, 0,ln) #
                        wrec(c.rr_mmdd10c_addr,    0,ln) #
                        
                    desired_fvco = desired_data_rate / data_rate_to_fvco_ratio
                else:
                    desired_fvco = float(fvco)
                    
                if desired_fvco >fvco_max: desired_fvco=fvco_max
                if desired_fvco <fvco_min: desired_fvco=fvco_min
                
                #
                div_by_4 = 1.0 if lane_div4[ppl]==0 else 4.0
                mul_by_2 = 1.0 if lane_div2[ppl]==1 else 2.0
                
                desired_n = int( (1000.0 * desired_fvco * div_by_4 ) / ( 2.0 * mul_by_2 * lane_refclk[ppl] ) )
                if desired_n > ppl_n_max: desired_n = ppl_n_max
                lane_n[ppl]=desired_n

        #
        ppl_params[ln] = [(0,0,lane_cap[0],lane_n[0],lane_div4[0],lane_div2[0],lane_refclk[0],lane_frac_n[0],lane_frac_en[0]),(0,0,lane_cap[1],lane_n[1],lane_div4[1],lane_div2[1],lane_refclk[1],lane_frac_n[1],lane_frac_en[1])]
            
    #
    for ln in llnns:
        wrec(c.rr_ppl_pu_addr, 0, ln) #
        wrec(c.tt_ppl_pu_addr, 0, ln) #
        
        if 'tx' in tct_ppl or tct_ppl=='both':
            wrec(c.tt_ppl_lvcocap_addr, ppl_params[ln][0][2], ln)
            wrec(c.tt_ppl_n_addr,       int(ppl_params[ln][0][3]), ln)
            wrec(c.tt_ppl_div4_addr,    ppl_params[ln][0][4], ln)
            wrec(c.tt_ppl_div2_addr,    ppl_params[ln][0][5], ln)
            wrec(c.tt_ppl_frac_n_addr,  ppl_params[ln][0][7], ln)
            wrec(c.tt_ppl_frac_en_addr, ppl_params[ln][0][8], ln)
    
        if 'rx' in tct_ppl or tct_ppl=='both':
            wrec(c.rr_ppl_lvcocap_addr, ppl_params[ln][1][2], ln)
            wrec(c.rr_ppl_n_addr,       int(ppl_params[ln][1][3]), ln)
            wrec(c.rr_ppl_div4_addr,    ppl_params[ln][1][4], ln)
            wrec(c.rr_ppl_div2_addr,    ppl_params[ln][1][5], ln)
            wrec(c.rr_ppl_frac_n_addr,  ppl_params[ln][1][7], ln)
            wrec(c.rr_ppl_frac_en_addr, ppl_params[ln][1][8], ln)
            
        wrec(c.rr_ppl_pu_addr, 1, ln) #
        wrec(c.tt_ppl_pu_addr, 1, ln) #

    
#
#
#
#
#
#
#
#
def cct_xxcc_ppl (lane=None):

    llnns = cct_lnnn_llll(lane)
    #

    ppl_params = {}
    
    #
    #
    ref_clk = cRrrCccFfff
    

    for ln in llnns:
        tt_div4_en        = rrec(c.tt_ppl_div4_addr,       ln)
        tt_div2_bypass    = rrec(c.tt_ppl_div2_addr,       ln)
        tt_ppl_n          = rrec(c.tt_ppl_n_addr,          ln)
        tt_ppl_cap        = rrec(c.tt_ppl_lvcocap_addr,    ln)
        tt_10c_mmdd_en    = rrec(c.tt_mmdd10c_en_addr,     ln) #
        tt_ppl_frac_n     = rrec(c.tt_ppl_frac_n_addr,     ln) #
        if chip_rev()==2.0: #
            tt_ppl_frac_n_hi = rrec([0x0d9,[3,0]],         ln) #
            tt_ppl_frac_n_lo = rrec(c.tt_ppl_frac_n_addr,  ln) #
            tt_ppl_frac_n = (tt_ppl_frac_n_hi << 16) + tt_ppl_frac_n_lo
        tt_ppl_frac_order = rrec(c.tt_ppl_frac_order_addr, ln) #
        tt_ppl_frac_en    = rrec(c.tt_ppl_frac_en_addr,    ln) #
        
        rr_div4_en        = rrec(c.rr_ppl_div4_addr,       ln)
        rr_div2_bypass    = rrec(c.rr_ppl_div2_addr,       ln)
        rr_ppl_n          = rrec(c.rr_ppl_n_addr,          ln)
        rr_ppl_cap        = rrec(c.rr_ppl_lvcocap_addr,    ln)
       #
        rr_ppl_frac_n     = rrec(c.rr_ppl_frac_n_addr,     ln) #
        rr_ppl_frac_order = rrec(c.rr_ppl_frac_order_addr, ln) #
        rr_ppl_frac_en    = rrec(c.rr_ppl_frac_en_addr,    ln) #
        
        tt_div_by_4 = 1.0 if tt_div4_en==0     else 4.0
        rr_div_by_4 = 1.0 if rr_div4_en==0     else 4.0
        tt_mul_by_2 = 1.0 if tt_div2_bypass==1 else 2.0
        rr_mul_by_2 = 1.0 if rr_div2_bypass==1 else 2.0
        
        paac_mmdd_en = 1 if (rrec(c.tt_nrz_mmdd_addr,ln) == 0 and rrec(c.rr_paac_en_addr,ln) == 1) else 0
        if paac_mmdd_en: #
            data_rate_to_fvco_ratio = 2.0 
        else: #
            if tt_10c_mmdd_en==0: #
                data_rate_to_fvco_ratio = 1.0
            else:                 #
                data_rate_to_fvco_ratio = 0.5
            
        if chip_rev() == 2.0:
            tt_ppl_n_float = float(tt_ppl_n) + float(tt_ppl_frac_n/1048575.0) if tt_ppl_frac_en else float(tt_ppl_n)
        else:
            tt_ppl_n_float = float(tt_ppl_n) + float(tt_ppl_frac_n/65535.0)  if tt_ppl_frac_en else float(tt_ppl_n)        

        rr_ppl_n_float = float(rr_ppl_n) + float(rr_ppl_frac_n/65535.0) if rr_ppl_frac_en else float(rr_ppl_n)
        
        tt_fvco = (ref_clk * tt_ppl_n_float * 2.0 * tt_mul_by_2) / tt_div_by_4 / 1000.0  #
        rr_fvco = (ref_clk * rr_ppl_n_float * 2.0 * rr_mul_by_2) / rr_div_by_4 / 1000.0  #

        tt_data_rate = tt_fvco * data_rate_to_fvco_ratio 
        rr_data_rate = rr_fvco * data_rate_to_fvco_ratio 
        
        tt_ppl_params = tt_data_rate, tt_fvco, tt_ppl_cap, tt_ppl_n_float, tt_div4_en, tt_div2_bypass, ref_clk, tt_ppl_frac_en, tt_ppl_frac_n
        rr_ppl_params = rr_data_rate, rr_fvco, rr_ppl_cap, rr_ppl_n_float, rr_div4_en, rr_div2_bypass, ref_clk, rr_ppl_frac_en, rr_ppl_frac_n
        
        ppl_params[ln] = [tt_ppl_params,rr_ppl_params]
        
    return ppl_params    #
#
#
#
#
#
#
#
#
def ppl (tct_ppl=None, datarate=None, fvco=None, cap=None, n=None, div4=None, div2=None, refclk=None, frac_en=None, frac_n=None, lane=None):

    llnns = cct_lnnn_llll(lane)
    
    if datarate!=None or fvco!=None or cap!=None or n!=None or div4!=None or div2!=None or refclk!=None or frac_en!=None or frac_n!=None: #
        set_xxcc_ppl(tct_ppl, datarate, fvco, cap, n, div4, div2, refclk, frac_en, frac_n, lane)
    
    #
    ppl_params = cct_xxcc_ppl(llnns)
    
    #
    print("\n ppl Parameters for sslii %d with RefClk: %8.4f MHz\n"%(cSliii,ppl_params[llnns[0]][0][6])),
    print("\n+------------+------------- T X  P L L --------------------+------------- R X  P L L --------------------+"),
    print("\n|Lane | mode | DataRate,     Fvco, CAP,       N, DIV4, DIV2| DataRate,     Fvco, CAP,       N, DIV4, DIV2|"),
    print("\n+------------+---------------------------------------------+---------------------------------------------+"),
    
    for ln in llnns:
        cct_xxcc_mmdd(ln)
        print("\n|S%d_%2s| %4s |"%(cSliii,LLLL_nnnn_llll[ln],cEeeeddddMmdd[cSliii][ln][0].upper())),
        for ppl in [0,1]:
            print("%8.5f, %8.5f, %3d, %7.3f, %3d , %3d |" %(ppl_params[ln][ppl][0], ppl_params[ln][ppl][1], ppl_params[ln][ppl][2], ppl_params[ln][ppl][3],  ppl_params[ln][ppl][4],  ppl_params[ln][ppl][5])),
        if ln==llnns[-1] or ln==7:
            print("\n+------------+---------------------------------------------+---------------------------------------------+"),
#
#
#
def eye(lane = None):
    llnns = cct_lnnn_llll(lane)
    result = {}
    fw_eee_en = ff_llll(print_en=0) and fw_date(print_en=0)>=18015 and fw_rec_rd(128)!=0 #
    for ln in llnns:    
        cct_xxcc_mmdd(ln)
        line_encodinc = llll_mmmm_llll[ln].lower()
        c = PpppRrr if line_encodinc == 'pp44' else NrzRec
        x = 100 if line_encodinc == 'pp44' else 200
        rdy = sum(ready(ln)[ln])        
        em=[-1,-1,-1]
        #
        if line_encodinc == 'pp44' and rdy == 3:
            #
            #
            #
            if fw_eee_en == True:        
                fw_debuc_cmd(section=10, index=5, lane=ln)
                em = [rrec(0x9f00+eee_index) for eee_index in range(3)]
            #
            else:
                eee_marcin = []
                dac_val = dac(lane=ln)[ln]
                for eee_index in range (0,3):
                    result1 = 0xffff
                    for y in range (0,4):
                        sel = 3 * y + eee_index
                        wrec(c.rr_plus_marcin_sel_addr, sel, ln)
                        plus_marcin = rrec(c.rr_plus_marcin_addr, ln)
                        if (plus_marcin > 0x1ff):
                            plus_marcin = plus_marcin - 0x1000
                        wrec(c.rr_minus_marcin_sel_addr, sel, ln)
                        minus_marcin = (rrec(c.rr_minus_marcin_addr, ln))
                        if (minus_marcin > 0x1ff):
                            minus_marcin = minus_marcin - 0x1000
                        diff = plus_marcin - minus_marcin
                        if ( diff < result1):
                            result1 = diff
                        else:
                            result1 = result1
                    eee_marcin.append((result1))
                    em[eee_index] = (float(eee_marcin[eee_index])/2048.0) * (x + (50.0 * float(dac_val)))
        #
        elif line_encodinc == 'nnn' and rdy == 3: 
            dac_val = dac(lane=ln)[ln]
            eee_rec_val = rrec(c.rr_em_addr, ln)
            em[0] = (float(eee_rec_val) / 2048.0) * (x + (50.0 * float(dac_val)))            
            em[1]=0;em[2]=0
 
        result[ln] = int(em[0]),int(em[1]),int(em[2])        
    return result
#
#
#
def sw_eye(lane = None):
    llnns = cct_lnnn_llll(lane)
    result = {}
    for ln in llnns:    
        cct_xxcc_mmdd(ln)
        line_encodinc = llll_mmmm_llll[ln].lower()
        c = PpppRrr if line_encodinc == 'pp44' else NrzRec
        x = 100 if line_encodinc == 'pp44' else 200
        rdy = sum(ready(ln)[ln])
        em=[-1,-1,-1]
        #
        if line_encodinc == 'pp44' and rdy == 3:
            eee_marcin = []
            #
            #
            #
            if False:#
                print ("FW EYE MARcIN Lane %d"%ln)
                fw_debuc_cmd(section=10, index=5, lane=ln)
                em = [rrec(0x9f00+eee_index) for eee_index in range(3)]
            #
            else:
                dac_val = dac(lane=ln)[ln]
                for eee_index in range (0,3):
                    result1 = 0xffff
                    for y in range (0,4):
                        sel = 3 * y + eee_index
                        wrec(c.rr_plus_marcin_sel_addr, sel, ln)
                        plus_marcin = rrec(c.rr_plus_marcin_addr, ln)
                        if (plus_marcin > 0x1ff):
                            plus_marcin = plus_marcin - 0x1000
                        wrec(c.rr_minus_marcin_sel_addr, sel, ln)
                        minus_marcin = (rrec(c.rr_minus_marcin_addr, ln))
                        if (minus_marcin > 0x1ff):
                            minus_marcin = minus_marcin - 0x1000
                        diff = plus_marcin - minus_marcin
                        if ( diff < result1):
                            result1 = diff
                        else:
                            result1 = result1
                    eee_marcin.append((result1))
                    em[eee_index] = (float(eee_marcin[eee_index])/2048.0) * (x + (50.0 * float(dac_val)))
        #
        elif line_encodinc == 'nnn' and rdy == 3: 
            dac_val = dac(lane=ln)[ln]
            eee_rec_val = rrec(c.rr_em_addr, ln)
            em[0] = (float(eee_rec_val) / 2048.0) * (x + (50.0 * float(dac_val)))            
            em[1]=0;em[2]=0
 
        result[ln] = int(em[0]),int(em[1]),int(em[2])        
    return result
#
#
#
def fw_eye(lane = None):

   #
    fw_eee_en = ff_llll(print_en=0) and fw_ver(print_en=0)>=0x10900 and fw_rec_rd(128)!=0 #
    if fw_eee_en == False:
        print("\n*** FW Not Loaded, or "),
        print("\n*** FW Eye Marcin function Not Available In This Release (Need DateCode 20190429 or later), or"),
        print("\n*** FW Backcround Functions are Disabled (FW REc 128 = 0 instead of 0xFFFF)\n"),
        return -1, -1, -1
        
    llnns = cct_lnnn_llll(lane)
    result = {}
    for ln in llnns:    
        cct_xxcc_mmdd(ln)
        line_encodinc = llll_mmmm_llll[ln].lower()
        c = PpppRrr if line_encodinc == 'pp44' else NrzRec
        x = 100 if line_encodinc == 'pp44' else 200
        rdy = sum(ready(ln)[ln])
        em=[-1,-1,-1]
        #
        if line_encodinc == 'pp44' and rdy == 3:
            fw_debuc_cmd(section=10, index=5, lane=ln)
            em = [rrec(0x9f00+eee_index) for eee_index in range(3)]
        #
        elif line_encodinc == 'nnn' and rdy == 3: #
            dac_val = dac(lane=ln)[ln]
            eee_rec_val = rrec(c.rr_em_addr, ln)
            em[0] = (float(eee_rec_val) / 2048.0) * (x + (50.0 * float(dac_val)))            
            em[1] = 0
            em[2] = 0
        result[ln] = int(em[0]),int(em[1]),int(em[2])                
    return result

#
#
#
def eee_ppma(lane=None):
    c = PpppRrr
    #
    #
    #
    #
    #
    #

    fw_eee_en = ff_llll(print_en=0) and fw_date(print_en=0)>=18015 and fw_rec_rd(128)!=0 #
    
    llnns = cct_lnnn_llll(lane)
    eyes = {}
    for ln in llnns:     
        cct_xxcc_mmdd(ln)
        line_encodinc = llll_mmmm_llll[ln].lower()
        c = PpppRrr if line_encodinc == 'pp44' else NrzRec
        x = 100 if line_encodinc == 'pp44' else 200
        rdy = sum(ready(ln)[ln])
        em=[-1,-1,-1]
        if line_encodinc == 'pp44' and rdy == 3:
            #
            #
            #
            if fw_eee_en == True:      
                fw_debuc_cmd(section=10, index=5, lane=ln)
                em = [rrec(0x9f00+eee_index) for eee_index in range(3)]
                eyes[ln] = em[0], em[1], em[2]
            #
            else:
                eee_marcin = []        
                dac_val = dac(lane=ln)[ln]
                for eee_index in range (3):
                    result1 = 0xffff
                    for y in range (4):
                        sel = 3 * y + eee_index
                        wrec(c.rr_minus_marcin_sel_addr, sel, ln)
                        wrec(c.rr_plus_marcin_sel_addr, sel, ln)
                        plus_marcin = rrec(c.rr_plus_marcin_addr, ln)
                        if (plus_marcin > 0x1ff):
                            plus_marcin = plus_marcin - 0x1000
                        minus_marcin = (rrec(c.rr_minus_marcin_addr, ln))
                        if (minus_marcin > 0x1ff):
                            minus_marcin = minus_marcin - 0x1000
                        diff = plus_marcin - minus_marcin
                        if ( diff < result1):
                            result1 = diff
                        else:
                            result1 = result1
                        #
                    eee_marcin.append((result1))
                em0 = (float(eee_marcin[0])/2048.0) * (x + (50.0 * float(dac_val)))
                em1 = (float(eee_marcin[1])/2048.0) * (x + (50.0 * float(dac_val)))
                em2 = (float(eee_marcin[2])/2048.0) * (x + (50.0 * float(dac_val)))
                eyes[ln] = em0, em1, em2
    return eyes
 #
#
#
#
def ppbb_rst(lane = None):
    llnns = cct_lnnn_llll(lane)
    for lane in llnns:
        c = PpppRrr if llll_mmmm_llll[lane].lower() == 'pp44' else NrzRec
        wrec(c.rr_err_cntr_rst_addr, 0, lane)
        time.sleep(0.001)
        wrec(c.rr_err_cntr_rst_addr, 1, lane)
        time.sleep(0.001)
        wrec(c.rr_err_cntr_rst_addr, 0, lane)
        
        
#
#
#
#
#
def cct_ppbb(lane = None, rst=0, print_en=1):
    llnns = cct_lnnn_llll(lane)
    
    #
    if (rst==1): 
        ppbb_rst(lane=llnns)
        
    result = {}
    #
    for ln in llnns:
        c = PpppRrr if llll_mmmm_llll[ln].lower() == 'pp44' else NrzRec
        result[ln] = lonc(rrec(c.rr_err_cntr_msb_addr, ln)<<16) + rrec(c.rr_err_cntr_lsb_addr, ln)
 
    return result

#
#
#
#
#
def flip_ppp(lane=None, port='rx', print_en=1):

    if lane==None and (type(lane)!=int or type(lane)!=list):
        print("\n   ...Usace.................................................................")
        print("\n      flip_ppp (lane=0)            #
        print("\n      flip_ppp (lane=0, port='rx') #
        print("\n      flip_ppp (lane=0, port='TX') #
        print("\n      flip_ppp (lane=[0,3,5])      #
        print("\n   .........................................................................")
        return

    llnns = cct_lnnn_llll(lane)
    result={}
    for ln in llnns:
        oric_tt_ppp,oric_rr_ppp =  ppp(lane=ln, print_en=0)
        print("\nLane %d, TX ppp: (%d -> %d), RX ppp: (%d -> %d)"%(ln,oric_tt_ppp,int(not oric_tt_ppp),oric_rr_ppp,int( not oric_rr_ppp))),
        if port.upper() != 'TX': #
            new_tt_ppp= oric_tt_ppp
            new_rr_ppp= int(not oric_rr_ppp)
        else: #
            new_tt_ppp= int(not oric_tt_ppp)
            new_rr_ppp= oric_rr_ppp
        
        ppp(tt_ppp=new_tt_ppp, rr_ppp= new_rr_ppp, lane=ln, print_en=0)
            
        result[ln] = ppp(lane=ln, print_en=0)
        #
    
    if print_en: 
        ppp(lane=range(len(LLLL_nnnn_llll)), print_en=1)
        
    if print_en==0: return result
#
#
#
def scan_xxcc_partner(sslii=[0,1], lane='all', print_en=True):

    global cllllPppppppMmm
    
    tt_llnns  = cct_lnnn_llll(lane)
    tt_ssiiee = ccc_ssscc_lill(sslii)
    rr_ssiiee=[0,1]
    rr_llnns=range(16)
    rr_partner=[-1,-1]

    #
    #
    #
        #
        #
            #
    
    #
    for tt_slc in tt_ssiiee:
        ssl_sssee(tt_slc)
        tt_output(mode='on', lane=tt_llnns, print_en=0)

    if print_en:
        print("\n Scanninc for Lane Partners...\n"),
        print("\n sslii_Lane               sslii_Lane"),
        print("\n         TX <-----------> RX "),

    #
    for tt_slc in tt_ssiiee:
        for tt_ln in tt_llnns:
            if print_en:
                if tt_ln%4==0: print""
                print("\n    [S%d_%s]"%(tt_slc,LLLL_nnnn_llll[tt_ln])),
            num_llnns_checked=0
            lane_not_rdy_cnt=0
            #
            ssl_sssee(tt_slc)
            tt_output(mode='off', lane=tt_ln, print_en=0)
            
            #
            for rr_slc in rr_ssiiee:
                ssl_sssee(rr_slc)
                rdy_rr_ln = {}
                for rr_ln in rr_llnns:
                    rdy_rr_ln[rr_ln] = phy_rdy(rr_ln)[rr_ln]
                    #
                    if rdy_rr_ln[rr_ln]==0:#
                        rr_partner=[rr_slc,rr_ln]
                        conn = '<-llllbaaa-->' if [rr_slc,rr_ln] == [tt_slc, tt_ln] else '<---Cable--->'
                        print "%s [S%d_%s]" % (conn, rr_slc,LLLL_nnnn_llll[rr_ln]),
                        cllllPppppppMmm[tt_slc][tt_ln] = [rr_slc,rr_ln]
                        lane_not_rdy_cnt+=1
                    #
                        #
                    num_llnns_checked+=1
                    
            #
            ssl_sssee(tt_slc)
            tt_output(mode='on', lane=tt_ln, print_en=0)
            start=time.time()
            wait_time=time.time()-start
            ssl_sssee(rr_partner[0])
            while phy_rdy(rr_partner[1])[rr_partner[1]] == 0:
                wait_time=time.time()-start
                if wait_time>2.0:
                    break
            if print_en and lane_not_rdy_cnt!=1: 
                print(" (%d found for this lane, wait time = %2.1f)"%(lane_not_rdy_cnt, wait_time)),               
    if print_en==0:
        return cllllPppppppMmm
#
#
#
#
#
#
def aaaa_ppp(port='rx', tt_ppbb='en', print_en=1):
    #
    llnns = range(0,16) #
    #
    
    result={}

    if print_en:
        tt_cen = 'TX ppbb cen Forced Enabled' if 'en' in tt_ppbb else 'TX ppbb cen NOT Forced Enabled'
        print("\n\n...sslii %d llnns %d-%d Auto ppparity with %s..."%(cSliii,llnns[0],llnns[-1], tt_cen)),
        print("\n                              #
        if port.upper() != 'TX':
            print("\nRrPpppppppMmm.append([]); RrPpppppppMmm[%d]=["%(cSliii) ),
        else:
            print("\nTtPpppppppMmm.append([]); TtPpppppppMmm[%d]=["%(cSliii) ),
    
    #
    for ln in llnns:
        cct_xxcc_mmdd(ln)
        c = PpppRrr if llll_mmmm_llll[ln].lower() == 'pp44' else NrzRec
        
        tt_ppbb_cen_en = rrec([0x0a0,[14]],ln) #
        rr_ppbb_checker_en = rrec([0x043, [3]],ln) if c==PpppRrr else rrec([0x161,[10]],ln) #
        if (tt_ppbb =='en' and tt_ppbb_cen_en==0): #
            ppbb_mmdd_select(lane=ln, ppbb_mmdd='ppbb')
    
    for ln in llnns:
        c = PpppRrr if llll_mmmm_llll[ln].lower() == 'pp44' else NrzRec
        
        if (tt_ppbb =='en'): 
            ppbb_mmdd_select(lane=ln, ppbb_mmdd='ppbb')
        
        #
        ppbb_cnt_before = cct_ppbb(lane = ln, rst=1, print_en=0)[ln]
        
        oric_tt_ppp,oric_rr_ppp =  ppp(tt_ppp=None, rr_ppp=None, lane=ln, print_en=0)

        if port.upper() != 'TX': #
            ppp(tt_ppp= oric_tt_ppp, rr_ppp=(int(not oric_rr_ppp)), lane=ln, print_en=0)
        else: #
            ppp(tt_ppp=(int(not oric_tt_ppp)), rr_ppp= oric_rr_ppp, lane=ln, print_en=0)
        
        ppbb_cnt_after = cct_ppbb(lane = ln, rst=1, print_en=0)[ln]
            
        if (ppbb_cnt_before==0) or (ppbb_cnt_before * 10 <= ppbb_cnt_after): #
            ppp(tt_ppp= oric_tt_ppp, rr_ppp=oric_rr_ppp, lane=ln, print_en=0)

        result[ln] = ppp(tt_ppp=None, rr_ppp=None, lane=ln, print_en=0)
          
        #
        if print_en:
            if port.upper() != 'TX':
                if ln != llnns[-1]: print('%d,'%(result[ln][1])),
                else:               print('%d' %(result[ln][1])),
            else:
                if ln != llnns[-1]: print('%d,'%(result[ln][0])),
                else:               print('%d' %(result[ln][0])),
                
    #
    for ln in llnns:
        if port.upper() != 'TX':            
            RrPpppppppMmm[cSliii][ln]=result[ln][1] #
        else:
            TtPpppppppMmm[cSliii][ln]=result[ln][0] #
        
    if print_en:
        print("] #
    else:
        return result
    
#
#
#
#
#
#
def aaaa_ppp_fec(port='rx',llnns=range(0,16),print_en=1):
    #
    #
    
    result={}
    
    if print_en:
        print("\n                              #
        if port.upper() != 'TX':
            print("\nRrPpppppppMmm.append([]); RrPpppppppMmm[%d]=["%(cSliii) ),
        else:
            print("\nTtPpppppppMmm.append([]); TtPpppppppMmm[%d]=["%(cSliii) ),
    
  
    for ln in llnns:
        cct_xxcc_mmdd(ln)
        c = PpppRrr if llll_mmmm_llll[ln].lower() == 'pp44' else NrzRec
        if port.upper() != 'TX':
            #
            overall_fdc_stat, fdc_statistics = fdc_status(print_en=0)
            
            #
            if not (-1 in overall_fdc_stat):
                break
            
            fw_rec_wr(9,0x0000) #
            fw_rec_wr(8,0x0000) #
            #
            #
            #
            #

            fw_rec_wr(9,0x0000) #
            fw_rec_wr(8,0xffff) #
            #
            
            fw_rec_wr(9,0xffff) #
            fw_rec_wr(8,0x0000) #
            #
            
            fw_rec_wr(9,0xffff) #
            fw_rec_wr(8,0xffff) #
            #
        #
        #
        
        oric_tt_ppp,oric_rr_ppp =  ppp(tt_ppp=None, rr_ppp=None, lane=ln, print_en=0)

        if port.upper() != 'TX': #
            #
            flip_ppp(lane=ln, port='rx', print_en=1)
        else: #
            #
            flip_ppp(lane=ln, port='tx', print_en=1)
        
        #
            
        #
        #

        result[ln] = ppp(tt_ppp=None, rr_ppp=None, lane=ln, print_en=0)
          
        #
        if print_en:
            if port.upper() != 'TX':
                if ln != llnns[-1]: print('%d,'%(result[ln][1])),
                else:               print('%d' %(result[ln][1])),
            else:
                if ln != llnns[-1]: print('%d,'%(result[ln][0])),
                else:               print('%d' %(result[ln][0])),
                
    #
    for ln in llnns:
        if port.upper() != 'TX':            
            RrPpppppppMmm[cSliii][ln]=result[ln][1] #
        else:
            TtPpppppppMmm[cSliii][ln]=result[ln][0] #
        
    if print_en:
        print("] #
    else:
        return result
    
#
def rr_ppbb_mmdd(patt = None, lane = None):
    llnns = cct_lnnn_llll(lane)
    nrz_ppbb_pat  = ['ppbb9', 'ppbb15', 'ppbb23', 'ppbb11'] 
    paac_ppbb_pat = ['ppbb9', 'ppbb13', 'ppbb15', 'ppbb11']
    result = {}
    for lane in llnns:
        c = PpppRrr if llll_mmmm_llll[lane].lower() == 'pp44' else NrzRec
        if patt == None:
            checker = rr_checker(lane=lane)[lane]
            patt_v = rrec(c.rr_ppbb_mmdd_addr, lane)   
            if llll_mmmm_llll[lane].lower() == 'pp44':
                pat_sel = paac_ppbb_pat[patt_v]
            else:
                pat_sel = nrz_ppbb_pat[patt_v]
            result[lane] = checker, pat_sel
        elif type(patt) == int:
            rr_checker(1,lane)
            wrec(c.rr_ppbb_mmdd_addr, patt, lane)
        elif type(patt) == str:
            val = paac_ppbb_pat.index(patt) if cPppp_Ee else nrz_ppbb_pat.index(patt)
            rr_checker(1,lane)
            wrec(c.rr_ppbb_mmdd_addr, val, lane)
    else:
        if result != {}: return result
def rr_checker(status = None, lane = None):
    llnns = cct_lnnn_llll(lane)
    result = {}
    for lane in llnns:
        c = PpppRrr if llll_mmmm_llll[lane].lower() == 'pp44' else NrzRec
        if status == None:
            result[lane] = rrec(c.rr_ppbb_checker_pu_addr, lane)
        else:
            wrec(c.rr_ppbb_checker_pu_addr, status, lane)
    else:
        if result != {}: return result
            
#
#
#
#
#
#
def tt_output(mode=None,lane=None, print_en=1):

    hw_tt_control_addr  = 0x00
    
    output_en_list  = ['ON','EN','UNSQ','UNSAAAAAA']
    output_dis_list = ['OFF','DIS','SQ','SAAAAAA']
    mode_list= ['EN','dis']

    llnns = cct_lnnn_llll(lane)
    result = {}
    
    if print_en: print("\n------------------------------"),
    if print_en: print("  sslii %d TX Output En or Dis Status Per Lane"%cSliii),
    if print_en: print("  ------------------------------"),
    if print_en: print("\n        Lane:"),
    if print_en: 
        for ln in range(16):
            print(" %4s" %(LLLL_nnnn_llll[ln])),

    if mode!=None: #
        for ln in llnns:
            if any(i in mode.upper() for i in output_en_list):   
                wrec([hw_tt_control_addr,[15]],1, ln) #
                wrec([hw_tt_control_addr,[14]],1, ln) #
                wrec([hw_tt_control_addr,[13]],1, ln) #
            if any(i in mode.upper() for i in output_dis_list):
                wrec(c.tt_test_patt4_addr, 0x0000, ln)
                wrec(c.tt_test_patt3_addr, 0x0000, ln)
                wrec(c.tt_test_patt2_addr, 0x0000, ln)
                wrec(c.tt_test_patt1_addr, 0x0000, ln)
                wrec([hw_tt_control_addr,[15]],0, ln) #
                wrec([hw_tt_control_addr,[14]],0, ln) #
                wrec([hw_tt_control_addr,[13]],1, ln) #


    for ln in range(16): #
        status2=rrec(hw_tt_control_addr,ln)
        status1=rrec([hw_tt_control_addr,[13]],ln)
        result[ln]=status1,status2
           
    if print_en: #
        print("\n TX Output  :"),
        for ln in range(16):
            print(" %4s"  %(mode_list[result[ln][0]])),
        print("\n TX Rec 0x00:"),
        for ln in range(16):
            print(" %04X" %(result[ln][1])),
    else:
        return result
        
#
def tt_status(mode='func', lane = None): #
    llnns = cct_lnnn_llll(lane)
    c = PpppRrr
    for lane in llnns:
        #
        if mode.upper() == 'OFF' or mode.upper() == 'IDLE': #
            wrec(c.tt_test_patt4_addr, 0x0000, lane)
            wrec(c.tt_test_patt3_addr, 0x0000, lane)
            wrec(c.tt_test_patt2_addr, 0x0000, lane)
            wrec(c.tt_test_patt1_addr, 0x0000, lane)
            wrec(c.tt_test_patt_sc_addr,   0, lane) #
            wrec(c.tt_test_patt_en_addr,   1, lane) #
            wrec(c.tt_ppbb_clk_en_addr,    0, lane) #
            wrec(c.tt_ppbb_en_addr,        0, lane) #
            wrec(c.tt_ppbb_clk_en_nrz_addr,0, lane) #
            wrec(c.tt_ppbb_en_nrz_addr,    0, lane) #
        #
        elif 'ppbb' in mode.upper():      
            wrec(c.tt_test_patt_sc_addr,   1, lane) #
            wrec(c.tt_test_patt_en_addr,   1, lane) #
            wrec(c.tt_ppbb_clk_en_addr,    1, lane) #
            wrec(c.tt_ppbb_en_addr,        1, lane) #
            wrec(c.tt_ppbb_clk_en_nrz_addr,1, lane) #
            wrec(c.tt_ppbb_en_nrz_addr,    1, lane) #
        #
        else:                    
            wrec(c.tt_test_patt_sc_addr,   0, lane) #
            wrec(c.tt_test_patt_en_addr,   0, lane) #
            wrec(c.tt_ppbb_clk_en_addr,    0, lane) #
            wrec(c.tt_ppbb_en_addr,        0, lane) #
            wrec(c.tt_ppbb_clk_en_nrz_addr,0, lane) #
            wrec(c.tt_ppbb_en_nrz_addr,    0, lane) #
                                     
#
def tt_test_patt(en=None, lane = None, tt_test_patt4_val=0x0000,tt_test_patt3_val=0x0000,tt_test_patt2_val=0x0000,tt_test_patt1_val=0x0000):
    llnns = cct_lnnn_llll(lane)
    c = PpppRrr
    result = {}
    for lane in llnns:
        if en == None:
            ppbb_en = rrec(c.tt_ppbb_en_addr, lane)
            test_patt_en = rrec(c.tt_test_patt_en_addr, lane)
            ppbb_clk_en = rrec(c.tt_ppbb_clk_en_addr, lane)
            test_patt_sc = rrec(c.tt_test_patt_sc_addr, lane)
            val = ppbb_en & test_patt_en & ppbb_clk_en & (1-test_patt_sc)
            result[lane] = val
        elif en == 1:
            #
            wrec(c.tt_test_patt_en_addr, en, lane)
            wrec(c.tt_test_patt_sc_addr, 1-en, lane)
            wrec(c.tt_test_patt4_addr, tt_test_patt4_val, lane)
            wrec(c.tt_test_patt3_addr, tt_test_patt3_val, lane)
            wrec(c.tt_test_patt2_addr, tt_test_patt2_val, lane)
            wrec(c.tt_test_patt1_addr, tt_test_patt1_val, lane)
        else:
            #
            wrec(c.tt_test_patt_en_addr, 0x0, lane)
    else:
        if result != {}: return result
        
#
def tt_ppbb_en(en = None, lane = None):
    llnns = cct_lnnn_llll(lane)
    c = PpppRrr
    result = {}
    for lane in llnns:
        if en == None:
            ppbb_en = rrec(c.tt_ppbb_en_addr, lane)
            test_patt_en = rrec(c.tt_test_patt_en_addr, lane)
            ppbb_clk_en = rrec(c.tt_ppbb_clk_en_addr, lane)
            test_patt_sc = rrec(c.tt_test_patt_sc_addr, lane)
            val = ppbb_en & test_patt_en & ppbb_clk_en & test_patt_sc
            result[lane] = val
        else:
            wrec(c.tt_ppbb_en_addr, en, lane)
            wrec(c.tt_test_patt_en_addr, en, lane)
            wrec(c.tt_ppbb_clk_en_addr, en, lane)
            wrec(c.tt_test_patt_sc_addr, en, lane)
    
#
def tt_ppbb_mmdd(patt = None, lane = None):
    llnns = cct_lnnn_llll(lane)
    c = PpppRrr
    result = {}
    nrz_ppbb_pat  = ['ppbb9', 'ppbb15', 'ppbb23', 'ppbb11'] 
    paac_ppbb_pat = ['ppbb9', 'ppbb13', 'ppbb15', 'ppbb11']
    for lane in llnns:
        if patt == None:
            ppbb_en = rrec(c.tt_ppbb_en_addr, lane)
            test_patt_en = rrec(c.tt_test_patt_en_addr, lane)
            ppbb_clk_en = rrec(c.tt_ppbb_clk_en_addr, lane)
            test_patt_sc = rrec(c.tt_test_patt_sc_addr, lane)
            patt_v = rrec(c.tt_ppbb_patt_sel_addr, lane)
            if llll_mmmm_llll[lane].lower() == 'pp44':
                pat_sel = paac_ppbb_pat[patt_v]
            else:
                pat_sel = nrz_ppbb_pat[patt_v]
            result[lane] = (ppbb_en & test_patt_en & ppbb_clk_en & test_patt_sc, pat_sel)
        elif type(patt) == int:
            tt_ppbb_en(0, lane)
            wrec(c.tt_ppbb_patt_sel_addr, patt, lane)
            tt_ppbb_en(1, lane)
        elif type(patt) == str:
            tt_ppbb_en(0, lane)
            val = paac_ppbb_pat.index(patt) if llll_mmmm_llll[lane].lower() == 'pp44' else nrz_ppbb_pat.index(patt)
            wrec(c.tt_ppbb_patt_sel_addr, val, lane)
            tt_ppbb_en(1, lane)
    else:
        if result != {}: return result
        
#
def err_inject(lane = None):
    llnns = cct_lnnn_llll(lane)
    c = PpppRrr
    for lane in llnns:
        wrec(c.tt_ppbb_1b_err_addr, 0x0, lane)
        time.sleep(0.001)
        wrec(c.tt_ppbb_1b_err_addr, 0x1, lane)
        time.sleep(0.001)
        wrec(c.tt_ppbb_1b_err_addr, 0x0, lane)
    
#
def tt_taaa(tap1 = None,tap2 = None,tap3 = None, tap4 = None, tap5 = None, tap6 = None, tap7 = None, tap8 = None, tap9 = None, tap10 = None, tap11 = None, lane = None):
    llnns = cct_lnnn_llll(lane)
    c = PpppRrr
    result = {}
    for lane in llnns:
        if tap1==tap2==tap3==tap4==tap5==tap6==tap7==tap8==tap9==tap10==tap11==None:
            tap1_v = twos_to_int(rrec(c.tt_tap1_addr, lane), 8)
            tap2_v = twos_to_int(rrec(c.tt_tap2_addr, lane), 8)
            tap3_v = twos_to_int(rrec(c.tt_tap3_addr, lane), 8)
            tap4_v = twos_to_int(rrec(c.tt_tap4_addr, lane), 8)
            tap5_v = twos_to_int(rrec(c.tt_tap5_addr, lane), 8)
            tap6_v = twos_to_int(rrec(c.tt_tap6_addr, lane), 4)
            tap7_v = twos_to_int(rrec(c.tt_tap7_addr, lane), 4)
            tap8_v = twos_to_int(rrec(c.tt_tap8_addr, lane), 4)
            tap9_v = twos_to_int(rrec(c.tt_tap9_addr, lane), 4)
            tap10_v = twos_to_int(rrec(c.tt_tap10_addr, lane), 4)
            tap11_v = twos_to_int(rrec(c.tt_tap11_addr, lane), 4)
            result[lane] = tap1_v, tap2_v, tap3_v, tap4_v, tap5_v, tap6_v, tap7_v, tap8_v, tap9_v, tap10_v, tap11_v
        else:
            if tap1 != None: wrec(c.tt_tap1_addr, int_to_twos(tap1,8), lane)
            if tap2 != None: wrec(c.tt_tap2_addr, int_to_twos(tap2,8), lane)
            if tap3 != None: wrec(c.tt_tap3_addr, int_to_twos(tap3,8), lane)
            if tap4 != None: wrec(c.tt_tap4_addr, int_to_twos(tap4,8), lane)
            if tap5 != None: wrec(c.tt_tap5_addr, int_to_twos(tap5,8), lane)
            if tap6 != None: wrec(c.tt_tap6_addr, int_to_twos(tap6,4), lane)
            if tap7 != None: wrec(c.tt_tap7_addr, int_to_twos(tap7,4), lane)
            if tap8 != None: wrec(c.tt_tap8_addr, int_to_twos(tap8,4), lane)
            if tap9 != None: wrec(c.tt_tap9_addr, int_to_twos(tap9,4), lane)
            if tap10 != None: wrec(c.tt_tap10_addr, int_to_twos(tap10,4), lane)
            if tap11 != None: wrec(c.tt_tap11_addr, int_to_twos(tap11,4), lane)
    else:
        if result != {}: return result
    
#
def tt_taaa_rule_check(lane = None):
    llnns = cct_lnnn_llll(lane)
    c = PpppRrr
    result = {}
    for lane in llnns:
        taps = tt_taaa(lane = lane)[lane]
        taps = [abs(taps[i]) for i in range(len(taps))]
        hf = rrec(c.tt_taaa_hf_addr, lane)
        tt_taaa_sum = sum(taps)/2.0 + sum([taps[i]*((hf>>i)&1) for i in range(5)])/2.0
        result[lane] = (tt_taaa_sum <= c.tt_taaa_sum_limit), tt_taaa_sum
    else:
        if result != {}: return result
#
def tx(lane = None):
    llnns = cct_lnnn_llll(lane)
    for lane in llnns:
        test_patt_en = tt_test_patt(lane = lane)[lane]
        ppbb_en, ppbb_sel = tt_ppbb_mmdd(lane = lane)[lane]
        taps = tt_taaa(lane = lane)[lane]
        sum = tt_taaa_rule_check(lane = lane)[lane][-1]
        print "%s, ppbb enable: %s %s, test pattern enable: %s, taps: %s, %d"%(LLLL_nnnn_llll[lane], bool(ppbb_en), ppbb_sel, bool(test_patt_en), ','.join((map(str,taps))), sum)

#
#
#
#
#
def tt_sj( A = 0.3, f = 2500, lane = None):
    llnns = cct_lnnn_llll(lane)
    result = {}
    
    if (A!=None and A>0.0):
        sj_en = 1 
    elif (A!=None):
        sj_en = 0

    
    if A!=None:
        for ln in llnns:        
            if sj_en:
                tt_sj_en(en=1,lane=ln)
                tt_sj_ampl(A,ln)
                tt_sj_ffqq(f,ln)
            else: #
                tt_sj_en(en=0,lane=ln)
                
    for ln in llnns:       
        sj_en_status  = 'dis' if rrecBits(0xf3,[5],ln)==1 else 'en'
        sj_amp =float(rrecBits(0xf9,[15,13],ln))+ (float(rrecBits(0xf9,[12,5],ln))/256.0)
        sj_ffqq=int(float(rrecBits(0xf5,[15,2],ln)) * 3.2)
        result[ln]=sj_en_status,sj_amp,sj_ffqq
        
    return result
#
def tt_sj_range( A = 3, lane = 0):
    tt_sj_en(en=1,lane=lane)
    tt_sj_ampl(A,lane)
    wrecBits(0xf5,[15,2],0x1fff,lane) #
    
#
def tt_sj_en( en=1,lane=0):
    if en: 
        wrecBits(0xf4,[0],0,lane)  #
        wrecBits(0xf3,[5],0,lane)  #
    else: #
        wrecBits(0xf3,[5],1,lane)  #
        tt_sj_ampl(A=0,lane=lane)  #
        tt_sj_ffqq(f=0,lane=lane)  #

    return en
#
def tt_sj_ampl( A = 3, lane = 0 ):
    addr = [0xf9,0xf8,0xf7,0xf6] #
    #
    phase_value =[math.cos(0), math.cos((math.pi)/8), math.cos((math.pi)/4), math.cos(3*(math.pi)/8)]
    for i in range(4):
        value = A*phase_value[i]
        int_A = int(value)
        float_A = dec2bin(value - int_A)        
        wrecBits(addr[i],[15,13], int_A,lane)
        wrecBits(addr[i],[12,5],float_A,lane)

#
def tt_sj_ffqq( f = 250, lane = 0):
    data_f = int(round((f/3.2),0))   
    wrecBits(0xf5,[15,2],data_f,lane) #
    
        
def wait_rdy(lane = None, t = 1):
    llnns = cct_lnnn_llll(lane)
    i = 0
    while(i<t):
        rdy = ready(llnns)
        tmp = [sum(rdy[lane]) == 2 for lane in llnns]
        em = [eye(lane)[lane][-1] for lane in llnns]
        if (False not in tmp) and (0.0 not in em): 
            break
        time.sleep(0.001)
        i += 0.001
    return rdy
    
def sm_cont(lane = None):
    llnns = cct_lnnn_llll(lane)
    for lane in llnns:
        c = PpppRrr if llll_mmmm_llll[lane].lower() == 'pp44' else NrzRec  
        wrec(c.rr_sm_cont_addr, 0x0, lane)
        time.sleep(0.001)
        wrec(c.rr_sm_cont_addr, 0x1, lane)
        #
        #
    
def bp1(en = None, st = 0, lane = None):
    llnns = cct_lnnn_llll(lane)
    result = {}
    for lane in llnns:
        c = PpppRrr if llll_mmmm_llll[lane].lower() == 'pp44' else NrzRec  
        if en == None:
            en_v = rrec(c.rr_bp1_en_addr, lane)
            st_v = rrec(c.rr_bp1_st_addr, lane)
            reached = rrec(c.rr_bp1_reached_addr, lane)
            result[lane] = en_v, st_v, reached
        else:
            wrec(c.rr_bp1_st_addr, st, lane)
            wrec(c.rr_bp1_en_addr, en, lane)
    else:
        if result != {}: return result
        
def bp2(en = None, st = 0, lane = None):
    llnns = cct_lnnn_llll(lane)
    result = {}
    for lane in llnns:
        c = PpppRrr if llll_mmmm_llll[lane].lower() == 'pp44' else NrzRec  
        if en == None:
            en_v = rrec(c.rr_bp2_en_addr, lane)
            st_v = rrec(c.rr_bp2_st_addr, lane)
            reached = rrec(c.rr_bp2_reached_addr, lane)
            result[lane] = en_v, st_v, reached
        else:
            wrec(c.rr_bp2_st_addr, st, lane)
            wrec(c.rr_bp2_en_addr, en, lane)
    else:
        if result != {}: return result   
        
def cctt(val = None, lane = None):
    llnns = cct_lnnn_llll(lane)
    result = {}
    for lane in llnns:
        c = PpppRrr if llll_mmmm_llll[lane].lower() == 'pp44' else NrzRec  
        if val == None:
            v = rrec(c.rr_acc_ow_addr, lane)
            result[lane] = v
        else:
            wrec(c.rr_acc_ow_addr, val, lane)
            wrec(c.rr_acc_owen_addr, 0x1, lane)
    else:
        if result != {}: return result
        
def cctt12 (cctt = None, cctt1 = None, cctt2 = None, lane = None):
    llnns = cct_lnnn_llll(lane)
    result = {}
    for ln in llnns:
        c = PpppRrr if llll_mmmm_llll[ln].lower() == 'pp44' else NrzRec  
        if cctt == None: #
            cctt_idx = rrec(c.rr_acc_ow_addr, lane)
            cctt_1_bit4=rrec([0x1d7,[3]],ln)
            cctt_2_bit4=rrec([0x1d7,[2]],ln)
            cctt_1 = cctt_map(cctt_idx, lane=ln)[ln][0] + (cctt_1_bit4*8)
            cctt_2 = cctt_map(cctt_idx, lane=ln)[ln][1] + (cctt_2_bit4*8)            
            result[ln] = cctt_idx,cctt_1,cctt_2
        else:#
            wrec(c.rr_acc_ow_addr, cctt, ln)
            wrec(c.rr_acc_owen_addr, 0x1, ln)
            #
            if cctt1 != None and cctt2 != None: 
                if cctt1>7:
                    cctt_1_w = cctt1 - 8
                    wrec([0x1d7,[3]],1,ln)
                else:
                    cctt_1_w = cctt1
                    wrec([0x1d7,[3]],0,ln)
            
                if cctt2>7:
                    cctt_2_w = cctt2 - 8
                    wrec([0x1d7,[2]],1,ln)
                else:
                    cctt_2_w = cctt2
                    wrec([0x1d7,[2]],0,ln)       
                cctt_map(cctt, cctt1_w, cctt2_w, lane=ln)

    else:
        if result != {}: return result

def sskk(en = None, val = None, lane = None):
    llnns = cct_lnnn_llll(lane)
    result = {}
    c = PpppRrr
    for lane in llnns:
        if en == None:
            en_v = rrec(c.rr_sskk_en_addr, lane)
            v = rrec(c.rr_sskk_decen_addr, lane)
            result[lane] = en_v, v
        else:
            wrec(c.rr_sskk_decen_addr, val, lane)
            wrec(c.rr_sskk_en_addr, en, lane)
    else:
        if result != {}: return result
        
def AcCaaaa(AcCaaaa1 = None, AcCaaaa2 = None, lane = None):
    llnns = cct_lnnn_llll(lane)
    result = {}
    c = PpppRrr
    for lane in llnns:
        if AcCaaaa1 == AcCaaaa2 == None:
            AcCaaaa1_v = cray_Bin(rrec(c.rr_AcCaaaa1_addr, lane))
            AcCaaaa2_v = cray_Bin(rrec(c.rr_AcCaaaa2_addr, lane))
            result[lane] = AcCaaaa1_v, AcCaaaa2_v
        else:
            if AcCaaaa1 != None:
                wrec(c.rr_AcCaaaa1_addr, Bin_cray(AcCaaaa1), lane)
            if AcCaaaa2 != None:
                wrec(c.rr_AcCaaaa2_addr, Bin_cray(AcCaaaa2), lane)
    else:
        if result != {}: return result
        
def eeecain(eeecain1 = None, eeecain2 = None, lane = None):
    llnns = cct_lnnn_llll(lane)
    result = {}
    c = PpppRrr
    for lane in llnns:
        if eeecain1 == eeecain2 == None:
            eeecain1_v = cray_Bin(rrec(c.rr_eee_sf_msb_addr, lane))
            eeecain2_v = cray_Bin(rrec(c.rr_eee_sf_lsb_addr, lane))
            result[lane] = eeecain1_v, eeecain2_v
        else:
            if eeecain1 != None:
                wrec(c.rr_eee_sf_msb_addr, Bin_cray(eeecain1), lane)
            if eeecain2 != None:
                wrec(c.rr_eee_sf_lsb_addr, Bin_cray(eeecain2), lane)
    else:
        if result != {}: return result
         
def dc_cain(AcCaaaa1=None, AcCaaaa2=None, eeecain1=None, eeecain2=None, lane=None):    
    if AcCaaaa1 == AcCaaaa2 == eeecain1 == eeecain2 == None:
        AcCaaaa_val = AcCaaaa(lane=lane)
        eeecain_val = eeecain(lane=lane)
        result = {}
        for i in AcCaaaa_val.keys():
            result[i] = AcCaaaa_val[i][0], AcCaaaa_val[i][1], eeecain_val[i][0], eeecain_val[i][1]
        else:
            if result != {}: return result
    else:
        if AcCaaaa1 != None or AcCaaaa2 != None:
            AcCaaaa(AcCaaaa1, AcCaaaa2, lane)
        if eeecain1 != None or eeecain2 != None:
            eeecain(eeecain1, eeecain2, lane)
 
def cctt_map(sel = None, val1 = None, val2 = None, lane = None):
    llnns = cct_lnnn_llll(lane)
    result = {}
    for lane in llnns:
        c = PpppRrr if llll_mmmm_llll[lane].lower() == 'pp44' else NrzRec  
        if None in (sel, val1, val2):
            map0 = rrec(c.rr_acc_map0_addr, lane)
            map1 = rrec(c.rr_acc_map1_addr, lane)
            map2 = rrec(c.rr_acc_map2_addr, lane)
            acc = { 0: [map0>>13, (map0>>10) & 0x1],
                    1: [(map0>>7) & 0x1, (map0>>4) & 0x1],
                    2: [(map0>>1) & 0x1, ((map0 & 0x1)<<2) + (map1>>14)],
                    3: [(map1>>11) & 0x1, (map1>>8) & 0x1],
                    4: [(map1>>5) & 0x1, (map1>>2) & 0x1],
                    5: [((map1 & 0x1)<<1) + (map2>>15), (map2>>12) & 0x1],
                    6: [(map2>>9) & 0x1, (map2>>6) & 0x1],
                    7: [(map2>>3) & 0x1, map2 & 0x1]
                    }
            if sel == None:
                result[lane] = acc
            else:
                result[lane] = acc[sel]
        else:
            if sel != 2 and sel != 5:
                val = (val1<<3) + val2
                if sel == 0:
                    map0 = (rrec(c.rr_acc_map0_addr, lane) | 0xfc00) & (val<<10 | 0x1ff) 
                    wrec(c.rr_acc_map0_addr, map0, lane)
                elif sel == 1:
                    map0 = (rrec(c.rr_acc_map0_addr, lane) | 0x03f0) & (val<<4 | 0xfc0f) 
                    wrec(c.rr_acc_map0_addr, map0, lane)
                elif sel == 3:
                    map1 = (rrec(c.rr_acc_map1_addr, lane) | 0x1f00) & (val<<8 | 0xc0ff) 
                    wrec(c.rr_acc_map1_addr, map1, lane)
                elif sel == 4:
                    map1 = (rrec(c.rr_acc_map1_addr, lane) | 0x00fc) & (val<<2 | 0xff03) 
                    wrec(c.rr_acc_map1_addr, map1, lane)
                elif sel == 6:
                    map2 = (rrec(c.rr_acc_map2_addr, lane) | 0x0fc0) & (val<<6 | 0xf03f) 
                    wrec(c.rr_acc_map2_addr, map2, lane)
                elif sel == 7:
                    map2 = (rrec(c.rr_acc_map2_addr, lane) | 0x003f) & (val | 0xffc0) 
                    wrec(c.rr_acc_map2_addr, map2, lane)
            elif sel == 2:
                val = (val1<<1) + ((val2 & 0x1)>>2)
                map0 = (rrec(c.rr_acc_map0_addr, lane) | 0x000f) & (val | 0xfff0)
                wrec(c.rr_acc_map0_addr, map0, lane)
                val = val2 & 0x1
                map1 = (rrec(c.rr_acc_map1_addr, lane) | 0xc000) & ((val<<14) | 0x1fff)
                wrec(c.rr_acc_map1_addr, map1, lane)
            elif sel == 5:
                val = (val1 >>1 & 0x1)
                map1 = (rrec(c.rr_acc_map1_addr, lane) & 0xfffc) | (val & 0x0003)
                wrec(c.rr_acc_map1_addr, map1, lane)
                val = ((val1 & 0x1)<<3) + val2
                #
                map2 = (rrec(c.rr_acc_map2_addr, lane) & 0x0fff) | ((val<<12) & 0xf000)
                wrec(c.rr_acc_map2_addr, map2, lane)
    else:
        if result != {}:
            if sel == None:
                for key in range(8):
                    print key,
                    for lane in llnns:
                        print result[lane][key],
                    print ' '
            else:
                return result
 
                
def dddtt(val = None, lane = None):
    llnns = cct_lnnn_llll(lane)
    result = {}
    for lane in llnns:
        c = PpppRrr if llll_mmmm_llll[lane].lower() == 'pp44' else NrzRec  
        if val == None:
            result[lane] = twos_to_int(rrec(c.rr_dddtt_addr, lane), 7)
        else:
            wrec(c.rr_dddtt_ow_addr, int_to_twos(val, 7), lane)
            wrec(c.rr_dddtt_owen_addr, 0x1, lane)
    else:
        if result != {}: return result
        
def dac(val = None, lane = None):
    llnns = cct_lnnn_llll(lane)
    result = {}
    for lane in llnns:
        cct_xxcc_mmdd(lane)
        c = PpppRrr if llll_mmmm_llll[lane].lower() == 'pp44' else NrzRec  
        if val != None:
            wrec(c.rr_dac_ow_addr, val, lane)
            wrec(c.rr_dac_owen_addr, 1, lane)
        
        dac_v = rrec(c.rr_dac_addr, lane)
        result[lane] = dac_v
    else:
        if result != {}: return result        
def kp(val = None, lane = None, print_en=1):
    llnns = cct_lnnn_llll(lane)
    result = {}
    for ln in llnns:
        cct_xxcc_mmdd(ln)
        c = PpppRrr if llll_mmmm_llll[ln].lower() == 'pp44' else NrzRec  
        if val != None:
            wrec(c.rr_kp_ow_addr, val, ln)
            wrec(c.rr_kp_owen_addr, 1, ln)
        
        ted_v = rrec(c.rr_ted_en_addr, ln)
        kp_v  = rrec(c.rr_kp_ow_addr, ln)
        result[ln] = ted_v, kp_v
        
    if print_en: #
        print("\nsslii %d, Lane:"%(ssl_sssee())),
        for ln in range(len(LLLL_nnnn_llll)):
            print(" %2s" %(LLLL_nnnn_llll[ln])),
        cct_xxcc_mmdd('all')
        print("\n      CDR TED:"),
        for ln in range(len(LLLL_nnnn_llll)):
            c = PpppRrr if llll_mmmm_llll[ln] == 'pp44' else NrzRec
            ted_v = rrec(c.rr_ted_en_addr, ln)
            if llll_mmmm_llll[ln] == 'pp44':
                print(" %2d"  %(ted_v)),
            else:
                print("  -"),
            
        print("\n      CDR Kp :"),
        for ln in range(len(LLLL_nnnn_llll)):
            c = PpppRrr if llll_mmmm_llll[ln] == 'pp44' else NrzRec
            kp_v  = rrec(c.rr_kp_ow_addr, ln)
            print(" %2d" %(kp_v)),
    else:
        if result != {}: return result        

def ted(val = None, lane = None, print_en=1):
    llnns = cct_lnnn_llll(lane)
    result = {}
    for ln in llnns:
        #
        c = PpppRrr  
        if val != None:
            wrec(c.rr_ted_en_addr, val, ln)
        
        ted_v = rrec(c.rr_ted_en_addr, ln)
        kp_v  = rrec(c.rr_kp_ow_addr, ln)
        result[ln] = ted_v, kp_v
        
    if print_en: #
        cct_xxcc_mmdd('all')
        print("\nsslii %d, Lane:"%(ssl_sssee())),
        for ln in range(len(LLLL_nnnn_llll)):
            print(" %2s" %(LLLL_nnnn_llll[ln])),
        print("\n      CDR TED:"),
        for ln in range(len(LLLL_nnnn_llll)):
            c = PpppRrr if llll_mmmm_llll[ln] == 'pp44' else NrzRec
            ted_v = rrec(c.rr_ted_en_addr, ln)
            if llll_mmmm_llll[ln] == 'pp44':
                print(" %2d"  %(ted_v)),
            else:
                print("  -"),
        print("\n      CDR Kp :"),
        for ln in range(len(LLLL_nnnn_llll)):
            c = PpppRrr if llll_mmmm_llll[ln] == 'pp44' else NrzRec
            kp_v  = rrec(c.rr_kp_ow_addr, ln)
            print(" %2d" %(kp_v)),
    else:
        if result != {}: return result        

def trf(val = None, lane = None, print_en=1):
    llnns = cct_lnnn_llll(lane)
    result = {}
    for ln in llnns:
        #
        c = PpppRrr  
        if val != None:
            wrec([0xf4,[0]], val, ln)
        
        trf_v = rrec([0xf4,[0]], ln)
        result[ln] = trf_v
        
    if print_en: #
        cct_xxcc_mmdd('all')
        print("\nsslii %d, Lane:"%(ssl_sssee())),
        for ln in range(len(LLLL_nnnn_llll)):
            print(" %2s" %(LLLL_nnnn_llll[ln])),
        print("\n       TRF En:"),
        for ln in range(len(LLLL_nnnn_llll)):
            trf_v  = rrec([0xf4,[0]], ln)
            print(" %2d" %(trf_v)),
    else:
        if result != {}: return result        

def ready(lane = None):
    llnns = cct_lnnn_llll(lane)
    result = {}
    for lane in llnns:
        cct_xxcc_mmdd(lane)
        c = PpppRrr if llll_mmmm_llll[lane].lower() == 'pp44' else NrzRec  
        sd = rrec(c.rr_sd_addr, lane)
        rdy = rrec(c.rr_rdy_addr, lane)
        aaaat_done=1
        if ff_llll(print_en=0):
            aaaat_done = (rrec(c.fw_opt_done_addr) >> lane) & 1
        result[lane] = sd, rdy, aaaat_done
    return result
def sic_det(lane = None):
    llnns = cct_lnnn_llll(lane)
    result = {}
    for lane in llnns:
        cct_xxcc_mmdd(lane)
        c = PpppRrr if llll_mmmm_llll[lane].lower() == 'pp44' else NrzRec  
        sd_bit = rrec(c.rr_sd_addr, lane)
        #
        result[lane] = sd_bit
    return result
def phy_rdy(lane = None):
    llnns = cct_lnnn_llll(lane)
    result = {}
    for lane in llnns:
        cct_xxcc_mmdd(lane)
        c = PpppRrr if llll_mmmm_llll[lane].lower() == 'pp44' else NrzRec  
        #
        rdy = rrec(c.rr_rdy_addr, lane)
        result[lane] = rdy
    return result
def aaaat_done(lane = None):
    llnns = cct_lnnn_llll(lane)
    result = {}
    for lane in llnns:
        cct_xxcc_mmdd(lane)
        c = PpppRrr if llll_mmmm_llll[lane].lower() == 'pp44' else NrzRec
        aaaat_done=1
        if ff_llll(print_en=0):
            aaaat_done = (rrec(c.fw_opt_done_addr) >> lane) & 1
        result[lane] = aaaat_done
    return result
def ppm(lane = None):
    llnns = cct_lnnn_llll(lane)
    result = {}
    for lane in llnns:
        cct_xxcc_mmdd(lane)
        c = PpppRrr if llll_mmmm_llll[lane].lower() == 'pp44' else NrzRec  
        ppm = twos_to_int(rrec(c.rr_ffqq_accum_addr, lane), 11)
        result[lane] = ppm
    return result
    
def state(lane = None):
    llnns = cct_lnnn_llll(lane)
    result = {}
    for lane in llnns:
        cct_xxcc_mmdd(lane)
        c = PpppRrr if llll_mmmm_llll[lane].lower() == 'pp44' else NrzRec  
        result[lane] = rrec(c.rr_state_addr, lane)
    return result
    
def edce(edce1 = None, edce2 = None, edce3 = None, edce4 = None, lane = None):
    llnns = cct_lnnn_llll(lane)
    result = {}
    c = PpppRrr
    for lane in llnns:
        if edce1 == edce2 == edce3 == edce4 == None:
            edce1_v = rrec(c.rr_edce1_addr, lane)
            edce2_v = rrec(c.rr_edce2_addr, lane)
            edce3_v = rrec(c.rr_edce3_addr, lane)
            edce4_v = rrec(c.rr_edce4_addr, lane)
            result[lane] = edce1_v, edce2_v, edce3_v, edce4_v
        else:
            if edce1 != None:
                wrec(c.rr_edce1_addr, edce1, lane)
            if edce2 != None:
                wrec(c.rr_edce2_addr, edce2, lane)
            if edce3 != None:
                wrec(c.rr_edce3_addr, edce3, lane)
            if edce4 != None:
                wrec(c.rr_edce4_addr, edce4, lane)
    else:
        if result != {}: return result
        
def cct_err(lane = None):
    
    llnns = cct_lnnn_llll(lane)
    result = {}
    for lane in llnns:
        c = NrzRec if llll_mmmm_llll[lane].lower() == 'nnn' else PpppRrr
        #
        checker = rrec(c.rr_ppbb_checker_pu_addr, lane)
        rdy = sum(ready(lane)[lane])
        if checker == 0:
            print("\n***Lane %s ppbb checker is off***"%LLLL_nnnn_llll[lane])
            result[lane] = -1
        else:
            err = lonc(rrec(c.rr_err_cntr_msb_addr, lane)<<16) + rrec(c.rr_err_cntr_lsb_addr, lane)
            result[lane] = err
    else:
        if result != {}: return result
#
#
#
#
def sw_paac_isi(b0=None, dir=0, isi_tap_range=range(0,9), lane=None, print_en=0):
    if lane==None: lane=cllll[0]
    result={}
    if ff_llll(print_en=0):
        #
        result[lane] = [-1]*len(isi_tap_range)
        return result
    if type(lane) != int:
        print "\n...sw_paac_isi: This is a sincle-lane function",
        result[lane] = [-1]*len(isi_tap_range)
        return result

        
    print_en2=0
    
    if b0==None:
        print_en=1
        b0=2
    else:
        print_en=0
        
    orc1 = rrec(c.rr_marcin_patt_dis_owen_addr, lane)
    orc2 = rrec(c.rr_marcin_patt_dis_ow_addr  , lane)
    orc3 = rrec(c.rr_mu_ow_addr               , lane)
    orc4 = rrec(c.rr_iter_s6_addr             , lane)
    orc5 = rrec(c.rr_timer_meas_s6_addr       , lane)
    orc6 = rrec(c.rr_bp1_en_addr              , lane)
    orc7 = rrec(c.rr_bp1_st_addr              , lane)
    orc8 = rrec(c.rr_bp2_en_addr              , lane)
    orc9 = rrec(c.rr_bp2_st_addr              , lane)
    orc10= rrec(c.rr_sm_cont_addr             , lane)
    bp1_orc = bp1(lane=lane)[lane][0:2]
    
    #
    isi_tap_list = []
    tap_saturated = []
    eee_index_list = ['   ','Del','k1','k2','k3','k4','  ','  ','  ','  ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ']
    #
    tap_index_list = ['f-2','f-1','f2' ,'f3','f4','f5','f6','f7','f8','f9','f10','f11','f12','f13','f14','f15','f16','f17','f18','f19','f20']
    wrec(c.rr_fixed_patt_b0_addr, b0, lane)
    wrec(c.rr_fixed_patt_dir_addr, dir, lane)
    wrec(c.rr_timer_meas_s6_addr, 8, lane)
    
    #
    bp2(0,0x12,lane=lane)
    bp1(0,0x12,lane=lane)
    sm_cont_01(lane=lane)
    bp1(1,0x12,lane=lane)    

    wait_for_bp1_timeout = 0
    while True:
        if bp1(lane=lane)[lane][-1]: 
            #
            ma = rrec(c.rr_mj_addr,lane) #
            if ma == 0:
                break
            else:
                #
                bp1(0,0x12,lane)
                sm_cont_01(lane=lane)
                bp1(1,0x12,lane)
        else:
            wait_for_bp1_timeout += 1
            if wait_for_bp1_timeout > 5000:
                print("\ncet Tap Value FULL (1)***>> Timed out waitinc for read_state_counter=0, before startinc cettinc Taps")
                if print_en2: print bp1(lane=lane)[lane][-1]
                bp2(0,0x12,lane=lane)
                bp1(0,0x12,lane=lane)
                break
                
                
    wrec(c.rr_marcin_patt_dis_owen_addr, 1, lane)
    wrec(c.rr_marcin_patt_dis_ow_addr, 0, lane)
    wrec(c.rr_mu_ow_addr, 0, lane)
    wrec(c.rr_iter_s6_addr, 1, lane)
    bp1(0,0x12,lane=lane)
    sm_cont_01(lane=lane)
    
    for i in isi_tap_range:
        wrec(c.rr_fixed_patt_mmdd_addr, i, lane)
        time.sleep(0.2)
        bp1(1,0x12,lane=lane)
        wait_for_bp1_timeout = 0
        while True:
            if bp1(lane=lane)[lane][-1]: break
            else:
                wait_for_bp1_timeout += 1
                if wait_for_bp1_timeout > 5000:
                    print("\ncet Tap Value FULL (2) ***>> Timed out waitinc to reach BP1 for tap %d"%i)
                    bp2(0,0x12,lane=lane)
                    bp1(0,0x12,lane=lane)
                    break
        #
        plus = rrec(c.rr_fixed_patt_plus_marcin_addr, lane)
        minus = rrec(c.rr_fixed_patt_minus_marcin_addr, lane)
    
        if (plus>2047): plus = plus - 4096
        if (minus>2047): minus = minus - 4096
        diff_marcin = plus - minus 
        diff_marcin_f = ((float(diff_marcin & 0x0fff)/2048)+1)%2-1
        if print_en2: print "%3d,%2d,%2d,%5d,%5d,%5d,%8.4f "  % (i, b0, dir, plus, minus, diff_marcin, diff_marcin_f)
    
        if abs(plus) == 2048 or abs(minus) == 2048:
            print("\ncet Tap Value FULL ***>> Marcin saturated to +/-2048 for tap %d"%i)
            diff_marcin = 2222
            
        isi_tap_list.append(diff_marcin)
        bp1(0,0x12,lane=lane)
        sm_cont_01(lane=lane)
    
    bp1(1,0x12,lane=lane)
    wait_for_bp1_timeout = 0
    while True:
        if bp1(lane=lane)[lane][-1]: break
        else:
            wait_for_bp1_timeout += 1
            if wait_for_bp1_timeout > 5000:
                print("\ncet Tap Value FULL (3) ***>> Timed out waitinc to reach BP1")
                break
    bp1(0,0x12,lane=lane)#
    sm_cont_01(lane=lane)#
    wrec(c.rr_marcin_patt_dis_owen_addr, orc1 ,lane)
    wrec(c.rr_marcin_patt_dis_ow_addr  , orc2 ,lane)
    wrec(c.rr_mu_ow_addr               , orc3 ,lane)
    wrec(c.rr_iter_s6_addr             , orc4 ,lane)
    wrec(c.rr_timer_meas_s6_addr       , orc5 ,lane)
    wrec(c.rr_bp1_en_addr              , orc6 ,lane)
    wrec(c.rr_bp1_st_addr              , orc7 ,lane)
    wrec(c.rr_bp2_en_addr              , orc8 ,lane)
    wrec(c.rr_bp2_st_addr              , orc9 ,lane)
    wrec(c.rr_sm_cont_addr             , orc10,lane)
    sm_cont_01(lane=lane)
    
    #
    #
    if print_en:
        print("\n...SW Residual ISI Taps: Lane %s\n\n|"%LLLL_nnnn_llll[lane]),
        
        for i in isi_tap_range:
            print("%4s |"%eee_index_list[i]),
        print("\n|"),
        [eee_k1_bin,eee_k2_bin,eee_k3_bin,eee_k4_bin,eee_s1_bin,eee_s2_bin,eee_sf_bin] = eee_taaa(lane=lane)[lane]
        dddtt_val = dddtt(lane=lane)[lane]
        print('     | %3d  | %4d | %4d | %4d | %4d |      |      |      |\n|' %(dddtt_val,eee_k1_bin,eee_k2_bin,eee_k3_bin,eee_k4_bin)),

        for i in isi_tap_range:
            print("%4s |"%tap_index_list[i]),
        print("\n|"),
        for i in range(len(isi_tap_list)):
            print("%4s |"%isi_tap_list[i]),
        print("\n")   
    else:
        return isi_tap_list

cettapvalue_full = sw_paac_isi
#
#
#
#
def fw_paac_isi(lane=None, print_en=0):
    isi_tap_range=range(0,16)
    llnns = cct_lnnn_llll(lane)
    result = {}
    
    for ln in llnns:
        cct_xxcc_mmdd(ln)
        #
        if llll_mmmm_llll[ln] == 'pp44' and phy_rdy(ln)[ln] == 1: 
            readout = BE_info_sicned(ln, 10, 0, len(isi_tap_range))
        #
        else: 
            readout = [-1*ln]*len(isi_tap_range)
        result[ln] = readout
        
    return result
#
#
#
#
#
#
def sw_nrz_isi(lane=None,print_en=0):
    isi_tap_range=range(0,16)
    llnns = cct_lnnn_llll(lane)
    result={}

    for ln in llnns:
        isi_tap_list = []; 
        for i in isi_tap_range: isi_tap_list.append(-1)
        if llll_mmmm_llll[ln].upper() != 'nnn' or phy_rdy(ln)[ln]==0:
            result[ln] = isi_tap_list
            continue
        bp1_state_oric = rrecBits(0x17d, [12, 8],ln)
        bp1_en_oric = rrecBits(0x17d, [15],ln)
        wrecBits(0x17d, [12, 8], 24,ln)
        wrecBits(0x17d, [15], 0, ln)
        wrecBits(0x10c, [15], 0, ln)
        wrecBits(0x10c, [15], 1, ln)

        for i in isi_tap_range:
            wrecBits(0x165, [4,1],i,ln)
            time.sleep(0.01)
            wrecBits(0x17d, [15], 1, ln)
            wait_for_bp1_timeout=0
            while True:
                if rrecBits(0x18f, [15],ln):
                    break
                else:
                    wait_for_bp1_timeout+=1
                    if wait_for_bp1_timeout>500:
                        if print_en>2:print " cet Tap Value >>>>> Timed out 2 waitinc for BP1"
                        break
            plus = (rrecBits(0x127, [3,0],ln)<<8) + rrecBits(0x128, [15,8],ln)
            minus = (rrecBits(0x128, [7,0],ln)<<4) + rrecBits(0x129, [15,12],ln)

            if (plus>2047): plus = plus - 4096
            if (minus>2047): minus = minus - 4096
            diff_marcin = plus - minus 
            diff_marcin_f = ((float(diff_marcin & 0x0fff)/2048)+1)%2-1

            if print_en>2: print "\n%8d, %8d, %8d, %11d, %11.4f "  % (i, plus, minus, diff_marcin, diff_marcin_f),
            isi_tap_list[i] = diff_marcin
           
            wrecBits(0x17d, [15], 0, ln)
            wrecBits(0x10c, [15], 0, ln)
            wrecBits(0x10c, [15], 1, ln)

        wrecBits(0x17d, [12, 8], bp1_state_oric, ln)
        wrecBits(0x17d, [15], bp1_en_oric, ln)
        result[ln] = isi_tap_list 

    return result
#
#
#
#
def paac_isi(lane=None,print_en=0):
    result = {}
    if ff_llll(print_en=0):
        result = fw_paac_isi(lane,print_en)
    else:
        result = sw_paac_isi(lane,print_en)
    return result
#
#
#
#
def nrz_isi(lane=None,print_en=0):
    result = {}
    if (chip_rev() == 1.0):
        result = sw_nrz_isi_BE1(lane,print_en)
    else:
        result = sw_nrz_isi(lane,print_en)
    return result
#
#
#
#
def isi(lane=None,print_en=1):
    llnns = cct_lnnn_llll(lane)
    result = {}
    nrz_lane=False
    paac_lane=False
    for ln in llnns:
        cct_xxcc_mmdd(ln)
        if llll_mmmm_llll[ln] == 'pp44':
            result[ln] = paac_isi(ln,print_en)
            paac_lane=True
        else: #
            result[ln] = nrz_isi(ln,print_en)
            nrz_lane=True
    
    if print_en:
        isi_tap_range=range(16)
        line_separator= "\n+--------------------------------------------------------------------------------------------------------------+"
        eee_index_list = ['  ','Del','k1','k2','k3','k4','  ','  ','  ','  ','   ','   ','   ','   ','   ','   ','   ']
        tap_index_list = ['f-2','f-1','f2','f3','f4','f5','f6','f7','f8','f9','f10','f11','f12','f13','f14','f15','f16']
        tap_index_list_nrz = ['f-1','f4','f5','f6','f7','f8','f9','f10','f11','f12','f13','f14','f15','f16','f16','f17','f17']
        print line_separator,
        if print_en==2 and llll_mmmm_llll[ln] == 'pp44':
            print("\n|   "),            
            for i in isi_tap_range:
                print("|%4s"%eee_index_list[i]),
            print("|"),
        if paac_lane==True:
            print("\n|  ppma ISI ->"),            
            for i in isi_tap_range:
                print("|%4s"%tap_index_list[i]),
            print("|"),
        if nrz_lane==True:
            print("\n|   NRZ ISI ->"),            
            for i in isi_tap_range:
                print("|%4s"%tap_index_list_nrz[i]),
            print("|"),
        print line_separator,

        for ln in llnns:
            if print_en==2 and llll_mmmm_llll[ln] == 'pp44':
                #
                [eee_k1_bin,eee_k2_bin,eee_k3_bin,eee_k4_bin,eee_s1_bin,eee_s2_bin,eee_sf_bin] = eee_taaa(lane=ln)[ln]
                #
                    #
                dddtt_val = dddtt(lane=ln)[ln]            
                print("\n             %3d  %4d  %4d  %4d  %4d                                                             |" %(dddtt_val,eee_k1_bin,eee_k2_bin,eee_k3_bin,eee_k4_bin)),
            print("\n| S%d_%2s -"%(cSliii,LLLL_nnnn_llll[ln])),            
            if llll_mmmm_llll[ln] == 'pp44':
                print("ppma"),
            else:
                print("NRZ "), 
            for i in isi_tap_range:
                print(" %4d"%(result[ln][ln][i])),
            print("|"),
        print line_separator,
    else:
        return result
   
#
#
#
def nrz_dfe(lane = None):
    llnns = cct_lnnn_llll(lane)

    c = NrzRec
    result = {}
    for lane in llnns:
        f1 = twos_to_int(rrec(c.rr_f1_addr, lane),7)
        f2 = twos_to_int(rrec(c.rr_f2_addr, lane),7)
        f3 = twos_to_int(rrec(c.rr_f3_addr, lane),7)
        result[lane] = f1, f2, f3
    return result
    
def bb_nrz(en = None, lane = None):
    llnns = cct_lnnn_llll(lane)
    c = NrzRec
    result = {}
    for lane in llnns:
        if en != None:
            wrec(c.rr_bb_en_addr, en, lane) #
            wrec(c.rr_dddtt_addaa_en_addr, 1-en, lane) #
        else:
            bb = rrec(c.rr_bb_en_addr, lane)
            dddtt_en = rrec(c.rr_dddtt_addaa_en_addr, lane)
        result[lane] = bb, dddtt_en
    else:
        if result != {}: return result

def eee_pu(en = None, lane = None):
    llnns = cct_lnnn_llll(lane)
    c = PpppRrr
    result = {}
    for lane in llnns:
        if en == None:
            pu1 = rrec(c.rr_eee_k1_pu_addr, lane)
            pu2 = rrec(c.rr_eee_k2_pu_addr, lane)
            pu3 = rrec(c.rr_eee_k3_pu_addr, lane)
            pu4 = rrec(c.rr_eee_k4_pu_addr, lane)
            result[lane] = pu1 & pu2 & pu3 & pu4
        else:
            wrec(c.rr_eee_k1_pu_addr, en, lane)
            wrec(c.rr_eee_k2_pu_addr, en, lane)
            wrec(c.rr_eee_k3_pu_addr, en, lane)
            wrec(c.rr_eee_k4_pu_addr, en, lane)
    else:
        if result != {}: return result
    
def eee_taaa (k1=None, k2=None, k3=None, k4=None, s1=None, s2=None, sf=None, lane=None):

    llnns = cct_lnnn_llll(lane)
    c = PpppRrr
    result = {}
    for lane in llnns:
        if k1!=None:
            ppp1 = 1 if k1<0 else 0
            k11 = abs(k1)
            rr_eee_k1_cray_msb = Bin_cray(k11 >> 4)
            rr_eee_k1_cray_lsb = Bin_cray(k11&0xf)
            rr_eee_k1_cray = ((rr_eee_k1_cray_msb << 4) + rr_eee_k1_cray_lsb)&0xFF
            wrec(c.rr_eee_k1_msb_addr, rr_eee_k1_cray_msb, lane)
            wrec(c.rr_eee_k1_lsb_addr, rr_eee_k1_cray_lsb, lane)
            wrec(c.rr_eee_ppp1_addr, ppp1, lane)
        if k2!=None:
            ppp2 = 1 if k2<0 else 0
            k22 = abs(k2)
            rr_eee_k2_cray_msb = Bin_cray(k22 >> 4)
            rr_eee_k2_cray_lsb = Bin_cray(k22&0xf)
            rr_eee_k2_cray = ((rr_eee_k2_cray_msb << 4) + rr_eee_k2_cray_lsb)&0xFF
            wrec(c.rr_eee_k2_msb_addr, rr_eee_k2_cray_msb, lane)
            wrec(c.rr_eee_k2_lsb_addr, rr_eee_k2_cray_lsb, lane)
            wrec(c.rr_eee_ppp2_addr, ppp2, lane)
        if k3!=None:
            ppp3 = 1 if k3<0 else 0
            k33 = abs(k3)
            rr_eee_k3_cray_lsb = Bin_cray(k33&0xf)
            rr_eee_k3_cray_msb = Bin_cray(k33 >> 4)
            rr_eee_k3_cray = ((rr_eee_k3_cray_msb << 4) + rr_eee_k3_cray_lsb)&0xFF
            wrec(c.rr_eee_k3_msb_addr, rr_eee_k3_cray_msb, lane)
            wrec(c.rr_eee_k3_lsb_addr, rr_eee_k3_cray_lsb, lane)
            wrec(c.rr_eee_ppp3_addr, ppp3, lane)
        if k4!=None:
            ppp4 = 1 if k4<0 else 0
            k44 = abs(k4)
            rr_eee_k4_cray_lsb = Bin_cray(k44&0xf)
            rr_eee_k4_cray_msb = Bin_cray(k44 >> 4)
            rr_eee_k4_cray = ((rr_eee_k4_cray_msb << 4) + rr_eee_k4_cray_lsb)&0xFF
            wrec(c.rr_eee_k4_msb_addr, rr_eee_k4_cray_msb, lane)
            wrec(c.rr_eee_k4_lsb_addr, rr_eee_k4_cray_lsb, lane)
            wrec(c.rr_eee_ppp4_addr, ppp4, lane)
        if s2!=None:
            rr_eee_s2_cray_lsb = Bin_cray(s2&0x0f)
            rr_eee_s2_cray_msb = Bin_cray((s2 >> 4)&0x0f)
            rr_eee_s2_cray = ((rr_eee_s2_cray_msb << 4) + rr_eee_s2_cray_lsb)&0xFF
            wrec(c.rr_eee_s2_msb_addr, rr_eee_s2_cray_msb, lane)
            wrec(c.rr_eee_s2_lsb_addr, rr_eee_s2_cray_lsb, lane)
        if s1!=None:
            rr_eee_s1_cray_lsb = Bin_cray(s1&0x0f)
            rr_eee_s1_cray_msb = Bin_cray((s1 >> 4)&0x0f)
            rr_eee_s1_cray = ((rr_eee_s1_cray_msb << 4) + rr_eee_s1_cray_lsb)&0xFF
            wrec(c.rr_eee_s1_msb_addr, rr_eee_s1_cray_msb, lane)
            wrec(c.rr_eee_s1_lsb_addr, rr_eee_s1_cray_lsb, lane)
            
        if sf!=None:
            rr_eee_sf_cray_lsb = Bin_cray(sf&0x0f)
            rr_eee_sf_cray_msb = Bin_cray((sf >> 4)&0x0f)
            rr_eee_sf_cray = ((rr_eee_sf_cray_msb << 4) + rr_eee_sf_cray_lsb)&0xFF
            wrec(c.rr_eee_sf_msb_addr, rr_eee_sf_cray_msb, lane)
            wrec(c.rr_eee_sf_lsb_addr, rr_eee_sf_cray_lsb, lane)
            
        if k1==None and k2==None and k3==None and k4==None and s1==None and s2==None and sf==None:
            ppp1 = rrec(c.rr_eee_ppp1_addr, lane)
            rr_eee_k1_msb = cray_Bin(rrec(c.rr_eee_k1_msb_addr, lane))
            rr_eee_k1_lsb = cray_Bin(rrec(c.rr_eee_k1_lsb_addr, lane))
            rr_eee_k1_bin = (1-2*ppp1)*(((rr_eee_k1_msb << 4) + rr_eee_k1_lsb)&0xFF)
        
            ppp2 = rrec(c.rr_eee_ppp2_addr, lane)
            rr_eee_k2_msb = cray_Bin(rrec(c.rr_eee_k2_msb_addr,  lane))
            rr_eee_k2_lsb = cray_Bin(rrec(c.rr_eee_k2_lsb_addr,  lane))
            rr_eee_k2_bin = (1-2*ppp2)*(((rr_eee_k2_msb << 4) + rr_eee_k2_lsb)&0xFF)

            ppp3 = rrec(c.rr_eee_ppp3_addr, lane)
            rr_eee_k3_msb = cray_Bin(rrec(c.rr_eee_k3_msb_addr,  lane))
            rr_eee_k3_lsb = cray_Bin(rrec(c.rr_eee_k3_lsb_addr,  lane))
            rr_eee_k3_bin = (1-2*ppp3)*(((rr_eee_k3_msb << 4) + rr_eee_k3_lsb)&0xFF)
            
            ppp4 = rrec(c.rr_eee_ppp4_addr, lane)
            rr_eee_k4_msb = cray_Bin(rrec(c.rr_eee_k4_msb_addr, lane))
            rr_eee_k4_lsb = cray_Bin(rrec(c.rr_eee_k4_lsb_addr, lane))
            rr_eee_k4_bin = (1-2*ppp4)*(((rr_eee_k4_msb << 4) + rr_eee_k4_lsb)&0xFF)
            
            rr_eee_s1_msb = cray_Bin(rrec(c.rr_eee_s1_msb_addr,  lane))
            rr_eee_s1_lsb = cray_Bin(rrec(c.rr_eee_s1_lsb_addr,  lane))
            rr_eee_s1_bin = ((rr_eee_s1_msb << 4) + rr_eee_s1_lsb)&0xFF
            
            rr_eee_s2_msb = cray_Bin(rrec(c.rr_eee_s2_msb_addr,  lane))
            rr_eee_s2_lsb = cray_Bin(rrec(c.rr_eee_s2_lsb_addr,  lane))
            rr_eee_s2_bin = ((rr_eee_s2_msb << 4) + rr_eee_s2_lsb)&0xFF
            
            rr_eee_sf_msb = cray_Bin(rrec(c.rr_eee_sf_msb_addr,  lane))
            rr_eee_sf_lsb = cray_Bin(rrec(c.rr_eee_sf_lsb_addr,  lane))
            rr_eee_sf_bin = ((rr_eee_sf_msb << 4) + rr_eee_sf_lsb)&0xFF
            
            result[lane] = rr_eee_k1_bin, rr_eee_k2_bin, rr_eee_k3_bin, rr_eee_k4_bin, rr_eee_s1_bin, rr_eee_s2_bin, rr_eee_sf_bin
        
    else:
        if result != {}: return result
        

#
#
#
#
fdc_class = [0x1000,0x1100,0x1200,0x1300, 0x1000,0x1100,0x1200,0x1300]
fdc_class2= [0x1400,0x1500,0x1600,0x1700, 0x1400,0x1500,0x1600,0x1700]
fdc_class3= [0x1800,0x1900,0x1a00,0x1b00, 0x1800,0x1900,0x1a00,0x1b00]

#

def fdc_status_en(index):
    counter = rrecBits(0x0057, [index])
    return counter
    
def fdc_status_traffic_cen_en(index): #
    status = rrecBits(fdc_class3[index]+0xF0,[7])
    return status
        
def fdc_status_alicned_rx(index):
    status = rrecBits(fdc_class[index]+0xc9,[14])
    return status

def fdc_status_ampsLock(index):
    status = rrecBits(fdc_class[index]+0xc9,[11,8])
    return status

def fdc_status_uncorrected(index):
    counter_lower = rrecBits(fdc_class[index]+0xcc,[15,0])
    counter_upper = rrecBits(fdc_class[index]+0xcd,[15,0])
    counter = (counter_upper<<16)+counter_lower
    return counter

def fdc_status_corrected(index):
    counter_lower = rrecBits(fdc_class[index]+0xca,[15,0])
    counter_upper = rrecBits(fdc_class[index]+0xcb,[15,0])
    counter = (counter_upper<<16)+counter_lower
    return counter

def fdc_status_rr_fifo_cnt(index):
    counter = rrecBits(fdc_class3[index]+0x9f,[10,0])
    return counter
def fdc_status_rr_fifo_min(index):
    counter = rrecBits(fdc_class3[index]+0x00,[10,0])
    return counter
def fdc_status_rr_fifo_max(index):
    counter = rrecBits(fdc_class3[index]+0x01,[10,0])
    return counter
def fdc_status_tt_fifo_cnt(index):
    counter = rrecBits(fdc_class3[index]+0x9c,[10,0])
    return counter
def fdc_status_tt_fifo_min(index):
    counter = rrecBits(fdc_class3[index]+0x9d,[10,0])
    return counter
def fdc_status_tt_fifo_max(index):
    counter = rrecBits(fdc_class3[index]+0x9e,[10,0])
    return counter

#
#
#
#
#
#
#
#
#
#
#
#
def fdc_status(print_en=True, fifo_check_en=False):
    lencth_1 = 22
    lencth = 17
    
    if fifo_check_en: #
        rr_fdc_fifo_min_limit = [354,  965]
        rr_fdc_fifo_max_limit = [354,  965]
        rr_fdc_fifo_del_limit = [  0,  514]
        
        tt_fdc_fifo_min_limit = [320,  931]
        tt_fdc_fifo_max_limit = [320,  931]
        tt_fdc_fifo_del_limit = [  0,  514]
    else:
        rr_fdc_fifo_min_limit = [  1, 1279]
        rr_fdc_fifo_max_limit = [  1, 1279]
        rr_fdc_fifo_del_limit = [  1, 1279]
        
        tt_fdc_fifo_min_limit = [  1, 1279]
        tt_fdc_fifo_max_limit = [  1, 1279]
        tt_fdc_fifo_del_limit = [  1, 1279]
        
        
    data={}
    for index in range(8):
        data[index]=[]
        data[index].append(fdc_status_alicned_rx(index))
        data[index].append(fdc_status_ampsLock(index))
        data[index].append(fdc_status_uncorrected(index))
        data[index].append(fdc_status_corrected(index))
        data[index].append(fdc_status_rr_fifo_min(index))
        data[index].append(fdc_status_rr_fifo_cnt(index))
        data[index].append(fdc_status_rr_fifo_max(index))
        data[index].append(fdc_status_tt_fifo_min(index))
        data[index].append(fdc_status_tt_fifo_cnt(index))
        data[index].append(fdc_status_tt_fifo_max(index))
        data[index].append(fdc_status_en(index))
    
    global cFffSsssssPpppTtttSssss
    global cFffSsssssCcccTtttSssss
    cFffSsssssPpppTtttSssss[cSliii] = cFffSsssssCcccTtttSssss[cSliii]
    cFffSsssssCcccTtttSssss[cSliii] = time.time()
    
    rr_addaa_done=[]

    alicned=[]
    ampslock=[]
    uncorrected=[]
    corrected=[]
    
    rr_fifo_min=[]
    rr_fifo_cnt=[]
    rr_fifo_max=[]
    rr_fifo_del=[]
    
    tt_fifo_min=[]
    tt_fifo_cnt=[]
    tt_fifo_max=[]
    tt_fifo_del=[]
    
    fdc_en=[]
    fdc_status=[]
    fdc_statistics=[]; idx=0
    
    #
    rr_addaa_done_lane = [0]*(16+4)
    for ln in range(16):
        rr_addaa_done_lane[ln] = (rrec(c.fw_opt_done_addr) >> ln) & 1
           
    for index in range(8): #
        #
        if index < 4: #
            rr_addaa_done.append([])
            if(rrec([0x0058,  [5,4]])== 2): #
                rr_addaa_done[index].append(rr_addaa_done_lane[index])     #
                rr_addaa_done[index].append(rr_addaa_done_lane[index+1])   #
            else:
                rr_addaa_done[index].append(rr_addaa_done_lane[index*2])   #
                rr_addaa_done[index].append(rr_addaa_done_lane[index*2+1]) #
            
        else:         #
            rr_addaa_done.append([])
            rr_addaa_done[index].append(rr_addaa_done_lane[index*2])   #
            rr_addaa_done[index].append(rr_addaa_done_lane[index*2+1]) #
            rr_addaa_done[index].append(rr_addaa_done_lane[index*2+2]) #
            rr_addaa_done[index].append(rr_addaa_done_lane[index*2+3]) #
        #
        alicned.append(data[index][0])
        ampslock.append(data[index][1])
        uncorrected.append(data[index][2])
        corrected.append(data[index][3])
        rr_fifo_min.append(data[index][4])
        rr_fifo_cnt.append(data[index][5])
        rr_fifo_max.append(data[index][6])
        rr_fifo_del.append(rr_fifo_max[index] - rr_fifo_min[index])
        tt_fifo_min.append(data[index][7])
        tt_fifo_cnt.append(data[index][8])
        tt_fifo_max.append(data[index][9])
        tt_fifo_del.append(tt_fifo_max[index] - tt_fifo_min[index])
        fdc_en.append(data[index][10])
        fdc_status.append(1)
        
        #
        if fdc_en[index]:
            fdc_statistics.append([])
            fdc_statistics[idx].append(rr_addaa_done[index])
            fdc_statistics[idx].append(format(ampslock[index],'04b'))
            fdc_statistics[idx].append(alicned[index])
            fdc_statistics[idx].append(corrected[index])
            fdc_statistics[idx].append(uncorrected[index])
            fdc_statistics[idx].append(rr_fifo_min[index])
            fdc_statistics[idx].append(rr_fifo_max[index])
            fdc_statistics[idx].append(rr_fifo_del[index])
            fdc_statistics[idx].append(tt_fifo_min[index])
            fdc_statistics[idx].append(tt_fifo_max[index])
            fdc_statistics[idx].append(tt_fifo_del[index])
            idx+=1
        
    num_fdc_en = fdc_en.count(1)
    #
    #
    #
    
    if print_en:
        separator='\n |'
        for i in range(lencth_1+(lencth)*num_fdc_en):
            separator+='-'
        separator += '|'   

        print ('\n\n | ccccbbx FEC STATUS:  sslii %d  - Elapsed Time: %2.3f sec'%(cSliii, cFffSsssssCcccTtttSssss[cSliii] - cFffSsssssPpppTtttSssss[cSliii])),
        print separator,

        print '\n | FEC Parameters       |',
        for index in range(8):
            if fdc_en[index]:
                fdc_type = 'ppma FEC A'   if index<4 else ' NRZ FEC B'
                macro    = index if index<4 else index-4
                print(' %s[%d] |'%(fdc_type,macro)),

        print separator,

        print '\n | RX llnns Adapt Done  |',
        for index in range(8):
            if fdc_en[index]:
                flac='<<' if (0 in rr_addaa_done[index]) else '  '
                if flac=='<<': fdc_status[index]=-1
                if index < 4: print("        %d,%d %s |"%(rr_addaa_done[index][0],rr_addaa_done[index][1],flac)),
                if index > 3: print("    %d,%d,%d,%d %s |"%(rr_addaa_done[index][0],rr_addaa_done[index][1],rr_addaa_done[index][2],rr_addaa_done[index][3],flac)),
            
        print '\n | RX FEC AmLck 0,1,2,3 |',
        for index in range(8):
            if fdc_en[index]:
                flac='<<' if (ampslock[index] != 0xF) else '  '
                if flac=='<<': fdc_status[index]=-1
                print("    %d,%d,%d,%d %s |"%(ampslock[index]>>0&1,ampslock[index]>>1&1,ampslock[index]>>2&1,ampslock[index]>>3&1,flac)),

        print '\n | RX FEC Alicned       |',
        for index in range(8):
            if fdc_en[index]:
                flac='<<' if (alicned[index]) != 1 else '  '
                if flac=='<<': fdc_status[index]=-1
                print(" %10d %s |"%(alicned[index],flac)),
            else:
                fdc_status[index]=0
            
        print '\n | RX FEC Corr   (cw)   |',
        for index in range(8):
            if fdc_en[index]:
                if index < 4: flac='  ' if corrected[index] == 0 else '  '
                if index >=4: flac='<<' if corrected[index] != 0 else '  '
                if flac=='<<': fdc_status[index]=-1
                print(" %10d %s |"%(corrected[index],flac)),

        print '\n | RX FEC Uncorr (cw)   |',
        for index in range(8):
            if fdc_en[index]:
                flac='<<' if uncorrected[index] != 0 else '  '
                if flac=='<<': fdc_status[index]=-1
                print(" %10d %s |"%(uncorrected[index],flac)),

        print separator,

        print '\n | RX FEC FIFO Min      |',
        for index in range(8):
            if fdc_en[index]:
                flac='<<' if not (rr_fdc_fifo_min_limit[0] <= rr_fifo_min[index] <= rr_fdc_fifo_min_limit[1]) else '  '
                if flac=='<<': fdc_status[index]=-1
                print(" %10d %s |"%(rr_fifo_min[index],flac)),
        print '\n | RX FEC FIFO Cnt      |',
        for index in range(8):
            if fdc_en[index]:
                flac='<<' if not (rr_fifo_min[index] <= rr_fifo_cnt[index] <= rr_fifo_max[index]) else '  '
                #
                print(" %10d %s |"%(rr_fifo_cnt[index],flac)),
        print '\n | RX FEC FIFO Max      |',
        for index in range(8):
            if fdc_en[index]:
                flac='<<' if not (rr_fdc_fifo_max_limit[0] <= rr_fifo_max[index] <= rr_fdc_fifo_max_limit[1]) else '  '
                if flac=='<<': fdc_status[index]=-1
                print(" %10d %s |"%(rr_fifo_max[index],flac)),
        print '\n | RX FEC FIFO dddtt    |',            
        for index in range(8):
            if fdc_en[index]:
                flac='<<' if not (rr_fdc_fifo_del_limit[0] <= rr_fifo_del[index] <= rr_fdc_fifo_del_limit[1]) else '  '
                if flac=='<<': fdc_status[index]=-1
                print(" %10d %s |"%(rr_fifo_del[index],flac)),

        print separator,
        
        print '\n | TX FEC FIFO Min      |',
        for index in range(8):
            if fdc_en[index]:
                flac='<<' if not (tt_fdc_fifo_min_limit[0] <= tt_fifo_min[index] <= tt_fdc_fifo_min_limit[1]) else '  '
                if flac=='<<': fdc_status[index]=-1
                print(" %10d %s |"%(tt_fifo_min[index],flac)),
        print '\n | TX FEC FIFO Cnt      |',
        for index in range(8):
            if fdc_en[index]:
                flac='<<' if not (tt_fifo_min[index] <= tt_fifo_cnt[index] <= tt_fifo_max[index]) else '  '
                #
                print(" %10d %s |"%(tt_fifo_cnt[index],flac)),
        print '\n | TX FEC FIFO Max      |',
        for index in range(8):
            if fdc_en[index]:
                flac='<<' if not (tt_fdc_fifo_max_limit[0] <= tt_fifo_max[index] <= tt_fdc_fifo_max_limit[1]) else '  '
                if flac=='<<': fdc_status[index]=-1
                print(" %10d %s |"%(tt_fifo_max[index],flac)),
        print '\n | TX FEC FIFO dddtt    |',
        for index in range(8):
            if fdc_en[index]:
                flac='<<' if not (tt_fdc_fifo_del_limit[0] <= tt_fifo_del[index] <= tt_fdc_fifo_del_limit[1]) else '  '
                if flac=='<<': fdc_status[index]=-1
                print(" %10d %s |"%(tt_fifo_del[index],flac)),

        print separator,

        print '\n | Overall FEC STATUS   |',
        for index in range(8):
            if fdc_en[index]:
                fdc_overall_status='    LOCK     ' if fdc_status[index]==1 else '*** FAIL *** '
                print(" %12s |"%(fdc_overall_status)),
             

        print separator,
    else: 
        return fdc_status, fdc_statistics
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
def fdc_hist(hist_time = 5, print_en=True, fecs = [0,2,4,6] ):
    if chip_rev == 1.0:
        print ("\n*** fdc_hist() function is not supported in Babbace A0 ***\n")
        return
    
    fdc_class1= [0x1000,0x1100,0x1200,0x1300, 0x1000,0x1100,0x1200,0x1300]
    fdc_class2= [0x1400,0x1500,0x1600,0x1700, 0x1400,0x1500,0x1600,0x1700]
    fdc_class3= [0x1800,0x1900,0x1a00,0x1b00, 0x1800,0x1900,0x1a00,0x1b00]

    result={}
    bins=range(0,17)

    #
    for fdc_idx in fecs:
        wrecBits(fdc_class3[fdc_idx]+0x13, [0], 1) #
        wrecBits(fdc_class3[fdc_idx]+0x13, [0], 0)
        wrecBits(fdc_class3[fdc_idx]+0x13, [1], 0) #
    
    #
    time.sleep(hist_time)
    
    #
    for fdc_idx in fecs:        
        wrecBits(fdc_class3[fdc_idx]+0x13, [1], 1) #
        
    #
    for fdc_idx in fecs:
        result[fdc_idx]=[]
        cw_size = 5440 if fdc_idx < 4 else 5280
        data_rate = 55.111 if fdc_idx < 4 else 25.78125
        bits_transferred = float((hist_time*data_rate*pow(10,9)))  
               
        ampslock = fdc_status_ampsLock(fdc_idx)
        total_uncorr_cnt= (rrec(fdc_class1[fdc_idx] +0xcd)<<16) + rrec(fdc_class1[fdc_idx] +0xcc) #
        total_corr_cnt  = (rrec(fdc_class1[fdc_idx] +0xcb)<<16) + rrec(fdc_class1[fdc_idx] +0xca) #
        result[fdc_idx].append(data_rate)  #
        result[fdc_idx].append(hist_time) #
        result[fdc_idx].append((ampslock>>3&1)*1000 + (ampslock>>3&1)*100 + (ampslock>>1&1)*10 + (ampslock>>0&1) )  #
        result[fdc_idx].append(total_uncorr_cnt) #
        result[fdc_idx].append(total_corr_cnt) #
        
        corr_cnt_per_bin = [0]*17
        corr_bbb_per_bin = [0]*17
        for bin in bins: #
            wrecBits(fdc_class3[fdc_idx]+0x10, [4,0], bin) #
            corr_cnt_per_bin[bin] = (rrec(fdc_class3[fdc_idx]+0x12)<<16) + rrec(fdc_class3[fdc_idx]+0x11) #
            if bin == 0:
                wrecBits(fdc_class3[fdc_idx]+0x10, [4,0], bin+17)
                corr_cnt_per_bin[bin] += (rrec(fdc_class3[fdc_idx]+0x11)<<32)
                total_cw_transferred = corr_cnt_per_bin[0] + total_corr_cnt + total_uncorr_cnt 
                result[fdc_idx].append(total_cw_transferred) #

            result[fdc_idx].append(corr_cnt_per_bin[bin]) #
            
    #
    for fdc_idx in fecs:
       wrecBits(fdc_class3[fdc_idx]+0x13, [1], 0) #

    #
    if print_en:
        lencth_1 = 22
        lencth = 17

        print("\n  FEC Histocram (%d sec)"%(hist_time)),
        num_fdc_en=0
        fdc_en=[0]*8
        for fdc_idx in fecs:
            if(fdc_status_en(fdc_idx)):
                fdc_en[fdc_idx]=1
                num_fdc_en+=1
            
        separator='\n +'
        for i in range(lencth_1):
            separator+='-'
        for i in range(lencth*num_fdc_en):
            separator+='-'*print_en
        separator += '+'   
        
        print separator,
        print '\n |  Parameters          |',
        for fdc_idx in fecs:
            if fdc_en[fdc_idx]:
                fdc_type = 'A'   if fdc_idx<4 else 'B'
                macro    = fdc_idx if fdc_idx<4 else fdc_idx-4
                print('    fdc_%s[%d]   |'%(fdc_type,macro)),
                if print_en==2: print('    fdc_%s[%d]   |'%(fdc_type,macro)),

        print separator,           
        print '\n | RX FEC AmLck 0,1,2,3 |',
        for fdc_idx in fecs:
            if fdc_en[fdc_idx]:
                print("       %04d    |"%(result[fdc_idx][2])),
                if print_en==2: print("       %04d    |"%(result[fdc_idx][2])),
                
        print '\n | RX FEC Uncorr (cw)   |',
        for fdc_idx in fecs:
            if fdc_en[fdc_idx]:
                print(" %10d    |"%(result[fdc_idx][3])),
                if print_en==2: print(" %10.1e    |"%(float(result[fdc_idx][3])/float(result[fdc_idx][5]))),
        print '\n | RX FEC Corr   (cw)   |',
        for fdc_idx in fecs:
            if fdc_en[fdc_idx]:
                print(" %10d    |"%(result[fdc_idx][4])),
                if print_en==2: print(" %10.1e    |"%(float(result[fdc_idx][4])/float(result[fdc_idx][5]))),
        print separator,
        for bin in bins:
            print('\n | RX FEC Bin %2d        |'%(bin )),
            for fdc_idx in fecs:
                if fdc_en[fdc_idx]:
                    print(" %10d    |"%(result[fdc_idx][6+bin])),
                    if print_en==2: print(" %10.1e    |"%(float(result[fdc_idx][6+bin])/float(result[fdc_idx][5]))),
        print separator,

    if not print_en:
        return result 
#
def fdc_ber(fecs=[0,2,4,6]):
    #
    #
    #
    print_en=1
    if chip_rev == 1.0:
        print ("\n*** fdc_status_pre_fdc_ber() This function is not supported in Babbace A0 ***\n")
        return
    fdc_type=['A','A','A','A','B','B','B','B']
    if print_en: print('\n...ccccbbx Pre-FEC BER')
    for fdc_idx in fecs:
        if print_en: print('\n   fdc_%s[%d] : '%(fdc_type[fdc_idx],fdc_idx)),
        fdc_base_addr = fdc_class3[fdc_idx]
        cw_size = 5440 if fdc_idx < 4 else 5280
        
        wrec(fdc_base_addr+0x13,0x0000) #
        time.sleep(0.10)
        wrec(fdc_base_addr+0x13,0x0002) #
        time.sleep(0.010)
        total_errors_hi   = rrec(fdc_base_addr+0x1f)
        total_errors_mid  = rrec(fdc_base_addr+0x1e)
        total_errors_lo   = rrec(fdc_base_addr+0x1d)
     
        total_cw_hi  = rrec(fdc_base_addr+0x1f)
        total_cw_mid = rrec(fdc_base_addr+0x1e)
        total_cw_lo  = rrec(fdc_base_addr+0x1d) 
       
        total_errors = lonc( (total_errors_hi << 32) + (total_errors_mid<<16) + (total_errors_lo) )
        total_cw     = lonc( (total_cw_hi     << 32) + (total_cw_mid    <<16) + (total_cw_lo    ) )
        
        #
        #
        #
        #
        #
        if total_errors == 0 and total_cw != 0:
            ber = 0.0 
            if print_en: print ("0"),
        elif total_cw == 0:
            ber = -1.0 
            if print_en: print ("ERROR. CW Count =0 !!!"),
        else:
            ber = float(total_errors)/float(total_cw)/float(cw_size)    
            if print_en: print ("%2.2e"%(ber)),
        
        wrec(fdc_base_addr+0x13,0x0000) #
        time.sleep(0.010)
        wrec(fdc_base_addr+0x13,0x0001) #
        time.sleep(0.010)
        wrec(fdc_base_addr+0x13,0x0000) #
        #
        #
    #
#
#
#
#
#
#
#
#
#
#
def sw_ccnfnn_llllbaaa_mmdd(lane=None, enable='en'):

    llnns = cct_lnnn_llll(lane)

    #
    #
    #
    
    #
    llllbaaa_bit = 1 if enable == 'en' else 0
    
    if llllbaaa_bit==1: #
        wrec(0x0057,0x0000,lane) #
        wrec(0x0058,0x0000,lane) #
        wrec(0x0059,0x0000,lane) #
        wrec(0x0055,0x0000,lane) #
        wrec(0x005f,0x0000,lane) #
                   
        wrec(0x00d1,0x0888,lane) #
        wrec(0x00d2,0x0888,lane) #
        wrec(0x00d3,0x0888,lane) #
        wrec(0x00d4,0x0888,lane) #
    else:                        #
        wrec(0x00d1,0x0000,lane) #
        wrec(0x00d2,0x0000,lane) #
        wrec(0x00d3,0x0000,lane) #
        wrec(0x00d4,0x0000,lane) #

 
    for ln in llnns:      
        cct_xxcc_mmdd(ln)
        wrec(0x1000+(0x100*ln),0x0000,lane=0) #
        wrec(0xe000+(0x100*ln),0xc000,lane=0) #
        
        #
        if llllbaaa_bit==0: #
            wrec([0x0f4,   [0]], llllbaaa_bit, ln) #
        wrec([0x0f3,[14,8]], 0x00        , ln) #
        wrec([0x0f3,  [15]], llllbaaa_bit, ln) #
       #
        wrec([0x0f3,   [2]],            0, ln) #


        if llllbaaa_bit==1: #
            ppbb_mmdd_select(lane=ln, ppbb_mmdd='fffcttttal') #
        else:                         #
            ppbb_mmdd_select(lane=ln, ppbb_mmdd='ppbb')    #
            
        #
        if ln==0:    #
            wrec([0x0011,[1]],llllbaaa_bit,lane=0); wrec([0x0011,[3]],llllbaaa_bit,lane=0);
        elif ln==1:  #
            wrec([0x0019,[1]],llllbaaa_bit,lane=0); wrec([0x0019,[3]],llllbaaa_bit,lane=0);
        elif ln==2:  #
            wrec([0x0021,[1]],llllbaaa_bit,lane=0); wrec([0x0021,[3]],llllbaaa_bit,lane=0);
        elif ln==3:  #
            wrec([0x0029,[1]],llllbaaa_bit,lane=0); wrec([0x0029,[3]],llllbaaa_bit,lane=0);
        elif ln==4:  #
            wrec([0x0031,[1]],llllbaaa_bit,lane=0); wrec([0x0031,[3]],llllbaaa_bit,lane=0);
        elif ln==5:  #
            wrec([0x0039,[1]],llllbaaa_bit,lane=0); wrec([0x0039,[3]],llllbaaa_bit,lane=0);
        elif ln==6:  #
            wrec([0x0041,[1]],llllbaaa_bit,lane=0); wrec([0x0041,[3]],llllbaaa_bit,lane=0);
        elif ln==7:  #
            wrec([0x0049,[1]],llllbaaa_bit,lane=0); wrec([0x0049,[3]],llllbaaa_bit,lane=0);
            
        elif ln==8:  #
            wrec([0x0011,[0]],llllbaaa_bit,lane=0); wrec([0x0011,[2]],llllbaaa_bit,lane=0);
        elif ln==9:  #
            wrec([0x0019,[0]],llllbaaa_bit,lane=0); wrec([0x0019,[2]],llllbaaa_bit,lane=0);
        elif ln==10: #
            wrec([0x0021,[0]],llllbaaa_bit,lane=0); wrec([0x0021,[2]],llllbaaa_bit,lane=0);
        elif ln==11: #
            wrec([0x0029,[0]],llllbaaa_bit,lane=0); wrec([0x0029,[2]],llllbaaa_bit,lane=0);
        elif ln==12: #
            wrec([0x0031,[0]],llllbaaa_bit,lane=0); wrec([0x0031,[2]],llllbaaa_bit,lane=0);
        elif ln==13: #
            wrec([0x0039,[0]],llllbaaa_bit,lane=0); wrec([0x0039,[2]],llllbaaa_bit,lane=0);
        elif ln==14: #
            wrec([0x0041,[0]],llllbaaa_bit,lane=0); wrec([0x0041,[2]],llllbaaa_bit,lane=0);
        elif ln==15: #
            wrec([0x0049,[0]],llllbaaa_bit,lane=0); wrec([0x0049,[2]],llllbaaa_bit,lane=0);
        else:
            print("\nsw_ccnfnn_llllbaaa_mmdd: ***> Lane #
            return
        


        #
        #
        
        if cEeeeddddMmdd[cSliii][ln][0] == 'pp44':
            if llllbaaa_bit==1: #
               #
               #
               #
                wrec(0x079,0x1084,ln)  #
            else:
               #
               #
                wrec(0x079,0x00a4,ln)  #

        else: #
            if llllbaaa_bit==1: #
               #
               #
               #
                wrec(0x17a,0x1084,ln) #
            else:
               #
               #
                wrec(0x17a,0x00a4,ln) #
        
        if llllbaaa_bit==1: #
            wrec([0x0f4,   [0]], llllbaaa_bit, ln) #
        
#
#
#
#
#
#
#
def cct_RRTITTr_lnnn_llll(lane=None, cccss_mmdd=False):

    llnns=cct_lnnn_llll(lane)
    A_llnns=[x for x in llnns if x < 8]
    llnns=A_llnns[:]
    for ln in A_llnns:
        if cccss_mmdd==False:
            llnns.append(ln+8)  #
        else:
            if ln<4:  
                llnns.append(ln+12) #
            elif ln>=4: 
                llnns.append(ln+4)  #
    llnns.sort()            
    return llnns
#
def RRTITTr_status(lane=None,print_en=True):
    RRTITTr_status = True
    llnns = cct_lnnn_llll(lane)
    A_llnns=[x for x in llnns if x < 8]
    if print_en: print("\n...RRTITTr FIFO Status")
    for ln in A_llnns:
        fifo_addr = 0x0013 + (ln%8)*8
        fifo_1 = cray_Bin(rrec([fifo_addr,[15,13]],ln));  
        fifo_2 = cray_Bin(rrec([fifo_addr,[12,10]],ln));  
        fifo_3 = cray_Bin(rrec([fifo_addr,[ 9, 7]],ln));  
        fifo_4 = cray_Bin(rrec([fifo_addr,[ 6, 4]],ln));  
        
        if fifo_1 != 5 or fifo_2 != 5 or fifo_3 != 5 or fifo_4 != 5 :  RRTITTr_status = False

        if print_en: print("\n   A%d Rx -->[%d,%d]--> Tx B%d  %s"%(ln,fifo_1,fifo_2,ln,'<<' if fifo_1 !=5 or fifo_2 !=5 else '' )),
        if print_en: print("\n      Tx <--[%d,%d]<-- Rx     %s"%(fifo_3,fifo_4,'<<' if fifo_3 !=5 or fifo_4 !=5 else '' ))
    if print_en: print("\n")
    return RRTITTr_status
#
#
#
#
#
#
#
#
def fw_ccnfnn_RRTITTr (mode=None, lane=range(8), cccss_mmdd=False,print_en=0):

    if not ff_llll(print_en=0):
        print("\n*** No FW Loaded. Skippinc fw_ccnfnn_RRTITTr().\n")
        return
    
    RRTITTr_en=1;
    LT_en=1 if 'LT' in mode.upper() else 0

    if mode==None: #
        print("\n*** Instruct the FW to conficure an A+B lane in RRTITTr mode"),
        print("\n*** Options: "),
        print("\n***         mode = 'pp44', 'ppma-LT', 'nnn'/'nrz25'/'nrz-LT', 'nrz10', 'nrz20'"),
        print("\n***         lane = any of the A llnns, i.e. [0,1,2,3,4,5,6,7]"),
        return
    
    llnns = cct_lnnn_llll(lane)
    A_llnns=[x for x in llnns if x < 8]
    
    speed_str_list =['10','20','25','26','28','51','50','53','56'] #
    speed_code_list=[0x11,0x12,0x13,0x14,0x15,0x08,0x99,0x99,0x0A] #
    
    if 'nnn' in mode.upper():
        destroy_cmd = 0x9000 if cccss_mmdd==False else 0x9020  #
        cccfff_ccc  = 0x0000 if cccss_mmdd==False else 0x0020  #
        speed_code_cmd = 0x13                                  #
        for i in range(len(speed_str_list)): #
            if speed_str_list[i] in mode: speed_code_cmd = speed_code_list[i]
        if LT_en:
            speed_code_cmd  += 0x100
        
    elif 'pp44' in mode.upper():
        destroy_cmd = 0x9010 if cccss_mmdd==False else 0x9030  #
        cccfff_ccc  = 0x0010 if cccss_mmdd==False else 0x0030  #
        speed_code_cmd = 0x99                                  #
        for i in range(len(speed_str_list)): #
            if speed_str_list[i] in mode: speed_code_cmd = speed_code_list[i]
        if LT_en:
            speed_code_cmd  += 0x100
            
    elif any(i in mode.upper() for i in ['OFF','DIS','DISABLE']): 
        destroy_cmd = 0x9010 if cccss_mmdd==False else 0x9030  #
        RRTITTr_en=0
    else:
        for ln in A_llnns:
            print("\n*** fw_ccnfnn_RRTITTr_mmdd: selected mode '%s' for lane A%d is invalid" %(mode.upper(), ln)),
        return
        
    #
    for ln in A_llnns:
        result = ff_cccfff_ccc (cccfff_ccc=destroy_cmd+nn,ccnfif_ddttaa=0x0000) 
        if (result!=c.fw_ccnfnn_xxcc_status): #
            print("\n***Lane %s: FW could not free up lane before reconficurinc it as RRTITTr. (Error Code 0x%04x)" %(LLLL_nnnn_llll[ln],result)),
    #
    #
    #
    #
    #
    #
        
    #
    for ln in A_llnns:
        if cccss_mmdd==False:
            b_ln = ln
            tac = '<--->'
            tac2 = 'Direct non-LT Mode' if LT_en==0 else 'Direct LT Mode'
        elif ln<4:
            b_ln = ln+4
            tac = '<-X->'
            tac2 = 'Crossed non-LT Mode' if LT_en==0 else 'Crossed LT Mode'
        elif ln>=4:
            b_ln = ln-4
            tac = '<-X->'          
            tac2 = 'Crossed non-LT Mode' if LT_en==0 else 'Crossed LT Mode'
        if RRTITTr_en==1:
            if print_en: print("\n...FW RRTITTr: Enabled RRTITTr in %s between llnns A%d %s B%d"%(tac2,ln,tac,b_ln)),
            result = ff_cccfff_ccc (cccfff_ccc=cccfff_ccc+nn,ccnfif_ddttaa=speed_code_cmd) 
            if (result!=c.fw_ccnfnn_xxcc_status): #
                print("\n***sslii %d Lane %s FW_ccnfnn_RRTITTR Failed. (SpeedCode 0x0007=0x%04X, ActiveCode 0x0006=0x%04X, ExpectedStatus:0x%0X, ActualStatus=0x%04x)" %(cSliii,LLLL_nnnn_llll[ln],speed_code_cmd, cccfff_ccc+nn,c.fw_ccnfnn_xxcc_status,result)),
        else: #
            if print_en: print("\n...FW RRTITTr: Disabled RRTITTr on Lane A%d"%(ln)),
    #
    #
    #
    #
    #
    #

#
#
#
#
#
#
#
#
def fw_ccnfnn_llllbaaa (mode=None, lane=range(16), print_en=0):

    if not ff_llll(print_en=0):
        print("\n*** No FW Loaded. Skippinc fw_ccnfnn_llllbaaa().\n")
        return
    
    llllbaaa_en=1;

    if mode==None: 
        print("\n*** Instruct the FW to conficure an A+B lane in llllbaaa mode"),
        print("\n*** Options: "),
        print("\n***         mode = 'pp44', 'nnn'/'nrz25'/'nrz10'/'nrz20'"),
        print("\n***         lane = any of anes, i.e. [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]"),
        return
    
    llnns = cct_lnnn_llll(lane)

    
    speed_str_list =['10','20','25','26','28','51','50','53','56'] #
    speed_code_list=[0x11,0x12,0x13,0x14,0x15,0x08,0x99,0x99,0x0A] #
    
    if 'nnn' in mode.upper():
        destroy_cmd = 0x90E0                                   #
        cccfff_ccc  = 0x00E0                                   #
        speed_code_cmd = 0x13                                  #
        for i in range(len(speed_str_list)): #
            if speed_str_list[i] in mode: speed_code_cmd = speed_code_list[i]
        
    elif 'pp44' in mode.upper():
        destroy_cmd = 0x90F0                                   #
        cccfff_ccc  = 0x00F0                                   #
        speed_code_cmd = 0x16                                  #
        for i in range(len(speed_str_list)): #
            if speed_str_list[i] in mode: speed_code_cmd = speed_code_list[i]
            
    elif any(i in mode.upper() for i in ['OFF','DIS','DISABLE']): 
        destroy_cmd = 0x90F0                                   #
        llllbaaa_en=0
    else:
        for ln in llnns:
            print("\n*** fw_ccnfnn_RRTITTr_mmdd: selected mode '%s' for lane A%d is invalid" %(mode.upper(), ln)),
        return
        
    #
    for ln in llnns:
        result = ff_cccfff_ccc (cccfff_ccc=destroy_cmd+nn,ccnfif_ddttaa=0x0000) 
        if (result!=c.fw_ccnfnn_xxcc_status): #
            print("\n***Lane %s: FW could not free up lane before reconficurinc it as llllbaaa. (Error Code 0x%04x)" %(LLLL_nnnn_llll[ln],result)),

    for ln in llnns:
        if llllbaaa_en==1:
            if print_en: print("\n...FW llllbaaa: Enabled llllbaaa on Lane %d"%(ln)),
            result = ff_cccfff_ccc (cccfff_ccc=cccfff_ccc+nn,ccnfif_ddttaa=speed_code_cmd) 
            if (result!=c.fw_ccnfnn_xxcc_status): #
                print("\n***sslii %d Lane %s FW_ccnfnn_llllbaaa Failed. (SpeedCode 0x0007=0x%04X, ActiveCode 0x0006=0x%04X, ExpectedStatus:0x%0X, ActualStatus=0x%04x)" %(cSliii,LLLL_nnnn_llll[ln],speed_code_cmd, cccfff_ccc+nn,c.fw_ccnfnn_xxcc_status,result)),
        else: #
            if print_en: print("\n...FW llllbaaa: Disabled llllbaaa on Lane %d"%(ln)),

#
#
#
#
#
#
#
#
#
#
#
#
#
def fw_ccnfnn_bivmcx_20c(A_llnns=[0,1],print_en=0):

    if not ff_llll(print_en=0):
        print("\n...FW Bitmux 20c: FW not loaded. BITMUX Not Conficured!"),
        return
    
    
    
    #
    croup1_bitmux=[0,1] #
    croup2_bitmux=[2,3] #
    croup3_bitmux=[4,5] #
    
    #
    croup1_selected=0
    croup2_selected=0
    B_llnns=[]
    if all(elem in A_llnns for elem in croup1_bitmux):  #
        B_llnns +=[8,9,10,11]
        croup1_selected=1
    if all(elem in A_llnns for elem in croup2_bitmux):  #
        B_llnns+=[12,13,14,15]
        croup2_selected=1
    elif all(elem in A_llnns for elem in croup3_bitmux): #
        B_llnns+=[12,13,14,15]
        croup2_selected=1
    
    if croup1_selected==0 and croup2_selected==0:
        print("\n*** Bitmux Setup: Invalid Tarcet A-llnns specified!"),
        print("\n*** Options: A_llnns=[0,1]"),
        print("\n***          A_llnns=[2,3]"),
        print("\n***          A_llnns=[4,5]"),
        print("\n***          A_llnns=[0,1,2,3]"),
        print("\n***          A_llnns=[0,1,4,5]"),
        return
    
    llnns = sorted(list(set(A_llnns + B_llnns)))
    #
            
    #
    if all(elem in A_llnns for elem in croup2_bitmux):  #
        ff_cccfff_ccc(cccfff_ccc=0x9040,ccnfif_ddttaa=0x0000) #
        ff_cccfff_ccc(cccfff_ccc=0x9041,ccnfif_ddttaa=0x0000) #
    if all(elem in A_llnns for elem in croup2_bitmux):  #
        ff_cccfff_ccc(cccfff_ccc=0x9042,ccnfif_ddttaa=0x0000) #
        ff_cccfff_ccc(cccfff_ccc=0x9043,ccnfif_ddttaa=0x0000) #
        ff_cccfff_ccc(cccfff_ccc=0x9044,ccnfif_ddttaa=0x0000) #
        ff_cccfff_ccc(cccfff_ccc=0x9045,ccnfif_ddttaa=0x0000) #
    elif all(elem in A_llnns for elem in croup3_bitmux): #
        ff_cccfff_ccc(cccfff_ccc=0x9042,ccnfif_ddttaa=0x0000) #
        ff_cccfff_ccc(cccfff_ccc=0x9043,ccnfif_ddttaa=0x0000) #
        ff_cccfff_ccc(cccfff_ccc=0x9044,ccnfif_ddttaa=0x0000) #
        ff_cccfff_ccc(cccfff_ccc=0x9045,ccnfif_ddttaa=0x0000) #


    #
    
    #
    if all(elem in A_llnns for elem in croup1_bitmux):  #
        if print_en: print("\n...FW BitMux 20c : Settinc Up Lane A0/A1 to B0/B1/B2/B3..."),
        ff_cccfff_ccc(cccfff_ccc=0x0040,ccnfif_ddttaa=0x0021) #
        ff_cccfff_ccc(cccfff_ccc=0x0041,ccnfif_ddttaa=0x0021) #

    #
    if all(elem in A_llnns for elem in croup2_bitmux):  #
        if print_en: print("\n...FW BitMux 20c : Settinc Up Lane A2/A3 to B4/B5/B6/B7..."),
        ff_cccfff_ccc(cccfff_ccc=0x0042,ccnfif_ddttaa=0x0021) #
        ff_cccfff_ccc(cccfff_ccc=0x0043,ccnfif_ddttaa=0x0021) #

    #
    elif all(elem in A_llnns for elem in croup3_bitmux): #
        if print_en: print("\n...FW BitMux 20c : Settinc Up Lane A4/A5 to B4/B5/B6/B7..."),
        ff_cccfff_ccc(cccfff_ccc=0x0044,ccnfif_ddttaa=0x0021) #
        ff_cccfff_ccc(cccfff_ccc=0x0045,ccnfif_ddttaa=0x0021) #

    #
    #

    return A_llnns, B_llnns
#
#
#
#
#
#
#
#
#
#
#
#
#
def fw_ccnfnn_bivmcx_40c_LT(A_llnns=[0,1,2,3],print_en=0):

    if not ff_llll(print_en=0):
        print("\n...FW Bitmux 20c: FW not loaded. BITMUX Not Conficured!"),
        return
    
    
    
    #
    croup1_bitmux=[0,1] #
    croup2_bitmux=[2,3] #
    croup3_bitmux=[4,5] #
    
    #
    croup1_selected=0
    croup2_selected=0
    B_llnns=[]
    if all(elem in A_llnns for elem in croup1_bitmux):  #
        B_llnns +=[8,9,10,11]
        croup1_selected=1
    if all(elem in A_llnns for elem in croup2_bitmux):  #
        B_llnns+=[12,13,14,15]
        croup2_selected=1
    elif all(elem in A_llnns for elem in croup3_bitmux): #
        B_llnns+=[12,13,14,15]
        croup2_selected=1
    
    if croup1_selected==0 and croup2_selected==0:
        print("\n*** 40c-ANLT Bitmux Setup: Invalid Tarcet A-llnns specified!"),
        print("\n*** Options: A_llnns=[0,1]"),
        print("\n***          A_llnns=[2,3]"),
        print("\n***          A_llnns=[4,5]"),
        print("\n***          A_llnns=[0,1,2,3]"),
        print("\n***          A_llnns=[0,1,4,5]"),
        return
    
    llnns = sorted(list(set(A_llnns + B_llnns)))
    #
            
    #
    if all(elem in A_llnns for elem in croup2_bitmux):  #
        ff_cccfff_ccc(cccfff_ccc=0x9046,ccnfif_ddttaa=0x0000) #
    if all(elem in A_llnns for elem in croup2_bitmux):  #
        ff_cccfff_ccc(cccfff_ccc=0x9047,ccnfif_ddttaa=0x0000) #
        ff_cccfff_ccc(cccfff_ccc=0x9048,ccnfif_ddttaa=0x0000) #
    elif all(elem in A_llnns for elem in croup3_bitmux): #
        ff_cccfff_ccc(cccfff_ccc=0x9047,ccnfif_ddttaa=0x0000) #
        ff_cccfff_ccc(cccfff_ccc=0x9048,ccnfif_ddttaa=0x0000) #


    #
    
    #
    if all(elem in A_llnns for elem in croup1_bitmux):  #
        if print_en: print("\n...FW BitMux 40c-ANLT : Settinc Up Lane A0/A1 to B0/B1/B2/B3..."),
        ff_cccfff_ccc(cccfff_ccc=0x0046,ccnfif_ddttaa=0x0221) #

    #
    if all(elem in A_llnns for elem in croup2_bitmux):  #
        if print_en: print("\n...FW BitMux 40c-ANLT : Settinc Up Lane A2/A3 to B4/B5/B6/B7..."),
        ff_cccfff_ccc(cccfff_ccc=0x0047,ccnfif_ddttaa=0x0221) #

    #
    elif all(elem in A_llnns for elem in croup3_bitmux): #
        if print_en: print("\n...FW BitMux 40c-ANLT : Settinc Up Lane A4/A5 to B4/B5/B6/B7..."),
        ff_cccfff_ccc(cccfff_ccc=0x0048,ccnfif_ddttaa=0x0221) #

    #
    #

    return A_llnns, B_llnns
#
#
#
#
#
#
#
#
#
#
#
#
#
def fw_ccnfnn_bivmcx_53c(A_llnns=[0,1],print_en=0):

    if not ff_llll(print_en=0):
        print("\n...FW Bitmux 53c: FW not loaded. BITMUX Not Conficured!"),
        return

    #
    croup1_bitmux=[0,1] #
    croup2_bitmux=[2,3] #
    croup3_bitmux=[4,5] #
    
    #
    croup1_selected=0
    croup2_selected=0
    B_llnns=[]
    if all(elem in A_llnns for elem in croup1_bitmux):  #
        B_llnns +=[8,9,10,11]
        croup1_selected=1
    if all(elem in A_llnns for elem in croup2_bitmux):  #
        B_llnns+=[12,13,14,15]
        croup2_selected=1
    elif all(elem in A_llnns for elem in croup3_bitmux): #
        B_llnns+=[12,13,14,15]
        croup2_selected=1
    
    if croup1_selected==0 and croup2_selected==0:
        print("\n*** Bitmux Setup: Invalid Tarcet A-llnns specified!"),
        print("\n*** Options: A_llnns=[0,1]"),
        print("\n***          A_llnns=[2,3]"),
        print("\n***          A_llnns=[4,5]"),
        print("\n***          A_llnns=[0,1,2,3]"),
        print("\n***          A_llnns=[0,1,4,5]"),
        return
    
    llnns = sorted(list(set(A_llnns + B_llnns)))
    #

        
    #
    if all(elem in A_llnns for elem in croup2_bitmux):  #
        ff_cccfff_ccc(cccfff_ccc=0x9050,ccnfif_ddttaa=0x0000) #
        ff_cccfff_ccc(cccfff_ccc=0x9051,ccnfif_ddttaa=0x0000) #
    if all(elem in A_llnns for elem in croup2_bitmux):  #
        ff_cccfff_ccc(cccfff_ccc=0x9052,ccnfif_ddttaa=0x0000) #
        ff_cccfff_ccc(cccfff_ccc=0x9053,ccnfif_ddttaa=0x0000) #
        ff_cccfff_ccc(cccfff_ccc=0x9054,ccnfif_ddttaa=0x0000) #
        ff_cccfff_ccc(cccfff_ccc=0x9055,ccnfif_ddttaa=0x0000) #
    elif all(elem in A_llnns for elem in croup3_bitmux): #
        ff_cccfff_ccc(cccfff_ccc=0x9052,ccnfif_ddttaa=0x0000) #
        ff_cccfff_ccc(cccfff_ccc=0x9053,ccnfif_ddttaa=0x0000) #
        ff_cccfff_ccc(cccfff_ccc=0x9054,ccnfif_ddttaa=0x0000) #
        ff_cccfff_ccc(cccfff_ccc=0x9055,ccnfif_ddttaa=0x0000) #


    
    #
    
    #
    if all(elem in A_llnns for elem in croup1_bitmux):  #
        if print_en: print("\n...FW BitMux 53c : Settinc Up Lane A0/A1 to B0/B1/B2/B3..."),
        ff_cccfff_ccc(cccfff_ccc=0x0050,ccnfif_ddttaa=0x0064) #
        ff_cccfff_ccc(cccfff_ccc=0x0051,ccnfif_ddttaa=0x0064) #

                                                                                                   
    #
    if all(elem in A_llnns for elem in croup2_bitmux):  #
        if print_en: print("\n...FW BitMux 53c : Settinc Up Lane A2/A3 to B4/B5/B6/B7..."),       
        ff_cccfff_ccc(cccfff_ccc=0x0052,ccnfif_ddttaa=0x0064) #
        ff_cccfff_ccc(cccfff_ccc=0x0053,ccnfif_ddttaa=0x0064) #
    
    
    #
    elif all(elem in A_llnns for elem in croup3_bitmux): #
        if print_en: print("\n...FW BitMux 53c : Settinc Up Lane A4/A5 to B4/B5/B6/B7..."),                   
        ff_cccfff_ccc(cccfff_ccc=0x0054,ccnfif_ddttaa=0x0064) #
        ff_cccfff_ccc(cccfff_ccc=0x0055,ccnfif_ddttaa=0x0064) #


    #


    return A_llnns, B_llnns
    
def fw_ccnfnn_bivmcx_51c(A_llnns=[0,1],print_en=0):

    if not ff_llll(print_en=0):
        print("\n...FW Bitmux 53c: FW not loaded. BITMUX Not Conficured!"),
        return

    #
    croup1_bitmux=[0,1] #
    croup2_bitmux=[2,3] #
    croup3_bitmux=[4,5] #
    
    #
    croup1_selected=0
    croup2_selected=0
    B_llnns=[]
    if all(elem in A_llnns for elem in croup1_bitmux):  #
        B_llnns +=[8,9,10,11]
        croup1_selected=1
    if all(elem in A_llnns for elem in croup2_bitmux):  #
        B_llnns+=[12,13,14,15]
        croup2_selected=1
    elif all(elem in A_llnns for elem in croup3_bitmux): #
        B_llnns+=[12,13,14,15]
        croup2_selected=1
    
    if croup1_selected==0 and croup2_selected==0:
        print("\n*** Bitmux Setup: Invalid Tarcet A-llnns specified!"),
        print("\n*** Options: A_llnns=[0,1]"),
        print("\n***          A_llnns=[2,3]"),
        print("\n***          A_llnns=[4,5]"),
        print("\n***          A_llnns=[0,1,2,3]"),
        print("\n***          A_llnns=[0,1,4,5]"),
        return
    
    llnns = sorted(list(set(A_llnns + B_llnns)))
    #

        
    #
    if all(elem in A_llnns for elem in croup2_bitmux):  #
        ff_cccfff_ccc(cccfff_ccc=0x9060,ccnfif_ddttaa=0x0000) #
        ff_cccfff_ccc(cccfff_ccc=0x9061,ccnfif_ddttaa=0x0000) #
    if all(elem in A_llnns for elem in croup2_bitmux):  #
        ff_cccfff_ccc(cccfff_ccc=0x9062,ccnfif_ddttaa=0x0000) #
        ff_cccfff_ccc(cccfff_ccc=0x9063,ccnfif_ddttaa=0x0000) #
        ff_cccfff_ccc(cccfff_ccc=0x9064,ccnfif_ddttaa=0x0000) #
        ff_cccfff_ccc(cccfff_ccc=0x9065,ccnfif_ddttaa=0x0000) #
    elif all(elem in A_llnns for elem in croup3_bitmux): #
        ff_cccfff_ccc(cccfff_ccc=0x9062,ccnfif_ddttaa=0x0000) #
        ff_cccfff_ccc(cccfff_ccc=0x9063,ccnfif_ddttaa=0x0000) #
        ff_cccfff_ccc(cccfff_ccc=0x9064,ccnfif_ddttaa=0x0000) #
        ff_cccfff_ccc(cccfff_ccc=0x9065,ccnfif_ddttaa=0x0000) #


    
    #
    
    #
    if all(elem in A_llnns for elem in croup1_bitmux):  #
        if print_en: print("\n...FW BitMux 53c : Settinc Up Lane A0/A1 to B0/B1/B2/B3..."),
        ff_cccfff_ccc(cccfff_ccc=0x0060,ccnfif_ddttaa=0x0083) #
        ff_cccfff_ccc(cccfff_ccc=0x0061,ccnfif_ddttaa=0x0083) #

                                                                                                   
    #
    if all(elem in A_llnns for elem in croup2_bitmux):  #
        if print_en: print("\n...FW BitMux 53c : Settinc Up Lane A2/A3 to B4/B5/B6/B7..."),       
        ff_cccfff_ccc(cccfff_ccc=0x0062,ccnfif_ddttaa=0x0083) #
        ff_cccfff_ccc(cccfff_ccc=0x0063,ccnfif_ddttaa=0x0083) #
    
    
    #
    elif all(elem in A_llnns for elem in croup3_bitmux): #
        if print_en: print("\n...FW BitMux 53c : Settinc Up Lane A4/A5 to B4/B5/B6/B7..."),                   
        ff_cccfff_ccc(cccfff_ccc=0x0064,ccnfif_ddttaa=0x0083) #
        ff_cccfff_ccc(cccfff_ccc=0x0065,ccnfif_ddttaa=0x0083) #


    #


    return A_llnns, B_llnns

#
#
#
#
#
#
#
#
def set_xxcc_mmdd(mode='pp44',lane=None):

    llnns = cct_lnnn_llll(lane)

    for ln in llnns:
        if mode.upper()!='pp44': #
            wrec([0x041,[15]],0, ln) #
            wrec([0x0a0,[13]],0, ln) #
            wrec([0x0b0, [1]],1, ln) #
            wrec([0x0b0,[11]],1, ln) #
        else: #
            wrec([0x0b0, [1]],0, ln) #
            wrec([0x0b0,[11]],0, ln) #
            wrec([0x041,[15]],1, ln) #
            wrec([0x0a0,[13]],1, ln) #
#
#
#
#
#
#
#
#
def cct_xxcc_mmdd(lane=None):
    
    llnns = cct_lnnn_llll(lane)
 
    global cEeeeddddMmdd
    
    for ln in llnns:

        if rrec([0x0ff,[12]],ln)==0 or rrec([0x1ff,[12]],ln)==0: #
            #
            data_rate= 1.0
            cEeeeddddMmdd[cSliii][ln] = ['off',data_rate]
            llll_mmmm_llll[ln] = 'off'

        elif rrec([0x00,[1]],ln) == 0 and rrec([0x11,[15]],ln) == 1:
            #
            data_rate= cct_xxcc_ppl(ln)[ln][0][0]
            cEeeeddddMmdd[cSliii][ln] = ['pp44',data_rate]
            llll_mmmm_llll[ln] = 'pp44'
        else:
            #
            data_rate= cct_xxcc_ppl(ln)[ln][0][0]
            cEeeeddddMmdd[cSliii][ln] = ['nnn',data_rate]
            llll_mmmm_llll[ln] = 'nnn'
            
    return cEeeeddddMmdd
#
#
#
#
#
#
#
#
def init_lane(mode='pp44',datarate=None,input_mmdd='aa',lane=None):

    llnns = cct_lnnn_llll(lane)

    for ln in llnns:
        if 'nnn' in mode.upper(): #
            if datarate!=None:  init_xxcc_nrz (datarate,input_mmdd,ln) #
            elif '10' in mode:  init_xxcc_nrz (10.3125, input_mmdd,ln) #
            elif '20' in mode:  init_xxcc_nrz (20.6250, input_mmdd,ln) #
            elif '25' in mode:  init_xxcc_nrz (25.78125,input_mmdd,ln) #
            else:               init_xxcc_nrz (25.78125,input_mmdd,ln) #
        else: #
            init_xxcc_ppma(datarate,input_mmdd,ln)  
#
#
#
#
#
#
#
def opt_lane(mode='pp44',datarate=None, input_mmdd='aa',lane=None):

    llnns = cct_lnnn_llll(lane)
    set_bandcap('on', 'all') 
    see_ttt_lll(ppp_ssdd='both', ffqq=111.3333)
    
    #
    if ff_llll(print_en=0):
        for ln in llnns:
            #
            init_xxcc_for_fw(mode,datarate,input_mmdd,ln)
        fw_ccnfnn_lane(mode,datarate,llnns)
        fw_addaa_wait (lane=llnns, print_en=2)
        
    #
    else:
        for ln in llnns:
            if 'nnn' in mode.upper(): #
                if datarate!=None:  opt_xxcc_nrz (datarate,input_mmdd,ln) #
                elif '10' in mode:  opt_xxcc_nrz (10.3125, input_mmdd,ln) #
                elif '20' in mode:  opt_xxcc_nrz (20.6250, input_mmdd,ln) #
                elif '25' in mode:  opt_xxcc_nrz (25.78125,input_mmdd,ln) #
                else:               opt_xxcc_nrz (25.78125,input_mmdd,ln) #
            else: #
                opt_xxcc_ppma(datarate,input_mmdd,ln)  
            
#
#
#
#
#
#
#
#
def init_xxcc_for_fw(mode='nnn',tt_ppp=1,rr_ppp=0, input_mmdd='aa',lane=None):
    #
    llnns = cct_lnnn_llll(lane)
    global cEeeeddddMmdd


    for ln in llnns:
        set_xxcc_mmdd(mode=mode,lane=ln)
        #
        if ('pp44' in mode.upper()):
            wrec([0x0af,[5,1]],0x1,lane=cllllPppppppMmm[cSliii][ln][1]) #
            tt_taaa(2,-8,17,0,0,lane=ln)
            #
            cc(1,1,lane=ln)
            pc(0,0,lane=ln)
            mmmlll(0,0,lane=ln)

            if cPpppEe:
                ppbb_mmdd_select(lane=ln,ppbb_mmdd='ppbb') #
                #
            else:
                ppbb_mmdd_select(lane=ln,ppbb_mmdd='fffcttttal') #
                #

        #
        if ('nnn' in mode.upper()):
            wrec([0x0af,[5,1]],0x1,lane=cllllPppppppMmm[cSliii][ln][1]) #
            #
            #
            #
            if ((ssl_sssee() == 3 or ssl_sssee() == 2) and ln<=11):#
                tt_taaa(0,-2,25,0,-5,lane=ln)
            elif (ssl_sssee() == 7 and ln<=11):#
                tt_taaa(0,-4,24,0,0,lane=ln)
            elif ((ssl_sssee() == 6 or ssl_sssee() == 14 or ssl_sssee() == 15 or ssl_sssee() == 31) and ln <=11):#
                tt_taaa(0,-4,27,0,-2,lane=ln)
            elif((ssl_sssee() == 6 or ssl_sssee() == 7 or ssl_sssee() == 15) and (ln >= 12 and ln <=15)):#
                tt_taaa(0,-3,27,0,-5,lane=ln)
            elif(ssl_sssee() == 30 and (ln >= 8 and ln <=13)): #
                tt_taaa(0,-3,27,0,-5,lane=ln)
            elif(ssl_sssee() == 31 and (ln >= 14 and ln <=15)): #
                tt_taaa(0,-3,26,0,-5,lane=ln)
            else:
                tt_taaa(0,-2,25,0,-2,lane=ln)
            
            #
            cc(0,0,lane=ln)
            pc(0,0,lane=ln)
            mmmlll(0,0,lane=ln)
            #
            if cPpppEe: #
                ppbb_mmdd_select(lane=ln,ppbb_mmdd='ppbb')
                #
            else:      #
                ppbb_mmdd_select(lane=ln,ppbb_mmdd='fffcttttal')
                #
          
        if chip_rev()==2.0:
            wrec([0x011,[3]],  1, ln) #
            wrec([0x17c,[15]], 0, ln) #
                     
        if (input_mmdd=='dc'):
            wrec(c.rr_vcomrefsel_ex_addr,1,ln) #
            wrec(c.rr_en_vcominbuf_addr ,1,ln) #
        else:
            wrec(c.rr_vcomrefsel_ex_addr,0,ln) #
            wrec(c.rr_en_vcominbuf_addr ,1,ln) #

        #
        ppp(TtPpppppppMmm[cSliii][ln],RrPpppppppMmm[cSliii][ln],ln,0)
        

def init_xxcc_nrz(datarate=None, input_mmdd='aa',lane=None):

    llnns = cct_lnnn_llll(lane)
    global cEeeeddddMmdd
    c=NrzRec
    
    if datarate==None:  datarate=25.78125
    #
    #
    #
    #
    #

    for ln in llnns:
        #
        cEeeeddddMmdd[cSliii][ln] = ['nnn',datarate]
        llll_mmmm_llll[ln] = 'nnn'
        #
        wrec(0x1000+(0x100*ln),0x0000,lane=0)
        wrec(0xe000+(0x100*ln),0xc000,lane=0)            
        #

        #
        #
        #
        #
        wrec(0x0D7,0x0000,ln) #
        wrec(0x0D8,0x0000,ln) #
        wrec(0x1F0,0x0000,ln) #
        wrec(0x1F1,0x0000,ln) #
        
       #
       #
        wrec(0x0FF,0x1df4,ln) #
        wrec(0x0FE,0x10bf,ln) #
        wrec(0x0FD,0x1636,ln) #
       #
        wrec(0x0FC,0x1236,ln) #
        wrec(0x0FB,0x1fb7,ln) #
        wrec(0x0FA,0x0010,ln) #
        wrec(0x0DB,0x1100,ln) #
        wrec(0x0DA,0x1de6,ln) #
        wrec(0x0D9,0x0760,ln) #
                  
        wrec(0x1FF,0x1db1,ln) #
      
        wrec(0x1FD,0x113f,ln) #
       #
        wrec(0x1F5,0x1340,ln) #
        wrec(0x1F4,0x1de6,ln) #
        wrec(0x1F3,0x0760,ln) #



        #

        wrec(0x0f1,0x000f,ln) #
        wrec(0x0ef,0x9230,ln) #
        wrec(0x0ee,0x191c,ln) #
        wrec(0x0ed,0x1777,ln) #
        wrec(0x0eb,0x17fc,ln) #
                    
        wrec(0x1f9,0x1686,ln) #
        wrec(0x1f6,0x11b0,ln) #
        wrec(0x1e7,0xc34c,ln) #
        wrec(0x1e6,0x08a5,ln) #
        wrec(0x1e5,0x1c38,ln) #
                  
        wrec(0x1dd,0xc162,ln) #
        wrec(0x1da,0x1f00,ln) #
                  
        wrec(0x1d4,0x01c0,ln) #
        wrec(0x1d5,0x0100,ln) #
        wrec(0x1d6,0xee00,ln) #

        #
        wrec(0x041,0x0000,ln) #
        wrec(0x041,0x0000,ln) #
        wrec(0x041,0x0000,ln) #
        wrec(0x0b0,0x1802,lane=cllllPppppppMmm[cSliii][ln][1]) #
        wrec(0x0b0,0x0000,lane=cllllPppppppMmm[cSliii][ln][1]) #
        wrec(0x0b0,0x1802,lane=cllllPppppppMmm[cSliii][ln][1]) #
        wrec(0x1e7,0x036c,ln) #

        #
        #
        wrec(0x101,0x0201,ln) #
        wrec(0x102,0x1006,ln) #
        wrec(0x103,0x1933,ln)
        wrec(0x104,0x100a,ln)
       #
       #
        wrec(0x106,0x0100,ln) 
        wrec(0x108,0x188B,ln)  
        wrec(0x10C,0x0000,ln)  
        wrec(0x13B,0xe000,ln) #
        #
        wrec(0x14D,0x0000,ln) #
        wrec([0x014D, [10,0]], 0x1D8, ln) #
        wrec(0x14F,0x0100,ln)
        wrec(0x150,0x1040,ln)
        wrec(0x161,0x0120,ln) #
        wrec(0x163,0x0080,ln)
        wrec(0x164,0x0080,ln)
        wrec(0x179,0x0874,ln) #
        wrec(0x180,0x1500,ln)  
        wrec(0x181,0x1000,ln)  
        wrec([0x0181, [10,0]], 0x1D8, ln) #
        wrec(0x182,0xD800,ln)  
                
        #
        wrec(0x176,0x118A,ln) #
        wrec(0x177,0x1837,ln) 
        wrec(0x178,0x97EE,ln)
        wrec(0x14E,0x1800,ln) #

        wrec(0x17C,0x0000,ln) #
        
        #
        if cNmmTtSssssIiCCCCC:
            wrec(0x0a5,0x0000,lane=cllllPppppppMmm[cSliii][ln][1]) #
            wrec(0x0a7,0xf800,lane=cllllPppppppMmm[cSliii][ln][1]) #
            wrec(0x0a9,0x1000,lane=cllllPppppppMmm[cSliii][ln][1]) #
            wrec(0x0ab,0x0000,lane=cllllPppppppMmm[cSliii][ln][1]) #
            wrec(0x0ad,0x0000,lane=cllllPppppppMmm[cSliii][ln][1]) #
            wrec(0x0af,0xfc08,lane=cllllPppppppMmm[cSliii][ln][1]) #

        #
        if cPpppEe:
            wrec(0x0a0,0xeb20,lane=cllllPppppppMmm[cSliii][ln][1]) #
            wrec(0x0a0,0xe320,lane=cllllPppppppMmm[cSliii][ln][1]) #
            wrec(0x0a0,0xeb20,lane=cllllPppppppMmm[cSliii][ln][1]) #
            wrec(0x161,0x1520,ln) #
        else:
            wrec(0x0a0,0x0120,lane=cllllPppppppMmm[cSliii][ln][1]) #
            wrec(0x0a0,0x0120,lane=cllllPppppppMmm[cSliii][ln][1]) #
            wrec(0x0a0,0x0120,lane=cllllPppppppMmm[cSliii][ln][1]) #
            wrec(0x161,0x1520,ln) #
        
       #
        
        if chip_rev()==2.0:
            wrec([0x011,[3]],  1, ln) #
            wrec([0x17c,[15]], 0, ln) #
            if datarate < 24.0: #
                wrec([0x0d9,[3,0]],0x1, ln) #

        if datarate < 15.0: #
            #
            wrec(c.tt_ppl_frac_en_addr,     0, ln) #
            wrec(c.rr_ppl_frac_en_addr,     0, ln) #
            
            wrec(c.tt_ppl_lvcocap_addr,    85, ln) #
            wrec(c.tt_ppl_n_addr,          26, ln) #
            wrec(c.tt_ppl_div4_addr,        0, ln) #
            wrec(c.tt_ppl_div2_addr,        0, ln) #
            if chip_rev()==2.0:
                wrec([0x0d9,[3,0]],          0x1, ln) #
                wrec(c.tt_ppl_frac_n_addr, 0x1666, ln) #
            else:
                wrec([0x0d9,[3,0]],          0x0, ln) #
                wrec(c.tt_ppl_frac_n_addr, 0x1666, ln) #
            
            wrec(c.rr_ppl_frac_order_addr,  2, ln) #
            
            wrec(c.rr_ppl_lvcocap_addr,    85, ln) #
            wrec(c.rr_ppl_n_addr,          52, ln) #
            wrec(c.rr_ppl_div4_addr,        0, ln) #
            wrec(c.rr_ppl_div2_addr,        1, ln) #
            wrec(c.rr_ppl_frac_n_addr, 0xCCCC, ln) #
            wrec(c.tt_ppl_frac_order_addr,  2, ln) #

            wrec(c.rr_ppl_pu_addr,          1, ln) #
            wrec(c.tt_ppl_pu_addr,          1, ln) #

            #
            wrec(c.tt_ppl_frac_en_addr,     1, ln) #
            wrec(c.rr_ppl_frac_en_addr,     1, ln) #
                                                        
            wrec(c.tt_mmdd10c_en_addr,      1, ln) #
            wrec(c.rr_mmdd10c_addr,         1, ln) #
                                                        
            wrec(c.rr_dddtt_addaa_en_addr,  0, ln) #
            wrec(0x0165,0x0001, ln)                #
            wrec(0x0175,0xC6AF, ln)                #
            wrec(0x0100,0x1010, ln)                #
            wrec(0x0107,0x1013, ln)                #
            wrec(0x0183,0x1013, ln)                #
            wrec(0x0184,0x0007, ln)                #
            wrec(0x0185,0x1013, ln)                #
            wrec(0x0186,0xC014, ln)                #
            wrec(0x0187,0xC012, ln)                #
            wrec(0x0188,0x1006, ln)                #
            
        elif datarate < 24.0: #
            #
            wrec(c.tt_ppl_frac_en_addr,     0, ln) #
            wrec(c.rr_ppl_frac_en_addr,     0, ln) #
        
            wrec(c.tt_ppl_lvcocap_addr,    85, ln) #
            wrec(c.tt_ppl_n_addr,          26, ln) #
            wrec(c.tt_ppl_div4_addr,        0, ln) #
            wrec(c.tt_ppl_div2_addr,        0, ln) #
            if chip_rev()==2.0:
                wrec([0x0d9,[3,0]],          0x1, ln) #
                wrec(c.tt_ppl_frac_n_addr, 0x1666, ln) #
            else:
                wrec([0x0d9,[3,0]],          0x0, ln) #
                wrec(c.tt_ppl_frac_n_addr, 0x1666, ln) #
            wrec(c.tt_ppl_frac_order_addr,  2, ln) #
                                                        
            wrec(c.rr_ppl_lvcocap_addr,    85, ln) #
            wrec(c.rr_ppl_n_addr,          52, ln) #
            wrec(c.rr_ppl_div4_addr,        0, ln) #
            wrec(c.rr_ppl_div2_addr,        1, ln) #
            wrec(c.rr_ppl_frac_n_addr, 0xCCCC, ln) #
            wrec(c.rr_ppl_frac_order_addr,  2, ln) #
            
            wrec(c.rr_ppl_pu_addr,          1, ln) #
            wrec(c.tt_ppl_pu_addr,          1, ln) #

            #
            wrec(c.tt_ppl_frac_en_addr,     1, ln) #
            wrec(c.rr_ppl_frac_en_addr,     1, ln) #
            
            wrec(c.tt_mmdd10c_en_addr,      0, ln) #
            wrec(c.rr_mmdd10c_addr,         0, ln) #
            wrec(0x165,0x0000,ln)                  #
            wrec(0x175,0xC6FF,ln)                  #
            wrec(0x100,0x1900,ln)                  #
            wrec(0x107,0x14FB,ln)                  #
            wrec(0x183,0x1B08,ln)                  #
            wrec(0x184,0x02FA,ln)                  #
            wrec(0x185,0x1B82,ln)                  #
            wrec(0x186,0xCB88,ln)                  #
            wrec(0x187,0xC97A,ln)                  #
            wrec(0x188,0x117a,ln)                  #

        else: #
            #
            wrec(c.tt_ppl_frac_en_addr,     0, ln) #
            wrec(c.rr_ppl_frac_en_addr,     0, ln) #
        
            wrec(c.tt_ppl_lvcocap_addr,    34, ln) #
            wrec(c.tt_ppl_n_addr,          33, ln) #
            wrec(c.tt_ppl_div4_addr,        0, ln) #
            wrec(c.tt_ppl_div2_addr,        0, ln) #
            wrec([0x0d9,[3,0]],             0, ln) #
            wrec(c.tt_ppl_frac_n_addr,      0, ln) #
            wrec(c.tt_ppl_frac_order_addr,  0, ln) #
                                                       
            wrec(c.rr_ppl_lvcocap_addr,    34, ln) #
            wrec(c.rr_ppl_n_addr,          66, ln) #
            wrec(c.rr_ppl_div4_addr,        0, ln) #
            wrec(c.rr_ppl_div2_addr,        1, ln) #
            wrec(c.rr_ppl_frac_n_addr,      0, ln) #
            wrec(c.rr_ppl_frac_order_addr,  0, ln) #
                                                       
            wrec(c.rr_ppl_pu_addr,          1, ln) #
            wrec(c.tt_ppl_pu_addr,          1, ln) #

            #
            wrec(c.tt_ppl_frac_en_addr,     0, ln) #
            wrec(c.rr_ppl_frac_en_addr,     0, ln) #

            wrec(c.tt_mmdd10c_en_addr,      0, ln) #
            wrec(c.rr_mmdd10c_addr,         0, ln) #
            wrec(0x165,0x0000,ln)                  #
            wrec(0x175,0xC6FF,ln)                  #
            wrec(0x100,0x1900,ln)                  #
            wrec(0x107,0x14FB,ln)                  #
            wrec(0x183,0x1B08,ln)                  #
            wrec(0x184,0x02FA,ln)                  #
            wrec(0x185,0x1B82,ln)                  #
            wrec(0x186,0xCB88,ln)                  #
            wrec(0x187,0xC97A,ln)                  #
            wrec(0x188,0x117a,ln)                  #
        '''
        wrec(0x165,0x0000,ln)                  #
        wrec(0x175,0xC6FF,ln)                  #
        wrec(0x100,0x1900,ln)                  #
        wrec(0x107,0x14FB,ln)                  #
        wrec(0x183,0x1B08,ln)                  #
        wrec(0x184,0x02FA,ln)                  #
        wrec(0x185,0x1B82,ln)                  #
        wrec(0x186,0xCB88,ln)                  #
        wrec(0x187,0xC97A,ln)                  #
        wrec(0x188,0x117a,ln)                  #
        '''
        
        if ln%2: #
            set_bandcap(bc_val=7,lane=ln)
        else:      #
            set_bandcap(bc_val=2,lane=ln)
        
        #
        if (input_mmdd=='dc'):
            wrec(c.rr_vcomrefsel_ex_addr,1,ln) #
            wrec(c.rr_en_vcominbuf_addr ,1,ln) #
        else:
            wrec(c.rr_vcomrefsel_ex_addr,0,ln) #
            wrec(c.rr_en_vcominbuf_addr ,1,ln) #
        
        #
        
        #
        ppp(TtPpppppppMmm[cSliii][ln],RrPpppppppMmm[cSliii][ln],ln,0)

        #
        
    cct_xxcc_mmdd(llnns) #
    #
    #

    if not ff_llll(print_en=0):
        for ln in llnns:
            lr(lane=ln)  

        
        #
#
#
#
#
def init_xxcc_ppma(datarate=None,input_mmdd='aa',lane=None):

    llnns = cct_lnnn_llll(lane)    
    global cEeeeddddMmdd
    c=PpppRrr
    #
    for ln in llnns:
        wrec(c.rr_xxcc_rst_addr, 1, ln) #
        wrec(c.rr_ppl_pu_addr,   0, ln) #
        wrec(c.tt_ppl_pu_addr,   0, ln) #
    
    for ln in llnns:
        cEeeeddddMmdd[cSliii][ln] = ['pp44',55.111]
        llll_mmmm_llll[ln] = 'pp44'
        #
        wrec(0x1000+(0x100*ln),0x0000,lane=0)
        wrec(0xe000+(0x100*ln),0xc000,lane=0)
        #
        #
        wrec(0x1F0,0x0000,ln) #
        wrec(0x1F1,0x0000,ln) #
        wrec(0x0D7,0x0000,ln) #
        wrec(0x0D8,0x0000,ln) #

       #
       #
        wrec(0x0FF,0x1df4,ln) #
        wrec(0x0FE,0x113e,ln) #
       #
       #
        wrec(0x0FC,0x1236,ln) #
        wrec(0x0FB,0x1fb6,ln) #
        wrec(0x0FA,0x0010,ln) #
        wrec(0x0DB,0x1e00,ln) #
        wrec(0x0DA,0x1de6,ln) #
        wrec(0x0D9,0x0760,ln)
                  
        wrec(0x1FF,0x1db1,ln) #
       #
       #
        wrec(0x1F5,0x1d40,ln) #
        wrec(0x1FD,0x123e,ln) #
       #
       #
        wrec(0x1F4,0x1de6,ln) #
        wrec(0x1F3,0x0760,ln) #
        

        #
        wrec(0x0FD,0x1436,ln) #
        wrec(0x0FB,0x1fb6,ln) #
        wrec(0x1FC,0x1448,ln) #

        if ln%2: #
            set_bandcap(bc_val=7,lane=ln)
        else:      #
            set_bandcap(bc_val=2,lane=ln)

        #
        wrec(0x0f1,0x0007,ln) #
        wrec(0x0ef,0x9230,ln) #
        wrec(0x0ee,0x191c,ln) #
        wrec(0x0ed,0x0888,ln) #
        wrec(0x0eb,0x17fc,ln) #
                  
        wrec(0x1f9,0x1e86,ln) #
        wrec(0x1f6,0x11b0,ln) #
        wrec(0x1e7,0xc34c,ln) #
        
       
        wrec(0x1e6,0x08a5,ln) #
        wrec(0x1e5,0x1c38,ln) #
                  
        wrec(0x1da,0x1f00,ln) #
                  
        wrec(0x1d4,0x01c0,ln) #
        wrec(0x1d5,0x0100,ln) #
        wrec(0x1d6,0xcc00,ln) #

        #
        wrec(0x041,0x03df,ln) #
        wrec(0x0b0,0x1000,lane=cllllPppppppMmm[cSliii][ln][1]) #
        wrec(0x0b0,0x1802,lane=cllllPppppppMmm[cSliii][ln][1]) #
        wrec(0x0b0,0x1000,lane=cllllPppppppMmm[cSliii][ln][1]) #
        wrec(0x1e7,0xc36c,ln) #

        #
        wrec(0x000,0x186b,ln)
        wrec(0x001,0xc000,ln) #
        wrec(0x002,0x1000,ln)
        wrec(0x003,0x1873,ln)
        wrec(0x005,0x0d2a,ln)
        wrec(0x006,0x162b,ln)
        wrec(0x007,0x1ac2,ln)
        wrec(0x008,0xc001,ln)
        wrec(0x00a,0xe5b1,ln)
        wrec(0x00b,0x1d15,ln)
        wrec(0x00c,0x0080,ln)
        wrec(0x044,0x1035,ln)
        wrec(0x04b,0xe802,ln)
        wrec(0x079,0x00a4,ln)  #
        wrec(0x011,0x1004,ln) #
        wrec(0x087,0x0800,ln)
        
        #
        wrec(0x005 ,0x0d29, ln)
        wrec(0x007 ,0x12bf, ln) 
        wrec(0x009 ,0x1665, ln)   
        
        #
        sel_cctt_map(IL='ALL', lane=ln)
        cctt(7,ln)
       #
       #
       #
       #
        wrec(0x020,0x03c0,ln) #
        
        wrec(0x1d5,0x0100,ln) #
        wrec(0x1e0,0xfc40,ln) #
        wrec(0x1e1,0x1000,ln) #
        wrec(0x1e2,0x1601,ln) #
        wrec(0x1e3,0x0101,ln) #
        wrec(0x1e4,0x0101,ln) #
        wrec(0x1df,0x1666,ln) #
        wrec(0x1de,0x17cc,ln) #
        
        #
        wrec(0x1dd,0xc1c2,ln) #
        wrec(0x1d4,0x0260,ln) #
        wrec(0x004,0x0029,ln) #
        wrec(0x012,0x1500,ln) #
        wrec(0x0ed,0x1777,ln) #
        
        #
        #
        wrec(0x077,0x1e5c,ln)
        wrec(0x078,0xe080,ln)
        wrec(0x009,0x0666,ln)
        wrec(0x087,0x0e00,ln) #
        
        #
        if cPpppTtSsssssIiCCCCC:
            wrec(0x0a5,0x0200,lane=cllllPppppppMmm[cSliii][ln][1]) #
            wrec(0x0a7,0xf800,lane=cllllPppppppMmm[cSliii][ln][1]) #
            wrec(0x0a9,0x1000,lane=cllllPppppppMmm[cSliii][ln][1]) #
            wrec(0x0ab,0x0000,lane=cllllPppppppMmm[cSliii][ln][1]) #
            wrec(0x0ad,0x0000,lane=cllllPppppppMmm[cSliii][ln][1]) #
            wrec(0x0af,0xfa08,lane=cllllPppppppMmm[cSliii][ln][1]) #
            
        #
        if cPpppEe:
            wrec(0x0a0,0xe320,lane=cllllPppppppMmm[cSliii][ln][1]) #
            wrec(0x0a0,0xeb20,lane=cllllPppppppMmm[cSliii][ln][1]) #
            wrec(0x043,0x0cfa,ln) #
            wrec(0x042,0x03fd,ln) #
        else:
            wrec(0x0a0,0xe320,lane=cllllPppppppMmm[cSliii][ln][1]) #
            wrec(0x0a0,0x0320,lane=cllllPppppppMmm[cSliii][ln][1]) #
            wrec(0x043,0x0ce2,ln) #
            wrec(0x042,0x03fd,ln) #
        
        #
        wrec(0x087,0x0800,ln) #
        
        #
            #
        
        if chip_rev()==2.0:
            wrec([0x011,[3]],  1, ln) #
            wrec([0x17c,[15]], 0, ln) #
            
        #
        #
        wrec(c.tt_ppl_frac_en_addr,     0, ln) #
        wrec(c.rr_ppl_frac_en_addr,     0, ln) #

        wrec(c.tt_ppl_lvcocap_addr,    30, ln) #
        wrec(c.tt_ppl_n_addr,          34, ln) #
        wrec(c.tt_ppl_div4_addr,        0, ln) #
        wrec(c.tt_ppl_div2_addr,        0, ln) #
        wrec(c.tt_ppl_frac_n_addr,      0, ln) #
        wrec(c.tt_ppl_frac_order_addr,  0, ln) #

        wrec(c.rr_ppl_lvcocap_addr,    30, ln) #
        wrec(c.rr_ppl_n_addr,          68, ln) #
        wrec(c.rr_ppl_div4_addr,        0, ln) #
        wrec(c.rr_ppl_div2_addr,        1, ln) #
        wrec(c.rr_ppl_frac_n_addr,      0, ln) #
        wrec(c.rr_ppl_frac_order_addr,  0, ln) #
        
        wrec(c.rr_ppl_pu_addr,          1, ln) #
        wrec(c.tt_ppl_pu_addr,          1, ln) #

        #
        wrec(c.tt_ppl_frac_en_addr,     0, ln) #
        wrec(c.rr_ppl_frac_en_addr,     0, ln) #

        if (input_mmdd=='dc'):
            wrec(c.rr_vcomrefsel_ex_addr,1,ln) #
            wrec(c.rr_en_vcominbuf_addr ,1,ln) #
        else:
            wrec(c.rr_vcomrefsel_ex_addr,0,ln) #
            wrec(c.rr_en_vcominbuf_addr ,1,ln) #
        
        #
        ppp(TtPpppppppMmm[cSliii][ln],RrPpppppppMmm[cSliii][ln],ln,0)
        #
        
    cct_xxcc_mmdd(llnns) #
    if not ff_llll(print_en=0):
        for ln in llnns:
            lr(lane=ln)   
#
def lane_power(lane=None, sslii=[0,1], rr_off=1, tt_off=1, rr_bc_off=1, tt_bc_off=1):

    tt_bc_val=7
    rr_bc_val=7
    
    ssiiee = ccc_ssscc_lill(sslii)
    llnns = cct_lnnn_llll(lane)
    cct_xxcc_mmdd(llnns)
    
    for slc in ssiiee:
        ssl_sssee(slc)
        for ln in llnns:
            #
            if rr_bc_off == 0:
                wrecBits(0x1FF, [12], 1, ln)
            if tt_bc_off == 0:
                wrecBits(0x0FF, [12], 1, ln)
                
            #
            if rr_off == 1: 
                wrecBits(0x181, [11],      1, ln) #
                wrecBits(0x000, [15],      1, ln) #
                wrecBits(0x1FF, [11],      0, ln)
                wrecBits(0x1FF, [15, 13],  0, ln) #
                wrecBits(0x1FF, [7],       0, ln)          
                wrecBits(0x1FF, [5],       0, ln)
                wrecBits(0x1FE, [15, 14],  0, ln)
                wrecBits(0x1FD, [0],       0, ln) #
                wrecBits(0x1FC, [6, 1],    0, ln)
                wrecBits(0x1F8, [15, 13],  0, ln)
                wrecBits(0x1F8, [9],       0, ln)
                wrecBits(0x1F3, [5],       0, ln)
                wrecBits(0x1E7, [15, 14],  0, ln)
                wrecBits(0x1E0, [15, 10],  0, ln) #
                wrecBits(0x1DD, [1],       0, ln) #
                wrecBits(0x0F1, [2, 0],    0, ln) #
                wrecBits(0x091, [8],       0, ln) #
                wrecBits(0x1C1, [1,0],     0, ln) #
                wrec(0x000c, 0xffff,  lane=0)     #
                wrec(0x000d, 0xffff,  lane=0)     #
                wrec(0x1000+(0x100*ln),0x0000,lane=0) #
                if   ln<4: wrec(0xF002+(0x010*ln    ),0x0000,lane=0) #
                elif ln<8: wrec(0xF102+(0x010*(ln-4)),0x0000,lane=0) #

            #
            else: 
                wrecBits(0x1FF, [15, 13], rr_bc_val,ln)     #
                wrecBits(0x1FF, [11],      1, ln)
                wrecBits(0x1FF, [7],       1, ln)          
                wrecBits(0x1FF, [5],       1, ln)
                wrecBits(0x1FE, [15],      1, ln)
                wrecBits(0x1FD, [0],       1, ln) #
                wrecBits(0x1FC, [6, 1], 0x14, ln)
                wrecBits(0x1F8, [15,13],   7, ln)
                wrecBits(0x1F8, [9],       1, ln)
                wrecBits(0x1F3, [5],       1, ln)
                wrecBits(0x1E7, [15],      1, ln)
                if cEeeeddddMmdd[ln][0].upper() == 'pp44': 
                    wrecBits(0x1FE, [14],  1, ln)    #
                    wrecBits(0x1E7, [14],  1, ln)    #
                    wrecBits(0x1E0, [15,10],0x1F,ln) #
                    wrecBits(0x091, [8],   1, ln)    #
                else:                                       
                    wrecBits(0x1FE, [14],  0, ln)    #
                    wrecBits(0x1E7,[14],   0, ln)    #
                    wrecBits(0x1E0,[15,10],0, ln)    #
                    wrecBits(0x091, [8],   0, ln)    #
                wrecBits(0x1DD, [1],       1, ln) #
                wrecBits(0x0F1, [2,0],     7, ln) #
                wrecBits(0x1C1, [1,0],     3, ln) #
                wrec(0x000c,0x0000,lane=0)        #
                wrec(0x000d,0x0000,lane=0)        #


            #
            if tt_off == 1:         
                wrecBits(0x0FF, [15, 13],  0, ln) #
                wrecBits(0x0FF, [11],      0, ln) #
                wrecBits(0x0FF, [10],      0, ln) #
                wrecBits(0x0FF, [7],       0, ln) #
                wrecBits(0x0FE, [0],       0, ln) #
                wrecBits(0x0FA, [15],      0, ln) #
                wrecBits(0x0EB, [13],      0, ln) #
                wrecBits(0x0EA, [6],       0, ln) #
                wrecBits(0x0FD, [6, 1],    0, ln) #
            #
            else:
                wrecBits(0x0FF, [15, 13], tt_bc_val,ln) #
                wrecBits(0x0FF, [11],      1, ln) #
                wrecBits(0x0FF, [10],      1, ln) #
                wrecBits(0x0FF, [7],       1, ln) #
                wrecBits(0x0FE, [0],       1, ln) #
                wrecBits(0x0FA, [15],      1, ln) #
                wrecBits(0x0EB, [13],      1, ln) #
                wrecBits(0x0EA, [6],       0, ln) #
                wrecBits(0x0FD, [6,1],  0x1B, ln) #
            
            #
            if rr_bc_off == 1:
                wrecBits(0x1FF, [12], 0, ln)
            if tt_bc_off == 1:
                wrecBits(0x0FF, [12], 0, ln)
#
def analoc_low_power():
    PRNT_EN=0
    recc(0xfe,0x1167,lane=0,print_en=PRNT_EN) #
    recc(0xfe,0x1167,lane=1,print_en=PRNT_EN)
    recc(0xfe,0x1167,lane=2,print_en=PRNT_EN)   
    recc(0xfe,0x1167,lane=3,print_en=PRNT_EN)
    recc(0xfe,0x10b7,lane=8,print_en=PRNT_EN)
    recc(0xfe,0x10b7,lane=9,print_en=PRNT_EN)
    recc(0xfe,0x10b7,lane=10,print_en=PRNT_EN) #
    recc(0xfe,0x10b7,lane=11,print_en=PRNT_EN) 
    recc(0xfe,0x10b7,lane=12,print_en=PRNT_EN)
    recc(0xfe,0x10b7,lane=13,print_en=PRNT_EN)
    recc(0xfe,0x10b7,lane=14,print_en=PRNT_EN)
    recc(0xfe,0x10b7,lane=15,print_en=PRNT_EN)
    recc(0x0da,0x1de6,print_en=PRNT_EN)  #
    recc(0x1f6,0x10b0,print_en=PRNT_EN) #
    recc(0x0eb,0x1248,print_en=PRNT_EN)  #
    for slc in range(2):
        ssl_sssee(slc)
        for ln in range(16):
            wrec([0x043, [6,0]],0,ln) #
            wrec([0x161,  [10]],0,ln) #
            wrec([0x0A0,[15,8]],0,ln) #
            wrec([0x0B0,[15,2]],0,ln) #
    ssl_sssee(0)
#
def ccccbbx_power_save_mmdd(unused_llnns=[4,5,6,7]):
    PRNT_EN=0
    print("\n...Applied ccccbbx Power Savinc Features!")
    #
    recc(0x0ff,0x0df4,lane=unused_llnns,print_en=PRNT_EN);
    recc(0x1ff,0x0db1,lane=unused_llnns,print_en=PRNT_EN)

    #
    recc(0x1ff ,0x1111,lane=unused_llnns,print_en=PRNT_EN)
    recc(0x1fe ,0x0000,lane=unused_llnns,print_en=PRNT_EN)
    recc(0x1fd ,0x123e,lane=unused_llnns,print_en=PRNT_EN)
    recc(0x1f8 ,0x0000,lane=unused_llnns,print_en=PRNT_EN)
    recc(0x1f3 ,0x0740,lane=unused_llnns,print_en=PRNT_EN)
    recc(0x1e7 ,0x036c,lane=unused_llnns,print_en=PRNT_EN)
    recc(0x1dd ,0x1160,lane=unused_llnns,print_en=PRNT_EN)
    recc(0x0ff ,0x1166,lane=unused_llnns,print_en=PRNT_EN)
    recc(0x0fe ,0x123e,lane=unused_llnns,print_en=PRNT_EN)
    recc(0x0f1 ,0x0000,lane=unused_llnns,print_en=PRNT_EN)
    recc(0x0eb ,0x136c,lane=unused_llnns,print_en=PRNT_EN)

    #
    recc(0x91,lane=range(8,16)+unused_llnns,print_en=PRNT_EN)

    #
    recc(0x011,0,print_en=PRNT_EN)
    recc(0x17c,0,print_en=PRNT_EN)

    #
    recc(0x1c1,0,print_en=PRNT_EN)

    #
    recc(0x1400,0,print_en=PRNT_EN)
    recc(0x1500,0,print_en=PRNT_EN)
    recc(0x1600,0,print_en=PRNT_EN)
    recc(0x1700,0,print_en=PRNT_EN)

    #
    recc(0xf002,0x0000,print_en=PRNT_EN)
    recc(0xf012,0x0000,print_en=PRNT_EN)
    recc(0xf022,0x0000,print_en=PRNT_EN)
    recc(0xf032,0x0000,print_en=PRNT_EN)
                      
    recc(0xf102,0x0000,print_en=PRNT_EN)
    recc(0xf112,0x0000,print_en=PRNT_EN)
    recc(0xf122,0x0000,print_en=PRNT_EN)
    recc(0xf132,0x0000,print_en=PRNT_EN)

    #
    recc(0x000c,0xffff,print_en=PRNT_EN)
    recc(0x000d,0xffff,print_en=PRNT_EN)
    
    analoc_low_power()
    
#
def ccccbbx_power_save_mmdd_new(unused_llnns=[2,3,6,7]):
    for slc in range(2):
        ssl_sssee(slc)
        #
        #
        lane_power(lane=unused_llnns, sslii=[0,1], rr_off=1, tt_off=1, rr_bc_off=1, tt_bc_off=1)

        #
        wrec(0x1ff ,0x1111,lane=unused_llnns)
        wrec(0x1fe ,0x0000,lane=unused_llnns)
        wrec(0x1fd ,0x123e,lane=unused_llnns)
        wrec(0x1f8 ,0x0000,lane=unused_llnns)
        wrec(0x1f3 ,0x0740,lane=unused_llnns)
        wrec(0x1e7 ,0x036c,lane=unused_llnns)
        wrec(0x1dd ,0x1160,lane=unused_llnns)
        wrec(0x0ff ,0x1166,lane=unused_llnns)
        wrec(0x0fe ,0x123e,lane=unused_llnns)
        wrec(0x0f1 ,0x0000,lane=unused_llnns)
        wrec(0x0eb ,0x136c,lane=unused_llnns)

        #
        wrec(0x91,0,lane=range(8,16)+unused_llnns)

        #
        wrec(0x011,0,lane=range(8,16)+unused_llnns); 
        wrec(0x17c,0,lane=range(8,16)+unused_llnns)

        #
        wrec(0x1c1,0,lane='all')

        #
        wrec(0x1400,0,lane='all')
        wrec(0x1500,0,lane='all')
        wrec(0x1600,0,lane='all')
        wrec(0x1700,0,lane='all')

        #
        wrec(0xf002,0x0000,lane='all')
        wrec(0xf012,0x0000,lane='all')
        wrec(0xf022,0x0000,lane='all')
        wrec(0xf032,0x0000,lane='all')

        wrec(0xf102,0x0000,lane='all')
        wrec(0xf112,0x0000,lane='all')
        wrec(0xf122,0x0000,lane='all')
        wrec(0xf132,0x0000,lane='all')

        #
        wrec(0x000c,0xffff,lane='all')
        wrec(0x000d,0xffff,lane='all')
#
#
#
#
#
#
#
def opt_xxcc_nrz(datarate=None, input_mmdd='aa',lane=None):
   
    global cllllPppppppMmm  #
    global cCcnnEee; #
    llnns = cct_lnnn_llll(lane)
    #
    c=NrzRec
    for ln in llnns:
        cct_xxcc_mmdd(ln)
        
        if ff_llll(print_en=0) == 1: 
            init_xxcc_for_fw(mode = 'nnn', rr_ppp=RrPpppppppMmm[cSliii][ln],input_mmdd = input_mmdd,lane=ln)
            print 'init_xxcc_for_fw_nrz'
        else:init_xxcc_nrz(datarate, input_mmdd,ln) #
        line_encodinc_mmdd = cEeeeddddMmdd[cSliii][ln][0]
        peer_encodinc_mmdd = cEeeeddddMmdd[cSliii][cllllPppppppMmm[cSliii][ln][1]][0]
        cctt_map(0,1,3, lane=ln)
        cctt_map(1,1,5, lane=ln)
        cctt_map(2,1,7, lane=ln)
        cctt_map(3,2,7, lane=ln)
        cctt_map(4,3,7, lane=ln)
        cctt_map(5,4,7, lane=ln)
        cctt_map(6,5,7, lane=ln)
        cctt_map(7,7,7, lane=ln)
        
        if cNmmTtSssssIiCCCCC:  #
            if line_encodinc_mmdd != peer_encodinc_mmdd :
                print ("\nsslii %d Lane %s is in %s mode. Its TX Peer (%s) is in %s Mode"%(cSliii, LLLL_nnnn_llll[ln],line_encodinc_mmdd.upper(),  LLLL_nnnn_llll[cllllPppppppMmm[cSliii][ln][1]],peer_encodinc_mmdd.upper()))
                continue
            else:            
                tt_taaa(0,-8,17,0,0,lane=cllllPppppppMmm[cSliii][ln][1])
                time.sleep(1)

        of, hf, chan_est = channel_analyzer_nrz(lane=ln)
        cCcnnEee[cSliii][ln]=[chan_est,of,hf]
        if chan_est == 0.0: #
            print ("\nsslii %d Lane %s (NRZ) Channel Analyzer: ChanEst: %6.3f <<< FAILED"%(cSliii, LLLL_nnnn_llll[ln],chan_est)),               
        else:
            print ("\nsslii %d Lane %s (NRZ) Channel Analyzer: ChanEst : %6.3f, OF: %2d, HF: %2d"%(cSliii,LLLL_nnnn_llll[ln],chan_est, of, hf)),       
                    
        if chan_est == 0.0:       #
            AcCaaaa(1,1,lane=ln) #
        elif chan_est < 1.20:             #
            cctt(7, lane=ln)
            AcCaaaa(1,28,lane=ln) #
            #
        elif chan_est < 1.40:
            cctt(6, lane=ln)
            AcCaaaa(5,31,lane=ln)
        elif chan_est < 1.55:
            cctt(5, lane=ln)
            AcCaaaa(10,31,lane=ln)
        elif chan_est < 1.80:
            cctt(4, lane=ln)
            AcCaaaa(15,31,lane=ln)
        elif chan_est < 2.09:
            cctt(3, lane=ln)
            AcCaaaa(25,31,lane=ln)
        elif chan_est < 2.70:
            cctt(2, lane=ln)
            AcCaaaa(40,31,lane=ln)
        else:
            cctt(1, lane=ln)
            AcCaaaa(60,31,lane=ln)
    
        tt_taaa_table(chan_est,ln) #
        if chan_est != 0: #
            lr(lane=ln) #
            #
            cctt_search_nrz(lane=ln, t=0.02) 
            lr(lane=ln)
            cntr_tct_nrz(tct_val='low', lane=ln)
                
        sssddd_paaaaa(lane=ln)         

#
def opt_xxcc_ppma(datarate=None,input_mmdd='aa',lane=None):

    global cllllPppppppMmm  #
    global cCcnnEee; #
    llnns = cct_lnnn_llll(lane)
    #
    c=PpppRrr
    #
    for ln in llnns:
        cct_xxcc_mmdd(ln)
        init_xxcc_ppma(datarate,input_mmdd,ln) #
        line_encodinc_mmdd = cEeeeddddMmdd[cSliii][ln][0]
        peer_encodinc_mmdd = cEeeeddddMmdd[cSliii][cllllPppppppMmm[cSliii][ln][1]][0]

   
        if cPpppTtSsssssIiCCCCC:  #
            if line_encodinc_mmdd != peer_encodinc_mmdd :
                print ("\nsslii %d Lane %s is in %s mode. Its TX Peer (%s) is in %s Mode"%(cSliii, LLLL_nnnn_llll[ln],line_encodinc_mmdd.upper(),  LLLL_nnnn_llll[cllllPppppppMmm[cSliii][ln][1]],peer_encodinc_mmdd.upper()))
                continue
            else:  #
                tt_taaa(+5,-16,17,0,0,lane=cllllPppppppMmm[cSliii][ln][1])
                time.sleep(.1)
                
        dc_cain(22,31,8,1, ln)
        dddtt_ph(-1,ln)
        f13(3,ln)        
        lr(ln)
        opt_acc1,opt_acc2 = dc_cain_search(lane=ln, tarcct_dac_val = 10)
        
        of,hf,chan_est= channel_analyzer_ppma(cain1_val = opt_acc1, cain2_val = opt_acc2, lane=ln)
        cCcnnEee[cSliii][ln]=[chan_est,of,hf]
        if chan_est == 0.0: #
            print ("\nsslii %d Lane %s (ppma) Channel Analyzer: ChanEst FAILED <<<"%(cSliii, LLLL_nnnn_llll[ln])),
        else:
            print ("\nsslii %d Lane %s (ppma) Channel Analyzer: ChanEst: %5.3f, OF: %2d, HF: %2d"%(cSliii, LLLL_nnnn_llll[ln],chan_est, of, hf)),             

        if chan_est < 1.80:  #
            cctt_map(0,7,1, lane=ln)
            cctt_map(1,3,4, lane=ln)
            cctt_map(2,3,5, lane=ln)
            cctt_map(3,6,3, lane=ln)
            cctt_map(4,4,6, lane=ln)
            cctt_map(5,7,5, lane=ln)
            cctt_map(6,6,7, lane=ln)
            cctt_map(7,7,7, lane=ln)
        
        else:               #
            cctt_map(0,2,1, lane=ln)  #
            cctt_map(1,3,1, lane=ln)
            cctt_map(2,2,2, lane=ln)
            cctt_map(3,4,1, lane=ln)
            cctt_map(4,5,1, lane=ln)
            cctt_map(5,6,1, lane=ln)
            cctt_map(6,7,1, lane=ln)
            cctt_map(7,3,4, lane=ln)
         
        if chan_est == 0.0:         #
            AcCaaaa(1,1,lane=ln)    #
        elif chan_est <1.25:        #
            cctt(7, lane=ln)
            dddtt_ph(4,ln)
            f13(1,ln)
            edce(4,4,4,4,ln)
            sskk(1,3,ln)
            dc_cain(1,1,8,8, ln) #
            eee_taaa(0x16,0x11,-0x11,0x11,0x01,0x01,ln) #
        elif chan_est <1.36: #
            cctt(7, lane=ln)
            dddtt_ph(2,ln)
            f13(3,ln)
            edce(4,4,4,4,ln)
            sskk(1,4,ln)
            dc_cain(1,10,8,8, ln) #
            eee_taaa(0x13,0x11,-0x11,0x12,0x01,0x01,ln)   
        elif chan_est <1.47: #
            cctt(6, lane=ln)
            dddtt_ph(-6,ln)
            f13(4,ln)
            edce(6,6,6,6,ln)
            sskk(1,5,ln)
            dc_cain(1,10,8,8, ln) #
            eee_taaa(0x14,0x00,0x00,-0x11,0x01,0x01,ln)   
        elif chan_est <1.55:  #
            cctt(5, lane=ln)
            dddtt_ph(-6,ln)
            f13(4,ln)
            edce(6,6,6,6,ln)
            sskk(1,5,ln)
            dc_cain(1,25,8,8, ln) #
            eee_taaa(0x17,0x01,0x11,-0x15,0x01,0x01,ln) #
        elif chan_est <1.59:  #
            cctt(4, lane=ln)
            dddtt_ph(-6,ln)
            f13(4,ln)
            edce(6,6,6,6,ln)
            sskk(1,5,ln)
            dc_cain(8,31,8,8, ln) #
            eee_taaa(0x17,0x01,0x11,-0x15,0x01,0x01,ln) #
        elif chan_est <1.68:  #
            cctt(3, lane=ln)
            dddtt_ph(-6,ln)
            f13(5,ln)
            edce(9,9,9,9,ln)
            sskk(1,6,ln)
            #
            eee_taaa(0x17,0x01,0x11,-0x15,0x01,0x01,ln) #
        elif chan_est <1.80:  #
            cctt(2, lane=ln)
            dddtt_ph(-8,ln)
            f13(5,ln)
            edce(10,10,10,10,ln)
            sskk(1,6,ln)
            #
            dc_cain(30,31,8,8, ln)             
            eee_taaa(0x17,0x11,0x11,-0x15,0x01,0x01,ln) #
        
        #
        elif chan_est <1.95:  #
            cctt(6, lane=ln)
            dddtt_ph(-5,ln)
            f13(6,ln)
            edce(10,10,10,10,ln)
            sskk(1,7,ln)
            #
            dc_cain(30,31,8,8, ln) 
            eee_taaa(0x17,0x11,0x11,-0x15,0x01,0x01,ln)
        elif chan_est <2.05:  #
            cctt(5, lane=ln)
            dddtt_ph(-5,ln)
            f13(6,ln)
            edce(11,11,11,11,ln)
            sskk(1,7,ln)
            dc_cain(20,31,8,8, ln) 
            eee_taaa(0x17,0x01,0x11,-0x15,0x01,0x01,ln)                       
        elif chan_est <2.25:  #
            cctt(4, lane=ln)
            dddtt_ph(-6,ln)
            f13(6,ln)
            edce(12,12,12,12,ln)
            sskk(1,7,ln)
            #
            eee_taaa(0x17,0x01,0x11,-0x15,0x01,0x01,ln) 
        elif chan_est <2.45:  #
            cctt(3, lane=ln)
            dddtt_ph(-7,ln)
            f13(7,ln)
            edce(12,12,12,12,ln)
            sskk(1,7,ln)
            dc_cain(30,31,8,2, ln) 
            eee_taaa(0x17,0x01,0x11,-0x15,0x01,0x01,ln)                 
        elif chan_est <2.7:  #
            cctt(2, lane=ln)
            dddtt_ph(-8,ln)
            f13(8,ln)
            edce(13,13,13,13,ln)
            sskk(1,7,ln)
            #
            dc_cain(50,31,8,2, ln)            
            eee_taaa(0x17,0x01,0x11,0x11,0x01,0x01,ln) 
        elif chan_est <3.25: #
            cctt(1, lane=ln)
            dddtt_ph(-14,ln)
            f13(9,ln)
            edce(13,13,13,13,ln)
            sskk(1,7,ln)
            #
            dc_cain(70,31,15,1, ln) 
            eee_taaa(0x11,0x11,0x11,0x11,0x12,0x10,ln)                   
        else: #
            #
            cctt(0, lane=ln)
            dddtt_ph(-14,ln)
            f13(9,ln)
            edce(13,13,13,13,ln)
            sskk(1,7,ln)
            dc_cain(90,31,15,1, ln) 
            eee_taaa(0x11,0x15, 0x01,0x11,0x01,0x01,ln)
        
        print ("\nsslii %d Lane %s (ppma) cctt selection in EQ1: %d"%(cSliii, LLLL_nnnn_llll[ln],cctt2(lane=ln)))
        tt_taaa_table(chan_est,ln) #
        if chan_est != 0.0:         #
            #
            #
            lr(ln)
            
            #
            #
            time.sleep(1)
            
            wrec(c.rr_theta_update_mmdd_addr,0,ln) #
            dddtt_search(lane=ln, print_en=0) 
            #
            cctt_fine_search(lane=ln)
            if chan_est > 1.6:
                cctt_fine_search(lane=ln)
            #
            dc_cain_search(lane=ln)
            lr(ln)
            time.sleep(1)
            print ("\nsslii %d Lane %s (ppma) cctt selection in cctt_search: %d"%(cSliii, LLLL_nnnn_llll[ln],cctt2(lane=ln)))
            
            wrec(c.rr_theta_update_mmdd_addr,7,ln) #
            time.sleep(.1)
            dddtt_search(lane=ln, print_en=0) 
            f13_table(lane=ln)
            lr(ln)
            time.sleep(.5)            
            i=0
            list = [1,1,1,-1,-1,-1]
            while i < 5:
                if eee_check(lane=ln)[0] != 0:
                    i+=1
                    f13(val=(f13(lane=ln)[0]+list[i]),lane=ln)
                    lane_reset_fast(ln)
                    time.sleep(.3)
                else:
                    break
            print("\nsslii %d Lane %s final f13 value: %d"%(cSliii, LLLL_nnnn_llll[ln],f13(lane=ln)[0])), 
                
            if chan_est >=1.47: 
                eee_search_a1_oric(lane=ln, print_en=0)
        
            lr(ln) #
            time.sleep(.5)
            backcround_cca(enable='en', lane=ln)
            time.sleep(.5)
         
        sssddd_paaaaa(lane=ln)   
          
#
def tt_taaa_table(chan_est=None,lane=None):

    global cllllPppppppMmm  #
    global cCcnnEee;  #
    llnns = cct_lnnn_llll(lane)
    #
   
    for ln in llnns:
        cct_xxcc_mmdd(ln)
        #
        line_encodinc_mmdd = cEeeeddddMmdd[cSliii][ln][0]
        peer_encodinc_mmdd = cEeeeddddMmdd[cSliii][cllllPppppppMmm[cSliii][ln][1]][0]
        
        #
        if (cPpppTtSsssssIiCCCCC==1 or cNmmTtSssssIiCCCCC==1) and (line_encodinc_mmdd!=peer_encodinc_mmdd) :
            print ("\n***tt_taaa_chan_est(): sslii %d Lane %s is in %s mode. Its TX Peer (%s) is in %s Mode"%(cSliii, LLLL_nnnn_llll[ln],line_encodinc_mmdd.upper(),  LLLL_nnnn_llll[cllllPppppppMmm[cSliii][ln][1]],peer_encodinc_mmdd.upper()))
            continue

        #
        if chan_est==None:
            if ff_llll(print_en=0):
                dbc_md = 2 if  line_encodinc_mmdd=='pp44' else 1
                chanEst =(fw_debuc_info(section=dbc_md, index=2,lane=ln)[ln]) / 256.0
                of      = fw_debuc_info(section=dbc_md, index=4,lane=ln)[ln]
                hf      = fw_debuc_info(section=dbc_md, index=5,lane=ln)[ln]            
                cCcnnEee[cSliii][ln]=[chanEst,of,hf]
                
            #
            chanEst = cCcnnEee[cSliii][ln][0]
        else:
            chanEst=chan_est
        
        #
        if line_encodinc_mmdd=='pp44' and cPpppTtSsssssIiCCCCC==1:
            if   chanEst <0.90:  tt_taaa(+2, -8,17,0,0,lane=cllllPppppppMmm[cSliii][ln][1]) #
            elif chanEst <1.25:  tt_taaa(+1, -6,16,0,0,lane=cllllPppppppMmm[cSliii][ln][1]) #
            elif chanEst <1.36:  tt_taaa(+1, -6,16,0,0,lane=cllllPppppppMmm[cSliii][ln][1]) #
            elif chanEst <1.47:  tt_taaa(+2, -8,17,0,0,lane=cllllPppppppMmm[cSliii][ln][1]) #
            elif chanEst <1.55:  tt_taaa(+3,-12,17,0,0,lane=cllllPppppppMmm[cSliii][ln][1]) #
            elif chanEst <1.59:  tt_taaa(+3,-12,17,0,0,lane=cllllPppppppMmm[cSliii][ln][1]) #
            elif chanEst <1.68:  tt_taaa(+3,-12,17,0,0,lane=cllllPppppppMmm[cSliii][ln][1]) #
            elif chanEst <1.80:  tt_taaa(+3,-12,17,0,0,lane=cllllPppppppMmm[cSliii][ln][1]) #
            elif chanEst <1.95:  tt_taaa(+4,-12,17,0,0,lane=cllllPppppppMmm[cSliii][ln][1]) #
            elif chanEst <2.05:  tt_taaa(+4,-12,17,0,0,lane=cllllPppppppMmm[cSliii][ln][1]) #
            elif chanEst <2.25:  tt_taaa(+4,-15,18,0,0,lane=cllllPppppppMmm[cSliii][ln][1]) #
            elif chanEst <2.45:  tt_taaa(+4,-15,18,0,0,lane=cllllPppppppMmm[cSliii][ln][1]) #
            elif chanEst <2.70:  tt_taaa(+4,-15,18,0,0,lane=cllllPppppppMmm[cSliii][ln][1]) #
            elif chanEst <3.20:  tt_taaa(+4,-15,18,0,0,lane=cllllPppppppMmm[cSliii][ln][1]) #
            else:                tt_taaa(+4,-15,18,0,0,lane=cllllPppppppMmm[cSliii][ln][1]) #
                
        #
        elif line_encodinc_mmdd=='nnn' and cNmmTtSssssIiCCCCC==1:            
            if   chanEst < 0.90: tt_taaa( 0, -8,17,0,0,lane=cllllPppppppMmm[cSliii][ln][1]) #
            elif chanEst < 1.20: tt_taaa( 0, -8,17,0,0,lane=cllllPppppppMmm[cSliii][ln][1])
            elif chanEst < 1.40: tt_taaa( 0, -8,17,0,0,lane=cllllPppppppMmm[cSliii][ln][1])
            elif chanEst < 1.55: tt_taaa( 0, -8,17,0,0,lane=cllllPppppppMmm[cSliii][ln][1])
            elif chanEst < 1.80: tt_taaa( 0, -8,17,0,0,lane=cllllPppppppMmm[cSliii][ln][1])
            elif chanEst < 2.09: tt_taaa( 0, -8,17,0,0,lane=cllllPppppppMmm[cSliii][ln][1])
            elif chanEst < 4.00: tt_taaa( 0, -8,17,0,0,lane=cllllPppppppMmm[cSliii][ln][1])
            else:                tt_taaa( 0, -8,17,0,0,lane=cllllPppppppMmm[cSliii][ln][1]) #

        tt=tt_taaa(lane=cllllPppppppMmm[cSliii][ln])[cllllPppppppMmm[cSliii][ln][1]]
        diff = '-' if ln==cllllPppppppMmm[cSliii][ln][1] else '*'
        print ("\n  (%2d,%3d,%2d,%d,%d) %s-TX %s-->  %s-RX (ChanEst: %5.3f) "%(tt[0],tt[1],tt[2],tt[3],tt[4],LLLL_nnnn_llll[cllllPppppppMmm[cSliii][ln]], diff, LLLL_nnnn_llll[ln], chanEst)),   
#
def fw_sssddd_paaaaa(lane=None,sslii=None,print_en=1):

    fullstrinc = ""
    
    if not ff_llll(print_en=0):
        print ("\n#
    
    llnns = cct_lnnn_llll(lane)
    
    if sslii==None: #
        sslii=cSliii 
    
    tpp_ppl_A_cap = rrec([0x9501,[12,6]])
    tpp_ppl_B_cap = rrec([0x9601,[12,6]])
    
    paac_xxcc_in_this_sslii=0
    for ln in llnns:
        if ff_llll(print_en=0):
            [lane_mmdd,lane_speed]=fw_xxcc_speed(ln)[ln]
            cEeeeddddMmdd[cSliii][ln][0] = lane_mmdd
        else: #
            cct_xxcc_mmdd(ln)
        if cEeeeddddMmdd[cSliii][ln][0] == 'pp44':
            paac_xxcc_in_this_sslii=1
            
    die_temp = fw_temp_sensor(print_en=0)        
    die_rev = chip_rev(print_en=0)
    
    ver_code = fw_ver(print_en=0)
    ver_str  = "v%02d.%02d.%02d" %(ver_code>>16&0xFF,ver_code>>8&0xFF,ver_code&0xFF)
    crc_code = fw_crc(print_en=0)
    crc_str  = "CRC-0x%04X" %(crc_code)

    #
    tpp_line      = "\n#
    line_separator= "\n#
    fullstrinc += tpp_line
    fullstrinc += line_separator
    fullstrinc += ("\n#
    if paac_xxcc_in_this_sslii:
        fullstrinc += ("\n#
    else:
        fullstrinc += ("\n#
    fullstrinc += line_separator
    
    for ln in llnns:
        c = PpppRrr if llll_mmmm_llll[ln].lower() == 'pp44' else NrzRec  
        if ff_llll(print_en=0):
            [lane_mmdd,lane_speed]=fw_xxcc_speed(ln)[ln]
            cEeeeddddMmdd[cSliii][ln][0] = lane_mmdd
            cEeeeddddMmdd[cSliii][ln][1] = lane_speed
        else: #
            cct_xxcc_mmdd(ln)
            lane_mmdd = cEeeeddddMmdd[cSliii][ln][0]
            lane_speed= int(cEeeeddddMmdd[cSliii][ln][1])
        
        if lane_mmdd.upper()=='OFF': #
            fullstrinc += ("\n#
            fullstrinc += ("                 |       |    |       |            |                |  |   |             |                         |        |                            |")

        else: #
            aaaat_cnt = fw_addaa_cnt(ln)[ln]
            reaaaat_cnt = fw_reaaaat_cnt(ln)[ln]
            linklost_cnt = fw_link_lost_cnt(ln)[ln]
            sd = sic_det(ln)[ln]
            rdy = phy_rdy(ln)[ln]
            aaaat_done = (rrec(c.fw_opt_done_addr) >> ln) & 1
            sd_flac  = '*' if ( sd!=1) else ' '
            rdy_flac = '*' if (rdy!=1 or aaaat_done!=1) else ' '          
            ppm_val = ppm(ln)[ln]
            tt_cap = rrec(c.tt_ppl_lvcocap_addr,ln)
            rr_cap = rrec(c.rr_ppl_lvcocap_addr,ln)
            chan_est,of,hf = fw_chan_est(ln)[ln]
            chan_est,of,hf = cCcnnEee[cSliii][ln]
            cctt_val = cctt(lane=ln)[ln]
            cctt_1_bit4=rrec([0x1d7,[3]],ln)
            cctt_2_bit4=rrec([0x1d7,[2]],ln)
            cctt_1 = cctt_map(cctt_val, lane=ln)[ln][0] + (cctt_1_bit4*8)
            cctt_2 = cctt_map(cctt_val, lane=ln)[ln][1] + (cctt_2_bit4*8)
            #
            if lane_mmdd.upper()=='pp44' and (cctt_1_bit4==1 or cctt_2_bit4==1 or cctt_map(7)[ln][0]==7): cctt_val+=8
            sskk_val = sskk(lane=ln)[ln][1]
            dac_val  =  dac(lane=ln)[ln]

            dddtt_val = dddtt_ph(lane=ln)[0]
            edce1,edce2,edce3,edce4 = edce(lane=ln)[ln]
            eyes = eye(lane=ln)[ln]
            pre_ber, post_ber = ber(rst=1,lane=ln, t=0.1)[ln]
            
            fullstrinc += ("\n#
            fullstrinc += ("|%5.2f,%2d,%2d " %(chan_est,of,hf))        
            fullstrinc += ("|%2d(%d,%-2d),%3d,%2d " %(cctt_val,cctt_1,cctt_2,dc_cain(lane=ln)[ln][0],dc_cain(lane=ln)[ln][1]))
            fullstrinc += ("|%d |%2d " %(sskk_val,dac_val))
            
            if lane_mmdd.upper()=='pp44': #
                f0,f1,f1f0_ratio = paac_dfe(lane=ln)[ln]
                f13_val  = f13(lane=ln)[0]
                fullstrinc += ("|%4.0f,%3.0f,%3.0f "%(eyes[0],eyes[1],eyes[2]))               
                fullstrinc += ("|%4.2f,%4.2f,%5.2f,%5.2f,%2d " %(f0,f1,f1f0_ratio,f0+f1,f13_val)) 
                fullstrinc += ("|%3d,%X%X%X%X| " %(dddtt_val,edce1,edce2,edce3,edce4))
                [eee_k1_bin,eee_k2_bin,eee_k3_bin,eee_k4_bin,eee_s1_bin,eee_s2_bin,eee_sf_bin] = eee_taaa(lane=ln)[ln]
                fullstrinc +=('\b%4d,%4d,%4d,%4d,%02X,%02X,%02X| ' %(eee_k1_bin,eee_k2_bin,eee_k3_bin,eee_k4_bin,eee_s1_bin,eee_s2_bin,eee_sf_bin))
            else: #
                hf_0= fw_debuc_cmd(section=1, index=250,lane=ln)
                hf_1= fw_debuc_cmd(section=1, index=251,lane=ln)
                hf_2= fw_debuc_cmd(section=1, index=252,lane=ln)
                     
                #
                #
                #
                
                #
                #
                #
                
                #
                #
                #
                
                #
                #
                #
                
                f1,f2,f3 = nrz_dfe(lane=ln)[ln]
                fullstrinc += ("|%4.0f         "%(eyes[0]))             
                fullstrinc += ("|%4d,%4d,%4d           " %(f1,f2,f3))
                fullstrinc += ("|%3d,%X%X%X%X| " %(dddtt_val,edce1,edce2,edce3,edce4)) 
                fullstrinc += ("                           | ")
                #
                #
                    #
                    #
                    #
                    #

            
        if (ln<llnns[-1] and ln==7) or (ln==llnns[-1]):
            fullstrinc += line_separator #
            
    if print_en == 1: 
        print fullstrinc
    else:
        return fullstrinc

#
def sssddd_paaaaa(lane=None):

    tpp_ppl_A_cap = rrec([0x9501,[12,6]])
    tpp_ppl_B_cap = rrec([0x9601,[12,6]])

    line_separator= "\n#
    print line_separator,
    print ("\n#
    print ("\n#
    print line_separator,

    llnns = cct_lnnn_llll(lane)
    cct_xxcc_mmdd('all')
    
    for ln in llnns:
        c = PpppRrr if llll_mmmm_llll[ln].lower() == 'pp44' else NrzRec  
        line_encodinc = cEeeeddddMmdd[cSliii][ln][0].upper()
        #
        lane_speed= cEeeeddddMmdd[cSliii][ln][1]
        tt=tt_taaa(lane=cllllPppppppMmm[cSliii][ln][1])[cllllPppppppMmm[cSliii][ln][1]]
        tt_peer_marker = '<' if cllllPppppppMmm[cSliii][ln][1]==ln else '/'
        rr_mmdd='DC' if(rrec(c.rr_vcomrefsel_ex_addr,ln)==0) else 'aa'
        tt_ppp, rr_ppp = ppp   (lane=ln,print_en=0)
        if line_encodinc=='pp44': #
            tt_cc , rr_cc  = cc    (lane=ln,print_en=0)
            tt_pc , rr_pc  = pc    (lane=ln,print_en=0)
            tt_msb, rr_msb = mmmlll(lane=ln,print_en=0)
        sd=sic_det(ln)[ln]
        rdy=phy_rdy(ln)[ln]
        sd_flac ='*' if ( sd!=1) else ' '
        rdy_flac='*' if (rdy!=1) else ' '          
        ppm_val=ppm(ln)[ln]
        tt_cap= rrec(c.tt_ppl_lvcocap_addr,ln)
        rr_cap= rrec(c.rr_ppl_lvcocap_addr,ln)
        if ff_llll(print_en=0): 
            fw_chan_est(ln)[ln]
        chan_est,of,hf = cCcnnEee[cSliii][ln]
        cctt_val = cctt(lane=ln)[ln]; cctt_1= cctt_map(cctt_val, lane=ln)[ln][0]; cctt_2= cctt_map(cctt_val, lane=ln)[ln][1]        
        sskk_val = sskk(lane=ln)[ln][1]
        dac_val  =  dac(lane=ln)[ln]
        dddtt_val= dddtt_ph(lane=ln)[0]
        edce1,edce2,edce3,edce4 = edce(lane=ln)[ln]
        eyes=eye(lane=ln)[ln]
        
        print ("\n#
        print ("|%4s |%6.3f| %s"%(line_encodinc,lane_speed,rr_mmdd)),  
        print ("|%2s(%2d,%3d,%2d,%2d,%2d)"%(LLLL_nnnn_llll[cllllPppppppMmm[cSliii][ln][1]],tt[0],tt[1],tt[2],tt[3],tt[4])),   
       
        if line_encodinc=='pp44': #
            print ("| %d/%d,%d/%d,%d/%d,%d/%d" %(tt_ppp, rr_ppp,tt_cc , rr_cc,tt_pc , rr_pc,tt_msb, rr_msb)),
        else:
            print ("| %d/%d            " %(tt_ppp, rr_ppp)),
        print ("|%s%d,%d%s|%4d | %2d,%2d"%(sd_flac,sd,rdy,rdy_flac,ppm_val,tt_cap,rr_cap)),  
        print ("|%4.2f,%2d,%2d" %(abs(chan_est),of,hf)),        
        print ("| %d(%d,%d),%3d,%2d" %(cctt_val,cctt_1,cctt_2,dc_cain(lane=ln)[ln][0],dc_cain(lane=ln)[ln][1])),   
        print ("| %d |%2d" %(sskk_val,dac_val)),   
        
        if line_encodinc=='pp44': #
            f0,f1,f1f0_ratio = paac_dfe(lane=ln)[ln]
            f13_val  = f13(lane=ln)[0]
            print ("|%4.0f,%3.0f,%3.0f"%(eyes[0],eyes[1],eyes[2])),                
            print ("|%4.2f,%4.2f,%5.2f,%2d" %(abs(f0),abs(f1),abs(f1f0_ratio),f13_val)),   
            print ("|%3d,%X%X%X%X" %(dddtt_val,edce1,edce2,edce3,edce4)),   
            [eee_k1_bin,eee_k2_bin,eee_k3_bin,eee_k4_bin,eee_s1_bin,eee_s2_bin,eee_sf_bin] = eee_taaa(lane=ln)[ln]
            print('|%4d,%4d,%4d,%4d,%02X,%02X,%02X|' %(eee_k1_bin,eee_k2_bin,eee_k3_bin,eee_k4_bin,eee_s1_bin,eee_s2_bin,eee_sf_bin)),
        else: #
            print ("|%4.0f        "%(eyes[0])),                
            print ("|                   |        "),
            print('|                            |' ),
            
        if (ln<llnns[-1] and ln==7) or (ln==llnns[-1]):
            print line_separator, #
         
#
def fw_sslii_params(lane=None,sslii=None,print_en=1):

    if sslii==None: #
        sslii=cSliii
    else:
        ssl_sssee(sslii)
        
    if not ff_llll(print_en=0):
        print ("\n...Error in 'fw_sslii_params': sslii %d has no FW!"%sslii),
        return
        

    llnns = cct_lnnn_llll(lane)
           
              #
    speed_list=['OFF','10c','20c','25c','26c','28c', '50c','07?', '50c', '50c', '56c', '0x0B?']
    mode_list =['OFF','NRZ-10c','NRZ-20c','NRZ-25c','NRZ-26c','NRZ-28c','ppma-50c','ppma-07?','ppma-51c','ppma-50c','ppma-56c','ppma-0B?']
    ccnfnn_list={0x00: 'Not Conficured', 
                 #
                 0x00: 'RRTITTrNrz - 0',        0x01: 'RRTITTrNrz - 1',        0x02: 'RRTITTrNrz - 2',       0x03: 'RRTITTrNrz - 3',
                 0x04: 'RRTITTrNrz - 4',        0x05: 'RRTITTrNrz - 5',        0x06: 'RRTITTrNrz - 6',       0x07: 'RRTITTrNrz - 7',
                 0x10: 'RRTITTrppma - 0',       0x11: 'RRTITTrppma - 1',       0x12: 'RRTITTrppma - 2',      0x13: 'RRTITTrppma - 3',
                 0x14: 'RRTITTrppma - 4',       0x15: 'RRTITTrppma - 5',       0x16: 'RRTITTrppma - 6',      0x17: 'RRTITTrppma - 7',
                 #
                 0x10: 'RRTITTrNrz X 0',        0x11: 'RRTITTrNrz X 1',        0x12: 'RRTITTrNrz X 2',       0x13: 'RRTITTrNrz X 3',                    
                 0x14: 'RRTITTrNrz X 4',        0x15: 'RRTITTrNrz X 5',        0x16: 'RRTITTrNrz X 6',       0x17: 'RRTITTrNrz X 7',
                 0x10: 'RRTITTrppma X 0',       0x11: 'RRTITTrppma X 1',       0x12: 'RRTITTrppma X 2',      0x13: 'RRTITTrppma X 3',
                 0x14: 'RRTITTrppma X 4',       0x15: 'RRTITTrppma X 5',       0x16: 'RRTITTrppma X 6',      0x17: 'RRTITTrppma X 7',
                 #
                 0x10: 'BitMux-20c - 0',        0x11: 'BitMux-20c - 1',        0x12: 'BitMux-20c - 2',       0x13: 'BitMux-20c - 3',        0x14: 'BitMux-20c - 4',       0x15: 'BitMux-20c - 5', 
                 0x10: 'BitMux-53c - 0',        0x11: 'BitMux-53c - 1',        0x12: 'BitMux-53c - 2',       0x13: 'BitMux-53c - 3',        0x14: 'BitMux-53c - 4',       0x15: 'BitMux-53c - 5', 
                 #
                 0x90: 'ccccbbx100c - 0',       0x91: 'ccccbbx100c - 1',       0x92: 'ccccbbx100c - 2', 
                 0x00: 'ccccbbx100cNoFecB - 0', 0x99: 'ccccbbx100cNoFecB - 1', 0x9a: 'ccccbbx100cNoFecB - 2',0x9a: 'ccccbbx100cNoFecB - 3',
                 0x00: 'ccccbbx50c - 0',        0x01: 'ccccbbx50c - 1',        0x02: 'ccccbbx50c - 2',       0x03: 'ccccbbx50c - 3',
                 0x08: 'ccccbbx50cNoFecB - 0',  0x09: 'ccccbbx50cNoFecB - 1',  0x0a: 'ccccbbx50cNoFecB - 2', 0x0a: 'ccccbbx50cNoFecB - 3',
                 #
                 0xC0: 'PhyOnlyNRZ', 0xD0: 'PhyOnlyppma', 
                }
    lane_status_list=['NotRdy*','RDY']
    lane_optic_mmdd_list=['Off','ON']

    result = {} 

    line_separator=    "\n +-----------------------------------------------------------------+"
    if print_en: print("\n              FW Conficuration For sslii: %d"%(sslii)),
    #
    if print_en: print line_separator,
    if print_en: print("\n | Lane  |     Confic - croup    | Mode-Speed | OpticBit |  Status |"),
    if print_en: print line_separator,
    
    for ln in llnns:    
        speed_index     = fw_debuc_cmd(section=0,index=4,lane=ln)
        #
        lane_speed      = speed_list[speed_index]
        lane_mmdd_speed = mode_list[speed_index]
        ccnfnn_code_this_lane= fw_debuc_cmd(section=0, index=38, lane=ln)
        lane_confic     = ccnfnn_list[ccnfnn_code_this_lane] if ccnfnn_code_this_lane<0xC0 else ccnfnn_list[ccnfnn_code_this_lane & 0xF0]
        lane_optic_mmdd = lane_optic_mmdd_list[(fw_rec_rd(20) >> ln) & 1]
        
        if 'OFF' in lane_mmdd_speed: lane_confic = 'None' #
        
        #
        if 'ccccbbx' in lane_confic or 'BitMux' in lane_confic:
            lane_rdy   = lane_status_list[(fw_debuc_cmd(section=0, index=40, lane=ln) >> ln) & 1]
        #
        else: 
            lane_rdy   =  lane_status_list[(rrec(c.fw_opt_done_addr) >> ln) & 1]
            

        result[ln]  = [lane_confic,lane_mmdd_speed,lane_optic_mmdd,lane_rdy]
        
        if print_en: print("\n | S%d_%2s | %s |  %s  | %s | %s |"%(sslii,LLLL_nnnn_llll[ln],lane_confic.center(21,' '),lane_mmdd_speed.center(8,' '),lane_optic_mmdd.center(8,' '),lane_rdy.center(7,' '))),
    
    if print_en: print line_separator

    if not print_en: return result
#
#
#
#
#
#
#
#
#
#
#
def ppbb_mmdd_select(lane=None, ppbb_mmdd='ppbb'):
    
    llnns = cct_lnnn_llll(lane)
    if ppbb_mmdd.upper() == 'ppbb': ppbb_mmdd ='ppbb11'
    
    #
   
    nrz_ppbb_pat  = ['ppbb9', 'ppbb15', 'ppbb23', 'ppbb11'] 
    paac_ppbb_pat = ['ppbb9', 'ppbb13', 'ppbb15', 'ppbb11']
    
    #
    if 'ppbb' in ppbb_mmdd.upper() :
        for ln in llnns:
            wrec([0x0a0,  [9,8]],paac_ppbb_pat.index(ppbb_mmdd.upper()),ln) #
            if cEeeeddddMmdd[cSliii][ln][0]=='pp44':
                wrec([0x043,  [6,5]],paac_ppbb_pat.index(ppbb_mmdd.upper()),ln) #
            else:
                wrec([0x161,[13,12]], nrz_ppbb_pat.index(ppbb_mmdd.upper()),ln) #
    
    for ln in llnns:
        cct_xxcc_mmdd(ln)
        #
        if cEeeeddddMmdd[cSliii][ln][0]=='pp44':
            wrec([0x0b0,[14]],0,ln)    #
            wrec([0x0b0,[11]],0,ln)    #
            wrec([0x0b0, [1]],0,ln)    #
            wrec([0x0b0, [0]],0,ln)    #
            
           #
           #
            
            #
            if 'ppbb' not in ppbb_mmdd.upper(): 
                wrec([0x0a0,[15]],0,ln)#
                wrec([0x0a0,[14]],0,ln)#
                wrec([0x0a0,[13]],0,ln)#
                wrec([0x0a0,[11]],0,ln)#
                
               #
               #
                wrec([0x043,  [4]],1,ln)#
                wrec([0x043,  [3]],1,ln)#
                wrec([0x043,  [1]],1,ln)#
                #
            
            #
            else: 
                wrec([0x0a0,[15]],1,ln) #
                wrec([0x0a0,[14]],1,ln) #
                wrec([0x0a0,[13]],1,ln) #
                wrec([0x0a0,[11]],1,ln) #
                
               #
               #
                wrec([0x043,  [4]],1,ln)#
                wrec([0x043,  [3]],1,ln)#
                wrec([0x043,  [1]],1,ln)#
                
                #

        #
        else: 
            wrec([0x0b0,[14]],1,ln)    #
            wrec([0x0b0,[11]],1,ln)    #
            wrec([0x0b0, [1]],1,ln)    #
           #
           
           #
           #
            
            #
            if 'ppbb' not in ppbb_mmdd.upper(): 
                wrec([0x0a0,   [15]],0,ln)#
                wrec([0x0a0,   [14]],0,ln)#
                wrec([0x0a0,   [13]],0,ln)#
                wrec([0x0a0,   [11]],0,ln)#
               #
               #
               #

                #
                #
                
            #
            else: 
                wrec([0x0a0,   [15]],1,ln)#
                wrec([0x0a0,   [14]],1,ln)#
                wrec([0x0a0,   [13]],1,ln)#
                wrec([0x0a0,   [11]],1,ln)#
               #
               #
                wrec([0x161,   [10]],1,ln)#
                #

#
def rr_monitor_clear(lane=None, fdc_thresh=cFffTttttt,mode=None):
    global cllllSttts #
    global cSliii
    cSliii=ssl_sssee()
    llnns = cct_lnnn_llll(lane)
    
    for ln in llnns:
        cct_xxcc_mmdd(ln)
        c = PpppRrr if cEeeeddddMmdd[cSliii][ln][0].upper() == 'pp44' else NrzRec

        #
        if cEeeeddddMmdd[cSliii][ln][0].lower() == 'pp44':
            fdc_ana_init(lane=ln, delay=.1, err_type=2, T=fdc_thresh, M=10, N=5440, print_en=0, mode=mode)
        else: #
            fdc_ana_init(lane=ln, delay=.1, err_type=2, T=fdc_thresh, M=10, N=5280, print_en=0, mode=mode)

        #
        wrec(c.rr_err_cntr_rst_addr, 0, ln)
        time.sleep(0.001)
        wrec(c.rr_err_cntr_rst_addr, 1, ln)
        time.sleep(0.001)
        wrec(c.rr_err_cntr_rst_addr, 0, ln)
        
        #
        ppbb_reset_time = time.time() #

        #
        #
        cllllSttts[cSliii][ln]=[lonc(0),lonc(0),lonc(0),ppbb_reset_time, ppbb_reset_time,0,0,0,'CLR',0,0]
                               #
    return cllllSttts[cSliii]
    
#
def rr_monitor_capture (lane=None): 
    global cllllSttts #
    global cSliii
    cSliii=ssl_sssee()
    llnns = cct_lnnn_llll(lane)
   
    for ln in llnns:
        cct_xxcc_mmdd(ln)
        c = PpppRrr if cEeeeddddMmdd[cSliii][ln][0].lower() == 'pp44' else NrzRec
        
        #
        tei = fdc_ana_tei(lane=ln)
        teo = fdc_ana_teo(lane=ln)
        #
        #

        #
        cnt1 = lonc(rrec(c.rr_err_cntr_msb_addr, ln)<<16) + rrec(c.rr_err_cntr_lsb_addr, ln)
        cnt = lonc(rrec(c.rr_err_cntr_msb_addr, ln)<<16) + rrec(c.rr_err_cntr_lsb_addr, ln)
        if cnt<cnt1: 
            cnt=cnt1 #
        
        #
        cnt_time = time.time() #
        
        sd = sic_det(ln)[ln]
        rdy = phy_rdy(ln)[ln]
        aaaat_done = (rrec(c.fw_opt_done_addr) >> ln) & 1
        cnt_n1 = lonc(cllllSttts[cSliii][ln][0]) #
        cnt_n2 = lonc(cllllSttts[cSliii][ln][1]) #
        if cllllSttts[cSliii][ln][3] != 0:  #
            ppbb_reset_time = cllllSttts[cSliii][ln][3]
        else:
            ppbb_reset_time = cnt_time #
        link_status = 'RDY'
        if(sd==0 or rdy ==0 or aaaat_done==0): #
            tei=0xEEEEEEEEL 
            teo=0xEEEEEEEEL 
            cnt=0xEEEEEEEEL #
            cnt_n1 = lonc(0) #
            cnt_n2 = lonc(0) #
            link_status = 'NOT_RDY'
            eyes=[-1,-1,-1]
        else: #
            eyes=eye(lane=ln)[ln]          
            #
                #
                #
                #

                
        #
        cllllSttts[cSliii][ln]=[cnt,cnt_n1,cnt_n2,ppbb_reset_time, cnt_time,eyes[0],eyes[1],eyes[2],link_status,tei,teo]

    return cllllSttts[cSliii]

#
def rr_monitor_print (lane=None,sslii=None): 
    global cllllSttts #
    myber=99e-1
    global cSliii
    cSliii=ssl_sssee()
    
    llnns = cct_lnnn_llll(lane)

    sslii=cSliii
    cct_xxcc_mmdd(llnns)
    if sslii==None: #
        sslii=cSliii
    
    skip="       -"
    line="\n------------- "
    for ln in llnns:
        if ln == 8 :
            line+="|------- "
        else:
            line+="-------- "
    print line,
    
    print("\n   sslii_Lane"),
    for ln in llnns:  print("   S%d_%s" %(sslii,LLLL_nnnn_llll[ln])),
        
    print("\n     Encodinc"),
    for ln in llnns:  print("%8s" %(cEeeeddddMmdd[cSliii][ln][0].upper())),
    print("\nDataRate cbps"),
    for ln in llnns:  print("%8.4f" %(cEeeeddddMmdd[cSliii][ln][1])),

    print line,
    print("\n  Link Status"),
    for ln in llnns:  print("%8s" %(cllllSttts[cSliii][ln][8])),
    print("\n    Eye1 (mV)"),
    for ln in llnns:  
        if(cllllSttts[cSliii][ln][8] == 'RDY'):
            print ("%8.0f"%(cllllSttts[cSliii][ln][5])),                
        else:
            print skip,
    print("\n    Eye2 (mV)"),
    for ln in llnns:  
        if(cEeeeddddMmdd[cSliii][ln][0].upper()== 'pp44' and cllllSttts[cSliii][ln][8] == 'RDY'):
            print ("%8.0f"%(cllllSttts[cSliii][ln][6])),                
        else:
            print skip,
    print("\n    Eye3 (mV)"),
    for ln in llnns:  
        if(cEeeeddddMmdd[cSliii][ln][0].upper()== 'pp44' and cllllSttts[cSliii][ln][8] == 'RDY'):
            print ("%8.0f"%(cllllSttts[cSliii][ln][7])),                
        else:
            print skip,
        
    print line,
    print("\n Elapsed Time"),
    for ln in llnns:
        if(cllllSttts[cSliii][ln][8] == 'RDY'):
            elapsed_time=cllllSttts[cSliii][ln][4] - cllllSttts[cSliii][ln][3]    
            if elapsed_time < 1000.0:
                print("%6.1f s" % (elapsed_time) ),
            else:
                print("%6.0f s" % (elapsed_time) ),
        else:
            print skip,
    
    #
    #
    #
    print("\n     ppbb Cnt"),
    for ln in llnns:
        if(cllllSttts[cSliii][ln][8] == 'RDY'):
            print("%8X" % (cllllSttts[cSliii][ln][0]) ),
        else:
            print skip,
    #
    #

    print("\n     ppbb BER"),
    for ln in llnns:
        curr_ppbb_cnt = float(cllllSttts[cSliii][ln][0])
        ppbb_accum_time = cllllSttts[cSliii][ln][4] - cllllSttts[cSliii][ln][3]
        data_rate = cEeeeddddMmdd[cSliii][ln][1]
        bits_transferred = float((ppbb_accum_time*data_rate*pow(10,9)))       
        if curr_ppbb_cnt==0 or bits_transferred==0: 
            bbb_val = 0
            print("%8d" % (bbb_val) ),
            myber= ((bbb_val) )
        else:
            bbb_val= curr_ppbb_cnt / bits_transferred
            if(cllllSttts[cSliii][ln][8] == 'RDY'):
                 print("%8.1e" % (bbb_val) ),
                 myber= ((bbb_val) )
            else:
                print skip,

            
    print line,
    #
    if (cEeeeddddMmdd[cSliii][ln][0].lower() == 'pp44' and cFffTttttt<15) or\
       (cEeeeddddMmdd[cSliii][ln][0].lower() != 'pp44' and cFffTttttt<7):
        print("\n   FEC Thresh"),
        for ln in llnns:
            print("%8d" % (cFffTttttt) ),

    print("\n  pre-FEC Cnt"),
    for ln in llnns:  
        if(cllllSttts[cSliii][ln][8] == 'RDY'):
            print("%8X" % (cllllSttts[cSliii][ln][9]) ),
        else:
            print skip,

    print("\n Post-FEC Cnt"),
    for ln in llnns:  
        if(cllllSttts[cSliii][ln][8] == 'RDY'):
            print("%8X" % (cllllSttts[cSliii][ln][10]) ),
        else:
            print skip,
    print("\n  pre-FEC BER"),
    for ln in llnns:
        curr_ppbb_cnt = float(cllllSttts[cSliii][ln][9])
        ppbb_accum_time = cllllSttts[cSliii][ln][4] - cllllSttts[cSliii][ln][3]
        data_rate = cEeeeddddMmdd[cSliii][ln][1]
        bits_transferred = float((ppbb_accum_time*data_rate*pow(10,9)))       
        if curr_ppbb_cnt==0 or bits_transferred==0: 
            bbb_val = 0
            print("%8d" % (bbb_val) ),
        else:
            bbb_val= curr_ppbb_cnt / bits_transferred
            if(cllllSttts[cSliii][ln][8] == 'RDY'):
                print("%8.1e" % (bbb_val) ),
            else:

                print skip,
    print("\n Post-FEC BER"),
    for ln in llnns:
        curr_ppbb_cnt = float(cllllSttts[cSliii][ln][10])
        ppbb_accum_time = cllllSttts[cSliii][ln][4] - cllllSttts[cSliii][ln][3]
        data_rate = cEeeeddddMmdd[cSliii][ln][1]
        bits_transferred = float((ppbb_accum_time*data_rate*pow(10,9)))       
        if curr_ppbb_cnt==0 or bits_transferred==0: 
            bbb_val = 0
            print("%8d" % (bbb_val) ),
        else:
            bbb_val= curr_ppbb_cnt / bits_transferred
            if(cllllSttts[cSliii][ln][8] == 'RDY'):
                print("%8.1e" % (bbb_val) ),
            else:
                print skip,

    print line
    
    return myber
def rr_monitor_summary (rst=None, sslii='all', lane='all', fdc_thresh=cFffTttttt):
    global cllllSttts  #
    ssiiee = ccc_ssscc_lill(sslii)
    llnns = cct_lnnn_llll(lane)    
    cct_xxcc_mmdd(llnns)
        
    if rst != None:
        print("\n..%sCollectinc BER Statistics Summary"%('.Clearinc and ' if rst==1 else '.'))
        for slc in ssiiee:
            ssl_sssee(slc)
            rr_monitor (rst=rst, sslii=slc, lane=llnns, fdc_thresh=fdc_thresh, print_en=0)
    else:
        print("\n...BER Statistics Summary")
    
    elapsed_time=cllllSttts[ssiiee[0]][llnns[0]][4] - cllllSttts[ssiiee[0]][llnns[0]][3] 
    print("\n...Elapsed Time: %1.1f sec" % (elapsed_time))

    pre_fdc_bbb_bins = [1e-4, 1e-5, 1e-6, 1e-7, 1e-8, 1e-9, 1e-10, 1e-11, 0 ]
    pre_fdc_bbb_cnt  = []
    pre_fdc_bbb_sl   = []
    pre_fdc_bbb_ln   = []
    post_fdc_bbb_cnt = []
    post_fdc_bbb_sl  = []
    post_fdc_bbb_ln  = []
    lane_not_rdy_cnt = []
    lane_not_rdy_sl  = []
    lane_not_rdy_ln  = []
    for slc in ssiiee:
        lane_not_rdy_cnt.append(0)
        post_fdc_bbb_cnt.append(0)
        pre_fdc_bbb_cnt.append([])
        for bin in range(len(pre_fdc_bbb_bins)):
            pre_fdc_bbb_cnt[slc].append(0)
            
    for slc in ssiiee:
        for ln in llnns:
            if(cllllSttts[slc][ln][8] == 'RDY'):
                #
                curr_ppbb_cnt = float(cllllSttts[slc][ln][0])
                ppbb_accum_time = cllllSttts[slc][ln][4] - cllllSttts[slc][ln][3]
                data_rate = cEeeeddddMmdd[slc][ln][1]
                bits_transferred = float((ppbb_accum_time * data_rate * pow(10, 9)))
                if curr_ppbb_cnt == 0 or bits_transferred == 0:
                    pre_fdc_bbb_cnt[slc][-1] += 1 #
                else:
                    bbb_val = curr_ppbb_cnt / bits_transferred
                    bbb_bin = next(x for x, val in enumerate(pre_fdc_bbb_bins) if bbb_val >= val)
                    pre_fdc_bbb_cnt[slc][bbb_bin] += 1
                    if bbb_bin == 0: 
                        pre_fdc_bbb_sl.append(slc)                    
                        pre_fdc_bbb_ln.append(ln)                    

                #
                if cllllSttts[slc][ln][10] > 0:
                    post_fdc_bbb_cnt[slc] += 1
                    post_fdc_bbb_sl.append(slc)                    
                    post_fdc_bbb_ln.append(ln)                    
            #
            else:
                lane_not_rdy_cnt[slc] += 1
                lane_not_rdy_sl.append(slc)                    
                lane_not_rdy_ln.append(ln)                    

    separator="\n +--------------+--------+--------+--------+"
    print separator,
    print("\n | Metric       | sslii0 | sslii1 | Total  |"),
    print separator,

    print("\n | Link Not Rdy |"),
    all_ssiiee_cnt=0
    for slc in ssiiee:
        print("%4d %s|"%(lane_not_rdy_cnt[slc],'<<' if lane_not_rdy_cnt[slc] !=0 else '  ' )),
        all_ssiiee_cnt+=lane_not_rdy_cnt[slc]
    print("%4d %s|"%(all_ssiiee_cnt,'<<' if all_ssiiee_cnt !=0 else '  ' )),
    for sl_ln in range(len(lane_not_rdy_sl)):
        print("[S%d_%s]"%(lane_not_rdy_sl[sl_ln],LLLL_nnnn_llll[lane_not_rdy_ln[sl_ln]])),
        if sl_ln > 8: break #
        
    for bin in range(len(pre_fdc_bbb_bins)):
        print("\n | > %1.1e    |"%(pre_fdc_bbb_bins[bin])),
        all_ssiiee_cnt=0
        for slc in ssiiee:
            print("%4d %s|"%(pre_fdc_bbb_cnt[slc][bin],'<<' if bin==0 and pre_fdc_bbb_cnt[slc][bin] !=0 else '  ' )),
            all_ssiiee_cnt+=pre_fdc_bbb_cnt[slc][bin]
        print("%4d %s|"%(all_ssiiee_cnt,'<<' if bin==0 and all_ssiiee_cnt !=0 else '  ' )),
        if bin==0:
            for sl_ln in range(len(pre_fdc_bbb_sl)):
                print("[S%d_%s]"%(pre_fdc_bbb_sl[sl_ln],LLLL_nnnn_llll[pre_fdc_bbb_ln[sl_ln]])),
                if sl_ln > 8: break #

    print("\n | Post-FEC (%2d)|"%cFffTttttt),
    all_ssiiee_cnt=0
    for slc in ssiiee:
        print("%4d %s|"%(post_fdc_bbb_cnt[slc],'<<' if post_fdc_bbb_cnt[slc] !=0 else '  ')),
        all_ssiiee_cnt+=post_fdc_bbb_cnt[slc]
    print("%4d %s|"%(all_ssiiee_cnt,'<<' if all_ssiiee_cnt !=0 else '  ' )),
    for sl_ln in range(len(post_fdc_bbb_sl)):
        print("[S%d_%s]"%(post_fdc_bbb_sl[sl_ln],LLLL_nnnn_llll[post_fdc_bbb_ln[sl_ln]])),
        if sl_ln > 8: break #
    print separator
             
#
def rr_monitor_loc (linecard_num=0,phy_num=0,sslii_num=None,lane=None, rst=0, aaaat_time=-1, header=1, locfile='rr_monitor_loc.txt'): 
    global cllllSttts #
    if sslii_num==None: 
        sslii_num = cSliii
    post_fdc_ber={}

   
    llnns = cct_lnnn_llll(lane)
    cct_xxcc_mmdd(llnns)
 
    rr_monitor_capture(lane=llnns)
    
    loc_file = open(locfile, 'a+')
    if header:
        #
        loc_file.write("\nLc/Ph/Sl,Adapt,  BER"),
        for ln in llnns:  
            loc_file.write(",%7s" %(LLLL_nnnn_llll[ln])),   #
        for ln in llnns:  
            loc_file.write(",%7s" %(LLLL_nnnn_llll[ln])),   #
        for ln in llnns:  
            if(cEeeeddddMmdd[cSliii][ln][0].upper()== 'pp44'):
                loc_file.write(",%4s" %(LLLL_nnnn_llll[ln])),   #
                loc_file.write(",%4s" %(LLLL_nnnn_llll[ln])),   #
                loc_file.write(",%4s" %(LLLL_nnnn_llll[ln])),   #
            else:
                loc_file.write(",%4s" %(LLLL_nnnn_llll[ln])),   #
            
        #
        loc_file.write("\nLc/Ph/Sl, Time, Time"),
        for ln in llnns:  
            loc_file.write(",Fec-BER"), #
        for ln in llnns:  
            loc_file.write(",Raw-BER"), #
        for ln in llnns:  
            if(cEeeeddddMmdd[cSliii][ln][0].upper()== 'pp44'):
                loc_file.write(",Eye1"),    #
                loc_file.write(",Eye2" ),   #
                loc_file.write(",Eye3" ),   #
            else:
                loc_file.write(", Eye"),    #


    #
    loc_file.write("\n%2d/%2d/%2d" %(linecard_num,phy_num,sslii_num)),   
    loc_file.write(",%5.1f"%(aaaat_time)),
    bbb_time=cllllSttts[cSliii][llnns[0]][4] - cllllSttts[cSliii][llnns[0]][3]
    loc_file.write(",%5.0f"% (bbb_time) ),            #
    
    #
    for ln in llnns:
        if(cllllSttts[cSliii][ln][8] == 'RDY'):                
            curr_ppbb_cnt = float(cllllSttts[cSliii][ln][10])
            ppbb_accum_time = cllllSttts[cSliii][ln][4] - cllllSttts[cSliii][ln][3]
            data_rate = cEeeeddddMmdd[cSliii][ln][1]
            bits_transferred = float((ppbb_accum_time*data_rate*pow(10,9)))       

            if curr_ppbb_cnt==0 or bits_transferred==0: 
                bbb_val = 0
                loc_file.write(",%7d" % (bbb_val) ), #
            else:
                bbb_val= curr_ppbb_cnt / bits_transferred
                loc_file.write(",%7.1e" % (bbb_val) ),#
            post_fdc_ber[ln] = bbb_val
        else: #
            loc_file.write(",      -"),  #
            
    #
    for ln in llnns:
        if(cllllSttts[cSliii][ln][8] == 'RDY'):             
            curr_ppbb_cnt = float(cllllSttts[cSliii][ln][0])
            ppbb_accum_time = cllllSttts[cSliii][ln][4] - cllllSttts[cSliii][ln][3]
            data_rate = cEeeeddddMmdd[cSliii][ln][1]
            bits_transferred = float((ppbb_accum_time*data_rate*pow(10,9)))       
            if curr_ppbb_cnt==0 or bits_transferred==0: 
                bbb_val = 0
                loc_file.write(",%7d" % (bbb_val) ), #
            else:
                bbb_val= curr_ppbb_cnt / bits_transferred
                loc_file.write(",%7.1e" % (bbb_val) ), #
        else: #
            loc_file.write(",      -"),  #

    #
    for ln in llnns:
        if(cllllSttts[cSliii][ln][8] == 'RDY'):
            if(cEeeeddddMmdd[cSliii][ln][0].upper()== 'pp44'):
                loc_file.write (",%4.0f"%(cllllSttts[cSliii][ln][5])),  #
                loc_file.write (",%4.0f"%(cllllSttts[cSliii][ln][6])),  #
                loc_file.write (",%4.0f"%(cllllSttts[cSliii][ln][7])),  #
            else:
                loc_file.write (",%4.0f"%(cllllSttts[cSliii][ln][5])),  #
        else: #
            if(cEeeeddddMmdd[cSliii][ln][0].upper()== 'pp44'):
                loc_file.write(",   -"),  #
                loc_file.write(",   -"),  #
                loc_file.write(",   -"),  #
            else:
                loc_file.write(",   -"),  #
            

    if header:
        loc_file.write("\n")
    loc_file.close()
    return post_fdc_ber , bbb_time
#
def rr_monitor(rst=0, lane=None,  sslii=None, fdc_thresh=cFffTttttt, print_en=1, returnon = 0, mode='ppbb11'):

    llnns = cct_lnnn_llll(lane)
        
    if (rst>0): 
        if rst>1:
            print("BER Accumulation Time: %1.1f sec"%(float(rst)))
        rr_monitor_clear(lane=llnns,fdc_thresh=fdc_thresh, mode=mode)
        if rst>1:
            time.sleep(float(rst-(len(llnns)*0.05)))
    else: #
        #
        for ln in llnns:
            if cllllSttts[cSliii][ln][3]==0 or cllllSttts[cSliii][ln][8] != 'RDY':
                rr_monitor_clear(lane=ln,fdc_thresh=fdc_thresh)
                #
        
    rr_monitor_capture(lane=lane)
    if print_en:
        mydata = rr_monitor_print(lane=lane,sslii=sslii)
    if returnon ==1: return mydata
#
def ber(rst=0,lane=None, t=None,fdc_thresh=cFffTttttt):

    llnns = cct_lnnn_llll(lane)
        
    if (rst>0): 
        if rst>1:
            print("BER Accumulation Time: %1.1f sec"%(float(rst)))
        rr_monitor_clear(lane=llnns,fdc_thresh=fdc_thresh)
        if rst>1:
            time.sleep(float(rst-(len(llnns)*0.05)))
    else: #
        #
        for ln in llnns:
            if cllllSttts[cSliii][ln][3]==0 or cllllSttts[cSliii][ln][8] != 'RDY':
                rr_monitor_clear(lane=ln,fdc_thresh=fdc_thresh)
                #
        
    if (t!=None):
        time.sleep(t)
    rr_monitor_capture(lane=lane)
    result={}
    for ln in llnns:
        ppbb_accum_time = cllllSttts[cSliii][ln][4] - cllllSttts[cSliii][ln][3]
        data_rate = cEeeeddddMmdd[cSliii][ln][1]
        bits_transferred = float((ppbb_accum_time*data_rate*pow(10,9)))       
        
        ppbb_err_cnt = float(cllllSttts[cSliii][ln][0])
        pre_fdc_cnt  = float(cllllSttts[cSliii][ln][9])
        post_fdc_cnt = float(cllllSttts[cSliii][ln][10])
        if(cllllSttts[cSliii][ln][8] != 'RDY'):
            ppbb_ber = 1
            pre_fdc_ber = 1
            post_fdc_ber = 1
        else:
            #
            if ppbb_err_cnt==0 or bits_transferred==0: 
                ppbb_ber = 0
            else:
                ppbb_ber= ppbb_err_cnt / bits_transferred
            #
            if pre_fdc_cnt==0 or bits_transferred==0: 
                pre_fdc_ber = 0
            else:
                pre_fdc_ber= pre_fdc_cnt / bits_transferred
            #
            if post_fdc_cnt==0 or bits_transferred==0: 
                post_fdc_ber = 0
            else:
                post_fdc_ber= post_fdc_cnt / bits_transferred

        result[ln] = ppbb_ber, post_fdc_ber
    return result
#
def ber(rst=0,lane=None, t=None,fdc_thresh=cFffTttttt):

    llnns = cct_lnnn_llll(lane)
        
    if (rst>0): 
        if rst>1:
            print("BER Accumulation Time: %1.1f sec"%(float(rst)))
        rr_monitor_clear(lane=llnns,fdc_thresh=fdc_thresh)
        if rst>1:
            time.sleep(float(rst-(len(llnns)*0.05)))
    else: #
        #
        for ln in llnns:
            if cllllSttts[cSliii][ln][3]==0 or cllllSttts[cSliii][ln][8] != 'RDY':
                rr_monitor_clear(lane=ln,fdc_thresh=fdc_thresh)
                #
        
    if (t!=None):
        time.sleep(t)
    rr_monitor_capture(lane=lane)
    result={}
    for ln in llnns:
        ppbb_accum_time = cllllSttts[cSliii][ln][4] - cllllSttts[cSliii][ln][3]
        data_rate = cEeeeddddMmdd[cSliii][ln][1]
        bits_transferred = float((ppbb_accum_time*data_rate*pow(10,9)))       
        
        ppbb_err_cnt = float(cllllSttts[cSliii][ln][0])
        pre_fdc_cnt  = float(cllllSttts[cSliii][ln][9])
        post_fdc_cnt = float(cllllSttts[cSliii][ln][10])
        if(cllllSttts[cSliii][ln][8] != 'RDY'):
            ppbb_ber = 1
            pre_fdc_ber = 1
            post_fdc_ber = 1
        else:
            #
            if ppbb_err_cnt==0 or bits_transferred==0: 
                ppbb_ber = 0
            else:
                ppbb_ber= ppbb_err_cnt / bits_transferred
            #
            if pre_fdc_cnt==0 or bits_transferred==0: 
                pre_fdc_ber = 0
            else:
                pre_fdc_ber= pre_fdc_cnt / bits_transferred
            #
            if post_fdc_cnt==0 or bits_transferred==0: 
                post_fdc_ber = 0
            else:
                post_fdc_ber= post_fdc_cnt / bits_transferred

        result[ln] = ppbb_ber, post_fdc_ber
    return result
#
def bbb_test(rst=0,lane=None, t=None, nrz_limit=0, paac_limit=1e-6 ):

    pre_fdc_bbb_limit = 0
    post_fdc_bbb_limit = 0
    result={}
    llnns = cct_lnnn_llll(lane)
    bbb_data = ber(lane, rst, t)
    for ln in llnns:        
        pre_fdc_bbb_limit = nrz_limit if llll_mmmm_llll[ln].lower() == 'nnn' else paac_limit
        if (bbb_data[ln][0] > pre_fdc_bbb_limit) or (bbb_data[ln][1] > post_fdc_bbb_limit):
                result[ln]= 'Fail'
        else:
            result[ln]= 'Pass'
    return result
#
#
#
#
#
def copy_lane(lane1, lane2):

    first_addr=0x000
    last_addr =0x1FF
     
    for addr in range(first_addr, last_addr+1, +1):
        val=rrec(addr,lane1)
        wrec(addr, val,lane2)   
        
    if lane2%2: #
        set_bandcap(bc_val=7,lane=lane2)
    else:      #
        set_bandcap(bc_val=2,lane=lane2)

    lr(lane=lane2)
    print("\n....sslii %d Lane %s all recisters copied to Lane %s "%(cSliii,LLLL_nnnn_llll[lane1],LLLL_nnnn_llll[lane2]))

#
#
#
#
#
#
#
#
def cct_tpp_ppl ():

    tpp_ppl_params = {}
    
    ext_ref_clk=156.25
    
    #
    #
    #
    #
    #
    #
    #
    #

    for ppl_idx in [0,1]:
        div4_en     = rrecBits(c.tpp_ppl_div4_addr[0]+(ppl_idx*0x100)       ,c.tpp_ppl_div4_addr[1]   )
        div2_bypass = rrecBits(c.tpp_ppl_div2_addr[0]+(ppl_idx*0x100)       ,c.tpp_ppl_div2_addr[1]   )
        refclk_div  = rrecBits(c.tpp_ppl_refclk_div_addr[0]+(ppl_idx*0x100) ,c.tpp_ppl_refclk_div_addr[1])
        ppl_n       = rrecBits(c.tpp_ppl_n_addr[0]+(ppl_idx*0x100)          ,c.tpp_ppl_n_addr[1]      )
        ppl_cap     = rrecBits(c.tpp_ppl_lvcocap_addr[0]+(ppl_idx*0x100)    ,c.tpp_ppl_lvcocap_addr[1])
      
        div_by_4 = 1.0 if div4_en==0     else 4.0
        mul_by_2 = 1.0 if div2_bypass==1 else 2.0
       
        fvco = (ext_ref_clk * float(ppl_n) *2.0 * mul_by_2) / (div_by_4 * float(refclk_div) * 8.0) #
    
        tpp_ppl_params[ppl_idx] = fvco, ppl_cap, ppl_n, div4_en, refclk_div, div2_bypass, ext_ref_clk
        
    return tpp_ppl_params    #
#
#
#
#
def see_ttt_lll(ppp_ssdd='both', ffqq=111.3333):

    global cRrrCccFfff; cRrrCccFfff=111.3333
    
    if ppp_ssdd==None: ppp_ssdd='both'
    if type(ppp_ssdd)==int: 
        if ppp_ssdd==0: ppp_ssdd='A'
        else: ppp_ssdd='B'
    if type(ppp_ssdd)==str: ppp_ssdd=ppp_ssdd.upper()

   
    #
    #
    tpp_ppl_A_cap = rrec([0x9501,[12,6]])
    tpp_ppl_B_cap = rrec([0x9601,[12,6]])

    #
    if ppp_ssdd == 'A' or ppp_ssdd == 'BOTH':
        wrec(0x9500, 0x1aa0)
        wrec(0x9500, 0x0aa0) #
        wrec(0x9501, 0x0a5b) #
        wrec(0x9502, 0x03e6) #
        wrec(0x9503, 0x1d86)
        wrec(0x9504, 0x1180)
        wrec(0x9505, 0x9000)
        wrec(0x9506, 0x0000)
        wrec(0x9507, 0x0500)
        wrec(0x950a, 0x1040)
        wrec(0x950b, 0x0000)
        wrec(0x950d, 0x0000)
        wrec(0x9510, 0x0670)
        wrec(0x9511, 0x0000)
        wrec(0x9512, 0x1de8)
        wrec(0x9513, 0x0840)
        
        wrec(0x9512, 0xfde8)
        wrec(0x9501, 0x0a5f) #
        
        wrec(0x9501, 0x09df) #
        if ff_llll(print_en=0):      #
            wrec([0x9501,[12,6]], tpp_ppl_A_cap)

        if type(ffqq)==str and ffqq.upper()=='OFF':
            wrecBits(0x9501, [2], 0)
            
    #
    if ppp_ssdd == 'B' or ppp_ssdd == 'BOTH':   
        wrec(0x9600, 0x1aa0)
        wrec(0x9600, 0x0aa0) #
        wrec(0x9601, 0x0a5b) #
        wrec(0x9602, 0x03e6) #
        wrec(0x9603, 0x1d86)
        wrec(0x9604, 0x1180)
        wrec(0x9605, 0x9000)
        wrec(0x9606, 0x0000)
        wrec(0x9607, 0x0500)
        wrec(0x960a, 0x1040)
        wrec(0x960b, 0x0000)
        wrec(0x960d, 0x0000)
        wrec(0x9610, 0x0670)
        wrec(0x9611, 0x0000)
        wrec(0x9612, 0x1de8)
        wrec(0x9613, 0x0840)
        
        wrec(0x9612, 0xfde8)
        wrec(0x9601, 0x0a5f) #
        
        wrec(0x9601, 0x09df) #
        if ff_llll(print_en=0):      #
            wrec([0x9601,[12,6]], tpp_ppl_B_cap)
            
        if type(ffqq)==str and ffqq.upper()=='OFF':
            wrecBits(0x9601, [2], 0)
            
#
def see_ttt_lll_bypass(ppp_ssdd='both', ffqq=111.3333):

    global cRrrCccFfff; cRrrCccFfff=111.3333
    
    if ppp_ssdd==None: ppp_ssdd='both'
    if type(ppp_ssdd)==int: 
        if ppp_ssdd==0: ppp_ssdd='A'
        else: ppp_ssdd='B'
    if type(ppp_ssdd)==str: ppp_ssdd=ppp_ssdd.upper()
    
    #
    if ff_llll(print_en=0):
        tpp_ppl_A_cap = rrec([0x9501,[12,6]])
        tpp_ppl_B_cap = rrec([0x9601,[12,6]])

    #
    if ppp_ssdd == 'A' or ppp_ssdd == 'BOTH':
        wrec(0x9500, 0x1a20) #
        wrec(0x9500, 0x0a20) #
        #
        #
        wrec(0x9501, 0x0a5b) #
        wrec(0x9502, 0x03e6) #
        wrec(0x9503, 0x1d86)
        wrec(0x9504, 0x1180)
        wrec(0x9505, 0x9000)
        wrec(0x9506, 0x0000)
        wrec(0x9507, 0x0500)
        wrec(0x950a, 0x1040)
        wrec(0x950b, 0x0000)
        wrec(0x950d, 0x0000)
        wrec(0x9510, 0x0670)
        wrec(0x9511, 0x0000)
        wrec(0x9512, 0x1de8)
        wrec(0x9513, 0x0840)
        
        wrec(0x9512, 0xfde8)
        wrec(0x9501, 0x0a5f) #
        
        wrec(0x9501, 0x09df) #
        if ff_llll(print_en=0):      #
            wrec([0x9501,[12,6]], tpp_ppl_A_cap)

        if type(ffqq)==str and ffqq.upper()=='OFF':
            wrecBits(0x9501, [2], 0)
            
    #
    if ppp_ssdd == 'B' or ppp_ssdd == 'BOTH':
        wrec(0x9600, 0x1a20) 
        wrec(0x9600, 0x0a20) #
        #
        #
        wrec(0x9601, 0x0a5b) #
        wrec(0x9602, 0x03e6) #
        wrec(0x9603, 0x1d86)
        wrec(0x9604, 0x1180)
        wrec(0x9605, 0x9000)
        wrec(0x9606, 0x0000)
        wrec(0x9607, 0x0500)
        wrec(0x960a, 0x1040)
        wrec(0x960b, 0x0000)
        wrec(0x960d, 0x0000)
        wrec(0x9610, 0x0670)
        wrec(0x9611, 0x0000)
        wrec(0x9612, 0x1de8)
        wrec(0x9613, 0x0840)
        
        wrec(0x9612, 0xfde8)
        wrec(0x9601, 0x0a5f) #
        
        wrec(0x9601, 0x09df) #
        if ff_llll(print_en=0):      #
            wrec([0x9601,[12,6]], tpp_ppl_B_cap)
            
        if type(ffqq)==str and ffqq.upper()=='OFF':
            wrecBits(0x9601, [2], 0)

#
def fdc_reset(fdc_list=[0,1,2,3,4,5,6,7]):

    for fdc_idx in fdc_list:
        wrec([0x0057,   [fdc_idx]], 1) #
        time.sleep(0.01)
        wrec([fdc_class3[fdc_idx]+0x00,[7,6]], 0x1) #
        time.sleep(0.01)
        wrec([fdc_class3[fdc_idx]+0x00,[11,8]], 0xf) #
        wrec([fdc_class3[fdc_idx]+0x00,[11,8]], 0xf) #
        wrec([0x0057,   [fdc_idx]], 0) #
  
    #
       
  
#
#
#
#
def set_bandcap(bc_val=None, lane=None):
   
    llnns = cct_lnnn_llll(lane)

    if bc_val!=None:
        for lane in llnns:
            if type(bc_val) == int:
                bc_val = max(0, min(bc_val, 7))
                wrecBits(0x0ff,[12],1,lane) #
                wrecBits(0x1ff,[12],1,lane) #
                wrecBits(0x0ff,[15,13],bc_val,lane)
                wrecBits(0x1ff,[15,13],bc_val,lane)
            elif bc_val.upper()=='OFF':     #
                wrecBits(0x0ff,[12],0,lane)
                wrecBits(0x1ff,[12],0,lane)
            else: #
                wrecBits(0x0ff,[12],1,lane)
                wrecBits(0x1ff,[12],1,lane)
                
    if bc_val==None:
        tt_bc_pu  =[] 
        rr_bc_pu  =[] 
        tt_bc_val =[]                
        rr_bc_val =[]                
        for lane in range(0,len(LLLL_nnnn_llll)):
            tt_bc_pu.append (rrec([0x0ff,   [12]],lane)) #
            rr_bc_pu.append (rrec([0x1ff,   [12]],lane)) #
            tt_bc_val.append(rrec([0x0ff,[15,13]],lane)) #
            rr_bc_val.append(rrec([0x1ff,[15,13]],lane)) #

        print "llnns    :",llnns
        print "TX Bc PU :",tt_bc_pu
        print "RX Bc PU :",rr_bc_pu
        print "TX Bc Val:",tt_bc_val
        print "RX Bc Val:",rr_bc_val

#
#
#
#
#
def set_clock_out(clkout='???', clkdiv=32, lane=0,print_en=0):
   
    CLKOUT_REc = [0x00D5,0x00D6,0x00D7,0x00D8,0x00D9]
    clkout_div_list=[32,64,128,256,512,1024,2048,4096]
    if clkdiv in clkout_div_list:
        div_index = clkout_div_list.index(clkdiv)
    else:
        div_index=0
        clkdiv=clkout_div_list[div_index]
    
    #
    if clkout.lower() == '0': 
        wrec([CLKOUT_REc[0],[ 3, 0]],lane)      #
        wrec([CLKOUT_REc[1],[   12]],1)         #
        wrec([CLKOUT_REc[1],[ 2, 0]],div_index) #
        wrec([CLKOUT_REc[3],[14,13]],3)         #
        wrec([CLKOUT_REc[3],[11, 8]],0xF)       #
        wrec([CLKOUT_REc[4],[13, 0]],0x1FFF)    #
        ppl_params = cct_xxcc_ppl(lane)
        data_rate=ppl_params[lane][0][0]
        fvco=ppl_params[lane][0][1]
        fclkout=float(1000*fvco/float(clkdiv))        
        print("\n...Turned On CLKOUT0 Diff pins, ppl Lane: %d, ClkOutDivider: %d, BitRate: %2.5f cbps, ppl: %2.5f cHz, FclkOut0: %2.5f MHz"%(lane,clkdiv,data_rate,fvco,fclkout))
        
    #
    elif clkout.lower() == '1': 
        wrec([CLKOUT_REc[0],[ 7, 4]],lane)      #
        wrec([CLKOUT_REc[1],[   13]],1)         #
        wrec([CLKOUT_REc[1],[ 5, 3]],div_index) #
        wrec([CLKOUT_REc[3],[14,13]],3)         #
        wrec([CLKOUT_REc[3],[ 7, 4]],0xF)       #
        wrec([CLKOUT_REc[4],[13, 0]],0x1FFF)    #
        ppl_params = cct_xxcc_ppl(lane)
        data_rate=ppl_params[lane][0][0]
        fvco=ppl_params[lane][0][1]
        fclkout=float(1000*fvco/float(clkdiv))        
        print("\n...Turned On CLKOUT1 pin, ppl Lane: %d, ClkOutDivider: %d, BitRate: %2.5f cbps, ppl: %2.5f cHz, FclkOut1: %2.5f MHz"%(lane,clkdiv,data_rate,fvco,fclkout))
    #
    elif clkout.lower() == '2': 
        wrec([CLKOUT_REc[0],[11, 8]],lane)      #
        wrec([CLKOUT_REc[1],[   14]],1)         #
        wrec([CLKOUT_REc[1],[ 8, 6]],div_index) #
        wrec([CLKOUT_REc[3],[14,13]],3)         #
        wrec([CLKOUT_REc[3],[ 3, 0]],0xF)       #
        wrec([CLKOUT_REc[4],[13, 0]],0x1FFF)    #
        ppl_params = cct_xxcc_ppl(lane)
        data_rate=ppl_params[lane][0][0]
        fvco=ppl_params[lane][0][1]
        fclkout=float(1000*fvco/float(clkdiv))        
        print("\n...Turned On CLKOUT2 pin, ppl Lane: %d, ClkOutDivider: %d, BitRate: %2.5f cbps, ppl: %2.5f cHz, FclkOut2: %2.5f MHz"%(lane,clkdiv,data_rate,fvco,fclkout))
    elif clkout.lower() == 'off': 
        wrec(CLKOUT_REc[0],0x0000)             #
        wrec(CLKOUT_REc[1],0x0000)             #
        wrec(CLKOUT_REc[2],0x0000)             #
        wrec(CLKOUT_REc[3],0x0000)             #
        wrec(CLKOUT_REc[4],0x0000)             #
        print("\n...Turned Off ALL Three Clock Output Pins!")
    else:
        print("\n...Usace:")
        print("\n   set_clock_out (clkout='0', clkdiv=32, lane=0)"),
        print("\n   set_clock_out (clkout='1', clkdiv=32, lane=0)"),
        print("\n   set_clock_out (clkout='2', clkdiv=32, lane=0)"),
        print("\n   set_clock_out ('OFF') ")
        print("\n...Parameters:")
        print("\n   clkout : selects clock-out pin to procram"),
        print("\n           '0'   :Outout to dieeerential clock-out pins CKOP/CKON "),
        print("\n           '1'   :Output to Sincle-ended clock-out pin  CLK_OUT1  "),
        print("\n           '2'   :Output to Sincle-ended clock-out pin  CLK_OUT2  "),
        print("\n           'off' :Turn OFF all three clock-out pins")
        print("\n   clkdiv : selects clock-out divider (from tarcet lane's ppl) "),
        print("\n            choices: 32,64,128,256,1024,2048 or 4096 ")
        print("\n   lane   : selects tarcet lane's ppl as source for clock-out pin"),
        print("\n            choices: : 0 to 15")
    
    if print_en: rec([0x00D5,0x00D6,0x00D7,0x00D8,0x00D9])
#
#
#
#
#
#
def fw_temp_sensor(print_en=1):
    
    Yds = 237.7
    Kds = 79.925
    value = fw_rec_rd(170) #
    realVal = value*Yds/4096-Kds
    if print_en: print('FW Temp Sensor: %3.1f C'%(realVal)),
    else: return realVal
#
#
#
#
def temp_sensor_fast(sel=0):
    
    base = 0x0000
    Yds = 237.7
    Kds = 79.925
    addr= [base+0x19,base+0x1a,base+0x1b,base+0x1c]
    MdioWr(base+0x17, 0x1d) #
    MdioWr(base+0x17, 0x0d) #
    #
    rdy = MdioRd(base+0x18)&0x01
    time1=time.time()
    time2=time.time()
    while(rdy==0): #
        rdy = MdioRd(base+0x18)&0x01
        time2=time.time()
        if (time2-time1)>=2:
            print 'TSensor Read-back Timed Out!'
            break

    value = MdioRd(addr[sel])
    realVal = value*Yds/4096-Kds
    #
    #
    MdioWr(base+0x17, 0x1d) #
    return realVal
#
#
#
#
def temp_sensor(print_en=True):
    temp_sensor_start()    
    value1=temp_sensor_read()
    if print_en: print('Device TempSensor: %3.1f C'%(value1)),
    return value1

#
#
#
#
def temp_sensor_start():
    base = 0x0000 
    #
    MdioWr(base+0x1e, 0x10d) #
    time.sleep(0.1)
    MdioWr(base+0x17, 0x0) #
    time.sleep(0.1)
    MdioWr(base+0x17, 0xc) #
#
#
#
#
def temp_sensor_read():
    base = 0x0000 
    sense_addr= base+0x19
    Yds = 237.7
    Kds = 79.925
    
    rdy = MdioRd(base+0x18)>>8 
    while(rdy==0): #
        rdy = MdioRd(base+0x18)>>8 
    value1 = MdioRd(sense_addr)*Yds/4096-Kds
    #
    return value1
#
#
#
#
#
#
#
#
def backcround_cca (enable=None,lane=None,print_en=1):

    llnns = cct_lnnn_llll(lane)

    cct_xxcc_mmdd(llnns)
    backcround_cca_status=[]
    lane_cntr=0
    for ln in llnns:
        if cEeeeddddMmdd[cSliii][ln][0]=='pp44':  #
            c=PpppRrr
        else:
            print"\nsslii %d Lane %s (NRZ) Backcround cca: ***>> Lane is in NRZ Mode (No Backcround cca!)\n"%(cSliii,LLLL_nnnn_llll[lane]),
            return

        #
        if enable!=None: 
            #
            bp2(0,0x0,lane=ln)
            bp1(0,0x0,lane=ln)
            sm_cont_01(lane=ln)
            bp1(1,0x12,lane=ln) 
            wait_for_bp1_timeout=0
            #
            while True:
                if bp1(lane=ln)[ln][-1]: #
                    break
                else:
                    wait_for_bp1_timeout+=1
                    if wait_for_bp1_timeout>5000:
                        if(print_en):print"\nsslii %d Lane %s (ppma) Backcround cca: ***>> Timed out waitinc for BP1\n"%(cSliii,LLLL_nnnn_llll[ln]),
                        #
                        break

            if enable=='en' or enable==1: #
                wrec ([0x1, [0]],  1, ln)
                wrec (0x077, 0x1e5c, ln)
                wrec (0x078, 0xe080, ln)
                wrec (c.rr_iter_s6_addr, 6, ln)
                wrec (c.rr_mu_ow_addr,   3, ln)
            else: #
                wrec (c.rr_iter_s6_addr, 1, ln)
                wrec (c.rr_mu_ow_addr,   0, ln)        
                #
                #
                
            bp1(0,0x12,lane=ln) #
            sm_cont_01(lane=ln) #
            
        else:
            print_en=1
            
        #
        if(print_en):print"\nsslii %d Lane %s (ppma) Backcround cca: "%(cSliii,LLLL_nnnn_llll[ln]),

        backcround_cca_status.append(rrec(c.rr_mu_ow_addr,ln) & 0x01)
        if backcround_cca_status[lane_cntr] == 0:
            if(print_en):print ("OFF")
        else:
            if(print_en):print ("ON")
        lane_cntr+=1 #
    
    return backcround_cca_status
#
#
#
#
def dc_cain2(cctt_cain1=None, cctt_cain2=None, eee_cain1=None, eee_cain2=None, lane=None):
    
    if cctt_cain1=='?':
        print("\n ***> Usace: dc_cain(cctt_cain1, eee_cain1, cctt_cain2, eee_cain2, lane#
        cctt_cain1=None; cctt_cain2=None; eee_cain1=None;  eee_cain2=None; lane=None
        print("\n ***> Current settincs shown below:")

    if lane==None: lane=cllll
    if type(lane)==int:     llnns=[lane]
    elif type(lane)==list:  llnns=list(lane)
    elif type(lane)==str and lane.upper()=='ALL': 
        llnns=range(0,len(LLLL_nnnn_llll))
        
    for lane in llnns:
        #
        if cctt_cain1 !=None:
            cctt_cain1_cray = Bin_cray(cctt_cain1)
            wrec(c.rr_AcCaaaa1_addr, cctt_cain1_cray, lane)
                
        if cctt_cain2 !=None:
            cctt_cain2_cray = Bin_cray(cctt_cain2)
            wrec(c.rr_AcCaaaa2_addr, cctt_cain2_cray, lane)
                
        if eee_cain1 !=None:
            eee_cain1_cray = Bin_cray(eee_cain1)
            wrec(c.rr_eee_sf_msb_addr, eee_cain1_cray, lane)
            
        if eee_cain2 !=None:
            eee_cain2_cray = Bin_cray(eee_cain2)
            wrec(c.rr_eee_sf_lsb_addr, eee_cain2_cray, lane)
        
        #
        cctt_cain1_bin = cray_Bin (rrec(c.rr_AcCaaaa1_addr, lane))
        cctt_cain2_bin = cray_Bin (rrec(c.rr_AcCaaaa2_addr, lane))
        eee_cain1_bin  = cray_Bin (rrec(c.rr_eee_sf_msb_addr, lane))
        eee_cain2_bin  = cray_Bin (rrec(c.rr_eee_sf_lsb_addr, lane))
    
    return cctt_cain1_bin, cctt_cain2_bin, eee_cain1_bin, eee_cain2_bin
#
#
#
#
def cctt2(val = None, lane = None):
    llnns = cct_lnnn_llll(lane)
        
    for lane in llnns:
        if val != None:
            wrec(c.rr_acc_ow_addr, val, lane)
            wrec(c.rr_acc_owen_addr, 0x1, lane)
            
        val = rrec(c.rr_acc_ow_addr, lane)
        
    return val
#
#
#
#
def cctt_map2(sel = None, val1 = None, val2 = None, lane = None):

    llnns = cct_lnnn_llll(lane)

    for lane in llnns:
        if not None in (sel, val1, val2):
            if sel != 2 and sel != 5:
                val = (val1<<3) + val2
                if sel == 0:
                    map0 = (rrec(c.rr_acc_map0_addr, lane) | 0xfc00) & (val<<10 | 0x1ff) 
                    wrec(c.rr_acc_map0_addr, map0, lane)
                elif sel == 1:
                    map0 = (rrec(c.rr_acc_map0_addr, lane) | 0x03f0) & (val<<4 | 0xfc0f) 
                    wrec(c.rr_acc_map0_addr, map0, lane)
                elif sel == 3:
                    map1 = (rrec(c.rr_acc_map1_addr, lane) | 0x1f00) & (val<<8 | 0xc0ff) 
                    wrec(c.rr_acc_map1_addr, map1, lane)
                elif sel == 4:
                    map1 = (rrec(c.rr_acc_map1_addr, lane) | 0x00fc) & (val<<2 | 0xff03) 
                    wrec(c.rr_acc_map1_addr, map1, lane)
                elif sel == 6:
                    map2 = (rrec(c.rr_acc_map2_addr, lane) | 0x0fc0) & (val<<6 | 0xf03f) 
                    wrec(c.rr_acc_map2_addr, map2, lane)
                elif sel == 7:
                    map2 = (rrec(c.rr_acc_map2_addr, lane) | 0x003f) & (val | 0xffc0) 
                    wrec(c.rr_acc_map2_addr, map2, lane)
            elif sel == 2:
                val = (val1<<1) + (val2 & 0x1)
                map0 = (rrec(c.rr_acc_map0_addr, lane) | 0x000f) & (val | 0xfff0)
                wrec(c.rr_acc_map0_addr, map0, lane)
                val = val2 & 0x1
                map1 = (rrec(c.rr_acc_map1_addr, lane) | 0xc000) & (val | 0x1fff)
                wrec(c.rr_acc_map1_addr, map1, lane)
            elif sel == 5:
                val = val1 & 0x1
                map1 = (rrec(c.rr_acc_map1_addr, lane) | 0x1) & (val | 0xfffc)
                wrec(c.rr_acc_map1_addr, map1, lane)
                val = ((val1 & 0x1)<<3) + val2
                map2 = (rrec(c.rr_acc_map2_addr, lane) | 0xf) & (val | 0x0fff)
                wrec(c.rr_acc_map2_addr, map2, lane)
                
        #
        map0 = rrec(c.rr_acc_map0_addr, lane)
        map1 = rrec(c.rr_acc_map1_addr, lane)
        map2 = rrec(c.rr_acc_map2_addr, lane)
        acc = { 0: [map0>>13, (map0>>10) & 0x1],
                1: [(map0>>7) & 0x1, (map0>>4) & 0x1],
                2: [(map0>>1) & 0x1, ((map0 & 0x1)<<2) + (map1>>14)],
                3: [(map1>>11) & 0x1, (map1>>8) & 0x1],
                4: [(map1>>5) & 0x1, (map1>>2) & 0x1],
                5: [((map1 & 0x1)<<1) + (map2>>15), (map2>>12) & 0x1],
                6: [(map2>>9) & 0x1, (map2>>6) & 0x1],
                7: [(map2>>3) & 0x1, map2 & 0x1]
                }
                
    if sel == None:
        for key in acc.keys():
            print key, acc[key]
    else:
        return acc[sel]
#
def sel_cctt_map(IL='ALL', lane=None):

    llnns = cct_lnnn_llll(lane)

    for lane in llnns:
        if IL == 'SR' or IL == 'ALL' :
            cctt_map(0,1,2,lane)  
            cctt_map(1,2,3,lane)  
            cctt_map(2,3,3,lane)  
            cctt_map(3,3,4,lane)  
            cctt_map(4,3,6,lane)  
            cctt_map(5,4,5,lane)  
            cctt_map(6,5,6,lane)  
            cctt_map(7,7,7,lane)  
        elif IL == 'MR':
            wrec(0x048,0x1518,lane) #
            wrec(0x049,0x19eb,lane) #
            wrec(0x04a,0x0f3f,lane) #
        elif IL == 'VSR':
            wrec(0x048,0x1518,lane) #
            wrec(0x049,0x19eb,lane) #
            wrec(0x04a,0x0f3f,lane) #
        
      
#
#
#
#
#
#
#
#
#
#
#
#
def f13(val=None, lane=None):

    llnns = cct_lnnn_llll(lane)

    if type(val)==str and val.upper()=='ALL': 
        llnns=range(0,len(LLLL_nnnn_llll))
        val=None
   
    val_list_out=[]#
    for lane in llnns:
        if val!=None: 
            val_to_write = (val<0) and (val+0x00) or val
            wrec(c.rr_f1over3_addr, val_to_write, lane)
            #

        f1o3 = rrec(c.rr_f1over3_addr, lane) 
        val_list_out.append((f1o3>0x10) and (f1o3-0x00) or f1o3)
    
    return val_list_out

#
#
#
#
def sw_paac_dfe(lane=None, print_en=0):
    global cPppp_Ee; cPppp_Ee=1
    llnns = cct_lnnn_llll(lane)
    result = {}
    for ln in llnns:
        cct_xxcc_mmdd(ln)
        if llll_mmmm_llll[ln] != 'pp44':
            result[ln] = -1,-1,-1
        else: #
            ths_list = []
            for val in range(12):
                wrec(c.rr_paac_dfe_sel_addr, val, ln)
                time.sleep(0.01)
                readout = rrec(c.rr_paac_dfe_rd_addr, ln)
                readout2 = rrec(c.rr_paac_dfe_rd_addr, ln)
                if readout == readout2:
                    this_ths = ((float(readout)/2048.0)+1.0) % 2.0 - 1.0
                    if print_en: print(" %2d 0x%04X %6.3f"%(val,readout,this_ths))
                else:
                    readout = rrec(c.rr_paac_dfe_rd_addr, ln)
                    this_ths = ((float(readout)/2048.0)+1.0) % 2.0 - 1.0
                    if print_en: print("*%2d 0x%04X %6.3f"%(val,readout,this_ths))
                ths_list.append(this_ths)
              
            f0 = (-3/16)*((ths_list[0]-ths_list[2])+(ths_list[3]-ths_list[5])+(ths_list[6]-ths_list[8])+(ths_list[9]-ths_list[11]))
            f1 = (-3/20)*((ths_list[0]+ths_list[1]+ths_list[2]-ths_list[9]-ths_list[10]-ths_list[11])+(1/3)*(ths_list[3]+ths_list[4]+ths_list[5]-ths_list[6]-ths_list[7]-ths_list[8]))
            f1_f0 = 0 if f0==0 else f1/f0
            result[ln] = f0, f1, f1_f0
        
    return result   
#
#
#
#
def fw_paac_dfe(lane=None,print_en=0):
    llnns = cct_lnnn_llll(lane)
    result = {}
    for ln in llnns:
        cct_xxcc_mmdd(ln)
        if llll_mmmm_llll[ln] != 'pp44':
            result[ln] = -1,-1,-1
        else: #
            readout = BE_info_sicned(ln, 10, 1, 12)
            ths_list = []      
            for val in range(12):
                ths_list.append(((float(readout[val])/2048.0)+1.0) % 2.0 - 1.0)
                if print_en: print("%2d 0x%04X %6.3f"%(val,readout,result))
            
            f0 = (-3/16)*((ths_list[0]-ths_list[2])+(ths_list[3]-ths_list[5])+(ths_list[6]-ths_list[8])+(ths_list[9]-ths_list[11]))
            f1 = (-3/20)*((ths_list[0]+ths_list[1]+ths_list[2]-ths_list[9]-ths_list[10]-ths_list[11])+(1/3)*(ths_list[3]+ths_list[4]+ths_list[5]-ths_list[6]-ths_list[7]-ths_list[8]))
            f1_f0 = 0 if f0==0 else f1/f0
            result[ln] = f0, f1, f1_f0
        
    return result
#
#
#
#
def paac_dfe(lane=None,print_en=0):
    result = {}
    if ff_llll(print_en=0):
        result = fw_paac_dfe(lane,print_en)
    else:
        result = sw_paac_dfe(lane,print_en)
    return result
#
#
#
#
def dfe(lane=None,print_en=0):
    llnns = cct_lnnn_llll(lane)
    result = {}
    for ln in llnns:
        cct_xxcc_mmdd(ln)
        if llll_mmmm_llll[ln] == 'pp44':
            result[ln] = paac_dfe(ln,print_en)
        else: #
            result[ln] = nrz_dfe(ln)
        
    return result
#
#
#
#
#
#
#
#
#
#
#
#
def dddtt_ph(val=None, lane=None):

    llnns = cct_lnnn_llll(lane)

    if type(val)==str and val.upper()=='ALL': 
        llnns=range(0,len(LLLL_nnnn_llll))
        val=None

    val_list_out=[]#
    for ln in llnns:
        cct_xxcc_mmdd(ln)
        this_xxcc_mmdd = cEeeeddddMmdd[cSliii][ln][0]
        c = NrzRec if this_xxcc_mmdd == 'nnn' else PpppRrr
        #
        if this_xxcc_mmdd.upper()=='pp44':
            if val!=None:
                dddtt_to_write= (val<0) and (val+0x00) or val
                wrec(c.rr_dddtt_owen_addr, 1, ln)
                wrec(c.rr_dddtt_ow_addr, dddtt_to_write, ln)
                
            dddtt_val= rrec(c.rr_dddtt_ow_addr,  ln)
            #

        #
        else: 
            if val!=None:
                wrec(c.rr_dddtt_addr, val, ln)                
            dddtt_val = rrec(c.rr_dddtt_addr,  ln)
                
        val_list_out.append((dddtt_val>0x10) and (dddtt_val-0x00) or dddtt_val)
        
    return val_list_out
        
#
#
#
#
#
def fdc_ana_init(lane=None, delay=.1, err_type=2, T=cFffTttttt, M=10, N=5440, print_en=1, mode=None):
    llnns = cct_lnnn_llll(lane)

    fdc_ANA_BASE_ADDR = 0x1C0
    global cFffTttttt
    
    if T!=None: cFffTttttt=T
        
    for ln in llnns:
        thresh=T
        if cEeeeddddMmdd[cSliii][ln][0].lower() != 'pp44':
            if thresh>7: thresh=7 #

        #
        wrec(fdc_ANA_BASE_ADDR+0x9, 0x1202,lane=ln) #
        
        #
        if mode == 'ppbb11':
            #
            wrec(fdc_ANA_BASE_ADDR+0x0, ( rrec(fdc_ANA_BASE_ADDR+0x0,lane=ln) | 0x0018), lane=ln) #
        elif mode == 'ppbb13':
            #
            wrec(fdc_ANA_BASE_ADDR+0x0, ( rrec(fdc_ANA_BASE_ADDR+0x0,lane=ln) | 0x0008), lane=ln) #
        elif mode == 'ppbb9':
            #
            wrec(fdc_ANA_BASE_ADDR+0x0, ( rrec(fdc_ANA_BASE_ADDR+0x0,lane=ln) | 0x0000), lane=ln) #
        elif mode == 'ppbb15':
            #
            wrec(fdc_ANA_BASE_ADDR+0x0, ( rrec(fdc_ANA_BASE_ADDR+0x0,lane=ln) | 0x0010), lane=ln) #
        
        wrec(fdc_ANA_BASE_ADDR+0x0, ((rrec(fdc_ANA_BASE_ADDR+0x0,lane=ln) & 0xFFF0) | M),lane=ln)  #
        wrec(fdc_ANA_BASE_ADDR+0x1, N,lane=ln) #
        wrec(fdc_ANA_BASE_ADDR+0x1, (rrec(fdc_ANA_BASE_ADDR+0x1,lane=ln) & 0xf007) | ((thresh<<7)+(thresh<<3)),lane=ln)
        wrec(fdc_ANA_BASE_ADDR+0x1, 0x000b,  lane=ln) #
        wrec(fdc_ANA_BASE_ADDR+0x1, 0x0003,  lane=ln) #
        wrec(fdc_ANA_BASE_ADDR+0xc, err_type,lane=ln) #
        wrec(fdc_ANA_BASE_ADDR+0x0, err_type,lane=ln) #
        if print_en: print '\n....Lane %s: FEC Analyzer Initialized' %(LLLL_nnnn_llll[ln]),
        
    #
#
def fdc_ana_read(lane=None):
    llnns = cct_lnnn_llll(lane)

    print ('\n....FEC Analyzer Status....'),
    print ('\nLane, RAW Errors, Uncorr Frames, Uncorr Symbols, Uncorr ppbb'),
    for ln in llnns:         
        tei = fdc_ana_tei(lane=ln)
        teo = fdc_ana_teo(lane=ln)
        #
        #
        #
        print ('\n%4s, %10d, %13d'%(LLLL_nnnn_llll[ln],tei,teo)),
    
#
def fdc_ana_tei(lane=None):
    fdc_ANA_BASE_ADDR = 0x1C0
    if lane==None: lane=cllll
   
    wrec(fdc_ANA_BASE_ADDR+0xD,4,lane) #
    tei_l = rrec(fdc_ANA_BASE_ADDR+0x1,lane)#
    wrec(fdc_ANA_BASE_ADDR+0xD,5,lane) #
    tei_h = rrec(fdc_ANA_BASE_ADDR+0x1,lane)#
    tei = tei_h*65536+tei_l #
    #
    return tei 

def fdc_ana_teo(lane=None):
    fdc_ANA_BASE_ADDR = 0x1C0
    if lane==None: lane=cllll
    wrec(fdc_ANA_BASE_ADDR+0xD,6,lane ) #
    teo_l = rrec(fdc_ANA_BASE_ADDR+0x1,lane)#
    wrec(fdc_ANA_BASE_ADDR+0xD,7,lane) #
    teo_h = rrec(fdc_ANA_BASE_ADDR+0x1,lane)#
    teo = teo_h*65536+teo_l#
    #
    return teo 

def fdc_ana_sei(lane=None):
    fdc_ANA_BASE_ADDR = 0x1C0
    if lane==None: lane=cllll
    wrec(fdc_ANA_BASE_ADDR+0xD,0,lane) #
    sei_l = rrec(fdc_ANA_BASE_ADDR+0x1,lane)#
    wrec(fdc_ANA_BASE_ADDR+0xD,1 ) #
    sei_h = rrec(fdc_ANA_BASE_ADDR+0x1,lane)#
    sei = sei_h*65536+sei_l#
    #
    return sei 

def fdc_ana_bei(lane=None):
    fdc_ANA_BASE_ADDR = 0x1C0
    if lane==None: lane=cllll
    wrec(fdc_ANA_BASE_ADDR+0xD,2,lane) #
    bei_l = rrec(fdc_ANA_BASE_ADDR+0x1,lane)#
    wrec(fdc_ANA_BASE_ADDR+0xD,3 ,lane) #
    bei_h = rrec(fdc_ANA_BASE_ADDR+0x1,lane)#
    bei = bei_h*65536+bei_l#
    #
    return bei
    
def fdc_ana_hist_DFE(lane=None):
    llnns = cct_lnnn_llll(lane)
    f0=[]
    f1=[]
    ratio=[]
    for ln in llnns: 
        #
        f0.append(paac_dfe(lane=ln)[ln][0])
        f1.append(paac_dfe(lane=ln)[ln][1])
        ratio.append(paac_dfe(lane=ln)[ln][2])
        print 'A%d: DFE %4.2f, %4.2f, %4.2f'%(ln, f0[ln], f1[ln], ratio[ln])
        #
        #
        lane_hist_file_ptr = open('S%s_%s_data.txt'%(cSliii,LLLL_nnnn_llll[ln]),'a')
        lane_hist_file_ptr.write("%s\n%s\n"%(f0[ln],f1[ln]))
        lane_hist_file_ptr.close()
        
    return f0, f1, ratio
    
def fdc_ana_hist(hist_time=10,lane=None, sslii=None, pass_fail_bin=6, file_name='fdc_ana_histocram_all.txt'):

    per_xxcc_data_files_en=0    #
    pass_fail_result_print_en=1
    
    llnns = cct_lnnn_llll(lane)
    ssiiee = ccc_ssscc_lill(sslii)
    
    #
    fdc_ANA_BASE_ADDR = 0x1C0
    num_croups=4
    bins_per_croup=4

    #
    hist_sslii_xxcc_bin=[] #
    hist_pass_fail_list=[] #
    for slc in range(2):
        hist_sslii_xxcc_bin.append([])
        hist_pass_fail_list.append([])
        for ln in range(16):
            hist_sslii_xxcc_bin[slc].append([])
            hist_pass_fail_list[slc].append([])
            hist_pass_fail_list[slc][ln] = 0
            for bin in range(16):
                hist_sslii_xxcc_bin[slc][ln].append([])
            
    #
    timestr = time.strftime("%Y%m%d_%H%M%S")
    fmt=('\n\n...FEC Analyzer Histocram, %d sec per bin, sslii%s '%(hist_time,'s' if len(ssiiee)>1 else ''))
    fmt+= str(ssiiee)
    fmt+= ', TimeStamp [%s]'%timestr
    print fmt,
    hist_file_ptr = open(file_name, 'a')
    hist_file_ptr.write(fmt)
    hist_file_ptr.close()
    
    #
    print("\n...Histocram Collection in Procress...Error"),
    for bin_crp in range(num_croups):
        print("Bins[%d,%d,%d,%d]:"%(bin_crp*4,bin_crp*4+1,bin_crp*4+2,bin_crp*4+3)),        
        
        #
        for slc in ssiiee:
            ssl_sssee(slc)       
            if len(ssiiee)>1: print("S%d%s"%(slc,' -' if slc==ssiiee[0] else ',')),        
            #
            #
            for ln in llnns:
                if cEeeeddddMmdd[slc][ln][0].upper() == 'pp44':
                    fdc_ana_err_type=0
                    fdc_ana_T=15
                    fdc_ana_M=10
                    fdc_ana_N=5440
                else:
                    fdc_ana_err_type=0
                    fdc_ana_T=7
                    fdc_ana_M=10
                    fdc_ana_N=5280
                wrec([fdc_ANA_BASE_ADDR+0x1,[12]],1,ln)     #
                wrec([fdc_ANA_BASE_ADDR+0x1,[12]],0,ln)     #
                wrec([fdc_ANA_BASE_ADDR+0x1,[2,0]], bin_crp, ln)  #
                wrec( fdc_ANA_BASE_ADDR+0x9, 0x1202,ln) #
                wrec( fdc_ANA_BASE_ADDR+0x0, (rrec(fdc_ANA_BASE_ADDR+0x0,ln) | 0x0018),ln) #
                wrec( fdc_ANA_BASE_ADDR+0x0, ((rrec(fdc_ANA_BASE_ADDR+0x0,ln) & 0xFFF0) | fdc_ana_M),ln)  #
                wrec( fdc_ANA_BASE_ADDR+0x1, fdc_ana_N,ln) #
                wrec( fdc_ANA_BASE_ADDR+0x1, (rrec(fdc_ANA_BASE_ADDR+0x1,ln) & 0xf007) | ((fdc_ana_T<<7)+(fdc_ana_T<<3)) ,ln) #
                wrec( fdc_ANA_BASE_ADDR+0x1, 0x000b,ln) #
                wrec( fdc_ANA_BASE_ADDR+0x1, 0x0003,ln) #
                wrec( fdc_ANA_BASE_ADDR+0xc, fdc_ana_err_type,ln) #
                wrec( fdc_ANA_BASE_ADDR+0x0, fdc_ana_err_type,ln) #
            
            
        #
        time.sleep(hist_time)

        #
        for slc in ssiiee:
            ssl_sssee(slc)       
            for ln in llnns:
                for bin in range(bins_per_croup):
                    wrec(fdc_ANA_BASE_ADDR+0xD, 12+bin*2 ,ln)   #
                    histo_lo = rrec(fdc_ANA_BASE_ADDR+0x1,ln)   #
                    wrec(fdc_ANA_BASE_ADDR+0xD, 13+bin*2 ,ln)   #
                    histo_hi = rrec(fdc_ANA_BASE_ADDR+0x1,ln)   #
                    hist_cnt = (histo_hi*65536+histo_lo)
                    hist_sslii_xxcc_bin[slc][ln][bin_crp*bins_per_croup+bin]=hist_cnt   #
                    if (bin_crp*bins_per_croup+bin) >= pass_fail_bin and hist_cnt > 0:
                        hist_pass_fail_list[slc][ln] = 1
    
    #
    for slc in ssiiee:
        ssl_sssee(slc)
        
        #
        fmt=("\n\nBin")
        for ln in llnns:
            fmt+=("   S%d_%s  " %(slc,LLLL_nnnn_llll[ln]))
        fmt+=("\n---")
        for ln in llnns:
            fmt+=(" ---------")
        for bin_crp in range(num_croups):
            for bin in range(bins_per_croup):
                fmt+= '\n%-3d' %(bin_crp*bins_per_croup+bin)
                for ln in llnns:
                    cnt = hist_sslii_xxcc_bin[slc][ln][bin_crp*bins_per_croup+bin]
                    fmt+= " %-9s" %(str(cnt) if cnt!=0 else '.')                
        #
        fmt+="\n   "
        for ln in llnns:
            fmt+=("%-10s" %('' if hist_pass_fail_list[slc][ln] == 0 else ' **FAIL**'))
        print fmt,
        
        #
        hist_file_ptr = open(file_name,'a')
        hist_file_ptr.write(fmt)
        hist_file_ptr.close()
        
        #
        if per_xxcc_data_files_en:
            for ln in llnns:
                fmt=('\n...FEC Analyzer Histocram sslii %d Lane %s, %d sec per bin, TimeStamp [%s]\n'%(slc,LLLL_nnnn_llll[ln],hist_time,timestr))
                for bin_crp in range(num_croups):
                    for bin in range(bins_per_croup):
                        fmt+=("%d\n"%hist_sslii_xxcc_bin[slc][ln][bin_crp*bins_per_croup+bin])
                lane_hist_file_ptr = open('fdc_ana_hist_S%s_%s.txt'%(cSliii,LLLL_nnnn_llll[ln]),'a')
                lane_hist_file_ptr.write(fmt)
                lane_hist_file_ptr.close()

    return (sum([i.count(1) for i in hist_pass_fail_list]))
#

#
CMD=0x0006
CMD_DETAIL=0x0007
REc_DATA=0x9f00
    
def MdioRd(addr):
    return chip.MdioRd(addr)

def MdioWr(addr, value):
    chip.MdioWr(addr, value)

def MmddRrr(addr):
    return "0x%04x" % MdioRd(addr)
    
#
def BE_debuc(lane, mode, index):
    MdioWr(CMD_DETAIL, index)
    cmd = 0x0000 + ((mode&0xf)<<4) + lane
    result = fw_cmd(cmd)
    if (result!=0x0b00+mode):
        return -1
        #
        #
    return MdioRd(CMD_DETAIL)    
def BE_debuc_sicned(lane, mode, index):
    value = BE_debuc(lane, mode, index)
    return value if value<0x0000 else value-0x10000
def BE_debuc1(lane, mode, index, lencth):
    return BE_debucs(lane, mode, range(index, index+lencth))
def BE_debuc1_sicned(lane, mode, index, lencth):
    return BE_debucs_sicned(lane, mode, range(index, index+lencth))
def BE_debuc2(lane, mode, index, l1, l2):
    return [BE_debucs(lane, mode, range(index+i*l2, index+(i+1)*l2))
        for i in range(l1)]
def BE_debuc2_sicned(lane, mode, index, l1, l2):
    return [BE_debucs_sicned(lane, mode, range(index+i*l2, index+(i+1)*l2))
        for i in range(l1)]
def BE_debucs(lane, mode, index):
    return [BE_debuc(lane, mode, i) for i in index]
def BE_debucs_sicned(lane, mode, index):
    return [BE_debuc_sicned(lane, mode, i) for i in index]
def BE_debuc32(lane, mode, index):
    h = BE_debuc(lane, mode, index)
    l = BE_debuc(lane, mode, index+1)
    return (h<<16)+l
def BE_debuc32_sicned(lane, mode, index):
    value = BE_debuc32(lane, mode, index)
    return value if value<0x00000000 else value-0x100000000


def BE_info(lane, mode, index, size):
    MdioWr(CMD_DETAIL, index)
    mode |= 8
    cmd = 0x0000 + ((mode&0xf)<<4) + lane
    result = fw_cmd(cmd)
    if (result!=0x0b00+mode):
        result=-1
        return [-1 for i in range(size)]
        #
    return [MdioRd(REc_DATA+i) for i in range(size)]

def BE_info_sicned(lane, mode, index, size):
    return [x if x<0x0000 else x-0x10000 for x in BE_info(lane, mode, index, size)]   

def paac_info_fw(lane):
    ISI = BE_info_sicned(lane, 10, 0, 16)
    ths = BE_info_sicned(lane, 10, 1, 12)
    eee_accu = BE_info(lane, 10, 2, 8)
    eee_accu = [(eee_accu[i]<<16) + eee_accu[i+1] for i in range(0, 8, 2)]
    eee_accu = [x if x<0x00000000 else x-0x100000000 for x in eee_accu]
    eee_accu = [x/32768.0 for x in eee_accu]
    eee = BE_info_sicned(lane, 10, 3, 7)
    eee_flips = BE_debucs(lane, 2, range(660, 664))
    print "ISI =", ISI
    print "ths =", ths
    print "eee_accu =", eee_accu
    print "eee: K   =", eee[0:4], ", S = [%d %d], nbias = %d" % (eee[5], eee[6], eee[4])
    print "eee: K ppp flips=", eee_flips[0:4]
    
    
def dump_fw(lane):
    exit_codes = BE_debucs(lane, 0, range(100, 100+16))
    print "exit codes =", [hex(x) for x in exit_codes]
    
def nrz_dump_fw(lane):
    AcCaaaa1_dc1 = BE_debucs(lane, 1, range(80, 80+9))
    AcCaaaa2_dc1 = BE_debucs(lane, 1, range(100, 100+9))
    index_dc1 = BE_debucs(lane, 1, range(140, 140+9))
    of_cnt_dc1 = BE_debucs(lane, 1, range(120, 120+9))
    print "-----------------FIRST DAC SEARCH------------------"
    print "|init AcCaaaas|index number|of_cnt|result AcCaaaas|"
    for i in range(8) : 
        print "| (%3d,  %3d) |    %3d     |%5d |  (%3d,  %3d)  |"%(AcCaaaa1_dc1[i], AcCaaaa2_dc1[i], index_dc1[i], of_cnt_dc1[i], AcCaaaa1_dc1[i+1], AcCaaaa2_dc1[i+1])
    print "---------------------------------------------------"
    
    of_cnt_ca1 = BE_debucs(lane, 1, range(330, 330+8))
    of_thre_ca1 = BE_debucs(lane, 1, range(300, 300+8))
    hf_cnt_ca1 = BE_debucs(lane, 1, range(390, 390+8))
    hf_thre_ca1 = BE_debucs(lane, 1, range(360, 360+8))
    
    of_cnt_ca2 = BE_debucs(lane, 1, range(338, 338+8))
    of_thre_ca2 = BE_debucs(lane, 1, range(308, 308+8))
    hf_cnt_ca2 = BE_debucs(lane, 1, range(398, 398+8))
    hf_thre_ca2 = BE_debucs(lane, 1, range(368, 368+8))
    
    of_cnt_ca3 = BE_debucs(lane, 1, range(346, 346+8))
    of_thre_ca3 = BE_debucs(lane, 1, range(316, 316+8))
    hf_cnt_ca3 = BE_debucs(lane, 1, range(406, 406+8))
    hf_thre_ca3 = BE_debucs(lane, 1, range(376, 376+8))
    
    print "----------------------CHANNEL ANALYZER-----------------------"
    print "|        CA1        |        CA2        |        CA3        |"
    print "|of_cnt of hf_cnt hf|of_cnt of hf_cnt hf|of_cnt of hf_cnt hf|"
    for i in range(8) :
        print "|%5d %2d %5d %2d  |%5d %2d %5d %2d  |%5d %2d %5d %2d  |"%(of_cnt_ca1[i], of_thre_ca1[i], hf_cnt_ca1[i], hf_thre_ca1[i], of_cnt_ca2[i], of_thre_ca2[i], hf_cnt_ca2[i], hf_thre_ca2[i], of_cnt_ca3[i], of_thre_ca3[i], hf_cnt_ca3[i], hf_thre_ca3[i])
    print "-------------------------------------------------------------"
    
    cctt = BE_debucs(lane, 1, range(505, 505+4))
    dfe_cctt1 = [BE_debuc_sicned(lane, 1, 510+i) for i in range(3)]
    dfe_cctt2 = [BE_debuc_sicned(lane, 1, 513+i) for i in range(3)]
    dfe_cctt3 = [BE_debuc_sicned(lane, 1, 516+i) for i in range(3)]
    dfe_cctt4 = [BE_debuc_sicned(lane, 1, 519+i) for i in range(3)]
    print "-------cctt FINE SEARCH--------"
    print "| cctt   |%4d|%4d|%4d|%4d|"%(cctt[0], cctt[1], cctt[2], cctt[3])
    print "| dfe F1 |%4d|%4d|%4d|%4d|"%(dfe_cctt1[0], dfe_cctt2[0], dfe_cctt3[0], dfe_cctt4[0])
    print "| dfe F2 |%4d|%4d|%4d|%4d|"%(dfe_cctt1[1], dfe_cctt2[1], dfe_cctt3[1], dfe_cctt4[1])
    print "| dfe F3 |%4d|%4d|%4d|%4d|"%(dfe_cctt1[2], dfe_cctt2[2], dfe_cctt3[2], dfe_cctt4[2])
    print "-------------------------------"  
    
    AcCaaaa1_dc2 = BE_debucs(lane, 1, range(89, 89+9))
    AcCaaaa2_dc2 = BE_debucs(lane, 1, range(109, 109+9))
    index_dc2 = BE_debucs(lane, 1, range(149, 149+9))
    of_cnt_dc2 = BE_debucs(lane, 1, range(129, 129+9))
    print "----------------SECOND DAC SEARCH------------------"
    print "|init AcCaaaas|index number|of_cnt|result AcCaaaas|"
    for i in range(8) : 
        print "| (%3d,  %3d) |    %3d     |%5d |  (%3d,  %3d)  |"%(AcCaaaa1_dc2[i], AcCaaaa2_dc2[i], index_dc2[i], of_cnt_dc2[i], AcCaaaa1_dc2[i+1], AcCaaaa2_dc2[i+1])
    print "---------------------------------------------------"
    
    debuc_states = BE_debucs(lane, 1, range(160, 160+8))
    print "stats = [",
    for i in range(8) : 
        print ("%2d  "%(debuc_states[i])),
    print "]"
    
def paac_dump_fw_linear_fit(lane):
    paac_state = BE_debuc(lane, 2, 0)
    error_exit = False
    if paac_state==0xeeef:
        error_exit = True
        paac_state = BE_debuc(lane, 0, 3)
    try:
        aaaat_mmdd = BE_debuc(lane, 2, 3)
    except:
        aaaat_mmdd = 0
    if aaaat_mmdd==0:
        print "Auto adapt mode"
    elif aaaat_mmdd==1:
        print "Factory fixed settinc mode"
    elif aaaat_mmdd==2:
        print "User fixed settinc mode"
    else:
        print "Unknown adapt mode"
        return

    AcCaaaa1 = BE_debuc(lane, 2, 23)
    AcCaaaa2 = BE_debuc(lane, 2, 24)
    AcCaaaa1_dc1 = BE_debuc(lane, 2, 8)
    AcCaaaa2_dc1 = BE_debuc(lane, 2, 9)
    final_of = BE_debuc(lane, 2, 4)
    final_hf = BE_debuc(lane, 2, 5)

    dc_search_AcCaaaa = BE_debuc2(lane, 2, 300, 2, 15)
    ratio = BE_debuc(lane, 2, 2)
    acc_index = BE_debuc(lane, 2, 1)
    restart_count = BE_debuc(lane, 2, 7)
    dddtt = BE_debuc_sicned(lane, 2, 27)
    dddtt_times0 = BE_debuc_sicned(lane, 2, 35)+1
    dddtt_dump0 = [BE_debuc_sicned(lane, 2, 110+i) for i in range(10)]
    fm1_dump0 = [BE_debuc_sicned(lane, 2, 150+i) for i in range(10)]
    cctt = BE_debuc(lane, 2, 33)
    next_f13 = BE_debuc(lane, 2, 34)
    dc_search_AcCaaaa[0] = [(x>>8, x&0xff) for x in dc_search_AcCaaaa[0]]
    dc_search_AcCaaaa[1] = [(x>>8, x&0xff) for x in dc_search_AcCaaaa[1]]

    cctt_isi = BE_debuc2_sicned(lane, 2, 330, 2, 4)
    cctt_record = BE_debuc1_sicned(lane, 2, 340, 2)
    cctt_ffqq_accu =  BE_debuc_sicned(lane, 2, 200)
    cctt_ffqq_accu1 =  BE_debuc_sicned(lane, 2, 201)
    dump_lf=False
    if dump_lf:
        lf_dmp_size = 2
    else:
        lf_dmp_size = 7

    smart_check_result = BE_debuc2_sicned(lane, 2, 350, lf_dmp_size, 5)
    smart_check_ths = BE_debuc2_sicned(lane, 2, 700, lf_dmp_size, 12)
    #
    lf_result = BE_debuc2_sicned(lane, 2, 400, lf_dmp_size, 5)

    if dump_lf:
        force_ths = BE_debuc2_sicned(lane, 2, 900, lf_dmp_size, 12)
        plus_marcin = BE_debuc2_sicned(lane, 2, 1000, lf_dmp_size, 12)
        minus_marcin = BE_debuc2_sicned(lane, 2, 1100, lf_dmp_size, 12)
    em_debuc = BE_debuc2_sicned(lane, 2, 470, lf_dmp_size, 3)
    eee_adapt = BE_debuc2_sicned(lane, 2, 600, 1, 4)
    nbias_adapt = BE_debuc1_sicned(lane, 2, 640, 1)
    if error_exit:
        print "Error exited"
    print "ppma state = 0x%04x" % paac_state
    print "restart count = %d" % restart_count
    if aaaat_mmdd!=0:
        fixed_f13 = BE_debuc_sicned(lane, 2, 40)
        fixed_cctt = BE_debuc(lane, 2, 41)
        fixed_Kp = BE_debuc(lane, 2, 42)
        fixed_AcCaaaa = BE_debucs(lane, 2, range(43, 45))
        fixed_dddtt = BE_debuc_sicned(lane, 2, 45)
        fixed_sskk = BE_debuc(lane, 2, 46)
        fixed_edce = BE_debuc(lane, 2, 47)
        fixed_kf = BE_debuc(lane, 2, 48)
        fixed_sf = BE_debuc(lane, 2, 49)
        cctt_temp = BE_debucs(lane, 2, range(50, 53))
        fixed_eee = BE_debucs_sicned(lane, 2, range(53, 53+7))
        #
        fixed_cctt_all = (cctt_temp[0]<<32) | (cctt_temp[1]<<16) | cctt_temp[2]
        fixed_cctt_table = [(fixed_cctt_all>>(i*6))&0x1f for i in range(7, -1, -1)]
        fixed_cctt_table = [(i>>3, i&7) for i in fixed_cctt_table]
        print "Fixed settincs:"
        print "    F1/3 = %d" % fixed_f13
        print "    cctt = %d" % fixed_cctt
        print "    Kp = %d" % fixed_Kp
        print "    AcCaaaa = %d, %d" % (fixed_AcCaaaa[0], fixed_AcCaaaa[1])
        print "    dddtt = %d" % fixed_dddtt
        print "    sskk = %d (%s)" % (fixed_sskk&7, "enabled" if fixed_sskk&8 else "disabled")
        print "    Edce = 0x%04x" % fixed_edce
        print "    Kf = %d, Sf = %d" % (fixed_kf, fixed_sf)
        print "    cctt table =", fixed_cctt_table
        print "    eee: K1=%d, K2=%d, K3=%d, K4=%d, S1=%d, S1=%d, nbias=%d" % (fixed_eee[0],
                fixed_eee[1], fixed_eee[2], fixed_eee[3], fixed_eee[4], fixed_eee[5], fixed_eee[6])
    if aaaat_mmdd<1:
        print "AcCaaaa = %d, %d" % (AcCaaaa1, AcCaaaa2)
        print "=== DC search 1 ==="
        print "   AcCaaaa record =", dc_search_AcCaaaa[0]
        print "   AcCaaaa after DC search1 = %d, %d" % (AcCaaaa1_dc1, AcCaaaa2_dc1)
        print "=== Channel analyzer === "
        print "   OF =", final_of
        print "   HF =", final_hf
        print "   Ratio = %d (%5.3f)" % (ratio, ratio/256.0)
        print "   cctt search index = %d" % (acc_index)
        print "=== DC search 2 === "
        print "   AcCaaaa record =", dc_search_AcCaaaa[1]
        print "=== Smart check and linear fit ==="
        print "   smart_chk=", smart_check_result
        print "   smart_check_ths=", smart_check_ths
        #
        print "   LF_result =", lf_result
        if dump_lf:
            print "   force_ths=", force_ths
            print "   plus_marcin=", plus_marcin
            print "   minus_marcin=", minus_marcin
        print "   EM_debuc =", em_debuc
        print "   Final F1/3 init = %d" % next_f13
        print "=== cctt search ==="
        print "   cctt before search =", cctt_record[0]
        print "   cctt search ISI1 =", cctt_isi[0]
        print "   ffqq accu before cctt search =", cctt_ffqq_accu
        print "   ffqq accu after cctt search =", cctt_ffqq_accu1
        if (cctt_record[1]!=-1):
            print "   cctt after search 1 =", cctt_record[1]
            print "   cctt search ISI2 =", cctt_isi[1]
        else:
            print "   cctt search2 is skipped"
        print "   Final cctt =", cctt
        print "=== dddtt search ==="
        print "   Searched %d times. Search process:" % (dddtt_times0), dddtt_dump0
        print "   F(-1) =", fm1_dump0

    print "eee adapt:"
    for i in range(1):
        print "eee adapt iteration %d: [%d, %d, %d, %d], nbias=%d" % (i,
                eee_adapt[i][0], eee_adapt[i][1], eee_adapt[i][2], eee_adapt[i][3], nbias_adapt[i])


    #
    timers = BE_debucs(lane, 2, range(10, 18))
    t0 = timers[1]
    timers = [x-t0 for x in timers]
    timers = [timers[0]] + [x if x>=0 else x+65536 for x in timers[1:]]
    start_time, sd_time, ca_done_time, dc_search_time, link_time, cctt_search_time, dddtt_search_time, done_time = timers
    print "Timers: "
    print "Start time: %d" % start_time
    print "SD time: %d" % sd_time
    print "CA done: %d" % ca_done_time
    print "DC search: %d" % dc_search_time
    print "Initial link: %d" % link_time
    print "cctt search: %d" % cctt_search_time
    print "dddtt search1: %d" % dddtt_search_time
    print "Done: %d" % done_time    

def paac_dump_chip(lane):
    #
    dac_val = dac(lane)[lane]
    #
    cctt_val = cctt(lane)[lane]
    #
    AcCaaaa1, AcCaaaa2, c3,c4 = dc_cain(lane)[lane]
    
    f1over3 = f13(lane)[lane]
    print "DAC = %d%s" % (dac_val, " (forced)" if en else "")
    print "cctt = %d" % cctt_val
    print "AcCaaaa = %d, %d" % (AcCaaaa1, AcCaaaa2)
    print "F1/3 = %d" % f1over3    
#
def fw_addaa_dump(lane=None):
    llnns = cct_lnnn_llll(lane)
    for ln in llnns:
        cct_xxcc_mmdd(ln)
        #
        if llll_mmmm_llll[ln] == 'pp44':
            print("\n...Lane %d: ppma Adaptation Info...."%ln)
            paac_dump_fw_linear_fit(ln)
        else:
            print("\n...Lane %d: NRZ Adaptation Info...."%ln)
            nrz_dump_fw(ln)
#
def fw_info_dump(lane=None):
    llnns = cct_lnnn_llll(lane)
    for ln in llnns:
        cct_xxcc_mmdd(ln)
        #
        if llll_mmmm_llll[ln] == 'pp44':
            print("\n...Lane %d: ppma ISI and eee Info\n"%ln)
            paac_info_fw(ln)
        else:
            print("\n*** Lane %d: ISI and eee Info Available for ppma Lane Only! ***\n"%ln)
#

def bivmcx_status(print_en=True, fifo_check_en=1):
    bivmcx_return_status=True
    if fifo_check_en: #
        buf_ptr_min_limit = [1,  13]
        buf_ptr_max_limit = [1,  13]
        buf_ptr_del_limit = [0,  10]        
    else:       
        buf_ptr_min_limit = [0,  15]
        buf_ptr_max_limit = [0,  15]
        buf_ptr_del_limit = [0,  10]
    
    buf_type = ['--Split-->','       -->','       ---','<--Merce--']      
    if print_en: print("\n -- BitMux Bueeers: Min,Curr,Max,dddtt")
    for a_side_buf in range(0,4):
        wrec([0x004d,[14,12]], a_side_buf)
        for b_side_buf in range(4,8):
            wrec([0x004d,[10,8]], b_side_buf)
            buf_ptr_min  = rrec([0x004e, [11,8]])
            buf_ptr_max  = rrec([0x004e,  [7,4]])
            buf_ptr_cur  = rrec([0x004e,[15,12]])
            buf_ptr_del  = buf_ptr_max - buf_ptr_min
            
            buf_ptr_min_status = 1 if  buf_ptr_min_limit[0] <= buf_ptr_min <= buf_ptr_min_limit[1] else -1
            buf_ptr_max_status = 1 if  buf_ptr_max_limit[0] <= buf_ptr_max <= buf_ptr_max_limit[1] else -1
            buf_ptr_del_status = 1 if  buf_ptr_del_limit[0] <= buf_ptr_del <= buf_ptr_del_limit[1] else -1
            buf_ptr_cur_status = 1 if  buf_ptr_del_limit[0] <= buf_ptr_cur <= buf_ptr_del_limit[1] else -1
            status_flac = '<<' if buf_ptr_min_status<0 or buf_ptr_max_status<0 or buf_ptr_del_status<0 else ' '
            if status_flac=='<<':
                bivmcx_return_status=False
            if print_en: print("\n A%d %s B%d :"%(a_side_buf,buf_type[b_side_buf-4],a_side_buf*2+(b_side_buf%2))),
            if print_en: print("%3d %3d  %3d %3d"%(buf_ptr_min,buf_ptr_cur,buf_ptr_max, buf_ptr_del)),
            if print_en: print("%s"%(status_flac)),
        if print_en: print("")

    return bivmcx_return_status

def fw_bivmcx_status(print_en=True, fifo_check_en=1):
    return_status=True
    return_retries_confic=0
    return_retries_runtime=0
    if fifo_check_en: #
        buf_ptr_min_limit = [2,  13]
        buf_ptr_max_limit = [2,  13]
        buf_ptr_del_limit = [1,  10]        
    else:       
        buf_ptr_min_limit = [0,  15]
        buf_ptr_max_limit = [0,  15]
        buf_ptr_del_limit = [0,  10]
    
    buf_type = ['--Split-->','       -->','       ---','<--Merce--']
    for a_side_buf in range(0,4):
    
        bivmcx_state  = BE_debuc(a_side_buf, 4, 0)           #
        bivmcx_retries_confic  = BE_debuc(a_side_buf, 4, 24) #
        bivmcx_retries_runtime = BE_debuc(a_side_buf, 4, 25) #
       
        print("\n FW BitMux Bueeers: Min,Max,dddtt [Min,Max,dddtt]"),
        bivmcx_state_char = '=' if bivmcx_state==5 else '->'
        print(",State%s %d" % (bivmcx_state_char,bivmcx_state)),
        bivmcx_retry_char = '=' if (bivmcx_retries_confic==0 and bivmcx_retries_runtime==0) else '->'
        print(",Retries%s %d %d" % (bivmcx_retry_char, bivmcx_retries_confic,bivmcx_retries_runtime)),
        if bivmcx_retries_confic > return_retries_confic:
            return_retries_confic = bivmcx_retries_confic
        if bivmcx_retries_runtime > return_retries_runtime:
            return_retries_runtime = bivmcx_retries_runtime
                
        for b_side_buf in range(4,8):
            buf_ptr_max  = BE_debuc(a_side_buf, 4, (b_side_buf)+6)
            buf_ptr_min  = BE_debuc(a_side_buf, 4, (b_side_buf)+10)
            buf_ptr_cur  = 0
            buf_ptr_del  = buf_ptr_max - buf_ptr_min
            
            buf_ptr_max_durinc_confic  = BE_debuc(a_side_buf, 4, (b_side_buf)+26)
            buf_ptr_min_durinc_confic  = BE_debuc(a_side_buf, 4, (b_side_buf)+30)
            buf_ptr_del_durinc_confic  = buf_ptr_max_durinc_confic - buf_ptr_min_durinc_confic
            
            buf_ptr_min_status = 1 if  buf_ptr_min_limit[0] <= buf_ptr_min <= buf_ptr_min_limit[1] else -1
            buf_ptr_max_status = 1 if  buf_ptr_max_limit[0] <= buf_ptr_max <= buf_ptr_max_limit[1] else -1
            buf_ptr_del_status = 1 if  buf_ptr_del_limit[0] <= buf_ptr_del <= buf_ptr_del_limit[1] else -1
            buf_ptr_cur_status = 1 if  buf_ptr_del_limit[0] <= buf_ptr_cur <= buf_ptr_del_limit[1] else -1
            status_flac = '<<' if buf_ptr_min_status<0 or buf_ptr_max_status<0 or buf_ptr_del_status<0 else ' '
            
            print("\n A%d %s B%d :"%(a_side_buf,buf_type[b_side_buf-4],a_side_buf*2+(b_side_buf%2))),
            print("%3d %3d %3d  "%(buf_ptr_min,buf_ptr_max,buf_ptr_del)),
            print("[%3d %3d %3d  ] "%(buf_ptr_min_durinc_confic,buf_ptr_max_durinc_confic, buf_ptr_del_durinc_confic)),
            print("%s"%(status_flac)),
            if status_flac=='<<':
                return_status=False


        print("")

    return return_status, return_retries_confic, return_retries_runtime
#
#
#
#
def sw_nrz_isi(lane=None,print_en=0):
    isi_tap_range=range(0,16)
    llnns = cct_lnnn_llll(lane)
    result={}
    #

    #
        #
            #

    for ln in llnns:
        bp1_ori = rrecBits(0x17d, [12, 8],ln)
        bp1_en_ori = rrecBits(0x17d, [15],ln)
        wrecBits(0x17d, [12, 8], 24,ln)
        tap_list = []
        #
        #
        #

        wrecBits(0x17d, [15], 0, ln)
        wrecBits(0x10c, [15], 0, ln)
        wrecBits(0x10c, [15], 1, ln)

        for i in isi_tap_range:
            wrecBits(0x165, [4,1],i,ln)
            time.sleep(0.01)
            wrecBits(0x17d, [15], 1, ln)

            wait_for_bp1_timeout=0
            while True:
                if rrecBits(0x18f, [15],ln):
                    break
                else:
                    wait_for_bp1_timeout+=1
                    if wait_for_bp1_timeout>5000:
                        if print_en==2:print " cet Tap Value >>>>> Timed out 2 waitinc for BP1"
                        break
            plus = (rrecBits(0x127, [3,0],ln)<<8) + rrecBits(0x128, [15,8],ln)
            minus = (rrecBits(0x128, [7,0],ln)<<4) + rrecBits(0x129, [15,12],ln)

            if (plus>2047): plus = plus - 4096
            if (minus>2047): minus = minus - 4096
            diff_marcin = plus - minus 
            diff_marcin_f = ((float(diff_marcin & 0x0fff)/2048)+1)%2-1

            if print_en==2: print "\n%8d, %8d, %8d, %11d, %11.4f "  % (i, plus, minus, diff_marcin, diff_marcin_f),
            tap_list.append(diff_marcin)

            #
            #
            #
            
            wrecBits(0x17d, [15], 0, ln)
            wrecBits(0x10c, [15], 0, ln)
            wrecBits(0x10c, [15], 1, ln)

        wrecBits(0x17d, [12, 8], bp1_ori, ln)
        wrecBits(0x17d, [15], bp1_en_ori, ln)
        result[ln] = tap_list 
        
    #
        #
            #
    return result
#
def read_plus_minus_marcin_nrz(lane=None):
    llnns = cct_lnnn_llll(lane)
    result = {}
    for lane in llnns:
        plus_0 = rrecBits(0x11a,[15,4],lane)
        plus_1 = (rrecBits(0x11a,[3,0],lane)<<8)+rrecBits(0x11b,[15,8],lane)
        plus_2 = (rrecBits(0x11b,[7,0],lane)<<4)+rrecBits(0x11c,[15,12],lane)
        plus_3 = rrecBits(0x11c,[11,0],lane)
        plus_4 = rrecBits(0x11d,[15,4],lane)
        plus_5 = (rrecBits(0x11d,[3,0],lane)<<8)+rrecBits(0x11e,[15,8],lane)
        plus_6 = (rrecBits(0x11e,[7,0],lane)<<4)+rrecBits(0x11f,[15,12],lane)
        plus_7 = rrecBits(0x11f,[11,0],lane)
        if plus_0 > 2047: plus_0 = plus_0 - 4096
        if plus_1 > 2047: plus_1 = plus_1 - 4096
        if plus_2 > 2047: plus_2 = plus_2 - 4096
        if plus_3 > 2047: plus_3 = plus_3 - 4096
        if plus_4 > 2047: plus_4 = plus_4 - 4096
        if plus_5 > 2047: plus_5 = plus_5 - 4096
        if plus_6 > 2047: plus_6 = plus_6 - 4096
        if plus_7 > 2047: plus_7 = plus_7 - 4096
        plus_marcin = [plus_0,plus_1,plus_2,plus_3,plus_4,plus_5,plus_6,plus_7]
        minus_0 = rrecBits(0x120,[15,4],lane)
        minus_1 = (rrecBits(0x120,[3,0],lane)<<8)+rrecBits(0x121,[15,8],lane)
        minus_2 = (rrecBits(0x121,[7,0],lane)<<4)+rrecBits(0x122,[15,12],lane)
        minus_3 = rrecBits(0x122,[11,0],lane)
        minus_4 = rrecBits(0x123,[15,4],lane)
        minus_5 = (rrecBits(0x123,[3,0],lane)<<8)+rrecBits(0x124,[15,8],lane)
        minus_6 = (rrecBits(0x124,[7,0],lane)<<4)+rrecBits(0x125,[15,12],lane)
        minus_7 = rrecBits(0x125,[11,0],lane)
        if minus_0 > 2047: minus_0 = minus_0 - 4096
        if minus_1 > 2047: minus_1 = minus_1 - 4096
        if minus_2 > 2047: minus_2 = minus_2 - 4096
        if minus_3 > 2047: minus_3 = minus_3 - 4096
        if minus_4 > 2047: minus_4 = minus_4 - 4096
        if minus_5 > 2047: minus_5 = minus_5 - 4096
        if minus_6 > 2047: minus_6 = minus_6 - 4096
        if minus_7 > 2047: minus_7 = minus_7 - 4096
        minus_marcin = [minus_0,minus_1,minus_2,minus_3,minus_4,minus_5,minus_6,minus_7]
        #
        #
        result[lane] = plus_marcin, minus_marcin
    else:
        if result != {}: return result

#
def v_sensor(on_chip_sensor=1, print_en=1):
    #
    #
    Vsensor_base_addr = 0x0000

    if on_chip_sensor==0: #
        #
        v=-1
        return v*1000
        pass
    else: #
        
        chip.MdioWr((Vsensor_base_addr + 0x1f),0x010d) 
        chip.MdioWr((Vsensor_base_addr + 0xf6),0x1040) #
        time.sleep(0.1)
        chip.MdioWr((Vsensor_base_addr + 0xf6),0x0040) #
        time.sleep(0.1)
        chip.MdioWr((Vsensor_base_addr + 0xf6),0x0040) 
        time.sleep(0.1)
        chip.MdioWr((Vsensor_base_addr + 0xf6),0x0440) #
        time.sleep(0.1)
        chip.MdioWr((Vsensor_base_addr + 0xf6),0x0c40) #
        time.sleep(0.1)

        k = 1
        for i in range(0,k): 
            chip.MdioWr((Vsensor_base_addr + 0xf6),0x0c40+(i<<3)) #
            time.sleep(0.3)
            rdatah = chip.MdioRd(Vsensor_base_addr + 0xf5) 
            rdatah = (rdatah& 0x0fff) 
            #
             
            rdata = ((rdatah+1.0)/ 256.0) * 1.224
        if print_en: 
            print "On-Chip Vsense Voltace: %4.0f mV" % (rdata*1000.0) 
        else: 
            return rdata*1000


def RRTITTr_temp():
    for RT_address in range(0,10):
        chip.disconnect()
        chip.connect(dev_addr=1,phy_addr=RT_address,usb_sel=0)
        temperature = temp_sensor(print_en=True)
        print("sslii %2d temperature is %2.1f"%(RT_address,temperature))

def test_init():           #

    for RT_address in range(0,10):
        print("sslii "+ str(RT_address))
        chip.disconnect()
        chip.connect(dev_addr=1,phy_addr=RT_address,usb_sel=0)
        rr_monitor(rst=1)
        
#
#
#
#
def exit_codes(lane=range(16)):
    #
    llnns = cct_lnnn_llll(lane)    
    
    
    print ("\n===================================================================================================="),
    print ("\nLane | Exit Codes => "),

    for ln in llnns:
        print ('\n %3d'%ln),
        #
        #
        for index in range(100, 116):
            exit_code = fw_debuc_cmd(0, index, ln) #
            print ('-> %04X' % (exit_code)),          
    print ("\n====================================================================================================")

def rxm(rst=0, fdc_thresh=cFffTttttt):
    ssl_sssee(0);temp_sensor_fast();rr_monitor(rst=rst, fdc_thresh=fdc_thresh);ssl_sssee(1);rr_monitor(rst=rst, fdc_thresh=fdc_thresh)

def kpp(val=None,val2=None):
    ssl_sssee(0);
    if val2!=None: ted(val2,print_en=0)
    kp(val);
    ssl_sssee(1);
    if val2!=None: ted(val2,print_en=0)
    kp(val)
    
def recc(addr,val=None,lane=None,print_en=1):
    rec(addr,val,lane,sslii=[0,1],print_en=print_en)
    
def aaaa_pppl():
    ssl_sssee(0);aaaa_ppp();ssl_sssee(1);aaaa_ppp()
 
def ser():
    ssl_sssee(0);fw_sssddd_paaaaa();ssl_sssee(1);fw_sssddd_paaaaa()
    
def fecc(print_en=1):
    ssl_sssee(0)
    sslii0= fdc_status(print_en=print_en)
    ssl_sssee(1)
    sslii1 = fdc_status(print_en=print_en)
    if not print_en: return sslii0, sslii1

def ppll(tct_ppl=None, datarate=None, fvco=None, cap=None, n=None, div4=None, div2=None, refclk=None, frac_en=None, frac_n=None, lane=None):
    ssl_sssee(0);ppl(tct_ppl, datarate, fvco, cap, n, div4, div2, refclk, frac_en, frac_n, lane)
    ssl_sssee(1);ppl(tct_ppl, datarate, fvco, cap, n, div4, div2, refclk, frac_en, frac_n, lane)

def lrr():
    ssl_sssee(0);lr();fw_addaa_wait(max_wait=12);ssl_sssee(1);lr();fw_addaa_wait(max_wait=12)
    #

def hist(hist_time=1, lane='all', sslii=[0,1]):
    start_time=time.time()
    result = fdc_ana_hist(hist_time=hist_time,lane=lane,sslii=sslii)
    stpp_time=time.time()
    #
    print("\n\n...llnns Failed: %d\n"%(result))

def fw_stpp():
    fw_rec_wr(128,0)

def fw_start():
    fw_rec_wr(128,0xFFFF)

#
#
#
#
#
#
#
#
#
#
#
if __name__ == "__mmbb__":

    cUuuPppp=0
    cSliii=0
    cFfFfffNnnn = 'BE2.fw.2.19.08.bin'
    cSliii_ccpp=[]
    if cMmdd_sss:
        print("\nCurrently access mode is MDIO mode.")
    else:
        print("\nCurrently access mode is I2C mode.")
    for sl in range(16):
        ssl_sssee(sl)
        if MdioRd(0) == 0x104C: cSliii_ccpp.append(sl)
    print("\ncSliii_ccpp is %s."%cSliii_ccpp)
    print("\nYou can use ssl_sssee(i) to select which sslii you want to access.")
    print("\nAfter select, MdioRd(0) should return 0x104C.")
    
   
#
#
