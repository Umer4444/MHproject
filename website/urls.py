from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="home"),
    path('cities_mirpur/', views.cities_mirpur, name="cities_mirpur"),

    #new cities of Mirpur
    path('14_August_Muncipal_Corporation_Plantation_Mirpur/', views.August_Muncipal_Corporation_Plantation_Mirpur, name="14_August_Muncipal_Corporation_Plantation_Mirpur"),
    path('14_August_Plantation/', views.August14_Plantation, name="14_August_Plantation"),
    path('Assistant_Commissioner_Islamghar_Mirpur/', views.Assistant_Commissioner_Islamghar_Mirpur, name="Assistant_Commissioner_Islamghar_Mirpur"),
    path('Bankhurma_Mirpur/', views.Bankhurma_Mirpur, name="Bankhurma_Mirpur"),
    path('Bankhurma_Chapran_Mirpur/', views.Bankhurma_Chapran_Mirpur, name="Bankhurma_Chapran_Mirpur"),
    path('Benazir_Medical_College_Plantation_2024Season2_Mirpur/', views.Benazir_Medical_College_Plantation_2024Season2_Mirpur, name="Benazir_Medical_College_Plantation_2024Season2_Mirpur"),
    path('C4_Ground_Mirpur/', views.C4_Ground_Mirpur, name="C4_Ground_Mirpur"),
    path('Degree_College_Mirpur/', views.Degree_College_Mirpur, name="Degree_College_Mirpur"),
    path('DHO_Mirpur_Fruit_garden/', views.DHO_Mirpur_Fruit_garden, name="DHO_Mirpur_Fruit_garden"),
    
    path('Benazir_Medical_College_Mirpur/', views.Benazir_Medical_College_Mirpur, name="Benazir_Medical_College_Mirpur"),
    path('Benazir_Medical_Collegetwo_Mirpur/', views.Benazir_Medical_Collegetwo_Mirpur, name="Benazir_Medical_Collegetwo_Mirpur"),
    path('Opposite_to_Kashmir_Mirpur/', views.Opposite_to_Kashmir_Mirpur, name="Opposite_to_Kashmir_Mirpur"),
    path('Chitrpari_Graveyard_Mirpur/', views.Chitrpari_Graveyard_Mirpur, name="Chitrpari_Graveyard_Mirpur"),
    path('DHO_Office_Mirpur/', views.DHO_Office_Mirpur, name="DHO_Office_Mirpur"),
    path('DHO_Officetwo_Mirpur/', views.DHO_Officetwo_Mirpur, name="DHO_Officetwo_Mirpur"),
    path('Muncipal_Corporation/', views.Muncipal_Corporation, name="Muncipal_Corporation"),
    path('ViewpointPark_Mirpur/', views.ViewpointPark_Mirpur, name="ViewpointPark_Mirpur"),
    path('Haul_Road_Mirpur/', views.Haul_Road_Mirpur, name="Haul_Road_Mirpur"),
    path('DHQ_Mirpur/', views.DHQ_Mirpur, name="DHQ_Mirpur"),
    path('Lehri_Zoo_Park_Mirpur/', views.Lehri_Zoo_Park_Mirpur, name="Lehri_Zoo_Park_Mirpur"),
    path('Fish_Hechri_Lehri/', views.Fish_Hechri_Lehri, name="Fish_Hechri_Lehri"),
    path('Jarikass_Poultry/', views.Jarikass_Poultry, name="Jarikass_Poultry"),
    path('Canal_bank_Mirpur/', views.Canal_bank_Mirpur, name="Canal_bank_Mirpur"),
    path('Girls_Degree_College_Kalyal/', views.Girls_Degree_College_Kalyal, name="Girls_Degree_College_Kalyal"),
    path('BangrillaCommunityHospital/', views.BangrillaCommunityHospital, name="BangrillaCommunityHospital"),
    path('Islamgarh_Welfare_Trust/', views.Islamgarh_Welfare_Trust, name="Islamgarh_Welfare_Trust"),
    path('Pilot_School_Mirpur/', views.Pilot_School_Mirpur, name="Pilot_School_Mirpur"),
    path('Solid_Waste_Project_Site_Mirpur/', views.Solid_Waste_Project_Site_Mirpur, name="Solid_Waste_Project_Site_Mirpur"),
    path('Muslim_Hands_Football_Academy_Mirpur/', views.Muslim_Hands_Football_Academy_Mirpur, name="Muslim_Hands_Football_Academy_Mirpur"),
    path('AllamaIqbalRoad/', views.AllamaIqbalRoad, name="AllamaIqbalRoad"),
    path('MUST_Uni_Ajk/', views.MUST_Uni_Ajk, name="MUST_Uni_Ajk"),
    path('Afzalpur_Mirpur/', views.Afzalpur_Mirpur, name="Afzalpur_Mirpur"),
    path('Allama_Iqbal_Open_Uni_Mirpur/', views.Allama_Iqbal_Open_Uni_Mirpur, name="Allama_Iqbal_Open_Uni_Mirpur"),
    path('MUST_JariKass_Campuss/', views.MUST_JariKass_Campuss, name="MUST_JariKass_Campuss"),
    path('SectorF4_Mirpur/', views.SectorF4_Mirpur, name="SectorF4_Mirpur"),
    path('environment_protection_agency/', views.environment_protection_agency, name="environment_protection_agency"),
    path('Chapran_Village_Mirpur/', views.Chapran_Village_Mirpur, name="Chapran_Village_Mirpur"),
    path('Nelum_Muzaffarabad/', views.Nelum_Muzaffarabad, name="Nelum_Muzaffarabad"),
    path('Rarra_Central_Jail_Muzaffarabad/', views.Rarra_Central_Jail_Muzaffarabad, name="Rarra_Central_Jail_Muzaffarabad"),
    path('Girls_High_School_Tararkhal/', views.Girls_High_School_Tararkhal, name="Girls_High_School_Tararkhal"),
    path('Tararkhal_Rawalakot/', views.Tararkhal_Rawalakot, name="Tararkhal_Rawalakot"),
    path('Nakyal_Kotli/', views.Nakyal_Kotli, name="Nakyal_Kotli"),
    path('Ghazighura_Bhimber/', views.Ghazighura_Bhimber, name="Ghazighura_Bhimber"),
    path('Ghura_Khurd_Dera_Mirpur/', views.Ghura_Khurd_Dera_Mirpur, name="Ghura_Khurd_Dera_Mirpur"),
    path('Patni_Bhimber/', views.Patni_Bhimber, name="Patni_Bhimber"),
    path('BHU_Bider_Brains_Bhimber/', views.BHU_Bider_Brains_Bhimber, name="BHU_Bider_Brains_Bhimber"),

    #new cities of Bhimber
    path('Alharmain_Daraiyan_Welfare_Foundation_Bhimber/', views.Alharmain_Daraiyan_Welfare_Foundation_Bhimber, name="Alharmain_Daraiyan_Welfare_Foundation_Bhimber"),
    path('Bhimber_Uni_Bhimber/', views.Bhimber_Uni_Bhimber, name="Bhimber_Uni_Bhimber"),
    path('BHU_Banain_Bhimber/', views.BHU_Banain_Bhimber, name="BHU_Banain_Bhimber"),
    path('BHU_Chaneer_Bhimber/', views.BHU_Chaneer_Bhimber, name="BHU_Chaneer_Bhimber"),
    path('BHU_Kherowal_Bhimber/', views.BHU_Kherowal_Bhimber, name="BHU_Kherowal_Bhimber"),
    path('BHU_Kot_Jamel_Bhimber/', views.BHU_Kot_Jamel_Bhimber, name="BHU_Kot_Jamel_Bhimber"),
    path('BHU_Maghloora_Bhimber/', views.BHU_Maghloora_Bhimber, name="BHU_Maghloora_Bhimber"),
    path('Darbar_Baba_Shadi_Shaheed/', views.Darbar_Baba_Shadi_Shaheed, name="Darbar_Baba_Shadi_Shaheed"),
    path('DHO_Bhimber/', views.DHO_Bhimber, name="DHO_Bhimber"),


    path('District_Jail_Bhimber/', views.District_Jail_Bhimber, name="District_Jail_Bhimber"),
    path('Dadyal_1/', views.Dadyal_1, name="Dadyal_1"),
    path('Dadyal_2/', views.Dadyal_2, name="Dadyal_2"),
    path('Pachwana_Dadyal/', views.Pachwana_Dadyal, name="Pachwana_Dadyal"),
    path('gardens/', views.gardens, name="gardens"),
    path('training/', views.training, name="training"),

    
    

    path('cities_muzaffarabad/', views.cities_muzaffarabad, name="cities_muzaffarabad"),
    #new cities of Muzaffarabad
    path('Civil_Veterinary_Hospital_Gharhi_Dupatta_Muzaffarabad/', views.Civil_Veterinary_Hospital_Gharhi_Dupatta_Muzaffarabad, name="Civil_Veterinary_Hospital_Gharhi_Dupatta_Muzaffarabad"),

    path('cities_rawalakot/', views.cities_rawalakot, name="cities_rawalakot"),
    path('cities_kotli/', views.cities_kotli, name="cities_kotli"),
    path('cities_bhimber/', views.cities_bhimber, name="cities_bhimber"),
    path('cities_dadyal/', views.cities_dadyal, name="cities_dadyal"),
    path('contact_us/', views.contact_us, name="contact_us"),
    path('about_us/', views.about_us, name="about_us"),
    path('gallery/', views.gallery, name="gallery"),
    path('events/', views.events, name='events'),
    path('contact/', views.contact_view, name='contact'),
    path('success/', views.success_view, name='success'),
]
