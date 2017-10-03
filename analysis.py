from scraping import *

print ''
print 'Off-momentum tail scraping analysis and profile reconstruction'
print 'Hector Garcia Morales, CERN'

print ''
print '-------------------------------------------------------'
print ''

centreTCPL = 0.2
sigmaB2TCP = 2*(8.0-centreTCPL)/8.0 

print 'TCP scrapings'
print 'B2H: centre =', centreTCPL ,', beam size =', sigmaB2TCP
print ''
BLMlist = "BLMTI.06R3.B2E10_TCP.6R3.B2:LOSS_RS09"

print 'TCP IR3 Left Jaw'
beamPlane = 'B2L'
TCPlistLD = "TCP.6R3.B2:MEAS_MOTOR_LD"
t1 =  '15.09.2017 17:51:00'
t2 = '15.09.2017 18:07:30'	

TCP_pos_sigma, BLM, integr = matchTCPvsBLM(t1,t2,TCPlistLD,BLMlist,'B2',centreTCPL,sigmaB2TCP,7.9)
plt.figure(4)
plotProfile(TCP_pos_sigma,integr,'TCP Left Jaw')
plt.figure(5)
plt.plot(TCP_pos_sigma,BLM,label='TCP Left Jaw')

print ''
print 'TCP IR3 Right Jaw'
beamPlane = 'B2R'
TCPlistLD = "TCP.6R3.B2:MEAS_MOTOR_RD"
t1 =  '15.09.2017 18:28:00'
t2 = '15.09.2017 18:35:30'	

TCP_pos_sigma, BLM, integr = matchTCPvsBLM(t1,t2,TCPlistLD,BLMlist,'B2',centreTCPL,sigmaB2TCP,7.9)
plt.figure(4)
plotProfile(TCP_pos_sigma,integr,'TCP Right Jaw')
plt.figure(5)
plt.plot(TCP_pos_sigma,BLM,label='TCP Right Jaw')

print ''
print 'TCP IR3 Left Jaw'
beamPlane = 'B2R'
TCPlistLD = "TCP.6R3.B2:MEAS_MOTOR_RD"
t1 =  '15.09.2017 20:36:00'
t2 = '15.09.2017 20:42:10'	
TCP_pos_sigma, BLM, integr = matchTCPvsBLM(t1,t2,TCPlistLD,BLMlist,'B2',centreTCPL,sigmaB2TCP,7.9)
plt.figure(4)
plotProfile(TCP_pos_sigma,integr,'TCP Right Jaw')
plt.figure(5)
plt.plot(TCP_pos_sigma,BLM,label='TCP Right Jaw')

print ''
print '-------------------------------------------------------'
print ''
centreTCPL = -0.14
sigmaB2TCP = 2*1.57
sigmaB2TCP = 2*(1.57-centreTCPL)/1.0 
print 'TCSG scrapings'
print 'B2H: centre =', centreTCPL ,', beam size =', sigmaB2TCP
print ''
BLMlist = "BLMTI.06L7.B2I10_TCSG.6L7.B2:LOSS_RS09"

print 'TCSG IR7 Left Jaw'
beamPlane = 'B2L'
TCPlistLD = "TCSG.6L7.B2:MEAS_MOTOR_LD"
t1 =  '15.09.2017 19:35:00'
t2 = '15.09.2017 19:44:40'
TCP_pos_sigma, BLM, integr = matchTCPvsBLM(t1,t2,TCPlistLD,BLMlist,'B2',centreTCPL,sigmaB2TCP,6.0)
plt.figure(4)
plotProfile(TCP_pos_sigma,integr,'TCSG Left Jaw')
plt.figure(5)
plt.plot(TCP_pos_sigma,BLM,label='TCSG Left Jaw')

print ''
print 'TCSG IR7 Right Jaw'
beamPlane = 'B2R'
TCPlistLD = "TCSG.6L7.B2:MEAS_MOTOR_RD"
t1 =  '15.09.2017 20:07:00'
t2 = '15.09.2017 20:15:40'	
TCP_pos_sigma, BLM, integr = matchTCPvsBLM(t1,t2,TCPlistLD,BLMlist,'B2',centreTCPL,sigmaB2TCP,6.0)
plt.figure(4)
plotProfile(TCP_pos_sigma,integr,'TCSG Right Jaw')
#x = np.linspace(0., 5., 50.)
#plt.plot(x,fitAbel(x, 0., 1.,getIntensity(t1,'B2')))
plt.figure(5)
plt.plot(TCP_pos_sigma,BLM,label='TCSG Right Jaw')

# Plot settings
plt.figure(4)
plt.yscale('log')
#plt.xlabel('Collimator position [$\sigma$]')
plt.ylabel('Normalized scraped intensity')
plt.ylabel('Scraped protons')
plt.xlim(-9.9,9.9)
plt.legend()

plt.figure(5)
plt.yscale('log')
plt.ylabel('BLM signal [Gy/s]')
plt.xlabel('Collimator position [$\sigma$]')
plt.xlim(-9.9,9.9)
plt.legend()
plt.show()
