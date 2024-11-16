from rest_framework import serializers
from .models import Client
from .models import Account
from .models import Bank
from .models import AccountType
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        #fields = ['cin','name','familyName','email','photo','client_documents'] ==> si on veut afficher que ces champs
        fields = '__all__'
        
class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = '__all__'

class AccountTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountType
        fields = '__all__'