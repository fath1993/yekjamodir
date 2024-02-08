from django.urls import path

from financial_accounting.views import FinancialBrokerNew, FinancialBrokerList, FinancialTransactionRecordNew, \
    FinancialTransactionRecordList, FinancialBrokerEdit, FinancialTransactionRecordEdit, \
    ajax_export_transaction_to_excel, FinancialBrokerRemove, FinancialTransactionRecordRemove, ajax_set_default_broker

app_name = 'financial'

urlpatterns = [
    # brokers
    path('financial-broker-list/', FinancialBrokerList.as_view(), name='financial-broker-list'),
    path('financial-broker-new/', FinancialBrokerNew.as_view(), name='financial-broker-new'),
    path('financial-broker-edit&broker-id=<int:broker_id>/', FinancialBrokerEdit.as_view(), name='financial-broker'
                                                                                                 '-edit-with-broker-id'),
    path('financial-broker-remove&broker-id=<int:broker_id>/', FinancialBrokerRemove.as_view(), name='financial'
                                                                                                     '-broker-remove'
                                                                                                     '-with-broker-id'),

    # financial transactions
    path('financial-transaction-record-list&broker-id=<int:broker_id>/', FinancialTransactionRecordList.as_view(),
         name='financial-transaction-record-list-with-broker-id'),
    path('financial-transaction-record-new&broker-id=<int:broker_id>/', FinancialTransactionRecordNew.as_view(),
         name='financial-transaction-record-new-with-broker-id'),
    path('financial-transaction-record-edit&transaction-id=<int:transaction_id>/',
         FinancialTransactionRecordEdit.as_view(), name='financial-transaction-record-edit-with-transaction-id'),
    path('financial-transaction-record-remove&transaction-id=<int:transaction_id>/',
         FinancialTransactionRecordRemove.as_view(), name='financial-transaction-record-remove-with-transaction-id'),

    # Ajax
    path('ajax-export-transaction-to-excel/', ajax_export_transaction_to_excel, name='ajax-export-transaction-to-excel'),
    path('ajax-set-default-broker/', ajax_set_default_broker, name='ajax-set-default-broker'),
]


