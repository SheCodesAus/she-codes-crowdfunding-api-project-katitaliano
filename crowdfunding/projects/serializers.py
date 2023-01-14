from rest_framework import serializers

from .models import Project, Pledge

class ProjectSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=None)
    goal= serializers.IntegerField()
    image = serializers.URLField()
    is_open = serializers.BooleanField()
    date_created = serializers.DateTimeField()
    owner = serializers.CharField(max_length=200)

    def create(self, validated_data):
        return Project.objects.create(**validated_data)

class PledgeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pledge
        fields = ['id', 'amount', 'comment', 'anonymous', 'project', 'supporter' ]


    # date created doesn't need auto_date_now because it isn't dealing with the database like the models are

