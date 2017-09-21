from scraping import *

print ''
print 'Off-momentum tail scraping analysis and profile reconstruction'
print 'Hector Garcia Morales, CERN'
print '2017.09.15'
print ''

centreTCPL = 0.2
sigmaB2TCP = 2*(8.0-centreTCPL)/8.0 

print 'TCP scrapings'
print 'B2H: centre =', centreTCPL ,', beam size =', sigmaB2TCP
print ''

t1 =  '15.09.2017 17:53:00'
t2 = '15.09.2017 20:43:00'	

print 'Initial time =', t1
print 'Final time =', t2
print ''
print 'Maximum B2 intensity in range =', getMaxIB(t1,t2,'B2')*1e-11

plt.figure(1)
plotBCTtime(t1,t2,'B2')
plt.xlabel('Time')
plt.ylabel('Beam intensity [p]')

x = np.linspace(0., 5., 50.)

print ''
print 'TCP IR3 Left Jaw'
beamPlane = 'B2L'
BLMlist = "BLMTI.06R3.B2E10_TCP.6R3.B2:LOSS_RS09"
TCPlistLD = "TCP.6R3.B2:MEAS_MOTOR_LD"
t1 =  '15.09.2017 17:52:00'
t2 = '15.09.2017 18:07:30'	

TCP_pos_sigma, BLM, integr = matchTCPvsBLM(t1,t2,TCPlistLD,BLMlist,'B2',centreTCPL,sigmaB2TCP)
plt.figure(4)
plt.yscale('log')
plotProfile(TCP_pos_sigma,integr,'TCP Left Jaw')
plt.xlabel('TCP position [$\sigma$]')
plt.ylabel('Beam population')
plt.legend()
plt.figure(5)
plt.plot(TCP_pos_sigma,BLM,label='TCP Left Jaw')
plt.legend()
plt.ylabel('BLM signal [Gy/s]')
plt.xlabel('TCP position [$\sigma$]')

print ''
print 'TCP IR3 Right Jaw'
beamPlane = 'B2R'
BLMlist = "BLMTI.06R3.B2E10_TCP.6R3.B2:LOSS_RS09"
TCPlistLD = "TCP.6R3.B2:MEAS_MOTOR_RD"
t1 =  '15.09.2017 18:28:00'
t2 = '15.09.2017 18:36:00'	

TCP_pos_sigma, BLM, integr = matchTCPvsBLM(t1,t2,TCPlistLD,BLMlist,'B2',centreTCPL,sigmaB2TCP)
plt.figure(4)
plt.yscale('log')
plotProfile(TCP_pos_sigma,integr,'TCP Right Jaw')
plt.xlabel('TCP position [$\sigma$]')
plt.ylabel('Beam population')
plt.legend()
plt.figure(5)
plt.plot(TCP_pos_sigma,BLM,label='TCP Right Jaw')
plt.legend()
plt.ylabel('BLM signal [Gy/s]')
plt.xlabel('TCP position [$\sigma$]')

print ''
print 'TCP IR3 Left Jaw'
beamPlane = 'B2R'
BLMlist = "BLMTI.06R3.B2E10_TCP.6R3.B2:LOSS_RS09"
TCPlistLD = "TCP.6R3.B2:MEAS_MOTOR_RD"
t1 =  '15.09.2017 20:36:00'
t2 = '15.09.2017 20:42:30'	

TCP_pos_sigma, BLM, integr = matchTCPvsBLM(t1,t2,TCPlistLD,BLMlist,'B2',centreTCPL,sigmaB2TCP)
plt.figure(4)
plt.yscale('log')
plotProfile(TCP_pos_sigma,integr,'TCP Right Jaw')
plt.xlabel('TCP position [$\sigma$]')
plt.ylabel('Beam population')
plt.legend()
plt.figure(5)
plt.plot(TCP_pos_sigma,BLM,label='TCP Right Jaw')
plt.legend()
plt.ylabel('BLM signal [Gy/s]')
plt.xlabel('TCP position [$\sigma$]')

centreTCPL = -0.014
sigmaB2TCP = 2.*1.57
print ''
print 'TCSG scrapings'
print 'B2H: centre =', centreTCPL ,', beam size =', sigmaB2TCP
print ''

print 'TCSG IR7 Left Jaw'
beamPlane = 'B2L'
BLMlist = "BLMTI.06L7.B2I10_TCSG.6L7.B2:LOSS_RS09"
TCPlistLD = "TCSG.6L7.B2:MEAS_MOTOR_LD"
t1 =  '15.09.2017 19:36:00'
t2 = '15.09.2017 19:45:30'	
TCP_pos_sigma, BLM, integr = matchTCPvsBLM(t1,t2,TCPlistLD,BLMlist,'B2',centreTCPL,sigmaB2TCP)
plt.figure(4)
plt.yscale('log')
plotProfile(TCP_pos_sigma,integr,'TCSG Left Jaw')
plt.xlabel('TCP position [$\sigma$]')
plt.ylabel('Beam population')
plt.legend()
plt.figure(5)
plt.plot(TCP_pos_sigma,BLM,label='TCSG Left Jaw')
plt.legend()
plt.ylabel('BLM signal [Gy/s]')
plt.xlabel('TCP position [$\sigma$]')

print ''
print 'TCSG IR7 Right Jaw'
beamPlane = 'B2R'
BLMlist = "BLMTI.06L7.B2I10_TCSG.6L7.B2:LOSS_RS09"
TCPlistLD = "TCSG.6L7.B2:MEAS_MOTOR_RD"
t1 =  '15.09.2017 20:07:00'
t2 = '15.09.2017 20:16:00'	
TCP_pos_sigma, BLM, integr = matchTCPvsBLM(t1,t2,TCPlistLD,BLMlist,'B2',centreTCPL,sigmaB2TCP)
plt.figure(4)
plt.yscale('log')
plotProfile(TCP_pos_sigma,integr,'TCSG Right Jaw')
plt.xlabel('TCP position [$\sigma$]')
plt.ylabel('Beam population')
plt.xlim(-7,7)
plt.legend()
#plt.plot(x,fitAbel(x, 0., 1.,getIntensity(t1,'B2')))
plt.figure(5)
plt.plot(TCP_pos_sigma,BLM,label='TCSG Right Jaw')
plt.legend()
plt.ylabel('BLM signal [Gy/s]')
plt.xlabel('TCP position [$\sigma$]')

plt.show()
