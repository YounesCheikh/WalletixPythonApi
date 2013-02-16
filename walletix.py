#!/usr/bin/python
# -*- coding: utf-8 -*-
# Filename: walletix.py
# Author: Cheikh Younes
# Version: 0.2

import sys

def getPythonVersion():
	version_info = str(sys.version_info) 
	retVal =-1
	if version_info.find('major=3')!=-1:
		retVal=3
	elif version_info.find('major=2')!=-1:
		retVal=2
	return retVal
  
isPython3 = ( getPythonVersion() == 3 )

class Response:
	def __init__(self,status, result ):
		(self.status, self.result) = (status, result)
		

if isPython3:
	import http.client, urllib.parse, json
	
	class Identify:
		"""
		Cette classe permet d'identifier sur walletix en utilisant vendorId et apiKey
		"""
		__vendorID=''
		__apiKey=''
		def __init__(self, vendorID, apiKey):
			if (vendorID!='' and apiKey!=''):
				self.__class__.__vendorID = vendorID
				self.__class__.__apiKey = apiKey
	
		def vendorInfoSet(self):
			return (self.__vendorID!='' and self.__apiKey!='')
	
		@staticmethod
		def __post(self,params, request):
			connection = http.client.HTTPSConnection('www.walletix.com')
			headers = {'Content-type': 'application/x-www-form-urlencoded'}
			if request==1:
				url = 'paymentcode'
			elif request==2:
				url= 'paymentverification'
			else:
				url='deletepayment'
			connection.request('POST', '/sandbox/api/'+url, params, headers)
			response = connection.getresponse()
			data=response.read().decode()
			return data
	
		def generatePaymentCode(self,purchaseID, amount, callbackUrl ):
			params = urllib.parse.urlencode({'vendorID': self.__vendorID,
				  'apiKey': self.__apiKey,
				  'purchaseID': purchaseID,
				  'amount': amount,
				  'callbackurl':callbackUrl,
				  'format':'json'
				  })
			json_data = self.__post(self,params,1)
			data = json.loads(json_data)
			return Response(data['status'], data['code'])
	
		def verifyPayment(self,paiementCode):
			params = urllib.parse.urlencode({'vendorID': self.__vendorID,
				  'apiKey': self.__apiKey,
				  'paiementCode': paiementCode,
				  'format':'json'
				  })
			json_data = self.__post(self, params,2)
			data = json.loads(json_data)
			return Response(data['status'], data['result'])
			
		def deletePayment(self,paiementCode):
			params = urllib.parse.urlencode({'vendorID': self.__vendorID,
				  'apiKey': self.__apiKey,
				  'paiementCode': paiementCode,
				  'format':'json'
				  })
			json_data = self.__post(self, params,3)
			data = json.loads(json_data)
			return Response(data['status'], data['result'])
			
else:
	import httplib, json,urllib2, urllib, urlparse
	
	class Identify(object):
		"""
		Cette classe permet d'identifier sur walletix en utilisant vendorId et apiKey
		"""
		__vendorID=''
		__apiKey=''
		def __init__(self, vendorID, apiKey):
			if (vendorID!='' and apiKey!=''):
				self.__class__.__vendorID = vendorID
				self.__class__.__apiKey = apiKey
	
		@staticmethod
		def vendorInfoSet(self):
			return (self.__vendorID!='' and self.__apiKey!='')
	
		@staticmethod
		def __post(self,params, request):
			connection = httplib.HTTPSConnection('www.walletix.com')
			headers = {'Content-type': 'application/x-www-form-urlencoded'}
			if request==1:
				url = 'paymentcode'
			elif request==2:
				url= 'paymentverification'
			else:
				url='deletepayment'
			connection.request('POST', '/sandbox/api/'+url, params, headers)
			response = connection.getresponse()
			data=response.read().decode()
			return data
	
		def generatePaymentCode(self,purchaseID, amount, callbackUrl ):
			params = urllib.urlencode({'vendorID': self.__vendorID,
				  'apiKey': self.__apiKey,
				  'purchaseID': purchaseID,
				  'amount': amount,
				  'callbackurl':callbackUrl,
				  'format':'json'
				  })
			json_data = self.__post(self,params,1)
			data = json.loads(json_data)
			return Response(data['status'], data['code'])
	
		def verifyPayment(self,paiementCode):
			params = urllib.urlencode({'vendorID': self.__vendorID,
				  'apiKey': self.__apiKey,
				  'paiementCode': paiementCode,
				  'format':'json'
				  })
			json_data = self.__post(self, params,2)
			data = json.loads(json_data)
			return Response(data['status'], data['result'])
		
		def deletePayment(self,paiementCode):
			params = urllib.urlencode({'vendorID': self.__vendorID,
				  'apiKey': self.__apiKey,
				  'paiementCode': paiementCode,
				  'format':'json'
				  })
			json_data = self.__post(self, params,3)
			data = json.loads(json_data)
			return Response(data['status'], data['result'])

