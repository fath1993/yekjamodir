# from django.contrib.auth.models import User
# from rest_framework import serializers
#
# from warehouse.models import DigitalProperty
#
#
# class DigitalPropertySerializer(serializers.ModelSerializer):
#     id = serializers.IntegerField(read_only=False)
#     property_assigned_to = serializers.PrimaryKeyRelatedField(read_only=False, queryset=User.objects.all())
#     created_by = serializers.PrimaryKeyRelatedField(read_only=False, queryset=User.objects.all())
#     updated_by = serializers.PrimaryKeyRelatedField(read_only=False, queryset=User.objects.all())
#
#     def create(self, validated_data):
#         try:
#             DigitalProperty.objects.get(id=validated_data.get('id'))
#             print('item: ' + str(validated_data.get('id')) + ' exist')
#         except:
#             new_digital_property = DigitalProperty(
#                 id=validated_data.get('id'),
#                 title=validated_data.get('title'),
#                 description=validated_data.get('description'),
#                 buying_price=validated_data.get('buying_price'),
#                 condition=validated_data.get('condition'),
#                 registration_code=validated_data.get('registration_code'),
#                 property_assigned_to=validated_data.get('property_assigned_to'),
#                 date_of_assignment=validated_data.get('date_of_assignment'),
#                 date_of_return=validated_data.get('date_of_return'),
#                 created_at=validated_data.get('created_at'),
#                 updated_at=validated_data.get('updated_at'),
#                 created_by=validated_data.get('created_by'),
#                 updated_by=validated_data.get('updated_by'),
#
#                 digital_property_type=validated_data.get('digital_property_type'),
#                 serial_code_1=validated_data.get('serial_code_1'),
#                 serial_code_2=validated_data.get('serial_code_2'),
#                 warranty_company=validated_data.get('warranty_company'),
#                 warranty_expiration_date=validated_data.get('warranty_expiration_date'),
#             )
#             new_digital_property.save()
#             images = validated_data.get('images')
#             for image in images:
#                 new_digital_property.images.add(image)
#                 new_digital_property.save()
#
#     class Meta:
#         model = DigitalProperty
#         fields = "__all__"
#
# # class HousePropertySerializer(serializers.ModelSerializer):
# #     id = serializers.IntegerField(read_only=False)
# #     created_by = serializers.PrimaryKeyRelatedField(read_only=False, queryset=User.objects.all())
# #     updated_by = serializers.PrimaryKeyRelatedField(read_only=False, queryset=User.objects.all())
# #
# #     def create(self, validated_data):
# #         try:
# #             FinancialBroker.objects.get(id=validated_data.get('id'))
# #             print('item: ' + str(validated_data.get('id')) + ' exist')
# #         except:
# #             new_broker = FinancialBroker(
# #                 id=validated_data.get('id'),
# #                 broker_name=validated_data.get('broker_name'),
# #                 account_owner=validated_data.get('account_owner'),
# #                 account_number=validated_data.get('account_number'),
# #                 account_ISBN=validated_data.get('account_ISBN'),
# #                 account_card_number=validated_data.get('account_card_number'),
# #                 created_at=validated_data.get('created_at'),
# #                 updated_at=validated_data.get('updated_at'),
# #                 created_by=validated_data.get('created_by'),
# #                 updated_by=validated_data.get('updated_by'),
# #             )
# #             new_broker.save()
# #
# #     class Meta:
# #         model = FinancialBroker
# #         fields = "__all__"
# #
# #
# # class CulturalPropertySerializer(serializers.ModelSerializer):
# #     id = serializers.IntegerField(read_only=False)
# #     broker = serializers.PrimaryKeyRelatedField(read_only=False, queryset=FinancialBroker.objects.all())
# #     created_by = serializers.PrimaryKeyRelatedField(read_only=False, queryset=User.objects.all())
# #     updated_by = serializers.PrimaryKeyRelatedField(read_only=False, queryset=User.objects.all())
# #
# #     def create(self, validated_data):
# #         try:
# #             FinancialAccount.objects.get(id=validated_data.get('id'))
# #             print('item: ' + str(validated_data.get('id')) + ' exist')
# #         except:
# #             new_financial_account = FinancialAccount(
# #                 id=validated_data.get('id'),
# #                 broker=validated_data.get('broker'),
# #                 calculated_credit_balance=validated_data.get('calculated_credit_balance'),
# #                 created_at=validated_data.get('created_at'),
# #                 updated_at=validated_data.get('updated_at'),
# #                 created_by=validated_data.get('created_by'),
# #                 updated_by=validated_data.get('updated_by'),
# #             )
# #             new_financial_account.save()
# #
# #     class Meta:
# #         model = FinancialAccount
# #         fields = "__all__"
# #
# #
# # class CulturalPropertyAddUpSerializer(serializers.ModelSerializer):
# #     id = serializers.IntegerField(read_only=False)
# #     broker = serializers.PrimaryKeyRelatedField(read_only=False, queryset=FinancialBroker.objects.all())
# #     created_by = serializers.PrimaryKeyRelatedField(read_only=False, queryset=User.objects.all())
# #     updated_by = serializers.PrimaryKeyRelatedField(read_only=False, queryset=User.objects.all())
# #
# #     def create(self, validated_data):
# #         try:
# #             FinancialAccount.objects.get(id=validated_data.get('id'))
# #             print('item: ' + str(validated_data.get('id')) + ' exist')
# #         except:
# #             new_financial_account = FinancialAccount(
# #                 id=validated_data.get('id'),
# #                 broker=validated_data.get('broker'),
# #                 calculated_credit_balance=validated_data.get('calculated_credit_balance'),
# #                 created_at=validated_data.get('created_at'),
# #                 updated_at=validated_data.get('updated_at'),
# #                 created_by=validated_data.get('created_by'),
# #                 updated_by=validated_data.get('updated_by'),
# #             )
# #             new_financial_account.save()
# #
# #     class Meta:
# #         model = FinancialAccount
# #         fields = "__all__"
# #
# #
# # class CulturalPropertyAssignmentSerializer(serializers.ModelSerializer):
# #     id = serializers.IntegerField(read_only=False)
# #     broker = serializers.PrimaryKeyRelatedField(read_only=False, queryset=FinancialBroker.objects.all())
# #     created_by = serializers.PrimaryKeyRelatedField(read_only=False, queryset=User.objects.all())
# #     updated_by = serializers.PrimaryKeyRelatedField(read_only=False, queryset=User.objects.all())
# #
# #     def create(self, validated_data):
# #         try:
# #             FinancialAccount.objects.get(id=validated_data.get('id'))
# #             print('item: ' + str(validated_data.get('id')) + ' exist')
# #         except:
# #             new_financial_account = FinancialAccount(
# #                 id=validated_data.get('id'),
# #                 broker=validated_data.get('broker'),
# #                 calculated_credit_balance=validated_data.get('calculated_credit_balance'),
# #                 created_at=validated_data.get('created_at'),
# #                 updated_at=validated_data.get('updated_at'),
# #                 created_by=validated_data.get('created_by'),
# #                 updated_by=validated_data.get('updated_by'),
# #             )
# #             new_financial_account.save()
# #
# #     class Meta:
# #         model = FinancialAccount
# #         fields = "__all__"
