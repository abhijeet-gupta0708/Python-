import qrcode as qr


# Taking Upi Id of User

id=input("Enter Your Upi Id = ")


# FOrmate of Upi id

# Upi Id= //pay?pa=UPI_ID&apn=NAME&am=Amount&cu=CURRENCY&tn=MESSAGE


phonepe_url=f'upi:://pay?pa:{id}&pn=Recipient%20Name%mc=1234'
paytm_url=f'upi:://pay?pa:{id}&pn=Recipient%20Name%mc=1234'
googlepay_url=f'upi:://pay?pa:{id}&pn=Recipient%20Name%mc=1234'


# Making the Qr Code image

phonepe_qr=qr.make(phonepe_url)
googlepay_qr=qr.make(googlepay_url)
paytm_qr=qr.make(paytm_url)


#display the qr code you need to have pillow liberary

phonepe_qr.show()
paytm_qr.show()
googlepay_qr.show()


choice=input("Press Yes if you want to save the image in your device : ")

if choice.lower()!="yes" :
    quit()


# Save the image in your local device

phonepe_qr.save('phonepe_qr')
googlepay_qr.save('googlepay_qr')
paytm_qr.save('paytm_qr')