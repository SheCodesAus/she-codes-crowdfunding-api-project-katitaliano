from rest_framework import serializers

from .models import Project, Pledge

class AUCurrencyField(serializers.Field):
    """
    Custom serializer field for handling AU currency values.
    """
    def to_representation(self, value):
        """
        Convert integer value to formatted AU currency string.
        """
        # Check if the value is not None
        if value is not None:
            # Convert integer value to string and format as AU currency
            return "${:,.2f}".format(value / 100)

    def to_internal_value(self, data):
        """
        Convert formatted AU currency string to integer value.
        """
        try:
            # Remove "$" and "," from the formatted AU currency string
            data = data.replace('$', '').replace(',', '')
            # Convert the string to float and multiply by 100 to get integer value
            return int(float(data) * 100)
        except (ValueError, TypeError):
            raise serializers.ValidationError("Invalid AU currency value")

    def validate_empty_values(self, data):
        """
        Validate that the field is not empty.
        """
        if data is None:
            raise serializers.ValidationError("This field may not be null.")

class ProjectSerializer(serializers.Serializer):
	id = serializers.ReadOnlyField()
	title = serializers.CharField(max_length=200)
	description = serializers.CharField(max_length=None)
	target = AUCurrencyField()
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

class PledgeSerializer(serializers.ModelSerializer):
    amount = AUCurrencyField()
    
    class Meta:
        model = Pledge
        fields = ['id', 'amount', 'comment', 'anonymous', 'project', 'supporter']
        read_only_fields =['id', 'supporter']

class ProjectDetailSerializer(ProjectSerializer):
	pledges = PledgeSerializer(many=True, read_only=True)

	# date created doesn't need auto_date_now because it isn't dealing with the database like the models are

