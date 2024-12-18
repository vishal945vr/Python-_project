import qrcode as qr
# import qr code libaray 
id =input("enter your id:")
#input user id 

QrData="https://github.com/vishal945vr?tab=projects"+id
#insert the URL link for Github id and add with  user id name  id name 

QrImg = qr.make(QrData)
# this code make for QR make 

QrImg.save(id+".png")
# last process for save QR picture in .png form in your folder 



