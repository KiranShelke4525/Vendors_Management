from django.urls import path
from .views import (
    VendorListCreateView,
    VendorRetrieveUpdateDeleteView,
    PurchaseOrderListCreateView,
    PurchaseOrderRetrieveUpdateDeleteView,
    VendorPerformanceView,
    PurchaseOrderCreateView, 
    PurchaseOrderListView, 
    PurchaseOrderDetailsView
)

urlpatterns = [
    path('vendors/', VendorListCreateView.as_view(), name='vendor-list-create'),
    path('vendors/<int:vendor_id>/', VendorRetrieveUpdateDeleteView.as_view(), name='vendor-retrieve-update-delete'),
    path('purchase_orders/', PurchaseOrderListCreateView.as_view(), name='purchase-order-list-create'),
    path('vendors/', PurchaseOrderRetrieveUpdateDeleteView.as_view(), name='purchase-order-retrieve-update-delete'),
    path('api/vendors/<int:vendor_id>/performance/', VendorPerformanceView.as_view(), name='vendor_performance'),
    path('api/purchase_orders/', PurchaseOrderListView.as_view(), name='purchase_order_list'),
    path('api/purchase_orders/<int:po_id>/', PurchaseOrderDetailsView.as_view(), name='purchase_order_details'),
    path('api/purchase_orders/create/', PurchaseOrderCreateView.as_view(), name='create_purchase_order'),
] 

