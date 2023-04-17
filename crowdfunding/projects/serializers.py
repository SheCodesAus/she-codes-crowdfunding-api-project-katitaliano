from rest_framework import serializers
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from .models import Project, Pledge

class ProjectSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=None)
    target = serializers.IntegerField()
    image = serializers.URLField()
    is_open = serializers.BooleanField()
    date_created = serializers.DateTimeField()
    owner = serializers.ReadOnlyField(source='owner_id')
        
    # Create method is responsible for creating and returning a new instance of the model associated with the serializer, with the validated data as the input.
    def create(self, validated_data):
        return Project.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.target = validated_data.get('target', instance.target)
        instance.image = validated_data.get('image', instance.image)
        instance.is_open = validated_data.get('is_open', instance.is_open)
        instance.date_created = validated_data.get('date_created', instance.date_created)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.save()
        return instance

    def validate_image(self, value):
        """
        Validate and convert the image URL to a URLField.
        """
        url_validator = URLValidator()
        try:
            url_validator(value)
        except ValidationError:
            raise serializers.ValidationError("Invalid image URL")

        return value

    def to_internal_value(self, data):
        """
        Convert image URL to a URLField before validating.
        """
        if 'image' in data:
            data['image'] = self.validate_image(data['image'])
        return super().to_internal_value(data)

class PledgeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Pledge
        fields = ['id', 'amount', 'comment', 'anonymous', 'project', 'supporter']
        read_only_fields =['id', 'supporter']

class ProjectDetailSerializer(ProjectSerializer):
    pledges = PledgeSerializer(many=True, read_only=True)


	# date created doesn't need auto_date_now because it isn't dealing with the database like the models are

