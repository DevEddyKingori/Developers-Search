from graphene_django import DjangoObjectType
import graphene

from projects.models import Project, Tag, Reviews
from users.models import Profile


# Defining Graphql Types
class ProfileType(DjangoObjectType):
    class Meta:
        model = Profile
        fields = "__all__"


class TagType(DjangoObjectType):
    class Meta:
        model = Tag
        fields = "__all__"


class ReviewType(DjangoObjectType):
    class Meta:
        model = Reviews
        fields = "__all__"


class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = "__all__"


# Root Query
class Query(graphene.ObjectType):
    all_projects = graphene.List(ProjectType)
    project = graphene.Field(ProjectType, id=graphene.Int(required=True))

    def resolve_all_projects(root, info):
        return Project.objects.all()

    def resolve_project(root, info, id):
        return Project.objects.get(id=id)


# Root Mutation (example: voting on project)
class VoteProject(graphene.Mutation):
    class Arguments:
        project_id = graphene.Int(required=True)
        value = graphene.String(required=True)

    project = graphene.Field(ProjectType)

    @classmethod
    def mutate(cls, root, info, project_id, value):
        user = info.context.user.profile
        project = Project.objects.get(id=project_id)

        review, created = Reviews.objects.get_or_create(
            owner=user,
            project=project,
        )
        review.value = value
        review.save()

        return VoteProject(project=project)


class Mutation(graphene.ObjectType):
    vote_project = VoteProject.Field()


# Final schema
schema = graphene.Schema(query=Query, mutation=Mutation)
