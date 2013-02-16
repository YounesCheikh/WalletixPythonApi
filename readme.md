Walletix API For Python Applications
====================================

import walletix.py module and start using Walletix services :-)

```
THIS VERSION WORKS ONLY WITH Python >=2.6  
```

### How to use? 
#### Example:
+ Identify:

```
import walletix
w = walletix.Identify(vendorID,apiKey)
```
+ Generate Payment Code:

```
gpc = w.generatePaymentCode('1','1','http://www.cyounes.com')
```
+ Verify payment:

```
if gpc.status == 1:
	vp = w.verifyPayment(gpc.result)
	if vp.status == 1:
		print(vp.result)
	else:
		print('Error')
```

+ Delete Payment:

```
if gpc.status == 1:
	dp = w.deletePayment(gpc.result)
	if dp.status == 1:
		print(dp.result)
```

+ See [Full Example](exemple.py) 
+ API Documentation: https://www.walletix.com/documentation-api 



