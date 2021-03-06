from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('selectcurrency/', views.selectcurrency, name="selectcurrency"),
    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),
    path('logout/', views.logoutUser, name='logout'),
    path('shop/', views.shop, name='shop'),
    path('<int:auction_id>/auctiondetail/', views.auctiondetail, name='auctiondetail'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),
    path('<int:auction_id>/placebid/', views.placebid, name='placebid'),
    path('<int:auction_id>/bidhistory/', views.bidhistory, name='bidhistory'),
    path('createnewauction/', views.createnewauction, name='createnewauction'),
    path('editprofile/', views.editprofile, name='editprofile'),
    path('yourauctions/', views.yourauctions, name='yourauctions'),
    path('yourbids/', views.yourbids, name='yourbids'),
    path('<int:auction_id>/success/', views.success, name='success'),
    path('<int:auction_id>/failure/', views.failure, name='failure'),
    path('create-stripe-account/', views.createstripeaccount, name='create-stripe-account'),
    path('<int:auction_id>/create-checkout-session/', views.createcheckoutsession, name='create-checkout-session'),
    path('<int:auction_id>/selectpaymentmethod/', views.selectpaymentmethod, name='selectpaymentmethod'),
    path('<int:auction_id>/checkout/<str:payment_method>', views.checkout, name='checkout'),
    path('<int:auction_id>/editauction/', views.editauction, name='editauction'),
    path('<int:auction_id>/deleteauction/', views.deleteauction, name='deleteauction'),
    path('<int:bid_id>/deletebid/', views.deletebid, name='deletebid'),
    path('<int:buy_request_id>/rejectbuyrequest/', views.rejectbuyrequest, name='rejectbuyrequest'),
    path('<int:auction_id>/createbuyrequest/', views.createbuyrequest, name='createbuyrequest'),
    path('<int:auction_id>/manageauction/', views.manageauction, name='manageauction'),
    path('<int:auction_id>/endwithoutselling/', views.endwithoutselling, name='endwithoutselling'),
    path('<int:auction_id>/endbyselling/', views.endbyselling, name='endbyselling'),
    path('<int:auction_id>/<int:buyer_id>/<int:buyreq_id>/endbysellrequest/', views.endbysellrequest, name='endbysellrequest'),
    path('orders/', views.orders, name='orders'),
    path('<int:order_id>/orderinfo/', views.orderinfo, name='orderinfo'),
    path('shop/<slug:category_slug>', views.auctionsbycategory, name='auctionsbycategory'),
    path('shop/search/', views.searchresults, name='searchresults'),
    path('search/', views.search, name='search'),
]

