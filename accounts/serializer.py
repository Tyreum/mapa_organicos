from rest_framework import serializers



class ProdutorSerializer(serializers.Serializer):

    id = serializers.IntegerField()
    nome_fantasia = serializers.CharField(max_length=50)
    logradouro = serializers.CharField(max_length=30)
    numero = serializers.IntegerField()
    latitude = serializers.CharField(max_length=20)
    longitude = serializers.CharField(max_length=20)
    tipo_produtor = serializers.CharField(max_length=1)