from rest_framework import serializers

from api_sample.models import TodosampleModel

class TodoSerializer(serializers.ModelSerializer):

    class Meta:

            model = TodosampleModel

            fields = "__all__"

    

