# accounts/api/views/trainer/make_trainer.py
from rest_framework import generics, status
from rest_framework.response import Response
from accounts.api.serializers.trainer.make_trainer import MakeTrainerSerializer
from permissions.manager_permission import IsManager


class MakeTrainerView(generics.CreateAPIView):
    serializer_class = MakeTrainerSerializer
    permission_classes = [IsManager]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["request"] = self.request
        return context

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        trainer = serializer.save()

        return Response(
            {
                "message": "Member promoted to trainer successfully",
                "trainer_id": trainer.id,
                "trainer_branch": trainer.branch.id,
                "user_id": trainer.user.id
            },
            status=status.HTTP_201_CREATED
        )
