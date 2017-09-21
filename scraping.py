import matplotlib.pyplot as plt
from matplotlib.dates import epoch2num
import time
import pytimber
import numpy as np
import sys 

db=pytimber.LoggingDB()

noise_level = 0.0

def convertTime(t0):
    pattern = '%d.%m.%Y %H:%M:%S'
    t = int(time.mktime(time.strptime(t0, pattern)))
    return t

def getTimberData(t01,t02,col,BLM):
    t1 = convertTime(t01) 
    t2 = convertTime(t02)
    data=db.get([col,BLM],t1,t2)
    tt_TCP,vv_TCP = data[col]
    tt_BLM,vv_BLM = data[BLM]
    return tt_TCP, vv_TCP, tt_BLM, vv_BLM

def findFills(t01,t02):
	fills = ldb.getLHCFillsByTime(t01, t02)
	#fills = ldb.getLHCFillsByTime(t1, t2, beam_modes='ADJUST')
	print([f['fillNumber'] for f in fills])
	return 0

def plotBLMtime(t01,t02,col,BLM,label):
     tt_TCP, vv_TCP, tt_BLM, vv_BLM = getTimberData(t01,t02,col,BLM)
     plotBLMtime = plt.plot_date(epoch2num(tt_BLM+2*3600), vv_BLM,'-', label=label)
     return plotBLMtime

def plotBCTtime(t01,t02,beam):
    if beam == 'B1':
	ib = "LHC.BCTDC.A6R4.B1:BEAM_INTENSITY"
    else:
	ib = "LHC.BCTDC.A6R4.B2:BEAM_INTENSITY"
    t1 = convertTime(t01)
    t2 = convertTime(t02)
    data=db.get([ib],t1,t2)
    tt_IB, vv_IB = data[ib]
    if beam == 'B1':
	    plotBCTtime = plt.plot_date(epoch2num(tt_IB+2*3600), vv_IB,'-', label=beam)
    else:
	    plotBCTtime = plt.plot_date(epoch2num(tt_IB+2*3600), vv_IB,'-',color='red', label=beam)
    return plotBCTtime

def getIntensity(t0,beam):
    if beam == 'B1':
	ib = "LHC.BCTDC.A6R4.B1:BEAM_INTENSITY"
    else:
	ib = "LHC.BCTDC.A6R4.B2:BEAM_INTENSITY"
    t1 = convertTime(t0)
    data=db.get([ib],t1,t1)
    tt_IB, vv_IB = data[ib]
    intensity = vv_IB[0]
    return intensity


def getMaxIB(t01,t02,beam):
    if beam == 'B1':
	ib = "LHC.BCTDC.A6R4.B1:BEAM_INTENSITY"
    else:
	ib = "LHC.BCTDC.A6R4.B2:BEAM_INTENSITY"
    t1 = convertTime(t01)
    t2 = convertTime(t02)
    data=db.get([ib],t1,t2)
    tt_IB, vv_IB = data[ib]
    ib1_0 = max(vv_IB)
    return ib1_0

def getBackground(t02):
    t2 = convertTime(t02) 
    t1 = t2 - 20.0
    BLMTL="BLMTI.06L7.B1E10_TCP.C6L7.B1:LOSS_RS09"
    data=db.get([BLMTL],t1,t2)
    tt_BLM,vv_BLM = data[BLMTL]
    backg = np.mean(vv_BLM)
    return backg

def plotTCPpos(t01,t02,col):
    t1 = convertTime(t01)
    t2 = convertTime(t02)
    data=db.get([col],t1,t2)
    tt_TCPpos,vv_TCPpos = data[col]
    plotTCPpos = plt.plot_date(epoch2num(tt_TCPpos+2*3600), vv_TCPpos,'-', label=col)
    return plotTCPpos

def matchTCPvsBLM(t01,t02,col,BLM,beam,TCPcenter,sigma):
    tt_TCP, vv_TCP, tt_BLM, vv_BLM = getTimberData(t01,t02,col,BLM)
    max_BLM = []
    BLM = []
    max_time = []
    TCP_pos = []
    ib1_0 = getMaxIB(t01,t02,beam)
    noise_level = getBackground(t01)

    int0 = getIntensity(t01,beam)
    intf = getIntensity(t02,beam)
    intDiff = int0-intf
    print "Scraped protons =", intDiff 

    #print
    #print "Beam intensity =", ib1_0*1e-11
    #print "Noise level = ", noise_level

    for i in range(len(tt_BLM)-1):
        if (vv_BLM[i-1]<vv_BLM[i] and vv_BLM[i]>vv_BLM[i+1]):
            #max_BLM.append(vv_BLM[i]-noise_level)
	    max_BLM.append(vv_BLM[i])
            max_time.append(tt_BLM[i])
            for l in range(len(tt_TCP)-1):
                if (tt_BLM[i]>tt_TCP[l] and tt_BLM[i]<tt_TCP[l+1]):
                    TCP_pos.append(vv_TCP[l])

    TCP_pos_sigma = []
    TCP_pos_mm = []
    calFact = sum(max_BLM)/intDiff
    print 'Calibration factor =', calFact, 'Gy/p'
    integr = []
    cummulative = 0

    for i in range(len(TCP_pos)):
        sigmaConv = (2.*(TCP_pos[i] - TCPcenter)/sigma)
	#print TCP_pos[i], sigmaConv
        if (sigmaConv < 4.8):
            TCP_pos_sigma.append(sigmaConv)
            TCP_pos_mm.append(TCP_pos[i])
            cummulative += max_BLM[i]
            #integr.append(1.0 - (int0 - cummulative/calFact)/int0)
            #integr.append(cummulative/calFact/int0)
            #integr.append(cummulative)
	    integr.append(max_BLM[i]/calFact)
            #BLM.append(max_BLM[i]/calFact/ib1_0)
	    BLM.append(max_BLM[i])

    return TCP_pos_sigma, BLM, integr


def convertTCPmmTOsigma(TCPpos,sigma,center):
    sigmaConv = ((TCPpos - center/2.)/sigma)
    return sigmaConv

def plotBLM(TCP_pos_sigma,max_BLM,lab):
    plotBLM = plt.plot(TCP_pos_sigma,max_BLM,label=lab)
    return plotBLM

def plotProfile(TCP_pos_sigma,integr,lab):
    #plotProfile = plt.plot(TCP_pos_sigma, integr/sum(integr),'-',label=lab)
    plotProfile = plt.plot(TCP_pos_sigma, integr,'o',label=lab)
    return plotProfile

def calcPopulation(sigma1,sigma2,TCP_pos_sigma,integr):
    population = 0
    for i in range(len(TCP_pos_sigma)):
        if(TCP_pos_sigma[i] > sigma1 and TCP_pos_sigma[i] < sigma2):
            population += integr[i]
    return population

def fitGaussian(x,mu,sig,int0):
    return (int0/np.sqrt(2.0*np.pi))*np.exp(-(x - mu)**2 / (2.0 * sig**2))

def fitAbel(x,mu,sig,int0):
    return (int0/np.sqrt(2.0*np.pi))*x*np.exp(-(x - mu)**2 / (2.0 * sig**2))




