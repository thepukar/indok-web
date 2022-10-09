import { alpha, ThemeOptions } from "@mui/material/styles";

export const Button: ThemeOptions["components"] = {
  MuiButton: {
    defaultProps: {
      disableElevation: true,
    },

    styleOverrides: {
      root: ({ theme }) => ({
        "&.MuiButton-outlinedInherit": {
          borderColor: alpha(theme.palette.text.primary, 0.25),
        },
        textTransform: "none",
        "& .MuiLoadingButton-text": {
          "& .MuiLoadingButton-startIcon": {
            marginLeft: 0,
          },
          "& .MuiLoadingButton-endIcon": {
            marginRight: 0,
          },
        },
      }),
    },
  },
};
