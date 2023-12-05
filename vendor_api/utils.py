from django.db.models import Avg, Count, F
from .models import PurchaseOrder, Vendor, HistoricalPerformance



def update_vendor_metrics(vendor):
    completed_orders = PurchaseOrder.objects.filter(vendor=vendor, status='completed')

    # Historical Performance Metrics
    historical_metrics = HistoricalPerformance.objects.create(
        vendor=vendor,
        on_time_delivery_rate=(vendor.on_time_delivery_rate or 0),
        quality_rating_avg=(vendor.quality_rating_avg or 0),
        average_response_time=(vendor.average_response_time or 0),
        fulfillment_rate=(vendor.fulfillment_rate or 0),
    )

    # Update Vendor Metrics
    total_completed_orders = completed_orders.count()
    on_time_deliveries = completed_orders.filter(delivery_date__lte=F('acknowledgment_date')).count()
    vendor.on_time_delivery_rate = (on_time_deliveries / total_completed_orders) * 100 if total_completed_orders > 0 else 0
    vendor.quality_rating_avg = completed_orders.filter(quality_rating__isnull=False).aggregate(Avg('quality_rating'))['quality_rating__avg'] or 0
    response_times = completed_orders.exclude(acknowledgment_date__isnull=True).annotate(
        response_time=F('acknowledgment_date') - F('issue_date')
    ).aggregate(Avg('response_time'))['response_time__avg'] or 0
    vendor.average_response_time = response_times.total_seconds() / 60 if response_times else 0
    successful_orders = completed_orders.filter(status='completed', issue_date__isnull=True)
    vendor.fulfillment_rate = (successful_orders.count() / total_completed_orders) * 100 if total_completed_orders > 0 else 0

    vendor.save()





