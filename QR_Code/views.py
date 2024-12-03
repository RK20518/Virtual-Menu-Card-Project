from django.shortcuts import render
from . forms import QRCodeForm
import qrcode 
import os
from django.conf import settings

def qr_code(reqeust):

    if reqeust.method == 'POST':
        form = QRCodeForm(reqeust.POST)
        if form.is_valid():
            res_name = form.cleaned_data['restaurant_name']
            url = form.cleaned_data['url']

            # print(res_name,url) #checking that we getting the data in backend or not i.e terminal

            #Generate QR Code
            qr = qrcode.make(url)
            # print(qr)#checking wehter we getting the image object address in backend or terminal
            qr_file = res_name.replace(' ','_').lower() + 'menu.png'
            file_path = os.path.join(settings.MEDIA_ROOT,qr_file) #.../media/balaji_menu.png
            qr.save(file_path)

            #create image url to display from front end to backend

            qr_url = os.path.join(settings.MEDIA_URL, qr_file)

            print('qr_url',qr_url)

            context = {
                'res_name':res_name,
                'qr_url':qr_url,
                'qr_file':qr_file,
            }

            return render(reqeust,'download.html',context)

    else:

        form = QRCodeForm()

        context = {
            'form':form,
                    }

        return render(reqeust,'qr_code.html',context)