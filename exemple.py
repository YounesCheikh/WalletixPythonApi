#!/usr/bin/python
# -*- coding: utf-8 -*-

import walletix, sys

# Vos Identifiants
vendorID = 'YOUR VENDOR ID'
apiKey = 'YOUR API KEY'

# Il faut identify une fois au debut du programme
w = walletix.Identify(vendorID,apiKey)

gpc = w.generatePaymentCode('1','1','http://www.cyounes.com')
if (gpc.status ==1):
    print('Generated Code Is:', gpc.result)
    print('Payment Verification: ',gpc.result)
    vp = w.verifyPayment(gpc.result)
    if (vp.status==1):
        if(vp.result==1):
            print('successful')
        else:
            print('unsuccessful')
    print('Delete Payment: ',gpc.result)
    dp = w.deletePayment(gpc.result)
    if (dp.status==1):
        if(dp.result==1):
            print('successful')
        else:
            print('unsuccessful')

else:
    print('Erreur lors la génération du code!')




