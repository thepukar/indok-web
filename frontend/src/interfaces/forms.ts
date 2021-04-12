import { User } from "@interfaces/users";

export interface Form {
  id: string;
  name: string;
  description: string;
  questions: Question[];
  responders: User[];
}

export interface Question {
  id: string;
  form: Form;
  question: string;
  description: string;
  questionType: QuestionType;
  mandatory: boolean;
  options: Option[];
  answers: Answer[];
}

export type QuestionType =
  | "PARAGRAPH"
  | "SHORT_ANSWER"
  | "MULTIPLE_CHOICE"
  | "CHECKBOXES"
  | "DROPDOWN"
  | "SLIDER"
  | "FILE_UPLOAD";

export interface Option {
  id: string;
  answer: string;
}

export interface Answer {
  id: string;
  answer: string;
  question: Question;
}

// interface for the variables in certain question mutations
export interface QuestionVariables {
  id: string;
  question: string;
  description: string;
  questionType: QuestionType;
  mandatory: boolean;
  options: {
    answer: string;
    id?: string;
  }[];
}
