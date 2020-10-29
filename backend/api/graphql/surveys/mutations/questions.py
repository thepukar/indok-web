from apps.surveys.models import (
    QuestionType as QuestionTypeModel,
    Question,
)

from ..types import (
    QuestionTypeType,
    QuestionType,
)
import graphene

class QuestionInput(graphene.InputObjectType):
    survey_id = graphene.ID()
    question_type_id = graphene.ID()
    question = graphene.String(required=False)
    description = graphene.String(required=False)
    position = graphene.Int()

class CreateQuestion(graphene.Mutation):
    ok = graphene.Boolean()
    question = graphene.Field(QuestionType)

    class Arguments:
        question_data = QuestionInput(required=True)

    @classmethod
    def mutate(cls, self, info, question_data):
        question = Question()
        for k, v in question_data.items():
            setattr(question, k, v)
        question.save()
        ok = True
        return cls(question=question, ok=ok)

class UpdateQuestion(graphene.Mutation):
    ok = graphene.Boolean()
    question = graphene.Field(QuestionType)

    class Arguments:
        id = graphene.ID(required=True)
        question_data = QuestionInput(required=False)

    @classmethod
    def mutate(cls, self, info, id, question_data):
        question = Question.objects.get(pk=id)
        for k, v, in question_data.items():
            setattr(question, k, v)
        question.save()
        ok = True
        return cls(question=question, ok=ok)

class DeleteQuestion(graphene.Mutation):
    ok = graphene.Boolean()
    deleted_id = graphene.ID()

    class Arguments:
        id = graphene.ID(required=True)

    @classmethod
    def mutate(cls, self, info, id):
        question = Question.objects.get(pk=id)
        deleted_id = question.id
        question.delete()
        ok = True
        return cls(ok=ok, deleted_id=deleted_id)

class QuestionTypeInput(graphene.InputObjectType):
    description = graphene.String(required=False)

class CreateQuestionType(graphene.Mutation):
    question_type = graphene.Field(QuestionTypeType)
    ok = graphene.Boolean()

    class Arguments:
        question_type_data = QuestionTypeInput(required=True)

    @classmethod
    def mutate(cls, self, info, question_type_data):
        question_type = QuestionTypeModel()
        for key, value in question_type_data.items():
            setattr(question_type, key, value)
        question_type.save()
        ok = True
        return cls(question_type=question_type, ok=ok)

class UpdateQuestionType(graphene.Mutation):
    question_type = graphene.Field(QuestionTypeType)
    ok = graphene.Boolean()

    class Arguments:
        id = graphene.ID(required=True)
        question_type_data = QuestionTypeInput(required=False)

    @classmethod
    def mutate(cls, self, info, id, question_type_data):
        question_type = QuestionTypeModel.objects.get(id=id)
        for key, value in question_type_data.items():
            setattr(question_type, key, value)
        question_type.save()
        ok = True
        return cls(question_type=question_type, ok=ok)

class DeleteQuestionType(graphene.Mutation):
    deleted_id = graphene.ID()
    ok = graphene.Boolean()

    class Arguments:
        id = graphene.ID(required=True)

    @classmethod
    def mutate(cls, self, info, id):
        question_type = QuestionTypeModel.objects.get(pk=id)
        deleted_id = question_type.id
        question_type.delete()
        ok = True
        return cls(deleted_id=deleted_id, ok=ok)
