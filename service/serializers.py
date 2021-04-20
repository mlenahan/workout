from rest_framework import serializers
from core.models import Exercise
from core.base import Musclegroup


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ['id', 'name', 'primary_musclegroup', 'secondary_musclegroup', 'description']

    def create(self, validated_data):
        return Exercise.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.primary_musclegroup = validated_data.get('primary_musclegroup', instance.primary_musclegroup)
        instance.secondary_musclegroup = validated_data.get('secondary_musclegroup', instance.secondary_musclegroup)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance

