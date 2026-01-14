from rest_framework import serializers
from accounts.models.trainer import Trainer

class TrainerSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = Trainer
        fields = ["id", "branch", "phone_number", "address", "created_at"]

        read_only_fields = ["id", "created_at"]