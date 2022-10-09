import { ThemeOptions } from "@mui/material";

export const CssBaseline: ThemeOptions["components"] = {
  MuiCssBaseline: {
    styleOverrides: (theme) => ({
      "*": {
        margin: 0,
        padding: 0,
        boxSizing: "border-box",
      },
      html: {
        width: "100%",
        height: "100%",
        WebkitOverflowScrolling: "touch",
      },
      "body, #__next": {
        width: "100%",
        height: "100%",
        display: "flex",
        flexDirection: "column",
      },
      ".content": {
        flex: "1 0 auto",
      },
      ".footer": {
        flexShrink: 0,
      },
      // List
      "& ul, & ol": {
        paddingLeft: 24,
        "& li": {
          lineHeight: 2,
        },
      },
      a: {
        color: theme.palette.primary.main,
      },
    }),
  },
};
