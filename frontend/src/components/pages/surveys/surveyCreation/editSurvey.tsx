import { useQuery, useMutation } from "@apollo/client";
import { SURVEY, QUESTIONTYPES } from "@graphql/surveys/queries";
import { CREATE_QUESTION, DELETE_QUESTION, UPDATE_QUESTION } from "@graphql/surveys/mutations";
import { useState, useEffect } from "react";
import { Survey, QuestionType, Question, QuestionVariables } from "@interfaces/surveys";
import QuestionPreview from "@components/pages/surveys/surveyCreation/questionPreview";
import EditQuestion from "@components/pages/surveys/surveyCreation/editQuestion";
import { Button, Grid } from "@material-ui/core";

const EditSurvey: React.FC<{ surveyId: string }> = ({ surveyId }) => {
  const { loading, error, data } = useQuery<{ survey: Survey }>(SURVEY, {
    variables: { ID: surveyId },
  });
  const [activeQuestion, setActiveQuestion] = useState<Question | undefined>();
  const [createQuestion] = useMutation<{ createQuestion: { question: Question } }>(CREATE_QUESTION, {
    update: (cache, { data }) => {
      const newQuestion = data?.createQuestion.question;
      const cachedSurvey = cache.readQuery<{ survey: Survey }>({
        query: SURVEY,
        variables: { ID: surveyId },
      });
      if (cachedSurvey && newQuestion) {
        cache.writeQuery({
          query: SURVEY,
          variables: { ID: surveyId },
          data: {
            survey: {
              questions: [...cachedSurvey.survey.questions, newQuestion],
            },
          },
        });
      }
    },
  });
  const [deleteQuestion] = useMutation<{ deleteQuestion: { deletedId: string } }>(DELETE_QUESTION, {
    update: (cache, { data }) => {
      const cachedSurvey = cache.readQuery<{ survey: Survey }>({
        query: SURVEY,
        variables: { ID: surveyId },
      });
      const deletedId = data?.deleteQuestion.deletedId;
      if (cachedSurvey && deletedId) {
        cache.writeQuery({
          query: SURVEY,
          variables: { ID: surveyId },
          data: {
            survey: {
              questions: cachedSurvey.survey.questions.filter((question) => question.id !== deletedId),
            },
          },
        });
      }
    },
  });
  const [updateQuestion] = useMutation<{ updateQuestion: { question: Question } }, QuestionVariables>(UPDATE_QUESTION, {
    update: (cache, { data }) => {
      const newQuestion = data?.updateQuestion.question;
      const cachedSurvey = cache.readQuery<{ survey: Survey }>({
        query: SURVEY,
        variables: { ID: surveyId },
      });
      if (cachedSurvey && newQuestion) {
        cache.writeQuery({
          query: SURVEY,
          variables: { ID: surveyId },
          data: {
            survey: {
              questions: cachedSurvey.survey.questions.map((question) =>
                question.id === newQuestion.id ? newQuestion : question
              ),
            },
          },
        });
      }
    },
  });
  const { loading: questionTypeLoading, error: questionTypeError, data: questionTypeData } = useQuery<{
    questionTypes: QuestionType[];
  }>(QUESTIONTYPES);
  const [standardQuestionType, setStandardQuestionType] = useState<QuestionType>();
  useEffect(() => {
    if (!questionTypeLoading && !questionTypeError && questionTypeData) {
      setStandardQuestionType(questionTypeData.questionTypes.find((type) => type.name === "Short answer"));
    }
  }, [questionTypeLoading, questionTypeError, questionTypeData]);
  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error</p>;
  return (
    <>
      {data && (
        <>
          <h3>{data.survey.descriptiveName}</h3>
          {questionTypeLoading ? (
            <p>Loading...</p>
          ) : questionTypeError ? (
            <p>Error fetching question types</p>
          ) : (
            questionTypeData && (
              <Grid item container direction="column">
                {data.survey.questions.map((question) =>
                  question === activeQuestion ? (
                    <EditQuestion
                      oldQuestion={question}
                      questionTypes={questionTypeData.questionTypes}
                      updateQuestion={updateQuestion}
                      deleteQuestion={deleteQuestion}
                      setInactive={() => setActiveQuestion(undefined)}
                    />
                  ) : (
                    <QuestionPreview
                      question={question}
                      setActive={() => {
                        if (activeQuestion) {
                          updateQuestion({
                            variables: {
                              id: activeQuestion.id,
                              question: activeQuestion.question,
                              description: activeQuestion.description,
                              position: activeQuestion.position,
                              questionTypeId: activeQuestion.questionType.id,
                            },
                          });
                        }
                        setActiveQuestion(question);
                      }}
                    />
                  )
                )}
                {standardQuestionType && (
                  <Button
                    onClick={(e) => {
                      e.preventDefault();
                      createQuestion({
                        variables: {
                          question: "",
                          description: "",
                          // TODO: implement automatic position generation in backend
                          position:
                            data.survey.questions
                              .map((question) => parseInt(question.position))
                              .reduce((prev, curr) => (prev > curr ? prev : curr), -1) + 1,
                          questionTypeId: standardQuestionType.id,
                          surveyId: data.survey.id,
                        },
                      });
                    }}
                  >
                    Legg til spørsmål
                  </Button>
                )}
              </Grid>
            )
          )}
        </>
      )}
    </>
  );
};

export default EditSurvey;
