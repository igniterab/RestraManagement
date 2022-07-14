from rest_framework import serializers
from .models import StaffUser


class StaffUserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return StaffUser.objects.create(**validated_data)

    class Meta:
        model = StaffUser
        fields = ('native_name', 'email', 'first_name', 'last_name', 'phone_no', 'busy', 'address' )
