from rest_framework import serializers
from workouts.models.workOut_plan import WorkOutPlan



class WorkOutPlanSerializer(serializers.ModelSerializer):

    class Meta:
        model = WorkOutPlan

        fields = [
            "id","title","description"
        ]

# validation, branch and created by added here,,so no need to send these.
        def create(self, validated_data):
            trainer = self.context["request"].user.trainer
            return WorkOutPlan.objects.create(created_by=trainer, branch=trainer.branch, **validated_data)
           
        
    

