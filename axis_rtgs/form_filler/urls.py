# # form_filler/urls.py

# from django.urls import path
# from .views import *
# from . import views

# urlpatterns = [
#     path('', views.landing_page, name='landing'),
#     path('sign_up/', views.sign_up, name='signup'),
#     path('select_bank_2/', views.select_bank_2, name='select_bank_2'),
#     path('select_bank/', views.select_bank, name='select_bank'),
#     path('bank_accounts/', views.bank_accounts, name='bank_accounts'),
#     path('select-bank/', views.select_bank, name='select_bank'),
#     path('login/', views.login_view, name='login'),
#     path('add_account/', views.add_account, name='add_account'),
#     # path('', select_bank, name='select_bank'),
#     path('axis-bank/', views.axis_bank, name='axis_bank'),
#     path('fetch-remitter/', views.fetch_remitter, name='fetch_remitter'),
#     path("union-bank/", views.union_bank, name="union_bank"),
#     path("list_placeholders/", list_docx_placeholders, name="list_placeholders"),
#     path("remitter-lookup/", remitter_lookup, name="remitter_lookup"),
#     path('save-bank/<str:bank_name>/', views.save_bank_account, name='save_bank'),
#     path('save-bank/<str:bank_name>/', views.save_bank_account, name='save_bank'),
#     path('bank/<str:bank_name>/', views.bank_accounts, name='bank_accounts'),
# ]



# from django.urls import path
# from . import views
# from .views import *

# urlpatterns = [
#     # ✅ Landing / Home route
#     path('', views.landing_page, name='landing'),

#     # ✅ Auth pages
#     path('sign_up/', views.sign_up, name='signup'),
#     path('login/', views.login_view, name='login'),

#     # ✅ Bank selection and account management
#     path('select_bank/', views.select_bank, name='select_bank'),
#     path('select_bank_2/', views.select_bank_2, name='select_bank_2'),
#     path('add_account/', views.add_account, name='add_account'),

#     # ✅ Bank-specific routes
#     path('axis-bank/', views.axis_bank, name='axis_bank'),
#     path('union-bank/', views.union_bank, name='union_bank'),

#     # ✅ Fetching and saving data
#     path('fetch-remitter/', views.fetch_remitter, name='fetch_remitter'),
#     path('save-bank/<str:bank_name>/', views.save_bank_account, name='save_bank'),
#     path('bank/<str:bank_name>/', views.bank_accounts, name='bank_accounts'),

#     # ✅ DOCX / Utility tools
#     path("list_placeholders/", list_docx_placeholders, name="list_placeholders"),
#     path("remitter-lookup/", remitter_lookup, name="remitter_lookup"),
# ]



# from django.urls import path
# from . import views

# urlpatterns = [
#     # 🏠 Landing / Home page
#     path('', views.landing_page, name='landing'),

#     # 👤 Authentication routes
#     path('sign_up/', views.sign_up, name='signup'),
#     path('login/', views.login_view, name='login'),
#     path('logout/', views.logout_view, name='logout'),  # ✅ added logout route

#     # 🏦 Bank selection & account management
#     path('select_bank/', views.select_bank, name='select_bank'),  # ✅ main bank selection page
#     path('add_account/', views.add_account, name='add_account'),
#     path('bank/<str:bank_name>/', views.bank_accounts, name='bank_accounts'),



#     # 🏧 Bank-specific routes
#     path('axis-bank/', views.axis_bank, name='axis_bank'),
#     path('union-bank/', views.union_bank, name='union_bank'),
#     path('fetch-beneficiaries/', views.fetch_beneficiary, name='fetch_beneficiaries'),
    

#     # 🔄 Data fetch/save utilities
#     path('fetch-remitter/', views.fetch_remitter, name='fetch_remitter'),
#     path('save-bank-account/<str:bank_name>/', views.save_bank_account, name='save_bank_account'),


#     # 📄 DOCX / Utility tools
#     path('list_placeholders/', views.list_docx_placeholders, name='list_placeholders'),
#     path('remitter-lookup/', views.remitter_lookup, name='remitter_lookup'),
#     path('select_bank_2/', views.select_bank_2, name='select_bank_2'),

#     path('beneficiaries/', views.beneficiaries_list, name='beneficiaries_list'),
#     path('download-beneficiaries-excel/', views.download_beneficiaries_excel, name='download_beneficiaries_excel'),



#     path('select-bank/', views.select_bank, name='select_bank'),
#     path('bank/<str:bank_name>/', views.select_specific_bank, name='select_specific_bank'),
# ]




from django.urls import path
from . import views

urlpatterns = [
    # 🏠 Landing / Home page
    path('', views.landing_page, name='landing'),

    # 👤 Authentication
    path('sign_up/', views.sign_up, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # 🏦 Bank selection & account management
    path('select_bank/', views.select_bank, name='select_bank'),
    path('add_account/', views.add_account, name='add_account'),

    # ✅ Single route for bank-specific account lists
    path('bank/<str:bank_name>/', views.select_specific_bank, name='select_specific_bank'),

    # 🏧 Bank-specific RTGS/NEFT form routes
    path('axis-bank/', views.axis_bank, name='axis_bank'),
    path('union-bank/', views.union_bank, name='union_bank'),

    # 🔄 Data utilities
    path('fetch-remitter/', views.fetch_remitter, name='fetch_remitter'),
    path('save-bank-account/<str:bank_name>/', views.save_bank_account, name='save_bank_account'),

    # 📄 DOCX & misc tools
    path('list_placeholders/', views.list_docx_placeholders, name='list_placeholders'),
    path('remitter-lookup/', views.remitter_lookup, name='remitter_lookup'),
    path('select_bank_2/', views.select_bank_2, name='select_bank_2'),
    path('select-bank-3/', views.select_bank_3, name='select_bank_3'),

    # 👥 Beneficiaries
    path('beneficiaries/', views.beneficiaries_list, name='beneficiaries_list'),
    path('download-beneficiaries-excel/', views.download_beneficiaries_excel, name='download_beneficiaries_excel'),
    path('beneficiaries/edit/<int:beneficiary_id>/', views.edit_beneficiary, name='edit_beneficiary'),
    path('beneficiaries/delete/<int:beneficiary_id>/', views.delete_beneficiary, name='delete_beneficiary'),

    path('fetch-beneficiaries/', views.fetch_beneficiary, name='fetch_beneficiaries'),



    path('hdfc-bank/', views.hdfc_bank_view, name='hdfc_bank'),


]
