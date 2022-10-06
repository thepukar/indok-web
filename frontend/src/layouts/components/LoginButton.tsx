import { useQuery } from "@apollo/client";
import { PersonOutlineRounded } from "@mui/icons-material";
import { Button } from "@mui/material";
import NextLink from "next/link";

import LoginRequired from "@/components/Auth/LoginRequired";
import { UserDocument } from "@/generated/graphql";

type Props = {
  fullWidth?: boolean;
  "data-test-id"?: string;
};

const LoginButton: React.FC<Props> = ({ fullWidth, "data-test-id": dataTestId }) => {
  const { data } = useQuery(UserDocument);

  return (
    <LoginRequired size="medium" color="contrast" data-test-id={dataTestId} fullWidth={fullWidth}>
      <NextLink href="/profile" passHref>
        <Button endIcon={<PersonOutlineRounded fontSize="small" />} variant="text" color="contrast" size="medium">
          {data?.user?.firstName}
        </Button>
      </NextLink>
    </LoginRequired>
  );
};

export default LoginButton;
