import { Question } from "@interfaces/surveys";
import QuestionTypePreview from "@components/pages/surveys/surveyAdmin/questionTypePreview";
import { Button, Grid } from "@material-ui/core";

// component to show a question when not in editing mode
const QuestionPreview: React.FC<{
  question: Question;
  setActive: () => void;
}> = ({ question, setActive }) => {
  return (
    <Grid container direction="column">
      <Grid container direction="row" justify="space-between">
        {question.question}
        <Button
          variant="contained"
          onClick={(e) => {
            e.preventDefault();
            setActive();
          }}
        >
          Rediger spørsmål
        </Button>
      </Grid>
      <QuestionTypePreview question={question} />
    </Grid>
  );
};

export default QuestionPreview;
