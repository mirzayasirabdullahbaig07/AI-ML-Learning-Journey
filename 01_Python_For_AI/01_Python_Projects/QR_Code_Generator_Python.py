# Creating QR Code Generator 
import qrcode as qr

qrimg = qr.make("https://yasirinsights.com/")
qrimg.save("YasirInsights.png")