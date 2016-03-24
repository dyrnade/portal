from rest_framework import serializers
from comodo.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id','title', 'message', 'is_accomplished')
        # filter_backends = (filters.DjangoFilterBackend,)
        # filter_fields = ('username',)
