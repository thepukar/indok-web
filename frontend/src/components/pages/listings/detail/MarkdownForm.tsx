import { Tab, Tabs, TextField } from "@material-ui/core";
import ReactMarkdown from "react-markdown";
import renderers from "@components/pages/listings/markdown/renderers";
import { ChangeEventHandler, useState } from "react";

const MarkdownForm: React.FC<{
  markdown: string;
  onTextChange: ChangeEventHandler<HTMLInputElement | HTMLTextAreaElement>;
}> = ({ markdown, onTextChange }) => {
  const [preview, setPreview] = useState(0);

  const handleChange = (_: React.ChangeEvent<any>, newValue: number) => {
    setPreview(newValue);
  };

  return (
    <>
      <Tabs
        value={preview}
        indicatorColor="primary"
        textColor="primary"
        onChange={handleChange}
        aria-label="Redigering og forhåndsvisningstabs"
        variant="scrollable"
        scrollButtons="auto"
      >
        <Tab label="Rediger" />
        <Tab label="Forhåndsvisning" />
      </Tabs>
      {preview ? (
        <ReactMarkdown renderers={renderers}>{markdown}</ReactMarkdown>
      ) : (
        <TextField fullWidth rows={24} variant="outlined" value={markdown} multiline onChange={onTextChange} />
      )}
    </>
  );
};

export default MarkdownForm;
