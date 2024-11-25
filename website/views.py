from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ContactFormForm
from django.conf import settings

# Create your views here.

def home(request):
    return render(request, 'website/index.html')

def cities_mirpur(request):
    return render(request, 'website/cities_mirpur.html')

def Benazir_Medical_College_Mirpur(request):
    return render(request, 'website/Benazir_Medical_College_Mirpur.html')

def Benazir_Medical_Collegetwo_Mirpur(request):
    return render(request, 'website/Benazir_Medical_Collegetwo_Mirpur.html')

def Opposite_to_Kashmir_Mirpur(request):
    return render(request, 'website/Opposite_to_Kashmir_Mirpur.html')

def Chitrpari_Graveyard_Mirpur(request):
    return render(request, 'website/Chitrpari_Graveyard_Mirpur.html')

def DHO_Office_Mirpur(request):
    return render(request, 'website/DHO_Office_Mirpur.html')

def DHO_Officetwo_Mirpur(request):
    return render(request, 'website/DHO_Officetwo_Mirpur.html')

def Muncipal_Corporation(request):
    return render(request, 'website/Muncipal_Corporation.html')

def ViewpointPark_Mirpur(request):
    return render(request, 'website/ViewpointPark_Mirpur.html')

def Haul_Road_Mirpur(request):
    return render(request, 'website/Haul_Road_Mirpur.html')

def DHQ_Mirpur(request):
    return render(request, 'website/DHQ_Mirpur.html')

def Lehri_Zoo_Park_Mirpur(request):
    return render(request, 'website/Lehri_Zoo_Park_Mirpur.html')

def Fish_Hechri_Lehri(request):
    return render(request, 'website/Fish_Hechri_Lehri.html')

def Jarikass_Poultry(request):
    return render(request, 'website/Jarikass_Poultry.html')

def Canal_bank_Mirpur(request):
    return render(request, 'website/Canal_bank_Mirpur.html')

def Girls_Degree_College_Kalyal(request):
    return render(request, 'website/Girls_Degree_College_Kalyal.html')

def BangrillaCommunityHospital(request):
    return render(request, 'website/BangrillaCommunityHospital.html')

def Islamgarh_Welfare_Trust(request):
    return render(request, 'website/Islamgarh_Welfare_Trust.html')

def Pilot_School_Mirpur(request):
    return render(request, 'website/Pilot_School_Mirpur.html')

def Solid_Waste_Project_Site_Mirpur(request):
    return render(request, 'website/Solid_Waste_Project_Site_Mirpur.html')

def Muslim_Hands_Football_Academy_Mirpur(request):
    return render(request, 'website/Muslim_Hands_Football_Academy_Mirpur.html')

def AllamaIqbalRoad(request):
    return render(request, 'website/AllamaIqbalRoad.html')

def MUST_Uni_Ajk(request):
    return render(request, 'website/MUST_Uni_Ajk.html')

def Afzalpur_Mirpur(request):
    return render(request, 'website/Afzalpur_Mirpur.html')

def Allama_Iqbal_Open_Uni_Mirpur(request):
    return render(request, 'website/Allama_Iqbal_Open_Uni_Mirpur.html')

def MUST_JariKass_Campuss(request):
    return render(request, 'website/MUST_JariKass_Campuss.html')

def SectorF4_Mirpur(request):
    return render(request, 'website/SectorF4_Mirpur.html')

def environment_protection_agency(request):
    return render(request, 'website/environment_protection_agency.html')

def Chapran_Village_Mirpur(request):
    return render(request, 'website/Chapran_Village_Mirpur.html')

#NEW MIRPUR CITY ADDING ON 01-11-2024

def August_Muncipal_Corporation_Plantation_Mirpur(request):
    return render(request, 'website/14_August_Muncipal_Corporation_Plantation_Mirpur.html')

def August14_Plantation(request):
    return render(request, 'website/14_August_Plantation.html')

def Assistant_Commissioner_Islamghar_Mirpur(request):
    return render(request, 'website/Assistant_Commissioner_Islamghar_Mirpur.html')

def Bankhurma_Mirpur(request):
    return render(request, 'website/Bankhurma_Mirpur.html')

def Bankhurma_Chapran_Mirpur(request):
    return render(request, 'website/Bankhurma_Chapran_Mirpur.html')

def Benazir_Medical_College_Plantation_2024Season2_Mirpur(request):
    return render(request, 'website/Benazir_Medical_College_Plantation_2024Season2_Mirpur.html')

def C4_Ground_Mirpur(request):
    return render(request, 'website/C4_Ground_Mirpur.html')

def Degree_College_Mirpur(request):
    return render(request, 'website/Degree_College_Mirpur.html')





def Nelum_Muzaffarabad(request):
    return render(request, 'website/Nelum_Muzaffarabad.html')

def Rarra_Central_Jail_Muzaffarabad(request):
    return render(request, 'website/Rarra_Central_Jail_Muzaffarabad.html')

#NEW MUZAFFARABAD CITY ADDING ON 01-11-2024

def Civil_Veterinary_Hospital_Gharhi_Dupatta_Muzaffarabad(request):
    return render(request, 'website/Civil_Veterinary_Hospital_Gharhi_Dupatta_Muzaffarabad.html')





def Girls_High_School_Tararkhal(request):
    return render(request, 'website/Girls_High_School_Tararkhal.html')

def Tararkhal_Rawalakot(request):
    return render(request, 'website/Tararkhal_Rawalakot.html')

def Nakyal_Kotli(request):
    return render(request, 'website/Nakyal_Kotli.html')

def Ghazighura_Bhimber(request):
    return render(request, 'website/Ghazighura_Bhimber.html')

def Ghura_Khurd_Dera_Mirpur(request):
    return render(request, 'website/Ghura_Khurd_Dera_Mirpur.html')

def Patni_Bhimber(request):
    return render(request, 'website/Patni_Bhimber.html')

def BHU_Bider_Brains_Bhimber(request):
    return render(request, 'website/BHU_Bider_Brains_Bhimber.html')

def District_Jail_Bhimber(request):
    return render(request, 'website/District_Jail_Bhimber.html')

#NEW BHIMBER CITY ADDING ON 02-11-2024
def Alharmain_Daraiyan_Welfare_Foundation_Bhimber(request):
    return render(request, 'website/Alharmain_Daraiyan_Welfare_Foundation_Bhimber.html')

def Bhimber_Uni_Bhimber(request):
    return render(request, 'website/Bhimber_Uni_Bhimber.html')

def BHU_Banain_Bhimber(request):
    return render(request, 'website/BHU_Banain_Bhimber.html')

def BHU_Chaneer_Bhimber(request):
    return render(request, 'website/BHU_Chaneer_Bhimber.html')

def BHU_Kherowal_Bhimber(request):
    return render(request, 'website/BHU_Kherowal_Bhimber.html')

def BHU_Kot_Jamel_Bhimber(request):
    return render(request, 'website/BHU_Kot_Jamel_Bhimber.html')

def BHU_Maghloora_Bhimber(request):
    return render(request, 'website/BHU_Maghloora_Bhimber.html')

def Darbar_Baba_Shadi_Shaheed(request):
    return render(request, 'website/Darbar_Baba_Shadi_Shaheed.html')

def DHO_Bhimber(request):
    return render(request, 'website/DHO_Bhimber.html')

def DHO_Mirpur_Fruit_garden(request):
    return render(request, 'website/DHO_Mirpur_Fruit_garden.html')




def Dadyal_1(request):
    return render(request, 'website/Dadyal_1.html')

def Dadyal_2(request):
    return render(request, 'website/Dadyal_2.html')

def Pachwana_Dadyal(request):
    return render(request, 'website/Pachwana_Dadyal.html')

def gardens(request):
    return render(request, 'website/gardens.html')

def training(request):
    return render(request, 'website/training.html')





def cities_muzaffarabad(request):
    return render(request, 'website/cities_muzaffarabad.html')

def cities_rawalakot(request):
    return render(request, 'website/cities_rawalakot.html')

def cities_kotli(request):
    return render(request, 'website/cities_kotli.html')

def cities_bhimber(request):
    return render(request, 'website/cities_bhimber.html')

def cities_dadyal(request):
    return render(request, 'website/cities_dadyal.html')

def contact_us(request):
    return render(request, 'website/contact_us.html')

def about_us(request):
    return render(request, 'website/about_us.html')

def events(request):
    return render(request, 'website/events.html')

def gallery(request):
    return render(request, 'website/gallery.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactFormForm(request.POST)
        if form.is_valid():
            contact_form = form.save()

            # Sending email to user
            send_mail(
                'Thank you for your message',
                f'Thank you for contacting us. Here is a copy of your message:\n\n{contact_form.message}',
                settings.EMAIL_HOST_USER,
                [contact_form.email],
            )

            # Sending email to admin
            send_mail(
                'New contact form submission',
                f'Name: {contact_form.name}\nEmail: {contact_form.email}\nMessage: {contact_form.message}',
                settings.EMAIL_HOST_USER,
                [settings.ADMIN_EMAIL],
            )

            return redirect('success')
    else:
        form = ContactFormForm()
    return render(request, 'website/contact_form.html', {'form': form})

def success_view(request):
    return render(request, 'website/success.html')
