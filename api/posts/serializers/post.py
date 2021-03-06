from rest_framework import serializers
from api.accounts.serializers.user import UserSerializer
from api.posts.models.post import Post
from api.replies.models.post_reply import PostReply
from api.replies.serializers.post_reply import PostReplySerializer
from api.votes.serializers.post_vote import PostVoteSerializer


class PostSerializer(serializers.ModelSerializer):
    post_reply_count = serializers.SerializerMethodField()
    post_votes = PostVoteSerializer(many=True, read_only=True)
    user = UserSerializer()

    class Meta:
        model = Post
        fields = '__all__'

    @staticmethod
    def get_post_reply_count(post):
        return PostReply.objects.filter(post=post).count()


class PostSerializerCreate(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
        fields = '__all__'


class PostSerializerFull(PostSerializer):
    post_replies = PostReplySerializer(many=True, read_only=True)


class PostSerializerUpdate(serializers.ModelSerializer):

    class Meta:
        model = Post
        exclude = ('user',)

    def validate(self, data):
        """
        Validate authenticated user
        """

        if self.instance.user != self.context['request'].user:
            raise serializers.ValidationError('You can not edit posts from other users')
        return data
